
import pandas as pd

def pregunta_08():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    df["suma"] = df["c0"] + df["c2"]
    return df
