# amigos_mios = {"Ana", "Luis", "Pedro"}
# amigos_otros = {"Pedro", "Laura", "Luis"}
# salida esperada: {"Luis", "Pedro"}
# amigos en comun??

amigos_mios = {"ana", "luis", "pedro"}
amigos_otros = {"pedro","laura","luis"}

# HAY 2 FORMAS DE HACERLO

# PRIMERA FORMA (SE OCUPA & PARA COMPARAR ENTRE LOS 2 SETS)
en_comun = amigos_mios & amigos_otros

print("Amigos en comun: ",en_comun)

#SEGUNDA FORMA (SE OCUPA .intersection() PARA VER LAS INTERSECCIONES ENTRE LOS 2 (TERMINOS COMUNES))
amigos_en_comun = amigos_mios.intersection(amigos_otros)

print("Amigos en comun 2.0: ",amigos_en_comun)