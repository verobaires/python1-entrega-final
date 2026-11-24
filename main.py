import base_datos
import colores
import entradas



def mostrar_productos(productos):
    if len(productos) == 0:
        colores.error("No se encontraron libros.")
    else:
        for id_producto, titulo, detalle, ejemplares, precio, genero in productos:
            print(f"ID: {id_producto} | {titulo} | {detalle} | Ejemplares: {ejemplares} | Precio: ${precio} | Género: {genero}")


def agregar_libro():
    titulo = entradas.pedir_texto("\nTítulo del libro: ")
    detalle = entradas.pedir_texto("Autor y estado (ejemplo: Borges, muy bueno): ")
    ejemplares = entradas.pedir_entero("Cantidad de ejemplares: ")
    precio = entradas.pedir_decimal("Precio: ")
    genero = entradas.pedir_texto("Género (ejemplo: Novela, Poesía, Historia): ")

    if base_datos.agregar(titulo, detalle, ejemplares, precio, genero):
        colores.exito(f"{titulo} agregado correctamente.")
    else:
        colores.error("No se pudo agregar el libro.")


def buscar_por_titulo():
    texto = entradas.pedir_texto("\nTítulo a buscar: ")
    mostrar_productos(base_datos.buscar_por_nombre(texto))


def buscar_por_genero():
    texto = entradas.pedir_texto("\nGénero a buscar: ")
    mostrar_productos(base_datos.buscar_por_categoria(texto))

def eliminar_libro():
    id_producto = entradas.pedir_entero("\nID del libro a eliminar (vendido o dado de baja): ")
    libro = base_datos.obtener(id_producto)

    if libro is None:
        colores.error("No existe un libro con ese ID.")
        return

    mostrar_productos([libro])
    confirmacion = input("¿Seguro que querés eliminarlo? (S/N): ").upper().strip()

    if confirmacion != "S":
        colores.error("Eliminación cancelada.")
    elif base_datos.eliminar(id_producto):
        colores.exito("Libro eliminado correctamente.")
    else:
        colores.error("No se pudo eliminar el libro.")



base_datos.crear_tabla()

while True:
    opcion = input("""
    L - Listar libros
    A - Agregar libro
    T - Buscar por título
    G - Buscar por género
    E - Eliminar libro   
    S - Salir
    Opción: """).upper().strip()

    match opcion:
        case "L":
            mostrar_productos(base_datos.listar())
        case "A":
            agregar_libro()
        case "T":
            buscar_por_titulo()
        case "G":
            buscar_por_genero()
      
        case "E":
            eliminar_libro()
      
        case "S":
            colores.exito("Programa finalizado.")
            break
        case _:
            colores.error("Opción no valida.")
