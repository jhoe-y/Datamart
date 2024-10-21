from database import obtener_conexion

def insertar_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Insertar datos en la tabla DimProducto
    productos = [
        (1, 'Manzana', 'Marca A', 'Fruta', 'Proveedor X', 'Kg', 'Activo'),
        (2, 'Leche', 'Marca B', 'Lácteo', 'Proveedor Y', 'Litro', 'Activo')
    ]
    cursor.executemany('INSERT INTO DimProducto VALUES (?, ?, ?, ?, ?, ?, ?)', productos)

    # Insertar datos en la tabla DimTienda
    tiendas = [
        (1, 'Supermercado Central', 'Calle 123', 'Ciudad A', 'Estado A', 'País A', 'Urbana'),
        (2, 'Supermercado Norte', 'Calle 456', 'Ciudad B', 'Estado B', 'País A', 'Rural')
    ]
    cursor.executemany('INSERT INTO DimTienda VALUES (?, ?, ?, ?, ?, ?, ?)', tiendas)

    # Insertar datos en la tabla DimFecha
    fechas = [
        (1, '2024-10-20', 20, 10, 4, 2, 2024, 'Domingo', 'Octubre'),
        (2, '2024-10-21', 21, 10, 4, 2, 2024, 'Lunes', 'Octubre')
    ]
    cursor.executemany('INSERT INTO DimFecha VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', fechas)

    # Insertar datos en la tabla DimCategoria
    categorias = [
        (1, 'Frutas y Verduras', 'Productos frescos del campo'),
        (2, 'Lácteos', 'Productos derivados de la leche')
    ]
    cursor.executemany('INSERT INTO DimCategoria VALUES (?, ?, ?)', categorias)

    # Insertar datos en la tabla de hechos: HechosInventario
    hechos_inventario = [
        (1, 1, 1, 1, 50, 1.20, 2.50, 30, 10),
        (2, 2, 2, 2, 100, 0.80, 1.50, 50, 20)
    ]
    cursor.executemany('INSERT INTO HechosInventario VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', hechos_inventario)

    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    insertar_datos()
