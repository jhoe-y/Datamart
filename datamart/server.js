// server.js
import express from 'express'
import path from 'path'
import inventoryRoutes from './routes/inventoryRoutes.js'

const app = express()
const PORT = 3000

app.use(express.static('public'))

app.use('/api/inventory', inventoryRoutes)

app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en http://localhost:${PORT}`)
})
