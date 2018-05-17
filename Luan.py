from maurinho import *

#DICCIONARIO PALABRAS
cantidad_repeticiones_palabra = 0
cantidad_letras_palabra = 1
palabra_usada = 2

#DICCIONARIO JUGADORES
orden_jugador = 0
puntaje_jugador = 1
palabra_a_adivinar = 2
palabra_oculta = 3
letras_acertadas = 4
letras_erradas = 5
ganador_ultima_partida = 6
jugador_eliminado = 7


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
    diccionario_palabras[palabra][palabra_usada] = True
    return diccionario_palabras
