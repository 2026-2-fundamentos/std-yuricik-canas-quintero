
import pandas as pd

def pregunta_10():
    df = pd.read_csv("data/tbl0.tsv", sep="\t")

    resultado = df.groupby("c1")["c2"].apply(
        lambda x: ":".join(map(str, sorted(x)))
    )

    return resultado.to_frame(name="c2").sort_index()
