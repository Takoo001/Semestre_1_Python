print()
juegos = [
    ("Catan", "Estrategia", 3, 4, 5),
    ("Dixit", "Party", 4, 6, 2),
    ("Carcassonne", "Estrategia", 2, 5, 3),
    ("Dobble", "Party", 2, 8, 0)
]

for juego in juegos:
    nombre, categoria, personas_min, personas_max, stock = juego
    print(nombre,":",categoria,"para",personas_min,"-",personas_max,"personas, Stock: ",stock)
    

disponibles = set()
agotados = set()

for juego in juegos:
    nombre = juego[0]
    stock = juego[4]
    
    if stock > 0:
        disponibles.add(nombre)
    else:
        agotados.add(nombre)
        
print()
print("Disponibles: ",disponibles)
print("Agotados: ",agotados)

stock_juegos = {
    "Catan".lower(): 5, 
    "Dixit".lower(): 2, 
    "Carcassonne".lower(): 3, 
    "Dobble".lower(): 0
}

pedido = input("Ingrese el nombre del juego que desea: ").lower()


if pedido in stock_juegos:
    if stock_juegos[pedido] > 0:
        stock_juegos[pedido] -= 1
        print("Prestamo hecho, Nuevo stock de: ",pedido,":",stock_juegos[pedido])
    else:
        print("No hay stock para : ",pedido)
else:
    print("El juego: ",pedido,"no esta en el inventario")
    
pedidos = ["Catan", "Dobble", "Catan", "Dixit", "Dixit"]

pedidos_realizados = {}

for juego in pedidos:
    if juego in pedidos_realizados:
        pedidos_realizados[juego] += 1  # Si ya existe, sumamos 1
    else:
        pedidos_realizados[juego] = 1 

print()
print("Pedidos realizados:", pedidos_realizados)