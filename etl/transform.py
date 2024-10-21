import pandas as pd 

def transformar_datos_producto(df):
    # Eliminar duplicados y transformar columnas si es necesario
    df = df.drop_duplicates(subset=['Nombre_Producto'])
    return df

def transformar_datos_tiempo(df):
    # Transformar fechas y extraer componentes
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.month
    df['Año'] = df['Fecha'].dt.year
    return df[['Fecha', 'Mes', 'Año']]
