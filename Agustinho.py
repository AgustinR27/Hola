from TP_texto import obtener_texto
import random

def formatear_palabras(palabra):
    dic_a_reemplazar = {"Ñ": "NI", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}
    palabra_vieja = palabra.upper()
    palabra_nueva = ''
    for letra in palabra_vieja:
        if letra not in dic_a_reemplazar:
            palabra_nueva += letra
        else:
            palabra_nueva += dic_a_reemplazar[letra]
    return palabra_nueva


def obtener_palabras():
    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_aux = linea.split(" ")
            for palabra in lista_aux:
                if palabra.isalpha() and len(palabra) >= 5:
                    if formatear_palabras(palabra) not in dic_palabras:
                        dic_palabras[formatear_palabras(palabra)] = 1
                    else:
                        dic_palabras[formatear_palabras(palabra)] += 1
    return dic_palabras


def enlistar_palabras(dic_palabras):
    lista_palabras = []
    for clave in dic_palabras:
        if clave not in lista_palabras:
            lista_palabras.append(clave)
    return lista_palabras


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


##def juego(letras_incorrectas, letras_correctas, palabra_adivinar):
  #  for letra in letras_incorrectas:
  #      print(letra, end=", ")
  #  espacios_de_letras = "_ " * len(str(palabra_adivinar))
   # for i in range(len(str(palabra_adivinar))):
       # if str(palabra_adivinar)[i] in letras_correctas:
            #espacios_de_letras = espacios_de_letras[:i] + palabra_adivinar[i] + espacios_de_letras[i + 1:]
    #for letra in espacios_de_letras:
    #print(espacios_de_letras)


def juego(letrasIncorrectas, letrasCorrectas, palabraOculta):
    for letra in letrasIncorrectas:
        print('Letras incorrectas:', letrasIncorrectas)
    espacio = '_' * len(palabraOculta)
    for i in range(len(palabraOculta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraOculta[i] in letrasCorrectas:
            espacio = espacio[:i] + palabraOculta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print(letra)


letrasIncorrectas = ""
letrasCorrectas = ""
dic_palabras = obtener_palabras()
lista_palabras = enlistar_palabras(dic_palabras)
palabraOculta = palabra_adivinar(lista_palabras)
finJuego = False
while True:
    juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
    # El usuario elije una letra.
    letra = ingresar_letra()
    if letra in palabraOculta:
        letrasCorrectas = letrasCorrectas + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraOculta)):
            if palabraOculta[i] not in letrasCorrectas:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print('¡Ganaste! La palabra secreta era ' + palabraOculta)
            finJuego = True
    else:
        letrasIncorrectas = letrasIncorrectas + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letrasIncorrectas) == 7:
            juego(letrasIncorrectas, letrasCorrectas, palabraOculta)
            print('¡Te quedaste sin intentos!\nDespues de ' + str(len(letrasIncorrectas)) + ' fallas y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era ' + palabraOculta)
            finJuego = True


letras_usadas = []
letra_ingresada = ingresar_letra()

palabra_adivinar = palabra_adivinar(lista_palabras)
palabra_a_averiguar = separar_palabra(palabra_adivinar)
juego(letra_ingresada, palabra_a_averiguar)
