# entrada: [1, 2, 3, 2]
# salida: True (tiene duplicados)

mi_lista = [1, 2, 3, 2]

tiene_duplicados = len(mi_lista) != len(set(mi_lista))
# COMPARANDO LONGITUD DE LA LISTA, SI LA PRIMERA LONGITUD DE LA LISTA ES DIFERENTE A LA LISTA QUITANDO LOS DUPLICADOS ES (True) SINO ES (False)


print("Valores totales de la lista: ",len(mi_lista))
print()
print("Valores totales quitando los duplicados: ",len(set(mi_lista)))

print("¿Tenia duplicados?: ", tiene_duplicados)
#LOS SETS ELIMINAN LOS DUPLICADOS AUTOMATICAMENTE. SI LA LONGITUD DEL SET ES MENOR QUE LA DE LA LISTA, ENTONCES HABIA DUPLICADOS.