"""Crear una lista de productos con sus precios. Usar un bucle
para encontrar el producto mas caro"""
productos = [("compu", 300000), ("notebook", 850000), ("audífonos", 90000), ("monitor", 250000)]

producto_mas_caro = productos[0][0]
precio_mas_alto = productos[0][1]


for producto, precio in productos:
    if precio > precio_mas_alto:
        precio_mas_alto = precio
        producto_mas_caro = producto


print("El producto más caro es:", producto_mas_caro, "con un precio de", precio_mas_alto)

"""Explicacion (Recordatorio): al pedir una lista de productos se hace una lista con tuplas para almacenar 
mas datos, (segun yo), para encontrar el producto mas caro, creamos 2 variables donde se va guardar los resultados
a medido de que se vaya recorriendo nuestra lista.

La primera (productos[0][0]) esta diciendo que esa variable comienza en la "Compu".
La segunda (productos[0][1]) esta tomando el segundo valor de la primera tupla (el precio).

Luego usamos 2 variables en nuestro for porque asi se desempaqueta la tupla, donde (producto) recorre los nombres y
(precio) recorre los precios que hay dentro de ellos.
luego si (precio) es mayor que la variable que teniamos como iniciacion se actualiza por ese producto y de la misma manera
el (producto_mas_caro), se actualiza por el que corresponde."""
