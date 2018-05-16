juego = True
nro_partida = 1

while juego:
    genero diccionario_palabras
    genero diccionario_jugadores
    partida = True

    while partida:
        diccionario_jugadores[orden]
        diccionario_jugadores[palabra]
        diccionario_jugadores[palabra_oculta]
        diccionario_palabras[palabra_usada] = True

        turno = True
        while turno:
            if diccionario_jugador[jugador_eliminado] == False:
                letra = elegir_letra()
                puntos = 0
                while letra in palabra
                    if letra not in diccionario_jugador[letras_acertadas]:
                        diccionario_jugador[letras_acertadas].append(letra)
                    diccionario_jugador[palabra_oculta].transformarGuionesBajos(letra)
                    puntos += 1

                if puntos > 0:
                    if diccionario_jugador[palabra_oculta] == diccionario_jugador[palabra]:
                        puntos += 30
                        diccionario_jugador[ganador_ultima_partida] = True
                        turno = False
                        partida = False
                    diccionario_jugador[puntaje] += puntos
                else:
                    puntos -= 2
                    diccionario_jugador[letras_erradas].append(letra)
                    if len(diccionario_jugador[letras_erradas]) == 7:
                        diccionario_jugador[jugador_eliminado] = True
                    diccionario_jugador[puntaje] += puntos
                    turno = False