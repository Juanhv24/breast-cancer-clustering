"""Constante del proyecto: semilla y rutas a la raiz del repositorio"""

from pathlib import Path

# Semilla única para toda función con azar (partición, CV, modelos, remuestreo)
SEMILLA = 42

# Raíz del proyecto calculada desde la ubicación de este archivo.
# config.py -> breast_cancer_clustering/ (0) src/ (1) -> raíz (2)
RAIZ = Path(__file__).resolve().parents[2]

RUTA_CRUDOS = RAIZ / "datos" / "crudos"
RUTA_PROCESADOS = RAIZ / "datos" / "procesados"
RUTA_INFORMES = RAIZ / "informes"

ARCHIVO_CRUDO = RUTA_CRUDOS / "wdbc.data"
ARCHIVO_DEPURADO = RUTA_PROCESADOS / "wdbc_depurado.parquet"

# Carpeta de informes asociada a cada actividad
CARPETAS_ACTIVIDAD = {
    1: "01_clustering"
}

def ruta_figuras (actividad: int) -> Path:
    """Devuelve la carpeta de figuras de una actividad y la crea si no existe."""
    ruta = RUTA_INFORMES / CARPETAS_ACTIVIDAD[actividad] / "figuras"
    ruta.mkdir(parents=True, exist_ok=True)
    return ruta