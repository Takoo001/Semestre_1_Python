# Dado dos inventarios con frutas:
inv1 = {"Manzana": 1200, "Plátano": 1000, "Cereza": 3000}
inv2 = {"Plátano": 1100, "Kiwi": 2500, "Manzana": 1300}

frutas_unicas = set(inv1.keys()).union(set(inv2.keys()))

print("Frutas Unicas: ", frutas_unicas)

print("Frutas ordenadas: ", sorted(frutas_unicas))


# Objetivo:
# 1. Obtener todas las frutas únicas entre los dos inventarios (sin repetir).
# 2. Mostrar cuántas frutas únicas hay en total.
# 3. Mostrar la lista ordenada alfabéticamente.
