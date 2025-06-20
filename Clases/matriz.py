# MATRIZ
matriz = [
    [1,2,3], # FILA 0
    [4,5,6], # FILA 1
    [7,8,9] # FILA 2
]  #C0 #C1 #C2   (COLUMNA 0, COLUMNA 1 Y COLUMNA 2)

for fila_id, fila in enumerate (matriz):
    for col_id, valor in enumerate(fila):
        print(f"Posicion ({fila_id},{col_id}) = {valor}")
        

# TECNICAS PARA SALIR DE BUCLES ANIDADOS
