
import pandas as pd

def pregunta_05():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    return df.groupby("c1")["c2"].max().sort_index()
