def dibujarHombrecito(rango):
    dibujo = ""
    hombrecito = ["\n | \n | \n"," 0\n","/","|","\ \n","/"," \ \n"]

    for posicion in range(rango):
        dibujo += "".join(hombrecito[posicion])
    return dibujo

print("turno 0:")
print(dibujarHombrecito(0))
print("NO MUESTRA NADA EN EL TURNO CERO")
print("\n")
print("turno 1:")
print(dibujarHombrecito(1))
print("\n")
print("turno 2:")
print(dibujarHombrecito(2))
print("\n")
print("turno 3:")
print(dibujarHombrecito(3))
print("\n")
print("turno 4:")
print(dibujarHombrecito(4))
print("\n")
print("turno 5:")
print(dibujarHombrecito(5))
print("\n")
print("turno 6:")
print(dibujarHombrecito(6))
print("\n")
print("turno 7:")
print(dibujarHombrecito(7))
