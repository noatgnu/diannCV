import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import variation
import matplotlib.pyplot as plt
if __name__ == "__main__":
    inp = "//mrc-smb.lifesci.dundee.ac.uk/mrc-group-folder/ALESSI/Toan/BGX001_OBG_easypqplib/report.pr_matrix.tsv"

    df = pd.read_csv(inp, sep="\t")
    conditions = ["164-166"] + ["165-167-168-169"] + ["164-166"] + ["165-167-168-169"]*3
    intensity_columns = []

    for n, i in enumerate(df.columns.values):
        if conditions[0].split("-")[0] in i:
            intensity_columns = df.columns[n:n+len(conditions)]
            break
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

    sns.kdeplot(data=fin_df, x="Coefficient of Variations", hue="Conditions")
    plt.savefig(inp.replace(".tsv", ".pdf"))
