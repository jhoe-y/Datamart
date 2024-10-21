# etl/extract.py
import pandas as pd

def extraer_datos_producto(csv_file):
    return pd.read_csv(csv_file)

def extraer_datos_tiempo(csv_file):
    return pd.read_csv(csv_file)
