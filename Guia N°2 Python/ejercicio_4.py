# HECHO POR: Samir Arana y Matias Rain

n = int(input("Ingrese la cantidad de cubos: ")) # PIDIENDO AL USUARIO LA CANTIDADAS DE CUBOS
impar = 1
# CREACION DEL BUCLE CON IMPRESION EN PIRAMIDE DE ACUERDO A CUBO INGRESADO POR EL USUARIOO
for i in range(1, n + 1): 
    suma = 0
    terminos = []

    for j in range(i):
        terminos.append(impar)
        suma += impar
        impar += 2

    expresion = " + ".join(map(str, terminos))
    print(f"{i}^3 = {expresion} = {suma}")