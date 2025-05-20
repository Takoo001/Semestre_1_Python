numero = int(input("Por favor coloque un numero para mostrar su impares: "))

for i in range(1, numero+1, 2):  # Empieza en 1 hasta llegar al (numero+1) y avanza de 2 en 2
    # Esto imprime el valor de i, pero en lugar de saltar de línea cada vez (como hace normalmente print()), usa una coma y un espacio al final.
    print(i, end=", ")
    # Así todos los números aparecen en la misma línea, separados por comas.
