N = int(input("Escriba la cantidad de focos que hay en el lote: "))
R = 0
V = 0
B = 0
for i in range(N):
    F = str(input("Escriba el nombre del color del foco: rojo, verde o blanco: "))
    if F == "rojo":
        R = R + 1
    if F == "verde":
        V = V + 1
    if F == "Blanco":
        B = B + 1
print("La cantidad de focos rojos es: ", R)
print("La cantidad de focos verdes es: ", V)
print("La cantidad de focos blanco es: ", B)


