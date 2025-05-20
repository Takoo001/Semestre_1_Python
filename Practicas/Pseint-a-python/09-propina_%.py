cuenta = float(
    input("Por favor ingrese el total de su cuenta: "))
print()
print("Ahora seleccione el porcentaje de propina que desea dejar")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Sin propina")
print()
while True:
    porcentaje = int(input("Por favor seleccione una opcion (1, 2, 3 o 4): "))
    print()
    if porcentaje in [1, 2, 3, 4]:
        break
    else:
        print("Opcion invalida, por favor seleccione una opciones de las anteriormente mostradas")
        print()

pr1 = (cuenta * 10 / 100) + cuenta
pr2 = (cuenta * 15 / 100) + cuenta
pr3 = (cuenta * 20 / 100) + cuenta


if porcentaje == 1:
    print("EL total de cuenta a pagar con el 10% de propina es de: {:.3f}".format(
        pr1), "pesos")
elif porcentaje == 2:
    print("El total de cuenta a pagar con el 15% de propina es de: {:.3f}".format(
        pr2), "pesos")
elif porcentaje == 3:
    print("El total de cuenta a pagar con el 20% de propina es de: {:.3f}".format(
        pr3), "pesos")
elif porcentaje == 4:
    print("EL total de cuenta sin propina son: {:.3f}".format(
        cuenta), "pesos")
else:
    print("Opcion no valida, por favor ingrese una de las opciones mostradas")
