def agregarPalabras(diccionario_jugadores, lista_palabra):
    palabraAleatoria = palabra_adivinar(lista_palabra)
    for jugador in diccionario_jugadores:
        diccionario_jugadores[jugador][2].append(palabraAleatoria)
    return diccionario_jugadores


def ingresar_letra():
    letra_ingresada = input("Ingrese una letra: ")
    letra_ingresada = letra_ingresada.upper()
    while len(letra_ingresada) != 1 and not letra_ingresada.isalpha():
        print("Ingreso un caracter invalido")
        letra_ingresada = input("Ingrese una letra: ")
    return letra_ingresada

ingresar_letra()