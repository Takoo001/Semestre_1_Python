palabra = input("Ingresa una palabra: ").lower()
contador = {} # AQUI SE GUARDAN LOS RESULTADOS

for letra in palabra:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print("Conteo de letras:", contador)
# Recorremos letra por letra la palabra "banana"
# Primero va por la "b", como no está en el diccionario, la guarda con valor 1
# Después va por la "a", tampoco está, así que también la guarda con valor 1
# Luego va por la "n", que tampoco estaba, así que la guarda con valor 1
# Después vuelve a encontrar la "a", como ya estaba, le suma 1 (ahora "a" vale 2)
# Luego vuelve la "n", como ya estaba también, le suma 1 (ahora "n" vale 2)
# Por último otra "a", como ya estaba con 2, le suma 1 más (ahora "a" vale 3)
# Al final tenemos un conteo de cuántas veces aparece cada letra