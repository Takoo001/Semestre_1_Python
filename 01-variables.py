""" INICIANDO EN PYTHON (VARIABLES)"""

nombre = "Matias"

apellido = "Rain"

# UTILIZANDO VARIABLES EN UN PRINT CON COMAS
print("Hola, mi nombre es",nombre,"y mi apellido es",apellido)

# IMPRIMIENDO CON OPERADOR DE CONCATENACION
print("Hola, mi nombre esw " + nombre + "y mi apellido es " + apellido)

# IMPRIMIENDO CON F-STRINGS (CADENAS LITERALES)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

# INICIALIZANDO MULTI VARIABLES EN UNA SOLA LINEA (NO ES RECOMENDADO)

ciudad, region, pais = "Castro", "Los lagos", "Chile"

print(f"Hola soy de {ciudad},{region},{pais}")
