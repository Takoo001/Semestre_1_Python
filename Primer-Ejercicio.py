"""PSEINT A PYTHON"""

v = int(input("Por favor, ingrese el valor de la cuenta a pagar: "))

print("Ahora seleccione el porcentaje de propina que desea dejar")
print("Esta propina será sumada a su cuenta total")
print("1. 10%")
print("2. 15%")
print("3. 20%")

numero = int(input("Por favor, eliga una opcion: "))

a = (v * 0.10) + v
b = (v * 0.15) + v
c = (v * 0.20) + v

if numero == 1:
    print("El valor total de su cuenta junto con la propina es de", a)
elif numero == 2:
    print("El valor total de su cuenta junto con la propina es de", b)
elif numero == 3:
    print("El valor total de su cuenta junto con la propina es de", c)
else:
    print("Opción inválida. Por favor seleccione entre 1, 2 o 3.")
