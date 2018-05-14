"""Tocan algo acá y les quemo el rancho..."""

from TP_auxiliar import *

"""Para esta funcion se requiere el diccionario de los jugadores, el jugador al cual se le van a modificar los puntos y
el parámetro. El parámetro va a ser un "acierto" para sumar 1 punto, "desacierto" para restar 2 puntos y "victoria" para
sumar 30 puntos. El parámetro tiene que estar escrito de forma exacta a como se pide para que funcione"""


def actualizarPuntos(diccionario_jugador, jugador, parametro):
    if parametro == "acierto":
        diccionario_jugador[jugador] += 1
    elif parametro == "desacierto":
        diccionario_jugador[jugador] -= 2
    if parametro == "victoria":
        diccionario_jugador[jugador] += 30
    return diccionario_jugador



