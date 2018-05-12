from TP_general import solicitarNombreJugador


def solicitarNombreJugadores():
    # pide nombre para la cantidad de personas
    lista_personas = []
    for indice in range(cant_personas()):
        lista_personas.append(solicitarNombreJugador("Ingrese nombre de la futura víctima: "))
    return lista_personas


def cant_personas():
    personas = int(input('Ingrese el número de personas a ahorcar: '))
    if personas <= 10:
        jugadores = personas
    else:
        print('Nos hemos quedado sin sogas para tantos cuellos!!! Solo contamos con 10. Intenta nuevamente...')
        jugadores = cant_personas()
    return jugadores


def mostrarDatosJugador(jugador):
    print("datos jugador")


def mostrarDesaciertos(jugador):
    print("desaciertos jugador")


def mostrarAciertos(jugador):
    print("aciertos jugador")

def eliminarJugador(lista_personas, jugador):
    #elimina un jugador. Se espera un nombre valido.
    lista_personas.remove(jugador)