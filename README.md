# Agrupamiento de tumores mamarios a partir de características nucleares

Proyecto de aprendizaje no supervisado sobre la base **Breast Cancer Wisconsin (Diagnostic)** (UCI). El objetivo es segmentar 569 tumores según la morfología de sus núcleos celulares, sin usar el diagnóstico, para proponer rutas de análisis prioritarias en un laboratorio. El diagnóstico se reserva para la validación externa.

## Enfoque

- **Preprocesamiento:** selección de 7 variables del bloque `_mean` sin redundancia (|ρ| < 0,9), transformación Yeo-Johnson y estandarización.
- **Técnicas:** K-means, clustering jerárquico (Ward) y DBSCAN.
- **Validación:** interna (silueta, Davies-Bouldin, Calinski-Harabasz, Dunn y silueta por tumor) y externa (concordancia entre métodos, estabilidad por remuestreo, robustez frente al bloque de variables y contraste con el diagnóstico).

## Resultados principales

- K-means y Ward coinciden en **dos grupos** (ARI entre ellos = 0,70). La estructura es débil (silueta = 0,30): los datos forman un continuo morfológico.
- El grupo de **núcleos grandes e irregulares** (239 tumores) es 75,3 % maligno. El de **núcleos pequeños y regulares** (330 tumores) es 90,3 % benigno.
- DBSCAN no encuentra grupos separados por baja densidad, pero identifica 20 tumores atípicos (3,5 %) para revisión individual.
- Técnica recomendada: **K-means**, por sus métricas internas, su estabilidad (ARI = 0,97) y su concordancia con el diagnóstico (ARI = 0,46).

## Estructura

```
datos/            crudos/ y procesados/ (no se versionan)
informes/         figuras generadas por el notebook
notebooks/        01_clustering.ipynb
scripts/          descargar_datos.py
src/              paquete breast_cancer_clustering (configuración y carga)
```

## Reproducir

Requiere [uv](https://docs.astral.sh/uv/) y Python 3.13.

```bash
uv sync
uv run python scripts/descargar_datos.py
uv run jupyter lab notebooks/01_clustering.ipynb
```

## Fuente de los datos

Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1995). *Breast Cancer Wisconsin (Diagnostic)* [Conjunto de datos]. UCI Machine Learning Repository. https://doi.org/10.24432/C5DW2B

---
Actividad 1 · Técnicas de Análisis No Supervisado · Especialización en Análisis Estadístico para Ciencia de Datos, Universidad de La Salle.