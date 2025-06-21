# Sumar columnas de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


num_columnas = len(matriz[0])

for j in range(num_columnas):
    suma_columna = 0
    for fila in matriz:
        suma_columna += fila[j]
    print(f"La suma total de la columna {j} es: {suma_columna}")
    
    
"""NO SE COMO LO HICE PERO ME FALTA ENTENDER, gg ez :p"""