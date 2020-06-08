P = float(input("Ingrese el precio: "))
D = 0
if P >= 200:
    D = P * 0.15
if P > 100 and P < 200:
    D = P * 0.12
if P < 100:
    D = P * 0.1
C = P - D
print("Costo total: ",C)
print("Descuento total: ",D)