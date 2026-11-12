
import pandas as pd

def pregunta_03():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    return df["c1"].value_counts().sort_index()
