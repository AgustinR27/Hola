from TP_modulos import solicitarCantJugadores
from TP_modulos import generarDiccionarioJugadores
from TP_modulos import generarDiccionarioPalabras
from TP_modulos import otorgarOrdenJugadores
from TP_modulos import ingresarLetra
from TP_modulos import generarListaPalabrasPorCantLetras
from TP_modulos import generarDiccionarioPartida
from TP_modulos import almacenarDatosPartida
from TP_modulos import otorgarPalabrasJugadores
from TP_modulos import actualizarDiccionarioPalabras
from TP_modulos import transformarGuionesBajos
from TP_modulos import dibujarHombrecito
from TP_modulos import mostrarDatosTurno
from TP_modulos import pausaParaContinuar
from TP_modulos import mostrarDatosPartida
from TP_modulos import mostrarDatosGeneralesPartidas
from TP_modulos import limpiarDatosJugadoresPartidaAnterior

#DICCIONARIO PALABRAS
cantidad_repeticiones_palabra = 0
cantidad_letras_palabra = 1
palabra_usada = 2

#DICCIONARIO JUGADORES
orden_jugador = 0
puntaje_jugador = 1
palabra_actual = 2
palabra_a_adivinar = 3
palabra_oculta = 4
letras_acertadas = 5
letras_erradas = 6
ganador_ultima_partida = 7
jugador_eliminado = 8
hombrecito = 9

#tiempo de espera por cada jugada. Modificar este valor para agilizar el juego.
tiempo_de_espera_por_turno = 0.0



juego = True
nro_partida = 1

while juego:
    print("####TP1 AHORCADO####")
    print("------------------------------------------------------------------------------------------------------------------")
    print("Creadores: Mauro Cuquejo, Luan Corrionero, Agustín Ramirez, Darío Giménez.")
    print("------------------------------------------------------------------------------------------------------------------\n")
    print("TIPS: cuando se ingrese una letra, correcta o incorrecta, la pantalla solicitará presionar Enter para continuar. Tenga en cuenta esto antes ingresar una letra, para evitar confusiones.\n")

    #genero diccionario de palabras
    diccionario_palabras = generarDiccionarioPalabras()

    #genero cantidad de jugadores
    cant_jugadores = solicitarCantJugadores()

    #genero diccionario de jugadores
    diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores) #me salté la parte de preguntar cant jugadores

    #como todavia no se jugó una partida, genero un diccionario vacío.
    diccionario_partida = {}

    #al iniciar el juego, inicializo partida en True. Mientras sea True, se está jugando una partida.
    partida = True

    #mientras la partida esté jugándose.
    while partida:

        nro_ronda = 1

        #si la partida es nueva, debe generarse un registro con los datos de la partida.
        if nro_partida not in diccionario_partida:

            # genero diccionario de Partida.
            diccionario_partida = generarDiccionarioPartida(diccionario_partida, nro_partida)

        #establezco el orden de los jugadores en diccionario_jugadores[orden_jugador]
        otorgarOrdenJugadores(nro_partida, diccionario_jugadores)

        #borro datos residuales de la partida anterior
        limpiarDatosJugadoresPartidaAnterior(diccionario_jugadores)


        #establezco las palabras a adivinar en diccionario_jugadores[palabra_a_adivinar]
        #establezco las palabra oculta igual a la palabra a adivinar en diccionario_jugadores[palabra_oculta]
        #actualizo el diccionario_palabras[palabra_usada] = True para la palabra a adivinar
        lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras, cant_jugadores)
        lista_palabras_usadas = otorgarPalabrasJugadores(diccionario_jugadores, lista_palabras)
        actualizarDiccionarioPalabras(diccionario_palabras, lista_palabras_usadas)

        # Se armó una lista de la clave de los jugadores ordenados por el campo orden
        lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1][orden_jugador])]

        # cuando arranca la ronda, inicializo ronda en True. Mientras sea True, se jugaran los turnos de los jugadores.
        ronda = True

        #cuando arranca la partida, no hay ningún jugador eliminado.
        contador_jugadores_eliminados = 0
        while ronda:
            # cuando arranca el turno, inicializo turno en True. Mientras sea True, un jugador está jugando un turno.
            turno = True

            # inicializo la posicion por la que voy a recorrer lista_jugadores_ordenada
            posicion = 0
            print("PARTIDA NRO: {} - RONDA NRO: {}".format(nro_partida, nro_ronda))

            while turno:
                #para facilitar la lectura, guardo en una variable al jugador actual.
                jugador = lista_jugadores_ordenada[posicion]

                #al iniciar el turno un jugador, aun no registra aciertos.
                cont_aciertos = 0

                #el jugador sólo puede jugar si no está eliminado.
                if not diccionario_jugadores[jugador][jugador_eliminado]:

                    continuar_buscando_letra = True

                    while continuar_buscando_letra:
                        mostrarDatosTurno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
                        letra_ingresada = ingresarLetra()

                        #esto es para verificar si la letra está repetida más de una vez en v_palabra_a_adivinar
                        while letra_ingresada in diccionario_jugadores[jugador][palabra_a_adivinar]:

                            # agregamos la letra a una lista de letras acertadas durante el turno.
                            diccionario_jugadores[jugador][letras_acertadas].append(letra_ingresada)

                            #actualizo la palabra oculta, borrando los guiones bajos y guardando la posicion en la que lo borré
                            transformarGuionesBajos(letra_ingresada, jugador, diccionario_jugadores)

                            #por cada vez que encuentre la letra, sumo un punto al acumulador.
                            diccionario_jugadores[jugador][puntaje_jugador] += 1

                            cont_aciertos +=1

                        # si luego de verificar que existiera la letra en la palabra, no encontro nada, es porque el jugador falló.
                        if cont_aciertos == 0:
                            # resto dos puntos al acumulador
                            diccionario_jugadores[jugador][puntaje_jugador] -= 2

                            # agregamos la letra a una lista de letras erradas durante el turno.
                            diccionario_jugadores[jugador][letras_erradas].append(letra_ingresada)

                            # cantidad_de_errores equivale a la cantidad de errores del usuario
                            cantidad_de_errores = len(diccionario_jugadores[jugador][letras_erradas])

                            # dibujo en pantalla el hombrecito ahorcado. Por cada error se dibuja una parte del cuerpo
                            diccionario_jugadores[jugador][hombrecito] = dibujarHombrecito(cantidad_de_errores)

                            #muestro los datos del jugador.
                            mostrarDatosTurno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
                            if cant_jugadores > 1:
                                print("FALLASTE, {}. LE TOCA AL SIGUIENTE JUGADOR.".format(jugador))
                            else:
                                print("FALLASTE, {}. OTRA VEZ SERÁ.".format(jugador))
                            pausaParaContinuar()

                            #si el jugador falla, deja de pedirle letras.
                            continuar_buscando_letra = False

                            # si la cantidad de errores es igual a siete, es porque el jugador perdió.
                            if cantidad_de_errores == 7:
                                contador_jugadores_eliminados += 1

                                # si el jugador perdió, queda eliminado, por lo que no podrá volver a jugar durante la partida.
                                diccionario_jugadores[jugador][jugador_eliminado] = True

                                # muestro los datos del jugador.
                                mostrarDatosTurno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
                                print("PERDISTE, {}. SE ACABÓ LA PARTIDA PARA VOS.".format(jugador))
                                pausaParaContinuar()

                        else: #cont_aciertos > 0
                            #si coincide la palabra oculta con la palabra a adivinar, es porque el jugador ganó la partida.
                            if diccionario_jugadores[jugador][palabra_oculta] == diccionario_jugadores[jugador][palabra_actual]:
                                # suma treinta puntos al acumulador
                                diccionario_jugadores[jugador][puntaje_jugador] += 30

                                # le avisa al diccionario que ganó la última partida.
                                diccionario_jugadores[jugador][ganador_ultima_partida] = True

                                # si ganó la partida, se acaba su turno.
                                turno = False

                                # si ganó la partida, se acaba la ronda.
                                ronda = False

                                # si ganó la partida, se acaba la partida.
                                partida = False

                                # muestro los datos del jugador.
                                mostrarDatosTurno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
                                print("GANASTE, {}. ESTA PARTIDA SE ACABA ACÁ.".format(jugador))
                                pausaParaContinuar()

                                # si el jugador ganó, dejo de buscar letra.
                                continuar_buscando_letra = False
                            else:
                                mostrarDatosTurno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
                                print("ACERTASTE, {}. PODÉS SEGUIR INGRESANDO LETRAS.".format(jugador))
                                pausaParaContinuar()
                                cont_aciertos = 0

                #verifico si todos los jugadores fueron eliminados:
                if contador_jugadores_eliminados == cant_jugadores:
                    print("GANÓ COM.")
                    # si todos perdieron la partida, se acaba el turno.
                    turno = False

                    # si todos perdieron la partida, se acaba la ronda.
                    ronda = False

                    # si todos perdieron la partida, se acaba la partida.
                    partida = False

                #si no están todos los jugadores eliminados, se continúa jugando.
                else:
                    #una vez que terminó de ejecutar para este jugador, me muevo al siguiente,
                    # aumentando la posicion de la lista.
                    posicion += 1

                    #si posicion es mayor a la ultima posicion de la lista de jugadores, se termina el turno,
                    # para evitar un index of bounds
                    if posicion > len(lista_jugadores_ordenada) - 1:
                        turno = False
            nro_ronda += 1

        #una vez terminada la partida, se actualiza el diccionario de la partida para todos los jugadores.
        #haciendolo de esta forma, fuera de la ronda, me permite actualizar todos los datos juntos para
        # esta partida.
        almacenarDatosPartida(diccionario_partida[nro_partida], diccionario_jugadores.items())

        #al finalizar la partida se muestran los datos de la misma.
        mostrarDatosPartida(diccionario_partida,nro_partida)

        #una vez que se acaba la partida, se le pregunta al jugador si quiere continuar.
        continuar = input("desea continuar jugando? (S/N)")
        while not continuar.upper() in ("S", "N"):
            continuar = input("Opcion incorrecta. ¿desea continuar jugando? (S/N)")

        #si decide continuar, se actualizan el numero de partida
        if continuar.upper() == 'S':
            nro_partida += 1

            #como el usuario decide continuar, reactivo la partida.
            partida = True

        #sino, se finaliza la partida y el juego
        else:
            partida = False
            juego = False

            mostrarDatosGeneralesPartidas(diccionario_partida)