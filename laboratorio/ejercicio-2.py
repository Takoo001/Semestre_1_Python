print("Hola, por favor ingresa un resumen de maximo 50 caracteres") # 1. INGRESAR RESUMEN EN FORMATO STRING

resumen = input() # USUARIO DEBE INGRESAR RESUMEN

len(resumen) # PASANDO EL RESUMEN A NUMERO DE CARACTERES

variable_booleana = len(resumen) < 50 # VARIABLE QUE GUARDA SI LOS NUMEROS DE CARACTERES DEL RESUMEN SUPERAN LOS 50 CARACTERES
print() # LINEA EN BLANCO (SALTO DE LINEA)
print(variable_booleana) # IMPRIMIENDO NUESTRA VARIABLE QUE DEBE DAR (TRUE O FALSE) DE ACUERDO A SI PASA LOS 50 O NO
print()
print("La longitud total de resumen es de: ",len(resumen),"caracteres")
print()
print("Resumen en mayusculas: ",resumen.upper()) # RESUMEN EN MAYUSCULAS CON FUNCION UPPER
print()
print("Resumen en minusculas: ",resumen.lower()) # RESUMEN MINUSCULAS CON FUNCION LOWER
print()

letra_e = resumen.count("e") # CONTADOR DE CUANTAS VECES APARECE EL CARACTER "e"

print("Las veces que aparece el caracter (e) son: ",letra_e,"veces")

primeros_15_caracteres = resumen[:15] # MOSTRANDO LOS PRIMEROS 15 CARACTERES
print("Primeros 15 caracteres del resumen: ",primeros_15_caracteres)
print()

ultimos_15_caracteres = resumen[-15:] # MOSTRANDO LOS ULTIMOS 15 CARACTERES
print("Ultimos 15 caracteres del resumen: ",ultimos_15_caracteres)
print()


print("Resumen separado por comas (,): ",resumen.split()) # RESUMEN SEPARADO POR COMAS

# hagalo valer profe dijo con comas :(
    