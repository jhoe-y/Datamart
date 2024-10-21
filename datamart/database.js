import sqlite3 from 'sqlite3'
import { open } from 'sqlite'

export async function getDBConnection() {
    const db = await open({
        filename: './datamart_inventario.db',
        driver: sqlite3.Database
    })
    return db
}
