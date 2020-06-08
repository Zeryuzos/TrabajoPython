CC = 0
MeC = 0
MaC = 0
N = int(input("Ingrese la variable: "))
for i in range(N):
    print("Proceso ", i )
    Can = float(input("Ingrese el valor de la cantidad: "))
    if Can == 0:
        CC = CC+1
    if Can < 0:
        MeC = MeC+1
    if Can > 0:
        MaC = MaC+1
print("Total de ceros", CC)
print("Total de menor a cero", MeC)
print("Total de mayor a cero", MaC)