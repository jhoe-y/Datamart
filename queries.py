from database import obtener_conexion

def consultar_inventario():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT p.nombre_producto, t.nombre_tienda, f.fecha_completa, c.nombre_categoria, h.cantidad_disponible
        FROM HechosInventario h
        JOIN DimProducto p ON h.producto_id = p.producto_id
        JOIN DimTienda t ON h.tienda_id = t.tienda_id
        JOIN DimFecha f ON h.fecha_id = f.fecha_id
        JOIN DimCategoria c ON h.categoria_id = c.categoria_id
    ''')

    resultados = cursor.fetchall()

    for fila in resultados:
        print(f'Producto: {fila[0]}, Tienda: {fila[1]}, Fecha: {fila[2]}, Categoría: {fila[3]}, Cantidad Disponible: {fila[4]}')

    conexion.close()

if __name__ == '__main__':
    consultar_inventario()
