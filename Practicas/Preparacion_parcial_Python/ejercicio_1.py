"""Pedir al usuario su nombre y edad,
luego mostrar cuantos años tendra en 10 años"""

nombre = input("Ingrese su nombre: ")
print()
edad = int(input("Ahora ingrese su edad: "))
print()

edad_en_10_años = edad + 10

print(f"Señor {nombre} usted tiene {edad} años y en 10 años tendra {edad_en_10_años} años")