Pu = float(input("Por favor, ingrese el precio unitario del libro: "))
print()
print("Entonces el precio unitario es de: ", Pu, "pesos")
print()
Cl = int(input("Ahora la cantidad de libros que desea comprar: "))
print()
print("Entonces la cantidad de libros son: ", Cl)
print()
print("Ahora por favor, seleccione la opcion que le corresponda para aplicar los descuento")
print()
print("1. Libro academico (15% des)")
print("2. Libro academico y afiliacion Ulagos (15% + 5% des)")
print("3. Ninguna de las anteriores")
print()

while True:
    numero = int(input("Seleccione una opcion (1, 2 o 3): "))
    if numero in [1, 2, 3]:
        break
    else:
        print("La opcion no existe, seleccione entre (1, 2 o 3): ")


Total = (Pu * Cl)

Desa = (Total * 0.15)
Dess = (Total - Desa)

Dayau = (Total * 0.20)
Dayy = (Total - Dayau)

Vtd = (Dayy * 0.05)
Vtdr = (Dayy - Vtd)


if numero == 1:
    print()
    print("Su monto original es de: ", Total, "pesos")
    print()
    print("Ahora, se le descontaran: ", Desa, "pesos de su monto original")
    print()
    print("El total a pagar con el descuento es de: ", Dess, "pesos")
elif numero == 2:
    print()
    print("Su monto original es de: ", Total, "pesos")
    print()
    print("El descuento a aplicar es de: ",
          Dayau, "pesos sobre el monto original")
    print()
    print("El total a pagar junto a los 2 descuentos es de: ", Dayy, "pesos")
elif numero == 3:
    print()
    print("No es beneficiario a ningun descuento")
    print()
    print("Por lo que su total a pagar es de: ", Total, "pesos")


if Dayy > 50000:
    print()
    print("Ya que su compra, junto a los descuentos supera los 50.000 con un total de: ", Dayy, "pesos")
    print()
    print("Se le va a aplicar un descuento adicional de: ", Vtd, "pesos")
    print()
    print("Su total a pagar junto al descuento adicional es de: ", Vtdr, "pesos")
