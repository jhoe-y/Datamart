import express from 'express'
import { getDBConnection } from '../database.js'

const router = express.Router()

router.get('/', async (req, res) => {
    try {
        const db = await getDBConnection()
        const inventario = await db.all(`
            SELECT p.nombre_producto, t.nombre_tienda, f.fecha_completa, c.nombre_categoria, h.cantidad_disponible
            FROM HechosInventario h
            JOIN DimProducto p ON h.producto_id = p.producto_id
            JOIN DimTienda t ON h.tienda_id = t.tienda_id
            JOIN DimFecha f ON h.fecha_id = f.fecha_id
            JOIN DimCategoria c ON h.categoria_id = c.categoria_id
        `)
        res.json(inventario)
        await db.close()
    } catch (error) {
        console.error('Error al obtener los datos del inventario:', error)
        res.status(500).json({ error: 'Error al obtener los datos del inventario', details: error.message })
    }
})

export default router
