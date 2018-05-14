"""Tocan algo acá y les quemo el rancho..."""

from TP_auxiliar import *
from Agustinho import *

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

jugando = True

def turnos(diccionario_jugador, jugador):
    for jugador in diccionario_jugador:
        finTurno = False
        while finTurno == False:
            letra = ingresar_letra()
            palabra = diccionario_jugador[jugador][2]
            if letra not in palabra:
                finTurno = True




def evaluacion(letra_ingresada, palabra):
    valor = False
    if letra not in palabra:
        valor = True
    return valor

def turnosYJuego(diccionario_jugador):
    finJuego = False
    while finJuego == False:
        for jugador in diccionario_jugador:
            print(jugador)
            letrasIncorrectas = ""
            letrasCorrectas = ""
            dic_palabras = obtener_palabras()
            lista_palabras = enlistar_palabras(dic_palabras)
            palabraOculta = palabra_adivinar(lista_palabras)
            finTurno = False
            while finTurno == False:
                juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
                letra = ingresar_letra()
                if letra in palabraOculta:
                    letrasCorrectas = letrasCorrectas + letra
                    # Se fija si el jugador ganó
                    letrasEncontradas = True
                    for i in range(len(palabraOculta)):
                        if palabraOculta[i] not in letrasCorrectas:
                            letrasEncontradas = False
                            break
                    if letrasEncontradas:
                        print('¡Ganaste! Despues de ' + str(len(letrasIncorrectas)) + ' fallas y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era ' + palabraOculta)
                        finTurno = True
                        funJuego = True
                else:
                    letrasIncorrectas += letra + " "
                    # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
                    if len(letrasIncorrectas) >= 14:
                        juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
                        print('¡Te quedaste sin intentos!\nDespues de ' + str(len(letrasIncorrectas)) + ' fallas y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era ' + palabraOculta)
                    finTurno = True

list = ("Luan", "Luis")
turnosYJuego(list)