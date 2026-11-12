import csv
import gzip
from pathlib import Path


def leer_datos():
    """Lee data/data.csv.gz, con o sin encabezados."""
    ruta = Path(__file__).resolve().parent.parent / "data" / "data.csv.gz"
    if not ruta.exists():
        ruta = Path("data/data.csv.gz")

    with gzip.open(ruta, "rt", encoding="utf-8-sig", newline="") as archivo:
        primera = archivo.readline()
        archivo.seek(0)
        # El formato habitual es TSV, pues codes y metrics contienen comas.
        if "\t" in primera:
            delimitador = "\t"
        elif ";" in primera:
            delimitador = ";"
        else:
            delimitador = ","
        lector = csv.reader(archivo, delimiter=delimitador)
        for fila in lector:
            if not fila or all(not campo.strip() for campo in fila):
                continue
            if len(fila) < 5:
                raise ValueError("Se esperaban cinco columnas en data/data.csv.gz")
            if fila[0].strip().lower() == "letter" and fila[1].strip().lower() == "value":
                continue
            yield tuple(campo.strip() for campo in fila[:5])


def pregunta_08():
    """Letras únicas y ordenadas para cada value."""
    from collections import defaultdict
    letras = defaultdict(set)
    for letra, valor, _, _, _ in leer_datos():
        letras[int(valor)].add(letra)
    return [(valor, sorted(grupo)) for valor, grupo in sorted(letras.items())]
