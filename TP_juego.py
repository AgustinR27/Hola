from TP_modulos import solicitar_cantidad_jugadores
from TP_modulos import generar_diccionario_jugadores
from TP_modulos import generar_diccionario_palabras
from TP_modulos import otorgar_orden_jugadores
from TP_modulos import ingresar_letra
from TP_modulos import generar_lista_palabras_por_cantidad_letras
from TP_modulos import generar_diccionario_partida
from TP_modulos import almacenar_datos_partida
from TP_modulos import otorgar_palabras_jugadores
from TP_modulos import actualizar_diccionario_palabras
from TP_modulos import transformar_guiones_bajos
from TP_modulos import dibujar_hombrecito
from TP_modulos import mostrar_datos_turno
from TP_modulos import pausa_para_continuar
from TP_modulos import mostrar_datos_partida
from TP_modulos import limpiar_datos_jugadores_partida_anterior
from TP_modulos import mostrar_datos_juego
from TP_modulos import preguntar_continuar_juego

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

def iniciar_juego():
	seguir_juego = True
	nro_partida = 1

	while seguir_juego:
		mostrar_datos_juego()
		diccionario_palabras = generar_diccionario_palabras()
		cant_jugadores = solicitar_cantidad_jugadores()
		diccionario_jugadores = generar_diccionario_jugadores(cant_jugadores)
		diccionario_partida = {}
		seguir_juego = iniciar_partida(nro_partida, diccionario_partida, diccionario_jugadores, cant_jugadores, diccionario_palabras)


def iniciar_partida(nro_partida, diccionario_partida, diccionario_jugadores, cant_jugadores, diccionario_palabras):
	seguir_partida = True

	while seguir_partida:
		nro_ronda = 1

		if nro_partida not in diccionario_partida:
			diccionario_partida = generar_diccionario_partida(diccionario_partida, nro_partida)

		otorgar_orden_jugadores(nro_partida, diccionario_jugadores)
		limpiar_datos_jugadores_partida_anterior(diccionario_jugadores)
		lista_palabras = generar_lista_palabras_por_cantidad_letras(diccionario_palabras, cant_jugadores)
		lista_palabras_usadas = otorgar_palabras_jugadores(diccionario_jugadores, lista_palabras)
		actualizar_diccionario_palabras(diccionario_palabras, lista_palabras_usadas)
		lista_jugadores_ordenada = [item[0] for item in sorted(diccionario_jugadores.items(), key=lambda x: x[1][orden_jugador])]
		iniciar_ronda(nro_partida, nro_ronda, lista_jugadores_ordenada, diccionario_jugadores)
		almacenar_datos_partida(diccionario_partida[nro_partida], diccionario_jugadores.items())
		mostrar_datos_partida(diccionario_partida, nro_partida)
		seguir_juego, seguir_partida, nro_partida = preguntar_continuar_juego(nro_partida, diccionario_partida)
	return seguir_juego


def iniciar_ronda(nro_partida, nro_ronda, lista_jugadores_ordenada, diccionario_jugadores):
	seguir_ronda = True

	contador_jugadores_eliminados = 0
	while seguir_ronda:

		seguir_ronda, partida = iniciar_turno(nro_partida, nro_ronda, lista_jugadores_ordenada, diccionario_jugadores, contador_jugadores_eliminados)
		nro_ronda += 1

def iniciar_turno(nro_partida, nro_ronda, lista_jugadores_ordenada, diccionario_jugadores, contador_jugadores_eliminados):
	seguir_partida = True
	seguir_ronda = True
	seguir_turno = True
	cant_jugadores = len(lista_jugadores_ordenada)

	posicion = 0
	print("\n" * 100)
	print("PARTIDA NRO: {} - RONDA NRO: {}".format(nro_partida, nro_ronda))
	print("-----------------------------------------\n")

	while seguir_turno:
		jugador = lista_jugadores_ordenada[posicion]
		cont_aciertos = 0

		if not diccionario_jugadores[jugador][jugador_eliminado]:
			continuar_buscando_letra = True

			while continuar_buscando_letra:
				mostrar_datos_turno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
				letra_ingresada = ingresar_letra()

				while letra_ingresada in diccionario_jugadores[jugador][palabra_a_adivinar]:
					diccionario_jugadores[jugador][letras_acertadas].append(letra_ingresada)
					transformar_guiones_bajos(letra_ingresada, jugador, diccionario_jugadores)
					diccionario_jugadores[jugador][puntaje_jugador] += 1
					cont_aciertos += 1

				if cont_aciertos == 0:
					diccionario_jugadores[jugador][puntaje_jugador] -= 2
					diccionario_jugadores[jugador][letras_erradas].append(letra_ingresada)
					cantidad_de_errores = len(diccionario_jugadores[jugador][letras_erradas])
					diccionario_jugadores[jugador][hombrecito] = dibujar_hombrecito(cantidad_de_errores)
					mostrar_datos_turno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])

					if cant_jugadores > 1:
						print("FALLASTE, {}. LE TOCA AL SIGUIENTE JUGADOR.".format(jugador))
					else:
						print("FALLASTE, {}. OTRA VEZ SERÁ.".format(jugador))
					pausa_para_continuar()

					continuar_buscando_letra = False

					if cantidad_de_errores == 7:
						contador_jugadores_eliminados += 1
						diccionario_jugadores[jugador][jugador_eliminado] = True
						mostrar_datos_turno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
						print("PERDISTE, {}. SE ACABÓ LA PARTIDA PARA VOS.".format(jugador))
						pausa_para_continuar()

				else:

					if diccionario_jugadores[jugador][palabra_oculta] == diccionario_jugadores[jugador][palabra_actual]:
						diccionario_jugadores[jugador][puntaje_jugador] += 30
						diccionario_jugadores[jugador][ganador_ultima_partida] = True
						seguir_turno = False
						seguir_ronda = False
						seguir_partida = False
						mostrar_datos_turno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
						print("GANASTE, {}. ESTA PARTIDA SE ACABA ACÁ.".format(jugador))
						pausa_para_continuar()
						continuar_buscando_letra = False

					else:
						mostrar_datos_turno(diccionario_jugadores, jugador, diccionario_jugadores[jugador][jugador_eliminado])
						print("ACERTASTE, {}. PODÉS SEGUIR INGRESANDO LETRAS.".format(jugador))
						pausa_para_continuar()
						cont_aciertos = 0

		if contador_jugadores_eliminados == cant_jugadores:
			print("GANÓ COM.")
			seguir_turno = False
			seguir_ronda = False
			seguir_partida = False

		else:
			posicion += 1

			if posicion > len(lista_jugadores_ordenada) - 1:
				seguir_turno = False

	return seguir_ronda, seguir_partida