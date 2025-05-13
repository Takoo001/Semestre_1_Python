Pu = float(input("Por favor, ingrese el precio unitario del libro: "))
print()
print("Entonces el precio unitario es de:", Pu)
print()
Cl = int(input("Ahora ingrese la cantidad de libros que desea comprar: "))
print()
print("Entonces la cantidad de libros que quiere comprar es de:", Cl)
print()
print("Ahora por favor, seleccion la opcion que le corresponda para aplicar los descuentos")
print()
print("1. Libro academico (15% des.)")
print("2. Libro academico y afiliacion Ulagos (15% + 5% des.)")
print("3. Ninguna de las anteriores")

while True:
    numero = int(input("Por favor, elija una opción (1, 2 o 3): "))
    if numero in [1, 2, 3]:
        break
    else:
        print("No existe la opcion. Por favor, seleccione entre: 1, 2 o 3.")

# Total sin descuentos
Total = (Pu * Cl)

# Descuento academico
Desa = (Total * 0.15)  # Descuento
Dess = (Total - Desa)  # Total con descuento aplicado

# Descuento academico + Afilicacion Ulagos
Dayau = (Total * 0.20)
Dayy = (Total - Dayau)

# Si la compra con los 2 descuentos supera los 50.000
Sp = (Dess + Dayy)

# Valor total con los 3 descuentos
Vtd = (Dayy * 0.05)
Vtdr = (Dayy - Vtd)


if numero == 1:
    print()
    print("Su monto original sin descuento es de: ", Total, "pesos")
    print("Ahora, se le descontaran: ", Desa, "pesos de su monto original")
    print()
    print("El valor total con descuento academico es de: ", Dess, "pesos")
elif numero == 2:
    print()
    print("Su monto original sin descuento es de: ", Total, "pesos")
    print("Ahora, se le descontaran: ", Dayau, "pesos de su monto original")
    print()
    print("El valor total con ambos descuentos es de: ", Dayy, "pesos")
elif numero == 3:
    print()
    print("No es beneficiario a ningun descuento")
    print("Por lo que su valor total a pagar es de: ", Total, "pesos")
print()
print("Gracias por su compra!!!")
