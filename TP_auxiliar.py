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

def generarDiccionario():
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


def turno_aleatorio(lista):
    lista_ordenada = []
    for i in range(len(lista)):
        lista_ordenada.append(lista.pop(random.randint(0, len(lista) - 1)))
    return lista_ordenada