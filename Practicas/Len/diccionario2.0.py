# Diccionario de precios por fruta
precios = {
    "Plátano": (1000, 1000, 1100, 1100),
    "Manzana": (1200, 1300, 1250),
    "Cereza": (3000, 3200, 3100),
}

# Recorrer cada fruta en el diccionario
for fruta in precios.keys():
    # Obtener precios únicos con set()
    precios_unicos = set(precios[fruta])

    # Calcular el promedio
    promedio = sum(precios_unicos) / len(precios_unicos)

    # Mostrar resultados
    print({fruta}, "Precios unicos: ", precios_unicos,
          "Promedio: {:.2f}".format(promedio))
