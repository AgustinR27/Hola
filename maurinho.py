from TP_texto import obtener_texto

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

diccionario_palabras = generarDiccionarioPalabras()
cant_jugadores = solicitarCantJugadores()

diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)

for jugador in diccionario_jugadores:
    imprimirDatosJugador(jugador)