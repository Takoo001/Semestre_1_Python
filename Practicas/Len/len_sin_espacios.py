palabra = input("Ingrese un resumen: ") # SE LE PIDE AL USUARIO INGRESAR UN TEXTO QUE SE GUARDA EN (PALABRA)

solo_palabras = [c for c in palabra if c.isalpha()] 
# AQUI SE UTILIZA LA FUNCION (isalpha()) LA CUAL VERIFICA SI ESTA ENTRE LA A-Z 

palabra_sin_espacios = len(solo_palabras)
# SE LE APLICA LA FUNCION (len) PARA QUE HAGA EL CONTEO DE PALABRAS SIN ESPACIOS
print()
print("La cantidad de letras del resumen son: ",palabra_sin_espacios,"palabras") 
# SE IMPRIME LA CANTIDAD DE LETRAS SIN ESPACIOS DEL TEXTO INGRESADO