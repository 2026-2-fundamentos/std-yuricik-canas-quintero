
import pandas as pd

def pregunta_12():
    df = pd.read_csv("data/tbl2.tsv", sep="\t")

    df["c5"] = df["c5a"].astype(str) + ":" + df["c5b"].astype(str)

    resultado = df.groupby("c0")["c5"].apply(
        lambda x: ",".join(sorted(x))
    )

    return resultado.reset_index().sort_values("c0").reset_index(drop=True)
