import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

DB_FOLDER = os.path.join(current_dir, 'datamart')
DB_PATH = os.path.join(DB_FOLDER, 'datamart_inventario.db')

if not os.path.exists(DB_FOLDER):
    print("La carpeta 'datamart' no existe.")
else:
    print("Conectando a la base de datos en 'datamart'")

def obtener_conexion():
    return sqlite3.connect(DB_PATH)

