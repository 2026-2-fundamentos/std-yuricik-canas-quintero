

import pandas as pd

def pregunta_09():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    df["year"] = df["c3"].str[:4]
    return df
