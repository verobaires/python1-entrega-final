import sqlite3

NOMBRE_BD = "libreria.db"
COLUMNAS = "id, nombre, descripcion, cantidad, precio, categoria"


def conectar():
    return sqlite3.connect(NOMBRE_BD)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


def agregar(nombre, descripcion, cantidad, precio, categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
            (nombre, descripcion, cantidad, precio, categoria),
        )
        conexion.commit()
        resultado = True
    except sqlite3.Error:
        conexion.rollback()
        resultado = False
    conexion.close()
    return resultado


def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT " + COLUMNAS + " FROM productos ORDER BY id")
    productos = cursor.fetchall()
    conexion.close()
    return productos


def obtener(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT " + COLUMNAS + " FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    return producto


def buscar_por_nombre(texto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT " + COLUMNAS + " FROM productos WHERE nombre LIKE ? ORDER BY id",
        ("%" + texto + "%",),
    )
    productos = cursor.fetchall()
    conexion.close()
    return productos


def buscar_por_categoria(texto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT " + COLUMNAS + " FROM productos WHERE categoria LIKE ? ORDER BY id",
        ("%" + texto + "%",),
    )
    productos = cursor.fetchall()
    conexion.close()
    return productos

def eliminar(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        resultado = True
    except sqlite3.Error:
        conexion.rollback()
        resultado = False
    conexion.close()
    return resultado
