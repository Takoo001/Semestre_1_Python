# HECHO POR: Samir Arana y Matias Rain

# VARIABLES DE INICIALIZACION
s = 0 
a = 500
b = 456

# VARIABLES PARA IR GUARDANDO RESULTADOS
suma_a = 0
resta_b = 0


# INICIO DEL BUCLE
while a <= 800:
    s = s + a
    suma_a = suma_a + a
    print("\nSumandole 10 al:",a)
    a += 10

    if b >= 0:
        s = s + b
        resta_b = resta_b + b
        print("\nRestandole 2 al:",b)
        b = b - 2

print("\nLa suma total de los valores de 500 de 10 en 10 es:",suma_a)
print("\nLa suma total de las restas de los valores de 456 de 2 en 2 es:",resta_b)
print("\nEstos dos valores sumados son:",s) 
print()