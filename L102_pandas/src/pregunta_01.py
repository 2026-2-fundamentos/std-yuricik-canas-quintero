
import pandas as pd

def pregunta_01():
    """
    Retorna la cantidad de registros de data/tbl0.tsv.
    """
    df = pd.read_csv("data/tbl0.tsv", sep="\t")
    return int(len(df))

