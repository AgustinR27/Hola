from TP_modulos import solicitarCantJugadores
from TP_modulos import generarDiccionarioJugadores
from TP_modulos import generarDiccionarioPalabras
from TP_modulos import almacenarDatosPartida
from TP_modulos import mostrarDatosPartida
from TP_modulos import mostrarDatosGeneralesPartidas
from TP_modulos import procesarTurno
from TP_modulos import incializarPartida

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
    print("####AHORCADO####\nCreadores: Mauro Cuquejo, Luan Corrionero, Agustín Ramirez Perez, Darío Inserte su apellido aquí.\n"
          "TIPS: cuando se ingrese una letra, correcta o incorrecta, la pantalla solicitará presionar Enter para continuar. Tenga en cuenta esto antes ingresar una letra, para evitar confusiones.")
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

        #inicializo variables que se utilizaran durante la partida
        nro_ronda, diccionario_partida, lista_jugadores_ordenada, ronda, contador_jugadores_eliminados = incializarPartida(nro_partida, diccionario_partida, diccionario_jugadores, diccionario_palabras)
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
                procesarTurno(diccionario_jugadores, jugador, contador_jugadores_eliminados, cont_aciertos)

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

            #se le pregunta al jugador si desea visualizar los datos generales de las partidas jugadas.
            mostrar_datos_partida = input("¿Desea visualizar las estadísticas generales de las partidas jugadas? (S/N)")
            while not mostrar_datos_partida.upper() in ("S", "N"):
                mostrar_datos_partida = input("Opcion incorrecta. ¿Desea ver las palabras del diccionario? (S/N)")

            # si decide mostrarlos, se actualizan el numero de partida
            if mostrar_datos_partida.upper() == 'S':
                mostrarDatosGeneralesPartidas(diccionario_partida)