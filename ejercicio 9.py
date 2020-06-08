T = 0
TF = 0
A = int(input("Ingresa la cantidad de aulas: "))
for i in range(A):
    print("Aula ",i)
    Es = int(input("Ingrese la cantidad de estudiantes: "))
    for a in range(Es):
        E = int(input(f"Ingresa la edad del  estudiante {a} : "))
        T = T + E
        P = T / Es
    print("El promedio del aula ", i, "es: ", P)
    TF = TF + P
    PT = TF / A
print("El promedio total de todas las aulas es: ", PT )
