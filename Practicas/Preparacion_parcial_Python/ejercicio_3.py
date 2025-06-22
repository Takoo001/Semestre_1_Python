"""Crear un programa que recorra una lista de frutas e imprima solo las que empiecen con "a" """

frutas = ["manzana", "banana", "arándano", "aguacate", "pera", "ananá"]

for fruta in frutas:
    if fruta.startswith("a"):
        print(fruta)


