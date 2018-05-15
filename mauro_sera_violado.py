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
    letra_ingresada = input("Ingrese una letra: ")
    letra_ingresada = letra_ingresada.upper()
    while len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
        print("Ingreso un caracter invalido")
        letra_ingresada = input("Ingrese una letra: ")
    return letra_ingresada


def separar_palabra(palabra_adivinar):
    palabra_a_averiguar = list(str(palabra_adivinar))
    return palabra_a_averiguar


def colocar_letras(letras_incorrectas, letras_correctas, letra_ingresada, palabra_a_averiguar):
    if letra_ingresada in palabra_a_averiguar:
        letras_correctas.append(letra_ingresada)
    else:
        letras_incorrectas.append(letra_ingresada)
    return letras_incorrectas, letras_correctas


def juego(letras_incorrectas, letras_correctas, palabra_adivinar):
    print("letras incorrectas: ", letras_incorrectas)
    for letra in letras_incorrectas:
        print(letra, end=", ")
    espacios_de_letras = "_ " * len(str(palabra_adivinar))
    for i in range(len(str(palabra_adivinar))):
        if str(palabra_adivinar)[i] in letras_correctas:
            espacios_de_letras = espacios_de_letras[:i] + palabra_adivinar[i] + espacios_de_letras[i + 1:]
    #for letra in espacios_de_letras:
    print(espacios_de_letras)


letras_incorrectas = []
letras_correctas = []
letras_usadas = []
ingresar_letra()
dic_palabras = obtener_palabras()
juego(letras_incorrectas,letras_correctas, "HOLA")
