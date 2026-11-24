import colores


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        colores.error("Este campo no puede estar vacio.")


def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                return numero
            colores.error("El numero no puede ser negativo.")
        except ValueError:
            colores.error("Ingresa un número entero valido.")


def pedir_decimal(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= 0:
                return numero
            colores.error("El numero no puede ser negativo.")
        except ValueError:
            colores.error("Ingresa un número valido ( por ej: 1500.50).")
