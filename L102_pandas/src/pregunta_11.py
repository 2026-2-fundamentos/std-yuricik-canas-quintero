
import pandas as pd

def pregunta_11():
    df = pd.read_csv("data/tbl1.tsv", sep="\t")

    resultado = df.groupby("c0")["c4"].apply(
        lambda x: ",".join(sorted(x))
    )

    return resultado.reset_index().sort_values("c0").reset_index(drop=True)
