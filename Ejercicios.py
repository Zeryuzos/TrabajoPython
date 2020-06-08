class ejercicios:
    def ejercicio1(self):
        S = float(input("Ingrese el salario incial: "))
        A = 0
        while A <= 6:
            if A == 0:
                S = S
                print("El año actual es: ", S)
            if A == 1:
                S = (S * 0.10) + S
                print("El primer año es: ", S)
            if A == 2:
                S = (S * 0.10) + S
                print("El segundo año es: ", S)
            if A == 3:
                S = (S * 0.10) + S
                print("El tercer año  es: ", S)
            if A == 4:
                S = (S * 0.10) + S
                print("El cuarto año es: ", S)
            if A == 5:
                S = (S * 0.10) + S
                print("El quinto año es: ", S)
            if A == 6:
                S = (S * 0.10) + S
                print("El sexto año es: ", S)
            A = A + 1
        print("El salario que recibira despues de 6 años es: ", S)
EjerPy=ejercicios()
Ejerpy.ejercicio1()