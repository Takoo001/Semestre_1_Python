p1 = float(input("Ingresa el primer promedio: "))
print()
p2 = float(input("Ingresa el segundo promedio: "))
print()
tr = float(input("Ingresa el promedio de las tareas: "))
print()
ppt = float(input("Ingresa el promedio de ppt: "))
print()


nf = (p1 * 0.3) + (p2 * 0.5) + (tr * 0.1) + \
    (ppt * 0.1)  # Nota final sin redondear

nf_redondeada = round(nf, 2)  # Nota final redondeada


if nf >= 4.0:
    print("Usted esta aprobado con un promedio de: ", nf_redondeada)
else:
    print("Usted esta reprobado con un promedio de: ", nf_redondeada)
