print("======= MENÚ =======")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo Italiano")

opcion = input("Por favor, elige una opción (1-3): ")

match opcion:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $5000")
    case "2":
        print("Has elegido Pizza. Precio: $7500")
    case "3":
        print("Has elegido Completo. Precio: $2500")
    case _:
        print("Opción no válida. Por favor, elige entre 1 y 3")
