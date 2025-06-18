# Crea un diccionario con 3 nombres como claves y sus números como valores.
# Agrega uno nuevo, cambia uno, y elimina otro. Luego imprime el diccionario final.

contactos = {
    "Juan": "123456789",
    "Ana": "987654321",
    "Luis": "555666777"
}
print("Contactos: ",contactos)
# Agregar
contactos["Pedro"] = "222333444"

# Cambiar
contactos["Ana"] = "000111222"

# Eliminar
del contactos["Luis"]

print()
print("Contactos finales:", contactos)
