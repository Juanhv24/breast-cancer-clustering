"""Carga de datos crudos y depurados"""

import pandas as pd

from breast_cancer_clustering.config import ARCHIVO_CRUDO, ARCHIVO_DEPURADO

# Diez medidas del núcleo celular, en el orden en el que aparecen en wdbc.names
MEDIDAS = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave_points", "symmetry", "fractal_dimension",
]

# Cada medida se reporta como media, error estándar y peor valor (promedio de los tres más grandes)
SUFIJOS = ["mean", "se", "worst"]

# Columnas en el orden de wdbc.data: id, diagnóstico y luego 10 medidas por cada sufijo
COLUMNAS = ["id", "diagnosis"] + [
    f"{medida}_{sufijo}" for sufijo in SUFIJOS for medida in MEDIDAS
]

def cargar_crudos() -> pd.DataFrame:
    """Lee wdbc.data asignando los nombres de la columna, sin otra transformación"""
    if not ARCHIVO_CRUDO.exists():
        raise FileNotFoundError(
            f"No se encontró {ARCHIVO_CRUDO.name}. "
            "Ejecutar primero: uv run python scripts/descargar_datos.py"
        )
    return pd.read_csv(ARCHIVO_CRUDO, header=None, names=COLUMNAS)

def cargar_depurados() -> pd.DataFrame:
    """Lee la base depurada que produce notebooks/01_clustering.ipynb."""
    if not ARCHIVO_DEPURADO.exists():
        raise FileNotFoundError(
            f"No se encontró {ARCHIVO_DEPURADO.name}. "
            "Se genera al final de notebooks/01_clustering.ipynb"
        )
    return pd.read_parquet(ARCHIVO_DEPURADO)