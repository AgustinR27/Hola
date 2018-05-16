from TP_auxiliar import *

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

juego = True
nro_partida = 1

while juego:
    diccionario_palabras = generarDiccionarioPalabras()
    diccionario_jugadores = generarDiccionarioJugadores(2)
    partida = True
    partida_nueva = True
    while partida:
        if partida_nueva:
            #diccionario_jugadores[orden_jugador]
            otorgarOrdenJugadores(partida, diccionario_jugadores)

            #diccionario_jugadores[palabra_a_adivinar]
            #diccionario_jugadores[palabra_oculta]
            #diccionario_palabras[palabra_usada] = True
            lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras)
            lista_palabras_usadas = otorgarPalabrasJugadores(lista_palabras)
            actualizarDiccionarioPalabras(lista_palabras_usadas)

        turno = True
        lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1])]
        posicion = 0
        while turno:
            jugador = lista_jugadores_ordenada[posicion] 
            if diccionario_jugadores[jugador][jugador_eliminado] == False:
                letra = ingresarLetra()
                puntos = 0
                v_palabra_a_adivinar = diccionario_jugadores[jugador][palabra_a_adivinar]
                while letra in v_palabra_a_adivinar:
                    if letra not in diccionario_jugadores[jugador][letras_acertadas]:
                        diccionario_jugadores[jugador][letras_acertadas].append(letra)
                    pos = diccionario_jugadores[jugador][palabra_oculta].transformarGuionesBajos(letra)
                    v_palabra_a_adivinar[pos] = "_"
                    puntos += 1

                if puntos > 0:
                    if diccionario_jugadores[jugador][palabra_oculta] == diccionario_jugadores[jugador][palabra_a_adivinar]:
                        puntos += 30
                        diccionario_jugadores[jugador][ganador_ultima_partida] = True
                        turno = False
                        partida = False
                        diccionario_jugadores[jugador][puntaje_jugador] += puntos
                else:
                    puntos -= 2
                    diccionario_jugadores[jugador][letras_erradas].append(letra)
                    if len(diccionario_jugadores[jugador][letras_erradas]) == 7:
                        diccionario_jugadores[jugador][jugador_eliminado] = True
                        diccionario_jugadores[jugador][puntaje_jugador] += puntos
                    turno = False