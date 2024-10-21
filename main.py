from create_tables import crear_tablas
from insert_data import insertar_datos
from queries import consultar_inventario

def main():
    crear_tablas()
    insertar_datos()
    consultar_inventario()

if __name__ == '__main__':
    main()
