"""edad = 15
while edad < 18:  # BUCLE INFINITO
    print("Eres menor de edad")"""
    
num = 0
while num <= 100:
    print(num)
    num += 2
print("Primer bucle terminado!!")

while num <= 200:
    print(num)
    num += 2
else:
    print("Mi condicion ea igual o mayor a 200")
print("Segundo bucle terminado!!")

# USO DEL BREAK 
while True:
    parametro = input(">")
    if parametro == "Salir".lower():
        break # TERMINA SI ESTO ES VERDADERO
    else: # SINO SIGUE IMPRIMIENDO EL PARAMETRO QUE SE LE DIO (>)
        print(parametro)
        
num2 = 0
while num2 >= 50:
    num2 += 1
    if num2 == 40:
        continue # SE SALTA LA LINEA DE 39 A 41 EN SU SUMA
    print(num2)
    
