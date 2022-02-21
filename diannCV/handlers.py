from io import StringIO
from uuid import uuid4

import pandas as pd
from tornado.escape import json_decode
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
import pickle
import os
from io import StringIO
from scipy.stats import variation
import seaborn as sns
import matplotlib.pyplot as plt

analysis_cache = {}

class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("access-control-allow-origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        self.set_status(204)
        self.finish()


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")


class WebSocketComm(WebSocketHandler):
    def open(self):
        self.write_message({"message": "connected"})

    def on_message(self, message):
        data = json_decode(message)
        if data["task"] == "upload":
            unique_id = str(uuid4())
            analysis_cache[unique_id] = pd.read_csv(data["file"], sep="\t")
            print(data)
            if data["filename"] in ["report.pr_matrix.tsv", "report.pg_matrix.tsv"]:
                print(analysis_cache[unique_id])
                self.write_message({"id": unique_id, "columns": analysis_cache[unique_id].columns.to_list()})
            elif data["filename"] == "report.tsv":
                self.write_message({"id": unique_id, "samples": data["File.Name"]})
        if data["task"] == "process":
            if data["filename"] in ["report.pr_matrix.tsv", "report.pg_matrix.tsv"]:
                conditions = data["conditions"]
                intensity_columns = data["intensity_columns"]
                df = analysis_cache[data["id"]]
                combo = {}
                for c, i in zip(conditions, intensity_columns):
                    if c not in combo:
                        combo[c] = []
                    combo[c].append(i)

                fin_df = []

                for i, r in df.iterrows():

                    for c in combo:
                        cv = variation(r[combo[c]])
                        fin_df.append([c, cv])

                fin_df = pd.DataFrame(fin_df, columns=["Conditions", "Coefficient of Variations"])
                plt.clf()
                sns.kdeplot(data=fin_df, x="Coefficient of Variations", hue="Conditions")
                plt.savefig("static/"+data["id"]+data["filename"].replace(".tsv", ".svg"))
                self.write_message(data["id"]+data["filename"].replace(".tsv", ".svg"))

            elif data["filename"] == "report.tsv":
                categories = ['PG.Quantity', 'PG.Normalised', 'PG.MaxLFQ']
                df = analysis_cache[data["id"]]

                for i, r in df.iterrows():
                    df.at[i, "Conditions"] = data["conditions"][r["File.Name"]]

                fin_df = []
                for i, g in df.groupby(["Conditions", "Protein.Group"]):
                    arr = [i[0]]
                    for cat in categories:
                        arr.append(variation(g[cat]))
                    fin_df.append(arr)

                fin_df = pd.DataFrame(fin_df, columns=["Conditions"] + categories)
                result = {}
                for cat in categories:
                    plt.clf()
                    s = fin_df[["Conditions", cat]]
                    s.rename(columns={cat: "Coefficient of Variations"}, inplace=True)
                    sns.kdeplot(data=s, x="Coefficient of Variations", hue="Conditions")
                    plt.savefig("static/"+data["id"]+data["filename"].replace(".tsv", f"{cat}.svg"))
                    result[cat] = data["id"]+data["filename"].replace(".tsv", f"{cat}.svg")
                self.write_message(result)

    def on_close(self):
        pass

    def check_origin(self, origin: str) -> bool:
        if origin == "http://localhost:4200" or origin == "http://dianncv.proteo.info":
            return True


class GetIDHandler(BaseHandler):
    async def post(self):
        data = json_decode(self.request.body)
        unique_id = str(uuid4())
        df = pd.read_csv(data["file"], sep="\t")
        if data["filename"] in ["report.pr_matrix.tsv", "report.pg_matrix.tsv"]:
            self.write({"id": unique_id, "columns": df.columns.to_list()})
        elif data["filename"] == "report.tsv":
            self.write({"id": unique_id, "columns": df["File.Name"].unique().to_list()})


class ProcessFileHandler(BaseHandler):
    async def post(self):
        data = json_decode(self.request.body)
        conditions = data["conditions"]

        if data["filename"] in ["report.pr_matrix.tsv", "report.pg_matrix.tsv"]:

            df = pd.read_csv(data["file"], sep="\t")
            combo = {}

            for c in df.columns:
                if c in conditions:
                    if conditions[c] not in combo:
                        combo[conditions[c]] = []
                    combo[conditions[c]].append(c)

            fin_df = []

            for i, r in df.iterrows():
                good_conditions = 0
                for c in combo:
                    if data["extra"]["minimumGoodSamples"] >= r[combo[c]].isna().sum():
                        good_conditions += 1
                if good_conditions >= data["extra"]["minimumGoodConditions"]:
                    for c in combo:
                        cv = variation(r[combo[c]])
                        fin_df.append([c, cv])

            fin_df = pd.DataFrame(fin_df, columns=["Conditions", "Coefficient of Variations"])

            sns.kdeplot(data=fin_df, x="Coefficient of Variations", hue="Conditions")
            p = data["file"].replace(".tsv", f".{data['id']}.pdf")
            plt.savefig(p)
            self.write({"file": p})

        elif data["filename"] == "report.tsv":
            categories = ['PG.Quantity', 'PG.Normalised', 'PG.MaxLFQ']
            df = pd.read_csv(data["file"], sep="\t")
            combo = {}
            for c in df.columns:
                if c in conditions:
                    if conditions[c] not in combo:
                        combo[conditions[c]] = []
                    combo[conditions[c]].append(c)
            for i, r in df.iterrows():
                df.at[i, "Conditions"] = conditions[r["File.Name"]]

            fin_df = []
            for i, g in df.groupby(["Protein.Group"]):
                for cat in categories:
                    v_count = g[cat].value_counts() <= data["extra"]["minimumGoodSamples"]

                    tf_count = v_count.value_counts()
                    if True in tf_count.index:
                        if tf_count[True] >= data["extra"]["minimumGoodConditions"]:
                            for i2, r2 in g.groupby("Conditions"):
                                arr = [i2, variation(r2[cat]), cat]
                                fin_df.append(arr)

            fin_df = pd.DataFrame(fin_df, columns=["Conditions", "Coefficient of Variations", "Categories"])
            result = {}
            for cat in categories:
                s = fin_df[fin_df["Categories"] == cat]
                plt.clf()
                sns.kdeplot(data=s, x="Coefficient of Variations", hue="Conditions")
                p = data["file"].replace(".tsv", f".{cat}.{data['id']}.pdf")
                plt.savefig(p)
                result[cat] = p
            self.write({"file": [v for v in result.values()]})