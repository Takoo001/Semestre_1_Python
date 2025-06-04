# Diccionario de precios por fruta
precios = {
    "Plátano": (1000, 1000, 1100, 1100),
    "Manzana": (1200, 1300, 1250),
    "Cereza": (3000, 3200, 3100),
}

for fruta in precios.keys():
    precios_unicos = set(precios[fruta])

    promedio = sum(precios_unicos) / len(precios_unicos)

    print(f"{fruta}: Precios unicos = {precios_unicos}, Promedio = {promedio:.2f}")
