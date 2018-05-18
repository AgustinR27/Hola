from TP_texto import obtener_texto
import random
from random import shuffle
import time

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


def dibujarHombrecito(nro_desaciertos):
    dibujo = ""
    hombrecito = ["\n | \n | \n", " 0\n", "/", "|", "\ \n", "/", " \ \n"]

    for posicion in range(nro_desaciertos):
        dibujo += "".join(hombrecito[posicion])
    return dibujo
# Autor: Mauro C., genera una hombre mientras se va perdiendo

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
# Autor: Luan.C, Reemplaza las letras "incorrectas" por las que se usaran en el juego


def esperar(tiempo):
    time.sleep(tiempo)


def mostrarPalabrasOrdenadas(diccionario_palabras):
    lista_palabras_ordenadas = sorted(diccionario_palabras.keys())
    print("PALABRAS DEL DICCIONARIO y CANTIDAD DE REPETICIONES:")
    auxiliar = ""
    for indice, palabra in enumerate(lista_palabras_ordenadas):
        auxiliar += "Palabras: {} - Cantidad de repeticiones: {} - ".format(palabra, diccionario_palabras[palabra][
            cantidad_repeticiones_palabra])

        # esto verifica que se frene el print cada 500 registros. Se queda unos 5 segundos y continúa imprimiendo.
        if indice % 5 == 0:
            esperar(0.05)
            print(auxiliar)
            auxiliar = ""
    if auxiliar != "":
        print(auxiliar)


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

    mostrar_diccionario = input("¿Desea ver las palabras del diccionario? (S/N): ")
    while not mostrar_diccionario.upper() in ("S", "N"):
        mostrar_diccionario = input("Opcion incorrecta. ¿Desea ver las palabras del diccionario? (S/N): ")

    # si decide continuar, se actualizan el numero de partida
    if mostrar_diccionario.upper() == 'S':
        # tambien se muestran las palabras ordenadas alfabéticamente.
        # se muestran de a 500 palabras, junto con su número de repeticiones.
        # además se muestra el número de palabra.
        mostrarPalabrasOrdenadas(dic_palabras)

    return dic_palabras
# Autor: Daro., genera el diccionario de la partida

def solicitarCantJugadores():
    continuar = True
    cant_jugadores = input("Ingrese la cantidad de jugadores: ")
    while continuar:
        if not cant_jugadores.isdigit():
            print("Valor incorrecto. La cantidad de jugadores debe ser numérica.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        elif int(cant_jugadores) < 1 or int(cant_jugadores) > 10:
            print("Valor incorrecto, la cantidad de jugadores jugadores minima es de un jugador y como máximo, pueden jugar diez personas.")
            cant_jugadores = input("Ingrese la cantidad de jugadores: ")
        else:
            continuar = False
    return int(cant_jugadores)
# Autor: Agustin.R, solicita la cantidad de jugadores verificando que este dentro de los parametros del juego

def solicitarNombreJugador():
    nombre_jugador = input("Ingrese Nombre para el Jugador: ")
    while not nombre_jugador.replace(" ", "").isalpha():
        nombre_jugador = input("Nombre incorrecto. Ingrese Nombre Jugador: ")
    return nombre_jugador
# Autor: Daro., solicita el nombre al jugador y verifica que no se usen caracteres incorrectos


def generarDiccionarioJugadores(cant_jugadores):
    #a partir de una cantidad de jugadores pasada por parametro, se solicita dicha cantidad de veces el nombre de jugadores.
    # Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [orden, puntaje, palabra, palabra a_adivinar, palabra_oculta, letras_acertadas,letras_falladas, ganador_ultima_partida, jugador_eliminado]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitarNombreJugador()
        if formatearPalabra(jugador) not in dic_jugadores:
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], [], [], [], [], False, False, ""]
        else:
            while formatearPalabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto.")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, 0, [], [], [], [], [], False, False,""]
    return dic_jugadores
# Autor: Mauro C., genera el diccionario de los jugadores en los que se almacenaran todos sus datos


def otorgarOrdenJugadoresPrimeraRonda(dic_jugadores, lista_jugadores):
    for indice in range(len(lista_jugadores)):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][orden_jugador] = indice+1
# Autor: Daro.,otroga el orden a los jugadores de manera aleatoria


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
# Autor: Agustin.R., separa al ganador de la ultima partida, asi quedaria primero en la sigunete partida

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
            shuffle(item[1])
            for elemento in item[1]:
                dic_jugadores[elemento][0] = cont
                cont += 1
# Autor: Mauro C., otroga el orden a los jugadores de manera aleatoria

def otorgarOrdenJugadores(nro_partida, dic_jugadores):
    lista_jugadores = list(dic_jugadores.keys())
    if nro_partida == 1:
        otorgarOrdenJugadoresPrimeraRonda(dic_jugadores, lista_jugadores)
    else:
        separarGanadorAnteriorPartida(dic_jugadores, lista_jugadores)
        otorgarOrdenJugadoresGeneral(dic_jugadores, lista_jugadores)
# Autor: Mauro C., genera una lista de palabras segun la cantidad de letras que decida el usuario


def generarDiccionarioPartida(diccionario_partida, nro_partida):
    diccionario_partida[nro_partida] = []
    return diccionario_partida
# Autor: Daro., genera el diccionario de la partida


def almacenarDatosPartida(diccionario_partida, datos_partida):
    #espera una lista con los datos de cada jugador, al finalizar el turno y los almacena en la partida
    diccionario_partida.extend(datos_partida)
# Autor: Mauro C.


def elegirPalabraAleatoria(lista_palabras):
    palabra_adivinar = lista_palabras.pop(random.randint(0, len(lista_palabras)-1))
    return palabra_adivinar
# Autor: Luan.C, elige una palabra aletoria


def otorgarPalabrasJugadores(diccionario_jugadores, lista_palabras):
    lista_palabras_utilizadas = []
    for jugador in diccionario_jugadores:
        palabra_aleatoria = elegirPalabraAleatoria(lista_palabras)
        lista_palabras_utilizadas.append(palabra_aleatoria)
        diccionario_jugadores[jugador][palabra_actual].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_a_adivinar].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_oculta].extend("_" * len(palabra_aleatoria))
    return lista_palabras_utilizadas
# Autor = Luan.C, otorga a los jugadores una palabra y genera la palabra oculta


def actualizarDiccionarioPalabras(diccionario_palabras, lista_palabras_utilizadas):
    for palabra in lista_palabras_utilizadas:
        diccionario_palabras[palabra][palabra_usada] = True
    return diccionario_palabras
# Autor: Luan.C, elimina las palabras usadas


def transformarGuionesBajos(letraIngresada, jugador, diccionario_jugadores):
    pos = diccionario_jugadores[jugador][palabra_a_adivinar].index(letraIngresada)
    diccionario_jugadores[jugador][palabra_a_adivinar][pos] = "_"
    diccionario_jugadores[jugador][palabra_oculta][pos] = diccionario_jugadores[jugador][palabra_actual][pos]
# Autor: Agustin.R, Segun la posicion en la que se encuentra la letra, la reemplaza donde estaba el "_"


def ingresarLetra():
    while True:
        letra_ingresada = input("Ingrese una letra: ")
        print("\n")
        letra_ingresada = letra_ingresada.upper()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Ingreso un caracter invalido")
        else:
            return letra_ingresada
# Autor: Agustin.R, verifica que la letra ingresada sea correcta para el juego


def generarListaPalabrasPorCantLetras(dic_palabras):
    lista_palabras = []
    while lista_palabras == []:
        cant_letras = input("Ingrese la cantidad de letras de la palabra a adivinar: ")
        while not cant_letras.isdigit():
            cant_letras = input("Valor incorrecto. Debe ingresar un número. Ingrese la cantidad de letras de la palabra a adivinar: ")
        for clave in dic_palabras:
            if dic_palabras[clave][1] == int(cant_letras) and dic_palabras[clave][2] == False:
                lista_palabras.append(clave)
        if lista_palabras == []:
            print("No se encontraron palabras con esa cantidad de letras.")
    return lista_palabras
# Autor: Mauro C., genera una lista de palabras segun la cantidad de letras que decida el usuario

def mostrarDatosTurno(diccionario_jugadores, jugador, jugador_eliminado):
    if not jugador_eliminado:
        print("\n"*100)
        print("JUGADOR ACTUAL: {}".format(jugador))
        print("Puntaje jugador {}: {} puntos.".format(jugador,diccionario_jugadores[jugador][puntaje_jugador]))
    else:
        print("PERDISTE, {}. Tenés que esperar que acabe la partida para volver a jugar.".format(jugador))
        print("La palabra era: {}".format(" ".join(diccionario_jugadores[jugador][palabra_actual])))
    if len(diccionario_jugadores[jugador][letras_acertadas]) > 0:
        print("Ingresaste las siguientes letras correctas: {}.".format(", ".join(diccionario_jugadores[jugador][letras_acertadas])))
    if len(diccionario_jugadores[jugador][letras_erradas]) > 0:
        print("Ingresaste las siguientes letras incorrectas: {}.".format(", ".join(diccionario_jugadores[jugador][letras_erradas])))
    print(" ".join(diccionario_jugadores[jugador][palabra_oculta]))
    print("\n-----------------------------------------")
    print(diccionario_jugadores[jugador][hombrecito])
    print("-----------------------------------------\n")


def calcularDatosPartidas(diccionario_partida, nro_partida):
    for datos_jugador in diccionario_partida[nro_partida]:
        v_nombre_jugador = datos_jugador[0]
        v_puntaje_jugador = datos_jugador[1][puntaje_jugador]
        v_cant_aciertos_jugador = len(datos_jugador[1][letras_acertadas])
        v_cant_errores_jugador = len(datos_jugador[1][letras_erradas])
    return v_nombre_jugador, v_puntaje_jugador, v_cant_aciertos_jugador,v_cant_errores_jugador

def mostrarDatosPartida(diccionario_partida, nro_partida):
    for jugador in diccionario_partida[nro_partida]:
        print("\n-----------------------------------------")
        print("DATOS DE LA PARTIDA {}:".format(nro_partida))
        v_nombre_jugador, v_puntaje_jugador, v_cant_aciertos_jugador, v_cant_errores_jugador = calcularDatosPartidas(diccionario_partida, nro_partida)
        print("NOMBRE JUGADOR: {}".format(v_nombre_jugador))
        print("INFORMACION PUNTAJE: {}".format(v_puntaje_jugador))
        print("INFORMACION CANTIDAD DE ACIERTOS: {}".format(v_cant_aciertos_jugador))
        print("INFORMACION CANTIDAD DE ERRORES: {}".format(v_cant_errores_jugador))
        print("-----------------------------------------\n")


def mostrarDatosGeneralesPartidas(diccionario_partida):
    print("\n-----------------------------------------")
    print("DATOS GENERALES DE LA PARTIDAS JUGADAS:")
    dic_datos_generales = {}
    for nro_partida in diccionario_partida:
        for i in range(len(diccionario_partida[nro_partida])):
            v_nombre_jugador, v_puntaje_jugador, v_cant_aciertos_jugador, v_cant_errores_jugador = calcularDatosPartidas(diccionario_partida, nro_partida)
            if v_nombre_jugador not in dic_datos_generales:
                dic_datos_generales[v_nombre_jugador] =[v_puntaje_jugador,v_cant_aciertos_jugador, v_cant_errores_jugador]
            else:
                dic_datos_generales[v_nombre_jugador][1] += v_cant_aciertos_jugador
                dic_datos_generales[v_nombre_jugador][2] += v_cant_errores_jugador
    for jugador in dic_datos_generales:
        print("NOMBRE JUGADOR: {}".format(jugador))
        print("INFORMACION PUNTAJE TOTAL: {}".format(dic_datos_generales[jugador][0]))
        print("INFORMACION CANTIDAD DE ACIERTOS TOTALES: {}".format(dic_datos_generales[jugador][1]))
        print("INFORMACION CANTIDAD DE ERRORES TOTALES: {}".format(dic_datos_generales[jugador][2]))
    print("-----------------------------------------\n")