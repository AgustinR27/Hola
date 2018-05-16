from maurinho import *


def generarPalabrasAleatorias(lista_palabras):
    palabraAleatoria = lista_palabras.pop(random.randint(0, len(lista_palabras) - 1))
    actualizarDiccionarioPalabras(palabraAleatoria)
    return palabraAleatoria


def otorgarPalabrasJugadores(diccionario_jugadores, lista_palabras_no_usadas):
    for jugador in diccionario_jugadores:
        palabra = generarPalabrasAleatorias(lista_palabras_no_usadas)
        diccionario_jugadores[jugador][palabra_a_adivinar].append(palabra)
    return diccionario_jugadores


def actualizarDiccionarioPalabras(diccionario_palabras, palabra):
    diccionario_palabras[palabra][2] = True
    return diccionario_palabras
