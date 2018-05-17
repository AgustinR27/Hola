from maurinho import solicitarCantJugadores
from maurinho import generarDiccionarioJugadores
from maurinho import generarDiccionarioPalabras
from maurinho import otorgarOrdenJugadores
from maurinho import ingresarLetra
from maurinho import generarListaPalabrasPorCantLetras
from maurinho import generarDiccionarioPartida
from maurinho import almacenarDatosPartida
from maurinho import otorgarPalabrasJugadores
from maurinho import actualizarDiccionarioPalabras
from maurinho import transformarGuionesBajos
from maurinho import dibujarHombrecito
import time
import os


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



juego = True
nro_partida = 1

while juego:

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

    #al iniciar el juego, inicializo partida_nueva en True. Al iniciar una partida nueva, deben ejecutarse algunas acciones especiales.
    partida_nueva = True

    #mientras la partida esté jugándose.
    while partida:

        nro_ronda = 1

        #si la partida es nueva, debe generarse un registro con los datos de la partida.
        if nro_partida not in diccionario_partida:

            # genero diccionario de Partida.
            diccionario_partida = generarDiccionarioPartida(diccionario_partida, nro_partida)

        #establezco el orden de los jugadores en diccionario_jugadores[orden_jugador]
        otorgarOrdenJugadores(nro_partida, diccionario_jugadores)

        if partida > 1:
            ####IMPORTANTE#####
            #borro datos residuales de la partida anterior
            for jugador in diccionario_jugadores:
                diccionario_jugadores[jugador][palabra_a_adivinar] = []
                diccionario_jugadores[jugador][palabra_actual] = []
                diccionario_jugadores[jugador][palabra_oculta] = []
                diccionario_jugadores[jugador][letras_acertadas] = []
                diccionario_jugadores[jugador][letras_erradas] = []
                diccionario_jugadores[jugador][jugador_eliminado] = False
                diccionario_jugadores[jugador][ganador_ultima_partida] = False
                diccionario_jugadores[jugador][hombrecito] = ""


        #establezco las palabras a adivinar en diccionario_jugadores[palabra_a_adivinar]
        #establezco las palabra oculta igual a la palabra a adivinar en diccionario_jugadores[palabra_oculta]
        #actualizo el diccionario_palabras[palabra_usada] = True para la palabra a adivinar
        lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras)
        lista_palabras_usadas = otorgarPalabrasJugadores(diccionario_jugadores, lista_palabras)
        actualizarDiccionarioPalabras(diccionario_palabras, lista_palabras_usadas)

        #aca hice un truquito con listas por comprension.
        # Armé una lista de la clave de los jugadores ordenados por el campo orden
        lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1][orden_jugador])]

        ronda = True
        contador_jugadores_eliminados = 0
        while ronda:
            # cuando arranca el turno, inicializo turno en True. Mientras sea True, un jugador está jugando un turno.
            turno = True
            # inicializo la posicion por la que voy a recorrer lista_jugadores_ordenada
            posicion = 0

            #mientras el turno esté jugandose
            while turno:
                #para facilitar la lectura, guardo en una variable al jugador actual.
                jugador = lista_jugadores_ordenada[posicion]


                #el jugador sólo puede jugar si no está eliminado.
                if not diccionario_jugadores[jugador][jugador_eliminado]:
                    print("\n" * 100)
                    print(jugador, "obtuvo ", diccionario_jugadores[jugador][puntaje_jugador], " puntos")
                    print("DEBUG: Su palabra es", " ".join(diccionario_jugadores[jugador][palabra_actual]))
                    print("Ingreso correctamente las letras: ", diccionario_jugadores[jugador][letras_acertadas])
                    print("Y fallo en: ", diccionario_jugadores[jugador][letras_erradas])
                    print(" ".join(diccionario_jugadores[jugador][palabra_oculta]))
                    print(diccionario_jugadores[jugador][hombrecito])

                    #se le solicita ingresar una letra al jugador.
                    letra_ingresada = ingresarLetra()

                    #guardo una variable de tipo lista con la palabra a adivinar, para poder ir modificandola.
                    # De todas formas, vamos a tener que modificarlo por una posicion del diccionario,
                    # para poder acceder a ella en el siguiente turno. Sino la perderíamos cuando cambie el turno.
                    # IMPORTANTE: Tener en cuenta que al cambiar el diccionario, cambian las constantes arriba definidas.

                    if letra_ingresada in diccionario_jugadores[jugador][palabra_a_adivinar]:
                        #esto es para verificar si la letra está repetida más de una vez en v_palabra_a_adivinar
                        while letra_ingresada in diccionario_jugadores[jugador][palabra_a_adivinar]:

                            #este if es para evitar agregar letras repetidas. OBSERVACION IMPORTANTE: por ahi es mejor dejar
                            # que se repitan para que si el jugador, por ejemplo, adivinó las primeras 4 letras
                            # de ABACO (o sea, ABAC), marque 4 letras acertadas haciendo el
                            # len(diccionario_jugadores[jugador][letras_acertadas])


                            # agregamos la letra a una lista de letras acertadas durante el turno.
                            # IMPORTANTE: CAMPO PARA INICIALIZAR EN SIGUIENTE PARTIDA (me faltaria revisar el resto de los campos)
                            diccionario_jugadores[jugador][letras_acertadas].append(letra_ingresada)

                            #actualizo la palabra oculta, borrando los guiones bajos y guardando la posicion en la que lo borré
                            transformarGuionesBajos(letra_ingresada, jugador, diccionario_jugadores)

                            #por cada vez que encuentre la letra, sumo un punto al acumulador.
                            diccionario_jugadores[jugador][puntaje_jugador] += 1

                        #al terminar de correr el while, si coincide la palabra oculta con la palabra a adivinar,
                        # es porque el jugador ganó la partida.
                        if diccionario_jugadores[jugador][palabra_oculta] == diccionario_jugadores[jugador][palabra_actual]:

                            #suma treinta puntos al acumulador
                            diccionario_jugadores[jugador][puntaje_jugador] += 30

                            #le avisa al diccionario que ganó la última partida.
                            # OBSERVACION IMPORTANTE: ESTE DATO SE TIENE QUE REINICIAR CUANDO GANE OTRO LA SIGUIENTE PARTIDA
                            diccionario_jugadores[jugador][ganador_ultima_partida] = True

                            #si ganó la partida, se acaba su turno.
                            turno = False

                            # si ganó la partida, se acaba la ronda.
                            ronda = False

                            #si ganó la partida, se acaba la partida.
                            partida = False

                        print("\n" * 100)
                        print(jugador, "obtuvo ", diccionario_jugadores[jugador][puntaje_jugador], " puntos")
                        print("DEBUG: Su palabra es", " ".join(diccionario_jugadores[jugador][palabra_actual]))
                        print("Ingreso correctamente las letras: ", diccionario_jugadores[jugador][letras_acertadas])
                        print("Y fallo en: ", diccionario_jugadores[jugador][letras_erradas])
                        print(" ".join(diccionario_jugadores[jugador][palabra_oculta]))
                        print(diccionario_jugadores[jugador][hombrecito])
                        letra_ingresada = ingresarLetra()

                    # Si letra_ingresada not in diccionario_jugadores[jugador][palabra_a_adivinar], por lo que es un intento fallado.
                    else:
                        #resto dos puntos al acumulador
                        diccionario_jugadores[jugador][puntaje_jugador] -= 2

                        # agregamos la letra a una lista de letras erradas durante el turno.
                        # IMPORTANTE: CAMPO PARA INICIALIZAR EN SIGUIENTE PARTIDA
                        # (me faltaria revisar el resto de los campos)
                        diccionario_jugadores[jugador][letras_erradas].append(letra_ingresada)

                        #equivale a la cantidad de errores del usuario
                        cantidad_de_errores = len(diccionario_jugadores[jugador][letras_erradas])

                        #dibujo en pantalla el ahorcado. Por cada error se dibuja una parte del cuerpo
                        diccionario_jugadores[jugador][hombrecito] = dibujarHombrecito(cantidad_de_errores)
                        print("\n" * 100)
                        print(jugador, "obtuvo ", diccionario_jugadores[jugador][puntaje_jugador], " puntos")
                        print("DEBUG: Su palabra es", " ".join(diccionario_jugadores[jugador][palabra_actual]))
                        print("Ingreso correctamente las letras: ", diccionario_jugadores[jugador][letras_acertadas])
                        print("Y fallo en: ", diccionario_jugadores[jugador][letras_erradas])
                        print(" ".join(diccionario_jugadores[jugador][palabra_oculta]))
                        print(diccionario_jugadores[jugador][hombrecito])

                        #si la cantidad de errores es igual a siete, es porque perdió.
                        if cantidad_de_errores == 7:
                            contador_jugadores_eliminados += 1
                            #si el jugador perdió, queda eliminado, por lo que no podrá volver a jugar durante la partida.
                            diccionario_jugadores[jugador][jugador_eliminado] = True

                #verifico si todos los jugadores fueron eliminados, con una funcion que recorra todos y verifique que:
                if contador_jugadores_eliminados == cant_jugadores:
                    print("Ganó COM.")
                    # si todos perdieron la partida, se acaba su turno.
                    turno = False

                    # si todos perdieron la partida, se acaba la ronda.
                    ronda = False

                    # si todos perdieron la partida, se acaba la partida.
                    partida = False

                #si no están todos los jugadores eliminados, tiene sentido seguir avanzando.
                else:
                    #una vez que terminé de ejecutar para este jugador, me muevo al siguiente,
                    # aumentando la posicion de la lista.
                    posicion += 1

                    #si posicion es mayor a la ultima posicion de la lista de jugadores, se termina el turno,
                    # para evitar un index of bounds
                    if posicion > len(lista_jugadores_ordenada) - 1:
                        turno = False

        #una vez terminada la partida, se actualiza el diccionario de la partida para todos los jugadores.
        #haciendolo de esta forma, fuera de la ronda, me permite actualizar todos los datos juntos para
        # esta partida.
        almacenarDatosPartida(diccionario_partida, diccionario_jugadores.items())

        #una vez que se acaba la partida, se le pregunta al jugador si quiere continuar.
        continuar = input("desea continuar jugando? (S/N)")
        while not continuar.upper() not in ("S", "N"):
            continuar = input("Opcion incorrecta. ¿desea continuar jugando? (S/N)")

        #si decide continuar, se actualizan el numero de partida
        if continuar == 'S':
            nro_partida += 1

            #como el usuario decide continuar, reactivo la partida.
            partida = True

        #sino, se finaliza la partida
        else:
            partida = False
            juego = False

            #una vez finalizado el juego, se muestran los datos de las partidas.
            print("DATOS DE LAS PARTIDAS:\n")
            print(diccionario_partida)

            #tambien se muestran las palabras ordenadas alfabéticamente.
            #se muestran de a 500 palabras, junto con su número de repeticiones.
            #además se muestra el número de palabra.
            lista_palabras_ordenadas = sorted(diccionario_palabras.keys())
            print("PALABRAS DEL DICCIONARIO y CANTIDAD DE REPETICIONES:\n")
            auxiliar = ""
            for indice, palabra in enumerate(lista_palabras_ordenadas):
                auxiliar += "Palabras: {} - Cantidad de repeticiones: {} - ".format(palabra,diccionario_palabras[palabra])

                #esto verifica que se frene el print cada 500 registros. Se queda unos 5 segundos y continúa imprimiendo.
                if indice % 5 == 0:
                    time.sleep(0.05)
                    print(auxiliar)
                    auxiliar = ""
            if auxiliar != "":
                print(auxiliar)