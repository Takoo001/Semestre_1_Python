# Encuentra el número más grande de una lista sin usar max().
numeros = [17, 3, 21, 5, 9, 30, 2]

lista = 0

for numero in numeros:
    if numero > lista:
        lista = numero
        
print("El numero mas grande es: ",lista)

"""EN ESTE EJERCICIO APRENDI QUE:
SE PUEDE ACTUALIZAR EL VALOR DE UNA VARIABLE COMO SE VE EN EL EJERCICIO ANTERIOR
EN EL CUAL DECIMOS QUE SI EL NUMERO RECORRIDO ES MAYOR QUE EL NUMERO QUE TENEMOS
EN NUESTA LISTA, ESTA SE ACTUALIZA AL NUMERO QUE ENCONTRAMOS Y ASI HASTA TERMINAR
Y ENCONTRAR EL NUMERO MAYOR :p"""