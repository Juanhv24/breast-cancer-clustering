"""Descarga el dataset Breast Cancer Wisconsin (UCI, id 17) en datos/crudos/."""

import io 
import urllib.request
import zipfile

from breast_cancer_clustering.config import ARCHIVO_CRUDO, RUTA_CRUDOS

URL = "https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip"

def main() -> None:
    if ARCHIVO_CRUDO.exists():
        print(f"Ya existe: {ARCHIVO_CRUDO}")
        return 

    RUTA_CRUDOS.mkdir(parents=True, exist_ok=True)
    print(f"Descargando {URL} ...")
    with urllib.request.urlopen(URL) as respuesta:
        contenido = respuesta.read()

    # El zip se procesa en memoria, sin guardarlo en disco.
    with zipfile.ZipFile(io.BytesIO(contenido)) as comprimido:
        print("Archivos en el zip:", comprimido.namelist())
        comprimido.extractall(RUTA_CRUDOS)

    if ARCHIVO_CRUDO.exists():
        print(f"Listo: {ARCHIVO_CRUDO}")
    else:
        print("El zip no trae wdbc.data con ese nombre; revisar datos/crudos/.")

if __name__ == "__main__":
    main()