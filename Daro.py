from string import ascii_uppercase
abecedario = ascii_uppercase
def ingresarLetra():
    #Entradas: Recibe una letra ingresada por teclado.
    #Salidas:  Devuelve una letra.
    #Restricciones: Debe ingresar caracter válido y de una longitud.
    while True:
        letraIngresada = input('Ingrese una letra: ')
        letra = letraIngresada.upper()
        if len(letra) != 1:
            print('Introduce una sola letra.')
        elif letra not in abecedario:
            print('Has ingresado un caracter invalido.')
        else:
            return letra

print(ingresarLetra())

def acierto():
    if acierto == True:
        