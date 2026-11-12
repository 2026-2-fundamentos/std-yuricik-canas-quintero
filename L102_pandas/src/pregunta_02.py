
import pandas as pd

def pregunta_02():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    return int(df.shape[1])

