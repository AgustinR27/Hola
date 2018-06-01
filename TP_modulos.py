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


def dibujar_hombrecito(nro_desaciertos):
    # Autor: Mauro Cuquejo. retorna el gráfico del hombrecito ahorcado, agregando las partes del cuerpo según la cantidad de desaciertos.
    dibujo = ""
    hombrecito = ["\n | \n | \n", " 0\n", "/", "|", "\ \n", "/", " \ \n"]

    for posicion in range(nro_desaciertos):
        dibujo += "".join(hombrecito[posicion])
    return dibujo


def formatear_palabra(palabra):
    # Autor: Luan Corrionero. recibe una palabra cualquiera y transforma las vocales con acento o las eñes. Retorna la palabra ya corregida.
    dic_a_reemplazar = {"Ñ": "NI", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}
    palabra_vieja = palabra.upper()
    palabra_nueva = ''
    for letra in palabra_vieja:
        if letra not in dic_a_reemplazar:
            palabra_nueva += letra
        else:
            palabra_nueva += dic_a_reemplazar[letra]
    return palabra_nueva


def pausa_para_continuar():
    # Autor: Mauro Cuquejo. Se genera un input que se utilizará durante la partida, para poder visualizar mejor la información. Esto porque cada vez que cambie el turno de un jugador, se limpiará la pantalla.
    # No retorna datos.
    input("presiona Enter para continuar...")
    print("\n" * 100)


def mostrar_palabras_ordenadas(diccionario_palabras):
    # Autor: Mauro Cuquejo. Imprime en pantalla el diccionario de palabras, ordenado alfabéticamente por clave. Se muestran en pantalla concatenaciones de cinco palabras, junto con sus repeticiones, cada 0.05 segundos.
    # Al finalizar la muestra,se imprime el excedente de palabras (ya que si no se llegaron a concatenar cinco palabras, no se muestra la concatenación).
    lista_palabras_ordenadas = sorted(diccionario_palabras.keys())
    print("PALABRAS DEL DICCIONARIO y CANTIDAD DE REPETICIONES:")
    auxiliar = ""
    for indice, palabra in enumerate(lista_palabras_ordenadas):
        auxiliar += "Palabras: {} - Cantidad de repeticiones: {} - ".format(palabra, diccionario_palabras[palabra][
            cantidad_repeticiones_palabra])
        if indice % 5 == 0:
            time.sleep(0.05)
            print(auxiliar)
            auxiliar = ""
    if auxiliar != "":
        print(auxiliar)


def generar_diccionario_palabras():
    # Autor: Dario Giménez. Se genera un diccionario de palabras con el siguiente formato:
    # clave = palabra valor = lista compuesta por [cantidad_de_repeticiones (numérico), cant_letras (numérico), palabra_ya_utilizada (booleano)]
    # se le pregunta a los jugadores si quieren visualizar dicho diccionario.
    # Retorna el diccionario generado y formateado, excluyendo lo que no sean palabras o modificando las ñ y las vocales con acento.

    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_auxiliar = linea.split(" ")
            for palabra in lista_auxiliar:
                if palabra.isalpha() and len(palabra) >= 5:
                    if formatear_palabra(palabra) not in dic_palabras:
                        dic_palabras[formatear_palabra(palabra)] = [1, len(palabra), False]
                    else:
                        dic_palabras[formatear_palabra(palabra)][cantidad_repeticiones_palabra] += 1

    mostrar_diccionario = input("¿Desea ver las palabras del diccionario? (S/N): ")
    while not mostrar_diccionario.upper() in ("S", "N"):
        mostrar_diccionario = input("Opcion incorrecta. ¿Desea ver las palabras del diccionario? (S/N): ")

    if mostrar_diccionario.upper() == 'S':
        mostrar_palabras_ordenadas(dic_palabras)

    return dic_palabras


def solicitar_cantidad_jugadores():
    # Autor: Agustin Ramirez. solicita la cantidad de jugadores verificando que este dentro de los parametros del juego.
    # Retorna la cantidad de jugadores.
    continuar = True
    cant_jugadores = input("Ingresa la cantidad de jugadores: ")
    while continuar:
        if not cant_jugadores.isdigit():
            print("Valor incorrecto. La cantidad de jugadores debe ser numérica.")
            cant_jugadores = input("Ingresa la cantidad de jugadores: ")
        elif int(cant_jugadores) < 1 or int(cant_jugadores) > 10:
            print("Valor incorrecto, la cantidad de jugadores jugadores minima es de un jugador y como máximo, pueden jugar diez personas.")
            cant_jugadores = input("Ingresa la cantidad de jugadores: ")
        else:
            continuar = False
    return int(cant_jugadores)


def solicitar_nombre_jugador():
    # Autor: Darío Giménez  solicita el nombre al jugador y verifica que no se usen caracteres incorrectos. Retorna nombre del jugador.
    nombre_jugador = input("Ingresa Nombre para el Jugador: ")
    while not nombre_jugador.replace(" ", "").isalpha():
        nombre_jugador = input("Nombre incorrecto. Ingresa Nombre Jugador: ")
    return nombre_jugador


def generar_diccionario_jugadores(cant_jugadores):
    # Autor: Mauro Cuquejo. Recibe cantidad de jugadores, se solicita dicha cantidad de veces el nombre de jugadores.
    # Se valida que los nombres no hayan sido utilizados ya en el diccionario.
    #el cual tiene el siguiente formato:
    #clave = jugador valor = lista compuesta por [orden (numérico), puntaje (numérico),
    # palabra_actual (lista de caracteres que forman la palabra a adivinar),
    # palabra a_adivinar (lista de caracteres que forman la palabra a adivinar y se utilizará para comparar
    # con la letra ingresada por el usuario),
    # palabra_oculta (lista con guiones bajos que se utilizará para dibujar en pantalla la palabra oculta.
    # Se irá reemplazando con las letras acertadas,
    # letras_acertadas (lista de caracteres acertados),
    # letras_falladas (lista de caracteres fallados,
    # ganador_ultima_partida (booleano que se utilizará para poner en primer lugar al jugador a partir de la segunda ronda),
    # jugador_eliminado (booleano que determinará si el jugador puede jugar el resto de la partida)]
    dic_jugadores = {}
    for numero_jugador in range(cant_jugadores):
        jugador = solicitar_nombre_jugador()
        if formatear_palabra(jugador) not in dic_jugadores:
            dic_jugadores[formatear_palabra(jugador)] = [0, 0, [], [], [], [], [], False, False, ""]
        else:
            while formatear_palabra(jugador) in dic_jugadores:
                print("El nombre ingresado ya fue utilizado por otra persona. Ingresa un nombre distinto.")
                jugador = solicitar_nombre_jugador()
            dic_jugadores[formatear_palabra(jugador)] = [0, 0, [], [], [], [], [], False, False, ""]
    return dic_jugadores


def otorgar_orden_jugadores_primera_ronda(dic_jugadores, lista_jugadores):
    # Autor: Darío Giménez. Recibe diccionario de jugadores y lista de jugadores. Actualiza el orden en el diccionario de
    # jugadores, para todos los jugadores de manera aleatoria. Se utiliza sólo si es la primera partida.
    # No retorna datos.
    for indice in range(len(lista_jugadores)):
        jugador = lista_jugadores.pop(random.randint(0, len(lista_jugadores) - 1))
        dic_jugadores[jugador][orden_jugador] = indice+1


def separar_ganador_anterior_partida(dic_jugadores, lista_jugadores):
    # Autor: Agustin Ramirez. Recibe diccionario de jugadores y lista de jugadores. Actualiza el diccionario de jugadores,
    # poniendo primero en orden al ganador de la partida anterior. Se utiliza a partir de la segunda partida.
    # No retorna datos.
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


def otorgar_orden_jugadores_general(dic_jugadores, lista_jugadores):
    # Autor: Mauro Cuquejo. Recibe diccionario de jugadores y lista de jugadores. Si sólo juega un jugador, siempre estará
    # en la primera posición. Si juega más de un jugador, primero agrupa por puntaje de mayor a menor.
    # Actualiza el diccionario de jugadores ordenando a los jugadores con este criterio. Si hay más de un jugador con el
    # mismo puntaje, se ordena aleatoriamente y se actualiza el diccionario.
    # No retorna datos.
    if len(lista_jugadores) == 1:
        dic_jugadores[lista_jugadores[0]][orden_jugador] = 1

    else:

        dic_orden_preliminar = {}
        for indice, jugador in enumerate(lista_jugadores):

            if dic_jugadores[jugador][puntaje_jugador] not in dic_orden_preliminar:
                dic_orden_preliminar[dic_jugadores[jugador][puntaje_jugador]] = [jugador]
            else:
                dic_orden_preliminar[dic_jugadores[jugador][puntaje_jugador]].append(jugador)

        lista_preliminar_ordenada = sorted(dic_orden_preliminar.items(), reverse=True)
        cont = 2
        for lista_jugadores in lista_preliminar_ordenada:
            cant_jugadores_por_puntaje = len(lista_jugadores[1])
            if cant_jugadores_por_puntaje == 1:
                nombre_jugador = lista_jugadores[1][0]
                dic_jugadores[nombre_jugador[0]][orden_jugador] = cont
                cont += 1
            else:
                shuffle(lista_jugadores[1])
                for v_nombre_jugador in lista_jugadores[1]:
                    dic_jugadores[v_nombre_jugador][orden_jugador] = cont
                    cont += 1


def otorgar_orden_jugadores(nro_partida, dic_jugadores):
    # Autor: Mauro Cuqejo. Recibe Nro de partida y diccionario de jugadores. Ordena a los jugadores dependiendo de si es la
    # primera partida o no. No retorna datos.
    lista_jugadores = list(dic_jugadores.keys())
    if nro_partida == 1:
        otorgar_orden_jugadores_primera_ronda(dic_jugadores, lista_jugadores)
    else:
        separar_ganador_anterior_partida(dic_jugadores, lista_jugadores)
        otorgar_orden_jugadores_general(dic_jugadores, lista_jugadores)


def generar_diccionario_partida(diccionario_partida, nro_partida):
    #Autor: Darío Giménez. Genera el diccionario de la partida
    diccionario_partida[nro_partida] = []
    return diccionario_partida



def almacenar_datos_partida(diccionario_partida, datos_partida):
    #Autor: Mauro Cuquejo. Espera una lista con los datos de cada jugador, al finalizar el turno y los almacena en la partida
    diccionario_partida.extend(datos_partida)



def elegir_palabra_aleatoria(lista_palabras):
    #Autor: Luan Corrionero. Elige una palabra aletoria
    palabra_adivinar = lista_palabras.pop(random.randint(0, len(lista_palabras)-1))
    return palabra_adivinar



def otorgar_palabras_jugadores(diccionario_jugadores, lista_palabras):
    #Autor: Luan.Corrionero. Otorga a los jugadores una palabra y genera la palabra oculta
    lista_palabras_utilizadas = []
    for jugador in diccionario_jugadores:
        palabra_aleatoria = elegir_palabra_aleatoria(lista_palabras)
        lista_palabras_utilizadas.append(palabra_aleatoria)
        diccionario_jugadores[jugador][palabra_actual].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_a_adivinar].extend(list(palabra_aleatoria))
        diccionario_jugadores[jugador][palabra_oculta].extend("_" * len(palabra_aleatoria))
    return lista_palabras_utilizadas



def actualizar_diccionario_palabras(diccionario_palabras, lista_palabras_utilizadas):
    #Autor: Luan Corrionero. Elimina las palabras usadas
    for palabra in lista_palabras_utilizadas:
        diccionario_palabras[palabra][palabra_usada] = True
    return diccionario_palabras



def transformar_guiones_bajos(letraIngresada, jugador, diccionario_jugadores):
    #Autor: Agustin Ramirez. Segun la posicion en la que se encuentra la letra, la reemplaza donde estaba el "_"
    pos = diccionario_jugadores[jugador][palabra_a_adivinar].index(letraIngresada)
    diccionario_jugadores[jugador][palabra_a_adivinar][pos] = "_"
    diccionario_jugadores[jugador][palabra_oculta][pos] = diccionario_jugadores[jugador][palabra_actual][pos]



def ingresar_letra():
    #Autor: Agustin Ramirez. Verifica que la letra ingresada sea correcta para el juego
    while True:
        letra_ingresada = input("Ingresa una letra: ")
        print("\n")
        letra_ingresada = letra_ingresada.upper()
        if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
            print("Ingreso un caracter invalido")
        else:
            return letra_ingresada



def generar_lista_palabras_por_cantidad_letras(dic_palabras, cant_jugadores):
    #Autor: Mauro Cuquejo. Genera una lista de palabras segun la cantidad de letras que decida el usuario
    lista_palabras = []
    while lista_palabras == [] or len(lista_palabras) < cant_jugadores:
        cant_letras = input("Ingresa la cantidad de letras de la palabra a adivinar, la palabra debe tener al menos 5 letras: ")
        while not cant_letras.isdigit():
            cant_letras = input("Valor incorrecto. Debe ingresar un número. Ingresa la cantidad de letras de la palabra a adivinar: ")
            while cant_letras.isdigit() and int(cant_letras) < 5:
                cant_letras = input("Recuerde que debe elegir palabras de al menos 5 letras. Intenta nuevamente: ")
        for clave in dic_palabras:
            if dic_palabras[clave][1] == int(cant_letras) and dic_palabras[clave][2] == False:
                lista_palabras.append(clave)
        if lista_palabras == [] or len(lista_palabras) < cant_jugadores:
            print("No se encontraron palabras con esa cantidad de letras.")
    return lista_palabras



def mostrar_datos_turno(diccionario_jugadores, jugador, jugador_eliminado):
    #Autor: Luan Corrionero. Muestra los datos relevantes para el turno.
    if not jugador_eliminado:
        print("-----------------------------------------\n")
        print("JUGADOR ACTUAL: {}".format(jugador))
        print("PUNTAJE: {} PUNTOS.".format(diccionario_jugadores[jugador][puntaje_jugador]))
    else:
        print("PERDISTE, {}. Tenés que esperar que acabe la partida para volver a jugar.".format(jugador))
        print("La palabra era: {}".format(" ".join(diccionario_jugadores[jugador][palabra_actual])))
    if len(diccionario_jugadores[jugador][letras_acertadas]) >= 0:
        print("CANTIDAD DE ACIERTOS: ", len(diccionario_jugadores[jugador][letras_acertadas]))
        print("INGRESASTE LAS SIGUIENTES LETRAS CORRECTAS: {}".format(", ".join(diccionario_jugadores[jugador][letras_acertadas])))
    if len(diccionario_jugadores[jugador][letras_erradas]) >= 0:
        print("CANTIDAD DE DESACIERTOS: ", len(diccionario_jugadores[jugador][letras_erradas]))
        print("INGRESASTE LAS SIGUIENTES LETRAS INCORRECTAS: {}".format(", ".join(diccionario_jugadores[jugador][letras_erradas])))
        print("\n")
    print(" ".join(diccionario_jugadores[jugador][palabra_oculta]))
    print("\n-----------------------------------------")
    print(diccionario_jugadores[jugador][hombrecito])
    print("-----------------------------------------\n")


def calcular_datos_partidas(diccionario_partida, jugador, nro_partida):
    # Autor: Agustin Ramirez. Procesa y calcula los datos generados durante la partida.
    for datos_jugador in diccionario_partida[nro_partida]:
        if datos_jugador[0] == jugador:
            jugador_actual = datos_jugador[0]
            puntaje_jugador_actual = datos_jugador[1][puntaje_jugador]
            cant_aciertos_jugador_actual = len(datos_jugador[1][letras_acertadas])
            cant_errores_jugador_actual = len(datos_jugador[1][letras_erradas])
    return jugador_actual, puntaje_jugador_actual, cant_aciertos_jugador_actual,cant_errores_jugador_actual


def mostrar_datos_partida(diccionario_partida, nro_partida):
    # Autor: Darío Giménez. Muestra los datos de la partida en curso.
    for datos_jugador in diccionario_partida[nro_partida]:
        jugador = datos_jugador[0]
        print("\n-----------------------------------------")
        print("DATOS DE LA PARTIDA {}:".format(nro_partida))
        v_nombre_jugador, v_puntaje_jugador, v_cant_aciertos_jugador, v_cant_errores_jugador = calcular_datos_partidas(diccionario_partida, jugador, nro_partida)
        print("NOMBRE JUGADOR: {}".format(v_nombre_jugador))
        print("INFORMACION PUNTAJE: {}".format(v_puntaje_jugador))
        print("INFORMACION CANTIDAD DE ACIERTOS: {}".format(v_cant_aciertos_jugador))
        print("INFORMACION CANTIDAD DE ERRORES: {}".format(v_cant_errores_jugador))
        print("-----------------------------------------\n")


def mostrar_datos_generales_partidas(diccionario_partida):
    # Autor: Agustin Ramirez. Muestra la estadística de las partidas jugadas.
    mostrar_datos_generales = input("¿Desea visualizar las estadísticas generales de las partidas jugadas? (S/N)")
    while not mostrar_datos_generales.upper() in ("S", "N"):
        mostrar_datos_generales = input("Opcion incorrecta. ¿Desea ver las palabras del diccionario? (S/N)")

    if mostrar_datos_generales.upper() == 'S':
        print("\n-----------------------------------------")
        print("DATOS GENERALES DE LA PARTIDAS JUGADAS:")
        dic_datos_generales = {}
        for nro_partida in diccionario_partida:
            for datos_jugador in diccionario_partida[nro_partida]:
                jugador = datos_jugador[0]
                v_nombre_jugador, v_puntaje_jugador, v_cant_aciertos_jugador, v_cant_errores_jugador = calcular_datos_partidas(diccionario_partida, jugador, nro_partida)
                if v_nombre_jugador not in dic_datos_generales:
                    dic_datos_generales[v_nombre_jugador] =[v_puntaje_jugador,v_cant_aciertos_jugador, v_cant_errores_jugador]
                else:
                    dic_datos_generales[v_nombre_jugador][1] += v_cant_aciertos_jugador
                    dic_datos_generales[v_nombre_jugador][2] += v_cant_errores_jugador
        for jugador in dic_datos_generales:
            print("\n-----------------------------------------")
            print("NOMBRE JUGADOR: {}".format(jugador))
            print("INFORMACION PUNTAJE TOTAL: {}".format(dic_datos_generales[jugador][0]))
            print("INFORMACION CANTIDAD DE ACIERTOS TOTALES: {}".format(dic_datos_generales[jugador][1]))
            print("INFORMACION CANTIDAD DE ERRORES TOTALES: {}".format(dic_datos_generales[jugador][2]))
        print("-----------------------------------------\n")


def limpiar_datos_jugadores_partida_anterior(diccionario_jugadores):
    # Autor: Luan Corrionero. Restaura los datos de los jugadores.
    for jugador in diccionario_jugadores:
        diccionario_jugadores[jugador][palabra_a_adivinar] = []
        diccionario_jugadores[jugador][palabra_actual] = []
        diccionario_jugadores[jugador][palabra_oculta] = []
        diccionario_jugadores[jugador][letras_acertadas] = []
        diccionario_jugadores[jugador][letras_erradas] = []
        diccionario_jugadores[jugador][jugador_eliminado] = False
        diccionario_jugadores[jugador][ganador_ultima_partida] = False
        diccionario_jugadores[jugador][hombrecito] = ""

def mostrar_datos_juego():
    # Autor: Darío Giménez. Muestra información acerca del juego.
    print("####TP1 AHORCADO####")
    print("------------------------------------------------------------------------------------------------------------------")
    print("Creadores: Mauro Cuquejo, Luan Corrionero, Agustín Ramirez, Darío Giménez.")
    print("------------------------------------------------------------------------------------------------------------------\n")
    print("TIPS: cuando se ingrese una letra, correcta o incorrecta, la pantalla solicitará presionar Enter para continuar. Tenga en cuenta esto antes ingresar una letra, para evitar confusiones.\n")

def preguntar_continuar_juego(nro_partida, diccionario_partida):
    # Autor: Agustin Ramirez. Establece la continuación o finalización del juego.
    seguir_juego = True

    continuar = input("¿queres continuar jugando? (S/N)")
    while not continuar.upper() in ("S", "N"):
        continuar = input("Opcion incorrecta. ¿queres continuar jugando? (S/N)")

    if continuar.upper() == 'S':
        nro_partida += 1

        seguir_partida = True

    else:
        seguir_partida = False
        seguir_juego = False

        mostrar_datos_generales_partidas(diccionario_partida)
    return seguir_juego, seguir_partida, nro_partida