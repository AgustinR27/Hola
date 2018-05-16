from TP_texto import obtener_texto
from TP_auxiliar import generarDiccionarioJugadores
from TP_auxiliar import generarDiccionarioPartida
from TP_auxiliar import solicitarCantJugadores
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

#################################################################################################################
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

#def obtener_palabras():
 #   texto = obtener_texto()
  #  dic_palabras = {}
   # for linea in texto:
    #    if len(linea) > 0:
     #       lista_aux = linea.split(" ")
      #      for palabra in lista_aux:
       #         if palabra.isalpha() and len(palabra) >= 5:
        #            if formatear_palabras(palabra) not in dic_palabras:
         #               dic_palabras[formatear_palabras(palabra)] = 1
          #          else:
           #             dic_palabras[formatear_palabras(palabra)] += 1
    #return dic_palabras


#def enlistar_palabras(dic_palabras):
    #lista_palabras = []
    #for clave in dic_palabras:
        #if clave not in lista_palabras:
            #lista_palabras.append(clave)
    #return lista_palabras


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
#########################################################################################################

def palabra_adivinar(lista_palabras):
    palabra_adivinar = random.choice(lista_palabras)
    return palabra_adivinar


def ingresar_letra():
    while True:
        letra_ingresada = input("Ingrese una letra: ")
        letra_ingresada = letra_ingresada.upper()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Ingreso un caracter invalido")
        else:
            return letra_ingresada


def separar_palabra(palabra_adivinar):
    palabra_a_averiguar = list(str(palabra_adivinar))
    return palabra_a_averiguar

############################################################################################
def elegirPalabraAleatoria(lista_palabras):
    print(lista_palabras)
    palabra_adivinar = lista_palabras.pop(random.randint(0, len(lista_palabras)-1))
    print("palabra a adivinar: ", palabra_adivinar)
    return palabra_adivinar


def agregarPalabras(diccionario_jugadores, jugador, lista_palabras, diccionario_palabras):
    palabra_aleatoria = elegirPalabraAleatoria(lista_palabras)
    diccionario_jugadores[jugador[0]][2].extend(list(palabra_aleatoria))
    print(diccionario_jugadores[jugador[0]][2])
    diccionario_jugadores[jugador[0]][3].extend("_" * len(palabra_aleatoria))
    print(diccionario_jugadores[jugador[0]][3])
    diccionario_palabras[palabra_aleatoria][2] = True

###################################################################################################


def juego(letrasIncorrectas, letrasCorrectas, palabraOculta):
    palabra = ""
    print('Letras incorrectas:', letrasIncorrectas)
    espacio = '_' * len(palabraOculta)
    for i in range(len(palabraOculta)):  # Remplaza los espacios por la letra en la posicion
        if palabraOculta[i] in letrasCorrectas:
            espacio = espacio[:i] + palabraOculta[i] + espacio[i+1:]
    for letra in espacio:  # Muestra la palabra oculta con espacios entre las letras
        palabra += letra + " "
    print(palabra)


letrasIncorrectas = ""
letrasCorrectas = ""
##########################################################################################################
dic_palabras = generarDiccionarioPalabras()
cant_jugadores = solicitarCantJugadores()
diccionario_jugadores = generarDiccionarioJugadores(cant_jugadores)
lista_palabras = generarListaPalabrasPorCantLetras(dic_palabras)
diccionario_palabras = generarDiccionarioPalabras()
diccionario_partida = generarDiccionarioPartida()
palabraOculta = palabra_adivinar(lista_palabras)
partida = diccionario_partida["nro_partida"]
#######################################################################################################
lista_jugadores_ordenado = sorted(diccionario_jugadores.items(), key=lambda x: x[1])

finJuego = False
while finJuego == False:
    juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
    letra = ingresar_letra()
    if letra in palabraOculta:  # analiza si el jugador ganó
        letrasCorrectas = letrasCorrectas + letra
        for jugador in lista_jugadores_ordenado:
            jugador[1][1] += 1
        letrasEncontradas = True
        for i in range(len(palabraOculta)):
            if palabraOculta[i] not in letrasCorrectas:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print('¡Ganaste! Despues de ' + str(len(letrasIncorrectas)//2) + ' fallas y ' + str(len(letrasCorrectas)) +
                  " aciertos, la palabra era " + palabraOculta)
            for jugador in lista_jugadores_ordenado:
                jugador[1][1] += 30  # Suma los 30 puntos si el jugador gana
                jugador[1][6] = True
            finJuego = True
    else:
        letrasIncorrectas += letra + " "
        for jugador in lista_jugadores_ordenado:
            jugador[1][1] -= 2  # Resta los 2 puntos por equivocarse
        # Comprueba la cantidad de letras que ha ingresado el jugador, si son 7, pierde su partida
        if len(letrasIncorrectas) >= 14:
            juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
            print('¡Te quedaste sin intentos y has sido eliminado!\n'
                  'Despues de ' + str(len(letrasIncorrectas)//2) + ' fallas y ' + str(len(letrasCorrectas)) +
                  ' aciertos, la palabra era ' + palabraOculta)
            for jugador in lista_jugadores_ordenado:
                jugador[1][7] = True
            finJuego = True

for jugador in lista_jugadores_ordenado:
    print("El jugador", jugador[0], "obtuvo", jugador[1][1], "puntos")
    print("palabra adivinar", jugador[1][2])
    print("palabra oculta", jugador[1][3])
    print("letras pegadas", jugador[1][4])
    print("palabra erradas", jugador[1][5])
    print(jugador[1][6])  # Imprime si el jugador gano = a True
    print(jugador[1][7])  # Se guarda si el jugador fue eliminado con un True

# La lista de los jugadores esta compuesto por las posiciones:
# [0] = Nombre
# [1][0] = Orden
# [1][1] = Puntaje
# [1][2] = Palabra que tiene que adivinar
# [1][3] = Palabra oculta ( queda la palabra con los "_" pero con las letras que puso bien"
# [1][4] = Letras que puso bien
# [1][5] = Letras que erro
# [1][6] = Ganador ultima partida
# [1][7] = Jugador fue eliminado? si=True, no=False
