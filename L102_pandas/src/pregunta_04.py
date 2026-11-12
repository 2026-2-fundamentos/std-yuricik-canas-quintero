
import pandas as pd

def pregunta_04():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    return df.groupby("c1")["c2"].mean().sort_index()
