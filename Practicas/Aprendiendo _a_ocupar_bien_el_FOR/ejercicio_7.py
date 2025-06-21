#  Suma de filas de una matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

columna1 = 0
columna2 = 0
columna3 = 0

for fila1 in matriz[0]:
    columna1 += fila1
print("Suma de la fila 1: ",columna1)

for fila2 in matriz[1]:
    columna2 += fila2
print("Suma de la fila 2: ",columna2)

for fila3 in matriz[2]:
    columna3 += fila3
print("Suma de la fila 3: ",columna3)