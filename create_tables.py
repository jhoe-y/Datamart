from database import obtener_conexion

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla de dimensiones: Productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DimProducto (
            producto_id INTEGER PRIMARY KEY,
            nombre_producto TEXT,
            marca TEXT,
            tipo TEXT,
            proveedor TEXT,
            unidad_medida TEXT,
            estado TEXT
        )
    ''')

    # Crear tabla de dimensiones: Tiendas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DimTienda (
            tienda_id INTEGER PRIMARY KEY,
            nombre_tienda TEXT,
            ubicacion TEXT,
            ciudad TEXT,
            estado TEXT,
            pais TEXT,
            tipo_tienda TEXT
        )
    ''')

    # Crear tabla de dimensiones: Fecha
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DimFecha (
            fecha_id INTEGER PRIMARY KEY,
            fecha_completa TEXT,
            dia INTEGER,
            mes INTEGER,
            trimestre INTEGER,
            semestre INTEGER,
            año INTEGER,
            dia_semana TEXT,
            nombre_mes TEXT
        )
    ''')

    # Crear tabla de dimensiones: Categorías
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DimCategoria (
            categoria_id INTEGER PRIMARY KEY,
            nombre_categoria TEXT,
            descripcion_categoria TEXT
        )
    ''')

    # Crear tabla de hechos: Inventario
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS HechosInventario (
            producto_id INTEGER,
            tienda_id INTEGER,
            fecha_id INTEGER,
            categoria_id INTEGER,
            cantidad_disponible INTEGER,
            costo_unitario REAL,
            precio_venta_unitario REAL,
            cantidad_entradas INTEGER,
            cantidad_salidas INTEGER,
            FOREIGN KEY (producto_id) REFERENCES DimProducto(producto_id),
            FOREIGN KEY (tienda_id) REFERENCES DimTienda(tienda_id),
            FOREIGN KEY (fecha_id) REFERENCES DimFecha(fecha_id),
            FOREIGN KEY (categoria_id) REFERENCES DimCategoria(categoria_id)
        )
    ''')

    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    crear_tablas()
