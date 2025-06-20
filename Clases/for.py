newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)
    
# SEGUNDA FORMA DE OCUPAR EL FOR
for i in range(1, 11,): # DEL UNO AL 10 PERO SE COLCA 11 PORQUE NO TOMA EL ULTIMO NUMERO
    print(i)           # ESTO DICE, COMIENZA EN 0 EN UN RANGO DESDE (1 A 11) 


# TERCERA FORMA DE OCUPAR EL FOR
for i in range(2, 21, 2): # ESTE FOR NOS DICE QUE VA EMPEZAR DE 2, HASTA LLEGAR A 20 Y VA IR DE 2 EN 2
    print(i)

# FOR ELSE
for n in range(2, 10): # N VA DE UN RANGO DE 2 HASTA 10
    for i in range(2, n): # i VA DE 2 HASTA N
        if n % i == 0: # SI n AL SER DIVIDIDO POR i ES IGUAL A 0 ENTONCES ES UN NUMUERO COMPUESTO
            print(f"{n} es un numero compuesto, divisible por {i}")
            break 
    else: # SINO NO ES UN NUMERO PRIMO
        print(f"{n} no es un numero primo")
