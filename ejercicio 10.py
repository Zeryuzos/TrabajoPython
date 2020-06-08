N = int(input("Ingrese el numero de trabajadores: "))
for i in range(N):
    print("Proceso ",i)
    NT = str(input("Ingresa el nombre del trabajador: " ))
    H = int(input("Ingresa las horas trabajadas: "))
    SH = int(input("Ingresa el sueldo por hora: "))
    SS = H * SH
    D = 0
    if SS > 0 and SS <= 150:
        D = SS * 0.05
    if SS > 150 and SS < 300:
        D = SS * 0.07
    if SS > 300 and SS < 450:
        D = SS * 0.09
    SS = SS - D
    print("Nombre del trabajador: ", NT)
    print("Descuento total: ", D)
    print("Sueldo semanal: ", SS)
