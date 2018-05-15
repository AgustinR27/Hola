from TP_texto import obtener_texto
import random


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
            print("La cantidad de jugadores debe ser numérica")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
            continuar = True
        elif int(cant_jugadores) > 10:
            print("cantidad de jugadores incorrecto, los jugadores deben ir de 1 hasta 10")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
            continuar = True
        elif int(cant_jugadores) == 0:
            print("No te pedí tu coeficiente intelectual. Ingresá una cantidad de jugadores valida: ")
            cant_jugadores = input("Ingrese la cantidad de jugadores")
            continuar = True
        else:
            continuar = False
    return int(cant_jugadores)


def esNombreValido(nombre_jugador):
    # pendiente. Hay que validar que sea un nombre correcto. ¿verificamos acá que no sea una clave ya usada en el diccionario?
    valor = True
    if nombre_jugador.isdigit():
        valor = False
    return valor


def solicitarNombreJugador():
    jugador = str(input("Ingrese Nombre Jugador: "))
    while not esNombreValido(jugador):
        jugador = input("Nombre incorrecto.\n Ingrese Nombre Jugador: ")
    return jugador


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
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [],[],[],[], False, False]
    return dic_jugadores


def generarDiccionarioPartida():
    dic_partida = {"nro_partida" : 1}
    return dic_partida


def otorgarOrdenJugadores(numero_partida, dic_jugadores):
    lista_jugadores = list(dic_jugadores.keys())
    for indice, valor_jugador in enumerate(lista_jugadores):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][0] = indice



def generarListaPalabrasPorCantLetras(dic_palabras):
    lista_palabras = []
    while lista_palabras == []:
        cant_letras = input("Ingrese la cantidad de letras de la palabra a adivinar: ")
        for clave in dic_palabras:
            if dic_palabras[clave][1] == int(cant_letras) and dic_palabras[clave][2] == False:
                lista_palabras.append(clave)
        if lista_palabras == []:
            print("No se encontraron palabras con esa cantidad de letras.")
    return lista_palabras


def elegirPalabraAleatoria(lista_palabras):
    print(lista_palabras)
    palabra_adivinar = lista_palabras.pop(random.randint(0, len(lista_palabras)-1))
    print("palabra a adivinar: ", palabra_adivinar)
    return palabra_adivinar

"""La función pide el diccionario de los jugadores, la lista de palabras procesada (válida) y el diccionario de palabras. 
Se usa una palabra aleatoria de la lista de palabras y se le asigna a una lista vacia dentro del diccionario de los jugadores.
Luego esa palabra asignada adquiere el valor booleano True en el diccionario de palabras-
Devuelve el diccionario jugadores, cada jugador con una palabra aleatoria asignada"""


def agregarPalabras(diccionario_jugadores, jugador, lista_palabras, diccionario_palabras):
        palabra_aleatoria = elegirPalabraAleatoria(lista_palabras)
        diccionario_jugadores[jugador[0]][2].extend(list(palabra_aleatoria))
        print(diccionario_jugadores[jugador[0]][2])
        diccionario_jugadores[jugador[0]][3].extend("_" * len(palabra_aleatoria))
        print(diccionario_jugadores[jugador[0]][3])
        diccionario_palabras[palabra_aleatoria][2] = True


def ingresarLetra():
    while True:
        letra_ingresada = input("Ingrese una letra: ")
        letra_ingresada = letra_ingresada.upper()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Ingreso un caracter invalido")
        else:
            return letra_ingresada