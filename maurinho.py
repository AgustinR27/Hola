from TP_texto import obtener_texto
import random
from random import shuffle

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


def dibujarHombrecito(nro_desaciertos):
    dibujo = ""
    hombrecito = ["\n | \n | \n", " 0\n", "/", "|", "\ \n", "/", " \ \n"]

    for posicion in range(nro_desaciertos):
        dibujo += "".join(hombrecito[posicion])
    return dibujo


def formatearPalabra(palabra):
    dic_a_reemplazar = {"Ñ": "NI", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}
    palabra_vieja = palabra.upper()
    palabra_nueva = ''
    for letra in palabra_vieja:
        if letra not in dic_a_reemplazar:
            palabra_nueva += letra
        else:
            palabra_nueva += dic_a_reemplazar[letra]
    return palabra_nueva


def generarDiccionarioPalabras():
    #a partir del string pasado por los profesores, se genera un diccionario de palabras con el siguiente formato:
    #clave = palabra valor = lista compuesta por [cantidad_de_repeticiones, cant_letras, palabra_ya_utilizada]
    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_auxiliar = linea.split(" ")
            for palabra in lista_auxiliar:
                if palabra.isalpha() and len(palabra) >= 5:
                    if formatearPalabra(palabra) not in dic_palabras:
                        dic_palabras[formatearPalabra(palabra)] = [1, len(palabra), False]
                    else:
                        dic_palabras[formatearPalabra(palabra)][cantidad_repeticiones_palabra] += 1
    return dic_palabras


def solicitarCantJugadores():
    continuar = True
    cant_jugadores = input("Ingrese la cantidad de jugadores: ")
    while continuar:
        if not cant_jugadores.isdigit():
            print("Valor incorrecto. La cantidad de jugadores debe ser numérica.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        elif int(cant_jugadores) < 2 or int(cant_jugadores) > 10:
            print("Valor incorrecto, la cantidad de jugadores jugadores minima es de dos jugadores y como máximo,"
                  " pueden jugar diez personas.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        else:
            continuar = False
    return int(cant_jugadores)


def solicitarNombreJugador():
    nombre_jugador = input("Ingrese Nombre para el Jugador: ")
    while not nombre_jugador.replace(" ", "").isalpha():
        nombre_jugador = input("Nombre incorrecto. Ingrese Nombre Jugador: ")
    return nombre_jugador


#MODIFICAR!------------------------------------------------------------------------------------------


def generarDiccionarioJugadores(cant_jugadores):
    #a partir de una cantidad de jugadores pasada por parametro, se solicita dicha cantidad de veces el nombre de jugadores.
    # Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [orden, puntaje, palabra, palabra a_adivinar, palabra_oculta, letras_acertadas,letras_falladas, ganador_ultima_partida, jugador_eliminado]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitarNombreJugador()
        if formatearPalabra(jugador) not in dic_jugadores:
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], [], [], [], [], False, False]
        else:
            while formatearPalabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto.")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], [], [], [], [], False, False]
    return dic_jugadores


#-------------------------------------------------------------------------------------------------------


def otorgarOrdenJugadoresPrimeraRonda(dic_jugadores, lista_jugadores):
    for indice in range(len(lista_jugadores)):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][orden_jugador] = indice+1


def separarGanadorAnteriorPartida(dic_jugadores, lista_jugadores):
    condicion = True
    cont = 0
    while condicion and cont <= len(lista_jugadores) - 1:
        valor_jugador = lista_jugadores[cont]
        ganador_ult_partida = dic_jugadores[valor_jugador][ganador_ultima_partida]
        if ganador_ult_partida == True:
            dic_jugadores[valor_jugador][orden_jugador] = 1
            lista_jugadores.pop(cont)
            condicion = False
        cont += 1

#REVISAR!---------------------------------------------------------------------------------------


def otorgarOrdenJugadoresGeneral(dic_jugadores, lista_jugadores):
    dic_auxiliar = {}
    for indice, jugador in enumerate(lista_jugadores):

        if dic_jugadores[jugador][puntaje_jugador] not in dic_auxiliar:
            dic_auxiliar[dic_jugadores[jugador][puntaje_jugador]] = [jugador]
        else:
            dic_auxiliar[dic_jugadores[jugador][puntaje_jugador]].append(jugador)

    lista_auxiliar = sorted(dic_auxiliar.items(), reverse=True)
    cont = 2
    for item in lista_auxiliar:
        if len(item[1]) == 1:
            dic_jugadores[item[1][0]][0] = cont
            cont += 1
        else:
            print(item[1])

            shuffle(item[1])
            print(item[1])
            for elemento in item[1]:
                dic_jugadores[elemento][0] = cont
                cont += 1


#-------------------------------------------------------------------------------------------------


def otorgarOrdenJugadores(nro_partida, dic_jugadores):
    lista_jugadores = list(dic_jugadores.keys())
    if nro_partida == 1:
        otorgarOrdenJugadoresPrimeraRonda(dic_jugadores, lista_jugadores)
    else:
        separarGanadorAnteriorPartida(dic_jugadores, lista_jugadores)
        otorgarOrdenJugadoresGeneral(dic_jugadores, lista_jugadores)


def imprimirDatosJugador(diccionario_jugadores, jugador):
    print("NOMBRE_JUGADOR: {}".format(jugador))
    print("ORDEN_JUGADOR: {}".format(diccionario_jugadores[jugador][orden_jugador]))
    print("PUNTAJE_JUGADOR: {}".format(diccionario_jugadores[jugador][puntaje_jugador]))
    print("PALABRA_A_ADIVINAR: {}".format(diccionario_jugadores[jugador][palabra_a_adivinar]))
    print("PALABRA_OCULTA: {}".format(diccionario_jugadores[jugador][palabra_oculta]))
    print("LETRAS ACERTADAS: {}".format(diccionario_jugadores[jugador][letras_acertadas]))
    print("LETRAS_ERRADAS: {}".format(diccionario_jugadores[jugador][letras_erradas]))
    print("GANADOR_ULTIMA_PARTIDA: {}".format(diccionario_jugadores[jugador][ganador_ultima_partida]))
    print("JUGADOR_ELIMINADO: {}\n\n".format(diccionario_jugadores[jugador][jugador_eliminado]))


def generarDiccionarioPartida(nro_partida):
    dic_partida = {nro_partida: []}
    return dic_partida


def almacenarDatosPartida(diccionario_partida, datos_partida):
    #espera una lista con los datos de cada jugador, al finalizar el turno y los almacena en la partida
    diccionario_partida.append(datos_partida)

def elegirPalabraAleatoria(lista_palabras):
    print(lista_palabras)
    palabra_adivinar = lista_palabras.pop(random.randint(0, len(lista_palabras)-1))
    print("palabra a adivinar: ", palabra_adivinar)
    return palabra_adivinar

def otorgarPalabrasJugadores(diccionario_jugadores, lista_palabras):
    lista_palabras_utilizadas = []
    for jugador in diccionario_jugadores:
        palabra_aleatoria = elegirPalabraAleatoria(lista_palabras)
        lista_palabras_utilizadas.append(palabra_aleatoria)
        diccionario_jugadores[jugador][palabra_actual].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_a_adivinar].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_oculta].extend("_" * len(palabra_aleatoria))
    return lista_palabras_utilizadas
#Autor = Luan


def actualizarDiccionarioPalabras(diccionario_palabras, lista_palabras_utilizadas):
    for palabra in lista_palabras_utilizadas:
        diccionario_palabras[palabra][palabra_usada] = True
    return diccionario_palabras

def transformarGuionesBajos(letraIngresada, jugador, diccionario_jugadores):
    pos = diccionario_jugadores[jugador][palabra_a_adivinar].index(letraIngresada)
    diccionario_jugadores[jugador][palabra_a_adivinar][pos] = "_"
    diccionario_jugadores[jugador][palabra_oculta][pos] = diccionario_jugadores[jugador][palabra_actual][pos]

def ingresarLetra():
    while True:
        letra_ingresada = input("Ingrese una letra: ")
        letra_ingresada = letra_ingresada.upper()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Ingreso un caracter invalido")
        else:
            return letra_ingresada
