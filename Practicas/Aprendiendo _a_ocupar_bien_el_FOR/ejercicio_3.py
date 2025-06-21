# Cuenta cuántos números de esta lista son mayores que 10:
numeros = [4, 15, 9, 22, 3, 18]

lista_de_numeros = 0

for numero in numeros:
    if numero > 10:
        lista_de_numeros += 1 
print("Hay",lista_de_numeros,"numeros mayores que 10")

"""PARA ESTE FOR LO QUE MAS SE USA ES LA LOGICA PORQUE:
 SI NUESTRO CONTADOR (numero) ENCUENTRA UN NUMERO MAYOR QUE 10
 EN LA lista_de_numeros SE SUMA 1. PORQUE ESTAMOS CONTANDO 
 CUANTOS NUMEROS MAYORES QUE 10 HAY EN TOTAL"""