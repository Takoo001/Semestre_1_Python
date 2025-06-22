"""Solicitar 3 notas y calcular el promedio. Mostar si esta aprobado"""

nota1 = float(input("Ingrese la primera nota: "))
print()
nota2 = float(input("Ingrese la segunda nota: "))
print()
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1+ nota2 + nota3) / 3

if promedio >= 4.0:
    print("Usted esta aprobrado")
else:
    print("Usted esta repobrado")