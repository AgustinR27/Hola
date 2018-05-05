from TP_general import solicitarValor
from TP_jugadores import ingresarNombrePersonas
from TP_jugadores import mostrarAciertos
from TP_jugadores import mostrarDatosJugador
from TP_jugadores import mostrarDesaciertos

CANT_MINIMA_PERSONAS = 1
CANT_MAXIMA_PERSONAS = 10


def generarTexto():
    #recibe la funcion que nos tiene que pasar los profesores
    texto = "bla bla bla"
    return texto


def generarDiccionario(texto):
    #formatea el texto en un diccionario solo letras, sin repetir, clave = palabra, valor = cant_repeticiones
    dic_palabras_validas = {}
    return dic_palabras_validas


def mostrarDiccionario(dic_palabras_validas):
    for clave in dic_palabras_validas:
        print(clave, ": ", dic_palabras_validas[clave])


def ingresarCantidadPersonas():
    #ingresar cantidad personas, tienen que ser menos de diez, y mas de una
    cant_personas = solicitarValor("Ingrese cantidad personas")
    while cant_personas < CANT_MINIMA_PERSONAS or CANT_MAXIMA_PERSONAS > 10:
        cant_personas = solicitarValor("Cantidad incorrecta. El juego se juega minimo de a dos, máximo de diez. "
                                       "Ingrese cantidad personas")
    return cant_personas


def otorgarOrdenPersonas(lista_personas, nro_partida):
    #te arma una lista ordenada de personas
    lista_personas_ordenada = []
    if nro_partida > 1:
        print("hacer algo")
        lista_personas_ordenada.extend(lista_personas)
    else:
        print("hacer otra cosa")
        lista_personas_ordenada.extend(lista_personas)
    return lista_personas_ordenada


def buscarPalabra(longitud, dic_palabras_validas):
    dic_palabra_longitud_solicitada = {}
    for palabra in dic_palabras_validas:
        if len(palabra) == longitud:
            dic_palabra_longitud_solicitada[len(palabra)] = palabra
    return dic_palabra_longitud_solicitada


def solicitarLongitudPalabras(persona, dic_palabras_validas):
    #para cada persona se solicita una lista de posibles palabras, segun la longitud ingresada.
    dic_palabra_persona = {}
    longitud_palabra = solicitarValor("Ingrese longitud palabra para adivinar: ")
    dic_palabras = buscarPalabra(longitud_palabra, dic_palabras_validas)
    return dic_palabras


def seleccionarPalabra(dic_palabras, jugador):
    #seleccionar una de las palabras de la lista de forma random para cada jugador.
    palabra = "x"
    return palabra


def procesarTurno(jugador):
    #muestra datos jugador y contabliza turno
    numero_turno = 0
    #mostrar datos para cada jugador
    mostrarDatosJugador(jugador)
    mostrarAciertos(jugador)
    mostrarDesaciertos(jugador)
    return numero_turno

