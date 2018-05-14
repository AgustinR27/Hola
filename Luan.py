"""Tocan algo acá y les quemo el rancho..."""

from TP_auxiliar import *


"""La función pide el diccionario de los jugadores, la lista de palabras procesada (válida) y el diccionario de palabras. 
Se usa una palabra aleatoria de la lista de palabras y se le asigna a una lista vacia dentro del diccionario de los jugadores.
Luego esa palabra asignada adquiere el valor booleano True en el diccionario de palabras-
Devuelve el diccionario jugadores, cada jugador con una palabra aleatoria asignada"""


def agregarPalabras(diccionario_jugadores, lista_palabra, diccionario_palabras):
    for jugador in diccionario_jugadores:
        palabraAleatoria = palabra_adivinar(lista_palabra)
        diccionario_jugadores[jugador][2].append(palabraAleatoria)
        diccionario_palabras[palabraAleatoria][2] = True #no se si esto cambia el valor booleano, por ahi hay q usar un replace.
        print("CLAVE: {} - Valor: {}".format(palabraAleatoria,diccionario_palabras[palabraAleatoria]))
    return diccionario_jugadores


"""La función pide el diccionario de palabras. Se crea una lista con aquellas palabras cuyo valor booleano en el diccionario
es False. Se devuelve una lista de palabras con aquellas que no han sido utilizadas aún."""


def valorBooleano(diccionario_palabras):
    lista_palabra = []
    for palabra in diccionario_palabras:
        if diccionario_palabras[palabra][2] == False:
            lista_palabra.append(palabra)
    return lista_palabra

