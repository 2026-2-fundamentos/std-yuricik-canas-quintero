
import pandas as pd

def pregunta_06():
    df = pd.read_csv("data/tbl1.tsv", sep="\t")
    return sorted(df["c4"].str.upper().unique().tolist())
