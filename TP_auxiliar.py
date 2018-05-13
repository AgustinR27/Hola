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


def esPalabraValida(palabra):
    return palabra.isalpha() and len(palabra) >= 5

def generarDiccionarioPalabras():
    #a partir del string pasado por los profesores, se genera un diccionario de palabras con el siguiente formato:
    #clave = palabra valor = lista compuesta por [cantidad_de_repeticiones, cant_letras, palabra_ya_utilizada]
    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_auxiliar = linea.split(" ")
            for palabra in lista_auxiliar:
                if esPalabraValida(palabra):
                    if formatearPalabra(palabra) not in dic_palabras:
                        dic_palabras[formatearPalabra(palabra)] = [1, len(palabra), False]
                    else:
                        dic_palabras[formatearPalabra(palabra)][0] += 1

    return dic_palabras

def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor


def solicitarCantJugadores():
    cant_jugadores = input("Ingrese la cantidad de jugadores: ")
    while cant_jugadores.isdigit():
        if int(cant_jugadores) > 11:
            print("cantidad de jugadores incorrecto, los jugadores deben ir de 1 hasta 10")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        elif int(cant_jugadores) == 0:
            print("Mucha lógica por suerte... Ingresa de nuevo un valor: ")
            cant_jugadores = input("Ingrese la cantidad de jugadores")
        else:
            return int(cant_jugadores)


def esNombreValido(nombre_jugador):
    # pendiente. Hay que validar que sea un nombre correcto. ¿verificamos acá que no sea una clave ya usada en el diccionario?
    valor = True
    if nombre_jugador.isdigit():
        valor = False
    elif len(nombre_jugador) < 3 or len(nombre_jugador) > 15:
        valor = False
    return valor


def solicitarNombreJugador():
    jugador = str(solicitarValor("Ingrese Nombre Jugador: "))
    while not esNombreValido(jugador):
        jugador = solicitarValor("Nombre incorrecto.\n Ingrese Nombre Jugador: ")
    return jugador

def generarDiccionarioJugadores(cant_jugadores):
    #a partir de una cantidad de jugadores pasada por parametro, se solicita dicha cantidad de veces el nombre de jugadores. Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [orden, puntaje, lista de palabras utilizadas, ganador_ultima_partida?, jugador_eliminado?]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitarNombreJugador()
        if formatearPalabra(jugador) not in dic_jugadores:
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], False, False]
        else:
            while formatearPalabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], False, False]
    return dic_jugadores

def generarDiccionarioPartida():
    dic_partida = {"nro_partida" : 1}
    return dic_partida

def otorgarOrdenJugadores(numero_partida, dic_jugadores):
    lista_jugadores = list(dic_jugadores.keys())
    nro_turno = 1
    for i in range(len(lista_jugadores)):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][0] = nro_turno
        nro_turno += 1


def generarListaPalabrasPorCantLetras(dic_palabras):
    lista_palabras = []
    while lista_palabras == []:
        cant_letras = input("Ingrese la cantidad de letras de la palabra a adivinar: ")
        for clave in dic_palabras:
            if dic_palabras[clave][1] == int(cant_letras):
                lista_palabras.append(clave)
        if lista_palabras == []:
            print("No se encontraron palabras con esa cantidad de letras.")
    return lista_palabras


def palabra_adivinar(lista_palabras):
    lista_palabras_elegidas = lista_palabras
    palabra_adivinar = random.choice(lista_palabras_elegidas)
    return palabra_adivinar
