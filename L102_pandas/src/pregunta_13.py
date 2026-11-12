
import pandas as pd

def pregunta_13():
    df0 = pd.read_csv("data/tbl0.tsv", sep="\t")
    df2 = pd.read_csv("data/tbl2.tsv", sep="\t")

    resultado = pd.merge(df0, df2, on="c0")

    return resultado.groupby("c1")["c5b"].sum().sort_index()
