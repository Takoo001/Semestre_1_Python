producto = input("Ingrese el nombre de un producto: ")
print()
precio_u = float(input("Ahora su precio unitario: "))
print()
stock = int(input("El stock disponible del producto: "))
print()

valor_total = precio_u * stock

umbral = valor_total > 100000


print(f"Producto: {producto}, Stock: {stock}, Valor Total: {valor_total:.2f} = {umbral}")