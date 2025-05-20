monto = float(input("Cual es el monto que desea invertir: "))
print()
intereses = float(input("Cuales son los intereses anuales: "))
print()
años = int(input("Cuanto años desea invertir: "))
print()

for i in range(años):
    # Esto es lo mismo que (monto = monto * (1 + intereses / 100))
    monto *= 1 + intereses / 100
    # str sirve para pasar cualquier valor en una cadena de texto (string)
    print("Su capital despues de", str(i+1),
          "años sera de:", str(round(monto, 2)))
    # Redondea el monto en 2 decimales


# EL MONTO *= 1 + INTERESES / 100 PUEDE SER LO MISMO QUE
# (x = x + 1)||(x += 1)
# (total = total * 2)|| total *= 2
# (n = n - 3)||(n -= 3)
