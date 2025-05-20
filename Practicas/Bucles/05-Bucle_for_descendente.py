n = int(input("Ingrese un numero para mostrarlo en orden descendente: "))

for i in range(n, 0, -1):  # Va empezar desde (n), va llegar hasta 0, va ir de -1 en -1
    print(i, end=", ")
