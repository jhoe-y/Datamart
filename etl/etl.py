from etl.extract import extraer_datos_producto, extraer_datos_tiempo  
from etl.transform import transformar_datos_producto, transformar_datos_tiempo
from etl.load import cargar_datos_producto, cargar_datos_tiempo 

def main():
    df_productos = extraer_datos_producto('path/to/productos.csv')
    df_tiempo = extraer_datos_tiempo('path/to/tiempo.csv')

    df_productos_transformados = transformar_datos_producto(df_productos)
    df_tiempo_transformados = transformar_datos_tiempo(df_tiempo)

    cargar_datos_producto(df_productos_transformados)
    cargar_datos_tiempo(df_tiempo_transformados)

if __name__ == "__main__":
    main()
