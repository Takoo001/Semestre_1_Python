# HECHO POR: Samir Arana y Matias Rain

try:
    # INGRESANDO EL PARRAFO
    parrafo = input("Ingrese el párrafo: ").strip().lower()
    
    # LANZANDO EXCEPCION SI EL PARRAFO ESTA VACIO
    if not parrafo:
        raise ValueError("El texto no puede estar vacío")
    
    # GUARDANDO EL PARRAFO EN UNA LISTA, SEPARADA POR COMAS Y LUEGO IMPRIMIENDOLA
    lista_palabras = parrafo.split()
    print("Palabra separada en lista",lista_palabras)
    
    # SOLICITANDO LA PALABRA QUE DESEA BUSCAR
    palabra_buscada = input("Ingrese la palabra que desea buscar: ").lower()

    # CONTANDO LAS VECES QUE APARECE LA PALABRA INGRESADA QUE DESEA BUSCAR
    cantidad = lista_palabras.count(palabra_buscada)

    print("La palabra",palabra_buscada,"aparece",cantidad,"veces en el párrafo.")

except ValueError as e:
    print(e)