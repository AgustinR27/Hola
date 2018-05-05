from TP_auxiliar import generarDiccionarioPalabras
from TP_auxiliar import solicitarCantJugadores
from TP_auxiliar import  generarDiccionarioJugadores

def jugar_ahorcado():
    diccionario_palabras = generarDiccionarioPalabras()
    print(diccionario_palabras.keys())
    cant_jugadores = solicitarCantJugadores()
    diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)
    print(diccionario_jugadores.keys())

jugar_ahorcado()