A = 0
R = 0
CA = int(input("Ingrese la nota aprobatoria: "))
N = int(input("Ingrese el numero de veses: "))
for i in range(N):
    print("Proseso ", i)
    C = int(input("Ingrese la nota: "))
    if C >= CA:
        A = A + 1
    else:
        R = R + 1
print("Total de aprobados: ",A)
print("Total de Reprobados: ",R)
