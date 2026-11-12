
import pandas as pd
import re


def pregunta_01():
    with open("data/clusters_report.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    registros = []
    cluster_actual = None

    patron = r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s*%\s*(.*)$"

    for linea in lineas:
        coincidencia = re.match(patron, linea)

        if coincidencia:
            if cluster_actual is not None:
                registros.append(cluster_actual)

            cluster_actual = {
                "cluster": int(coincidencia.group(1)),
                "cantidad_de_palabras_clave": int(coincidencia.group(2)),
                "porcentaje_de_palabras_clave": float(
                    coincidencia.group(3).replace(",", ".")
                ),
                "principales_palabras_clave": coincidencia.group(4).strip()
            }

        elif cluster_actual is not None and linea.strip():
            cluster_actual["principales_palabras_clave"] += " " + linea.strip()

    if cluster_actual is not None:
        registros.append(cluster_actual)

    df = pd.DataFrame(registros)

    df["principales_palabras_clave"] = df[
        "principales_palabras_clave"
    ].apply(
        lambda texto: ", ".join(
            palabra.strip()
            for palabra in texto.split(",")
            if palabra.strip()
        )
    )

    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.rstrip(". ")
    )

    return df
