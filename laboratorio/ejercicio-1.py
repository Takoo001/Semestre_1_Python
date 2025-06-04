#CONSOLA PRECIOS UNITARIOS Y CANTIDAD DE PRODUCTOS
martillo = float(input("Ingrese el precio unitario de martillo: "))
martillo2 = int(input("Ingrese la cantidad de martillos que llevara: "))
clavos = float(input("Ingrese el precio unitario de cajas de clavos: "))
clavos2 = int(input("Ingrese la cantidad de cajas de clavos que llevara: "))
serrucho = float(input("Ingrese el precio unitario de serrucho: "))
serrucho2 = int(input("Ingrese la cantidad de serruchos que llevara: "))
tornillos = float(input("Ingrese el precio unitario de tornillos: "))
tornillos2 = int(input("Ingrese la cantidad de cajas de tornillos que llevara: "))

#CALCULAR Y MOSTRAR LOS SUBTOTALES DE CADA PRODUCTO
subtotal_m = martillo * martillo2
print("Subtotal martillos: ",(round(subtotal_m,2)))
print()
subtotal_c = clavos * clavos2
print("Subtotal clavos: ",(round(subtotal_c,2)))
print()
subtotal_s = serrucho * serrucho2
print("Subtotal serruchos: ",(round(subtotal_s,2)))
print()
subtotal_t = tornillos * tornillos2
print("Subtotal tornillos: ",(round(subtotal_t,2)))
print()

#SUMA DE LOS SUBTOTALES DE LOS PRODUCTOS
subtotal = subtotal_c + subtotal_m + subtotal_s + subtotal_t
print(f"La suma de sus subtotales es: {subtotal}")
print()

#VALOR MAXIMO Y VALOR MINIMO DE LOS SUBTOTALES
print("Valor maximo de los subtotales: ",(max(subtotal_c, subtotal_m, subtotal_s, subtotal_t)))
print("Valor minimo de los subtotales: ",(min(subtotal_c, subtotal_m, subtotal_s, subtotal_t)))
print()

#PROMEDIO DE LOS PRECIOS UNITARIOS
prom = (martillo + serrucho + clavos + tornillos) / 4
print("El promedio de los precios unitarios de cada herramienta es: ", (round(prom,2)))
print()

#IVA TOTAL DE LOS SUBTOTALES 
iva = subtotal * 0.19
print(f"El IVA de su subtotal es: {iva}")
