enteros = int(input("Ingrese un numero entero: "))
print()
flotante = float(input("Ahora ingrese un numero flotante (con decimales): "))
print()
complejo = complex(input("Ahora ingrese un numero complejo (ejemplo: 2j): "))
print()

# OPERACIONES
potencia_compleja = complejo ** enteros
suma_mixta = complejo + flotante
Producto_mixto = complejo * enteros

modulo_potencia_compleja = round(abs(potencia_compleja), 3)

print("Potencia compleja: ",potencia_compleja)
print()
print("Suma mixta: ",suma_mixta)
print()
print("Producto mixto: ",Producto_mixto)
print()
print("Modulo de potencia compleja: ",modulo_potencia_compleja)