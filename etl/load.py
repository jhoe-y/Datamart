# etl/load.py
import sqlite3
import os

DB_PATH = 'datamart/datamart_inventario.db'  # Asegúrate de que la ruta sea correcta

def cargar_datos_producto(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('Dim_Producto', conn, if_exists='replace', index=False)
    conn.close()

def cargar_datos_tiempo(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('Dim_Tiempo', conn, if_exists='replace', index=False)
    conn.close()

def cargar_datos_hechos(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('HechosInventario', conn, if_exists='replace', index=False)
    conn.close()
