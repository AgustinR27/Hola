from texto import obtener_texto

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
    #clave = palabra valor = lista compuesta por [cantidad_de_repeticiones, palabra_ya_utilizada]
    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_auxiliar = linea.split(" ")
            for palabra in lista_auxiliar:
                if esPalabraValida(palabra):
                    if formatearPalabra(palabra) not in dic_palabras:
                        dic_palabras[formatearPalabra(palabra)] = [1, False]
                    else:
                        dic_palabras[formatearPalabra(palabra)][0] += 1

    return dic_palabras

def solicitarValor(mensaje):
    valor = input(mensaje)
    return valor

def esCantidadValida(cantidad_jugadores):
    return cantidad_jugadores > 1 and cantidad_jugadores <= 10


def solicitarCantJugadores():
    cant_jugadores = int(solicitarValor("Ingrese cantidad de jugadores"))
    while not esCantidadValida(cant_jugadores):
        cant_jugadores = int(solicitarValor("Cantidad incorrecta, tienen que ser al menos dos y máximo diez jugadores.\n Ingrese cantidad de jugadores:"))
    return cant_jugadores

def esNombreValido(nombre_jugador):
    #pendiente. Hay que validar que sea un nombre correcto. ¿verificamos acá que no sea una clave ya usada en el diccionario?
    return True

def solicitarNombreJugador():
    jugador = str(solicitarValor("Ingrese Nombre Jugador"))
    while not esNombreValido(jugador):
        jugador = int(solicitarValor("Nombre incorrecto.\n Ingrese Nombre Jugador:"))
    return jugador

def generarDiccionarioJugadores(cant_jugadores):
    #a partir de una cantidad de jugadores pasada por parametro, se solicita dicha cantidad de veces el nombre de jugadores. Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [puntaje, lista de palabras utilizadas, ganador_ultima_partida?, jugador_eliminado?]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitarNombreJugador()
        if formatearPalabra(jugador) not in dic_jugadores:
            dic_jugadores[formatearPalabra(jugador)] = [0, [], False, False]
        else:
            while formatearPalabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingrese un nombre distinto")
                jugador = solicitarNombreJugador()
            dic_jugadores[formatearPalabra(jugador)] = [0, [], False, False]
    return dic_jugadores
