"""Tocan algo acá y les quemo el rancho..."""

from TP_auxiliar import *

"""Se pide el diccionario y el jugador a quien se le sumará puntos. El jugador (clave del diccionario) sumara 1 punto cada
vez que se llame la funcion"""


def actualizarpuntos(diccionario_jugador, jugador, acierto, victoria):
    if acierto == True:
        diccionario_jugador[jugador][1] += 1
    else:
        diccionario_jugador[jugador][1] -= 2
    if victoria == True:
        diccionario_jugador[jugador][1] += 30
    return diccionario_jugador



