from TP_texto import obtener_texto
import random
from random import shuffle
from TP_auxiliar import *
import time

def dibujarHombrecito(nro_desaciertos):
    dibujo = ""
    hombrecito = ["\n | \n | \n"," 0\n","/","|","\ \n","/"," \ \n"]

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
                        dic_palabras[formatearPalabra(palabra)][0] += 1
    return dic_palabras

def solicitarCantJugadores():
    continuar = True
    cant_jugadores = input("Ingrese la cantidad de jugadores: ")
    while continuar:
        if not cant_jugadores.isdigit():
            print("Valor incorrecto. La cantidad de jugadores debe ser numérica.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        elif int(cant_jugadores) < 2 or int(cant_jugadores) > 10:
            print("Valor incorrecto, la cantidad de jugadores jugadores minima es de dos jugadores y como máximo, pueden jugar diez personas.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        else:
            continuar = False
    return int(cant_jugadores)

def solicitarNombreJugador():
    nombre_jugador = input("Ingrese Nombre para el Jugador: ")
    while not nombre_jugador.replace(" ","").isalpha():
        nombre_jugador = input("Nombre incorrecto. Ingrese Nombre Jugador: ")
    return nombre_jugador

def generarDiccionarioJugadores(cant_jugadores):
    #a partir de una cantidad de jugadores pasada por parametro, se solicita dicha cantidad de veces el nombre de jugadores. Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [orden, puntaje, palabra a_adivinar, palabra_oculta, letras_acertadas,letras_falladas, ganador_ultima_partida, jugador_eliminado]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitarNombreJugador()
        if formatearPalabra(jugador) not in dic_jugadores:
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [],[],[],[], False, False]
        else:
            while formatearPalabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto.")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [],[],[],[], False, False]
    return dic_jugadores


def otorgarOrdenJugadoresPrimeraRonda(dic_jugadores,lista_jugadores):
    for indice in range(len(lista_jugadores)):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][0] = indice+1

def separarGanadorAnteriorPartida(dic_jugadores,lista_jugadores):
    condicion = True
    cont = 0
    while condicion and cont <= len(lista_jugadores) - 1:
        valor_jugador = lista_jugadores[cont]
        ganador_ultima_partida = dic_jugadores[valor_jugador][6]
        if ganador_ultima_partida == True:
            dic_jugadores[valor_jugador][0] = 1
            lista_jugadores.pop(cont)
            condicion = False
        cont += 1

def otorgarOrdenJugadoresGeneral(dic_jugadores,lista_jugadores):
    dic_auxiliar = {}
    for indice, jugador in enumerate(lista_jugadores):

        if dic_jugadores[jugador][1] not in dic_auxiliar:
            dic_auxiliar[dic_jugadores[jugador][1]] = [jugador]
        else:
            dic_auxiliar[dic_jugadores[jugador][1]].append(jugador)

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



def otorgarOrdenJugadores(nro_partida, dic_jugadores):
    lista_jugadores = list(dic_jugadores.keys())
    if nro_partida == 1:
        otorgarOrdenJugadoresPrimeraRonda(dic_jugadores, lista_jugadores)
    else:
        separarGanadorAnteriorPartida(dic_jugadores, lista_jugadores)
        otorgarOrdenJugadoresGeneral(dic_jugadores, lista_jugadores)

def imprimirDatosJugador(jugador):
    print("NOMBRE_JUGADOR: {}".format(jugador))
    print("ORDEN_JUGADOR: {}".format(diccionario_jugadores[jugador][0]))
    print("PUNTAJE_JUGADOR: {}".format(diccionario_jugadores[jugador][1]))
    print("PALABRA_A_ADIVINAR: {}".format(diccionario_jugadores[jugador][2]))
    print("PALABRA_OCULTA: {}".format(diccionario_jugadores[jugador][3]))
    print("LETRAS ACERTADAS: {}".format(diccionario_jugadores[jugador][4]))
    print("LETRAS_ERRADAS: {}".format(diccionario_jugadores[jugador][5]))
    print("GANADOR_ULTIMA_PARTIDA: {}".format(diccionario_jugadores[jugador][6]))
    print("JUGADOR_ELIMINADO: {}\n\n".format(diccionario_jugadores[jugador][7]))

def generarDiccionarioPartida(dic_partida, nro_partida):
    dic_partida[nro_partida] = []

def almacenarDatosPartida(diccionario_partida, datos_partida):
    #espera una lista con los datos de cada jugador, al finalizar el turno y los almacena en la partida
    diccionario_partida.append(datos_partida)

diccionario_palabras = generarDiccionarioPalabras()
cant_jugadores = solicitarCantJugadores()

diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)
nro_partida = 1

diccionario_partida = {}
generarDiccionarioPartida(diccionario_partida,nro_partida)

for jugador in diccionario_jugadores:
    turno = True
    letra = ingresarLetra()


for jugador in diccionario_jugadores:
    almacenarDatosPartida(diccionario_partida[nro_partida], diccionario_jugadores[jugador])
print(diccionario_partida)

#diccionario_jugadores["A"][6] = True
#diccionario_jugadores["A"][1] = 30
#diccionario_jugadores["B"][1] = 25
#diccionario_jugadores["C"][1] = 20
#diccionario_jugadores["D"][1] = 20
#diccionario_jugadores["E"][1] = -13
#otorgarOrdenJugadores(nro_partida+1, diccionario_jugadores)
#print(diccionario_jugadores)

lista_palabras_ordenadas = sorted(diccionario_palabras.keys())
print("PALABRAS DEL DICCIONARIO y CANTIDAD DE REPETICIONES:\n")
for indice, palabra in enumerate(lista_palabras_ordenadas):
    print("Palabra: {} - Cantidad de repeticiones: {}".format(palabra, diccionario_palabras[palabra]))
    if indice%500 == 0:
        time.sleep(5.0)
    print(indice)