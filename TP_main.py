from TP_auxiliar import *



def jugar_ahorcado():
    diccionario_palabras = generarDiccionarioPalabras()
    cant_jugadores = solicitarCantJugadores()
    diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)
    diccionario_partida = generarDiccionarioPartida()
    partida = diccionario_partida["nro_partida"]
    otorgarOrdenJugadores(partida, diccionario_jugadores)
    lista_jugadores_ordenado = sorted(diccionario_jugadores.items(), key=lambda x: x[1])

    print("los jugadores jugaran en el siguiente orden:\n")
    for jugador in lista_jugadores_ordenado:
        print(jugador[0])

    lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras)
    jugar = True
    ronda = 1
    while jugar:
        for jugador in lista_jugadores_ordenado:
            if ronda == 1:
                agregarPalabras(diccionario_jugadores, jugador, lista_palabras, diccionario_palabras)
            letra_ingresada = ingresarLetra()



        continuar = input("Desea continuar?")

        if continuar != "s":
            jugar = False
        ronda += 1



    #print(diccionario_jugadores) #lo agregue para checkear el diccionario antes de ser transformado
    #lista_palabras = generarListaPalabrasPorCantLetras(diccionario_palabras)
    #agregarPalabras(diccionario_jugadores, lista_palabras, diccionario_palabras) #funcion a prueba (Luan)
    #print("\nDEBUG: Lista de palabras generada")
    #print(lista_palabras)
    #palabra_a_adivinar = elegirPalabraAleatoria(lista_palabras)
    #print(palabra_a_adivinar)
    #print(diccionario_jugadores) #mostrar el diccionario despues de asignarle palabras a los jugadores

jugar_ahorcado()
