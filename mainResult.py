import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import variation
import matplotlib.pyplot as plt
if __name__ == "__main__":
    inp = r"\\mrc-smb.lifesci.dundee.ac.uk\mrc-group-folder\ALESSI\Toan\BGX001_OBG_easypqplib\report.tsv"
    df = pd.read_csv(inp, sep="\t")
    categories = ['PG.Quantity', 'PG.Normalised', 'PG.MaxLFQ']
    conditions = ["164-166"] + ["165-167-168-169"]
    fin_df = []

    for i, r in df.iterrows():
        for c in conditions:
            for co in c.split("-"):
                if co in r["File.Name"]:
                    df.at[i, "Conditions"] = c
                    break

    for i, g in df.groupby(["Conditions", "Protein.Group"]):
        arr = [i[0]]
        for cat in categories:
            arr.append(variation(g[cat]))
        fin_df.append(arr)

    fin_df = pd.DataFrame(fin_df, columns=["Conditions"] + categories)
    for cat in categories:
        plt.clf()
        s = fin_df[["Conditions", cat]]
        s.rename(columns={cat: "Coefficient of Variations"}, inplace=True)
        sns.kdeplot(data=s, x="Coefficient of Variations", hue="Conditions")
        plt.savefig(inp.replace(".tsv", f"{cat}.pdf"))
