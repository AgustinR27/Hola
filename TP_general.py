def validarLetra(valor):
    while len(valor) != 1 or not valor.isalpha():
        valor = solicitarLetra("Por favor ingrese solo una letra valida: ")
    return valor

def validarNombre(nombre):
    while len(nombre) < 3 or not nombre.isalpha():
        nombre = solicitarNombreJugador("Por favor ingrese un nombre válido: ")
    return nombre


def solicitarLetra(mensaje):
    letra = input(mensaje)
    letra_valida = validarLetra(letra).upper()
    return letra_valida


def solicitarNombreJugador(mensaje):
    nombre = input(mensaje)
    nombre_valido = validarNombre(nombre)
    return nombre_valido


def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor


print(solicitarNombreJugador("Ingrese su nombre: "))
print(solicitarLetra("Ingrese una letra: "))