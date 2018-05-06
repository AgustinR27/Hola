from TP_auxiliar import *

def jugar_ahorcado():
    diccionario_palabras = generarDiccionarioPalabras()
    cant_jugadores = solicitarCantJugadores()
    diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)
    diccionario_partida = generarDiccionarioPartida()
    partida = diccionario_partida["nro_partida"]
    otorgarOrdenJugadores(partida, diccionario_jugadores)
    lista_jugadores_ordenado = sorted(diccionario_jugadores.items(), key = lambda x : x[1])

    for jugador in lista_jugadores_ordenado:
        print(jugador[0])


jugar_ahorcado()