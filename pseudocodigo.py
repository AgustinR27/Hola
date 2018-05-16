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
    #genero diccionario de palabras
    diccionario_palabras = generarDiccionarioPalabras()

    #genero diccionario de jugadores

    diccionario_jugadores = generarDiccionarioJugadores(2) #me salté la parte de preguntar cant jugadores

    #al iniciar el juego, inicializo partida en True. Mientras sea True, se está jugando una partida.
    partida = True
    #al iniciar el juego, inicializo partida_nueva en True. Al iniciar una partida nueva, deben ejecutarse algunas acciones especiales.
    partida_nueva = True

    #mientras la partida esté jugándose.
    while partida:
        #ejecutar sólo si la partida es nueva.
        if partida_nueva
            #establezco el orden de los jugadores en diccionario_jugadores[orden_jugador]
            otorgarOrdenJugadores(nro_partida, diccionario_jugadores)

            #si es la primera partida, ordeno a los jugadores
            if nro_partida == 1:
                #establezco las palabras a adivinar en diccionario_jugadores[palabra_a_adivinar]
                #establezco las palabra oculta igual a la palabra a adivinar en diccionario_jugadores[palabra_oculta]
                #actualizo el diccionario_palabras[palabra_usada] = True para la palabra a adivinar
                lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras)
                lista_palabras_usadas = otorgarPalabrasJugadores(lista_palabras)
                actualizarDiccionarioPalabras(lista_palabras_usadas)

        #cuando arranca el turno, inicializo turno en True. Mientras sea True, un jugador está jugando un turno.
        turno = True

        #aca hice un truquito con listas por comprension.
        # Armé una lista de la clave de los jugadores ordenados por el campo orden
        lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1])]

        #inicializo la posicion por la que voy a recorrer lista_jugadores_ordenada
        posicion = 0

        #mientras el turno esté jugandose
        while turno:
            #para facilitar la lectura, guardo en una variable al jugador actual.
            jugador = lista_jugadores_ordenada[posicion]

            #el jugador sólo puede jugar si no está eliminado.
            if diccionario_jugadores[jugador][jugador_eliminado] == False:
                #se le solicita ingresar una letra al jugador.
                letra = ingresarLetra()

                #inicializo el puntaje que va a obtener el jugador durante su turno.
                puntos = 0

                #guardo una variable de tipo lista con la palabra a adivinar, para poder ir modificandola.
                # De todas formas, vamos a tener que modificarlo por una posicion del diccionario,
                # para poder acceder a ella en el siguiente turno. Sino la perderíamos cuando cambie el turno.
                # IMPORTANTE: Tener en cuenta que al cambiar el diccionario, cambian las constantes arriba definidas.
                v_palabra_a_adivinar = diccionario_jugadores[jugador][palabra_a_adivinar]

                #esto es para verificar si la letra está repetida más de una vez en v_palabra_a_adivinar
                while letra in v_palabra_a_adivinar:
                    #este if es para evitar agregar letras repetidas. OBSERVACION IMPORTANTE: por ahi es mejor dejar
                    # que se repitan para que si el jugador, por ejemplo, adivinó las primeras 4 letras
                    # de ABACO (o sea, ABAC), marque 4 letras acertadas haciendo el
                    # len(diccionario_jugadores[jugador][letras_acertadas])
                    if letra not in diccionario_jugadores[jugador][letras_acertadas]:
                        # agregamos la letra a una lista de letras acertadas durante el turno.
                        # IMPORTANTE: CAMPO PARA INICIALIZAR EN SIGUIENTE PARTIDA (me faltaria revisar el resto de los campos)
                        diccionario_jugadores[jugador][letras_acertadas].append(letra)
                    #actualizo la palabra oculta, borrando los guiones bajos y guardando la posicion en la que lo borré
                    pos = diccionario_jugadores[jugador][palabra_oculta].transformarGuionesBajos(letra)
                    #conociendo la posicion, directamente la modifico por un guión bajo en palabra adivinar,
                    # para marcarla como "encontrada"
                    v_palabra_a_adivinar[pos] = "_"
                    puntos += 1

                if puntos > 0:
                    if diccionario_jugadores[jugador][palabra_oculta] == diccionario_jugadores[jugador][palabra_a_adivinar]:
                        puntos += 30
                        diccionario_jugadores[jugador][ganador_ultima_partida] = True
                        turno = False
                        partida = False
                        partida_nueva = True
                        diccionario_jugadores[jugador][puntaje_jugador] += puntos
                else:
                    puntos -= 2
                    diccionario_jugadores[jugador][letras_erradas].append(letra)
                    if len(diccionario_jugadores[jugador][letras_erradas]) == 7:
                        diccionario_jugadores[jugador][jugador_eliminado] = True
                        diccionario_jugadores[jugador][puntaje_jugador] += puntos
                    turno = False
                    partida_nueva = False
            posicion += 1

            #si posicion es mayor a la ultima posicion de la lista de jugadores, se termina el turno
            if posicion > len(lista_jugadores_ordenada) - 1:
                turno = False
        nro_partida += 1