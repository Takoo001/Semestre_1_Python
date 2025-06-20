# HECHO POR: Samir Arana y Matias Rain

while True:
    num = int(input("\nIngrese el número para calcular su factorial: "))
    if num < 0:
        print("\nEl factorial no está definido para números negativos.\n")
    elif num == 0:
        print("\nEl factorial de 0 es: 1\n")
    else:
        n = 1
        for i in range(num, 0, -1):
            n = n * i
        print(f"\nEl factorial de {num} es: {n}\n")
    print("(1) Para seguir calculando factoriales")
    print("(2) Para terminar de calcular")
    decicion = input("Eleccion: ")
    if decicion == "2":
        print()
        print("Adios!!")
        break
    elif decicion == "1":
        print()
        print("Ok, Sigamos!!")