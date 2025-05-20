# Ingresa tu edad (input), el numero lo paso a entero (int), esto se guarda en (edad)
edad = int(input("Por favor, ingrese su edad actual: "))

for i in range(edad):  # Repite lo que esta dentro de for, una vez por cada numero, desde 0 hasta uno antes de llegar a (edad)
    # Mientras el bucle esta activo, muestra esto al usuario
    print("Cumpliste", i + 1, "años")
