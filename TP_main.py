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


def main():
    variable = obtener_texto()
    dic_palabras = {}
    for linea in variable:
        if len(linea) > 0:
            lista_aux = linea.split(" ")
            for palabra in lista_aux:
                if palabra.isalpha() and len(palabra) >= 5:
                    if formatearPalabra(palabra) not in dic_palabras:
                        dic_palabras[formatearPalabra(palabra)] = 1
                    else:
                        dic_palabras[formatearPalabra(palabra)] += 1

    for clave in dic_palabras:
        print(clave)

    print(len(dic_palabras))


main()
print("hola")