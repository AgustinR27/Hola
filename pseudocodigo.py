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
    genero diccionario_palabras
    genero diccionario_jugadores
    partida = True

    while partida:
        diccionario_jugadores[orden_jugador]
        diccionario_jugadores[palabra_a_adivinar]
        diccionario_jugadores[palabra_oculta]
        diccionario_palabras[palabra_usada] = True

        turno = True
        lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1])]
        posicion = 0
        while turno:
            jugador = lista_jugadores_ordenada[posicion] 
            if diccionario_jugador[jugador][jugador_eliminado] == False:
                letra = elegir_letra()
                puntos = 0
                while letra in palabra
                    if letra not in diccionario_jugador[jugador][letras_acertadas]:
                        diccionario_jugador[jugador][letras_acertadas].append(letra)
                    diccionario_jugador[jugador][palabra_oculta].transformarGuionesBajos(letra)
                    puntos += 1

                if puntos > 0:
                    if diccionario_jugador[jugador][palabra_oculta] == diccionario_jugador[jugador][palabra]:
                        puntos += 30
                        diccionario_jugador[jugador][ganador_ultima_partida] = True
                        turno = False
                        partida = False
                    diccionario_jugador[jugador][puntaje] += puntos
                else:
                    puntos -= 2
                    diccionario_jugador[jugador][letras_erradas].append(letra)
                    if len(diccionario_jugador[jugador][letras_erradas]) == 7:
                        diccionario_jugador[jugador][jugador_eliminado] = True
                    diccionario_jugador[jugador][puntaje] += puntos
                    turno = False