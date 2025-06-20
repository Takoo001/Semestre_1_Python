from colorama import init, Fore
init()
productos = ["Smartphone", "Laptop", "Tablet", "Smartwatch"]
valores = [300, 800, 150, 200]
stock = {
    "Smartphone": 25,
    "Notebook": 12,
    "Tablet": 8,
    "Smartwatch": 4
}

# MIN - MAX
precio_max = max(valores)
precio_min = min(valores)

# PRODUCTO MAS CARO 
producto_max = productos[valores.index(precio_max)]
producto_min = productos[valores.index(precio_min)]
print()
print(Fore.YELLOW,"El producto mas Caro y mas Barato".center(60, "-"))
print("El roducto mas Caro es:",producto_max,"con el valor de $",precio_max)
print("El producto mas Barato es:",producto_min,"con el valor de $",precio_min)
print(Fore.YELLOW,"-" * 60)
# CATEGORIAS
for prod, precio in zip(productos, valores):
    if precio < 200:
        categoria = "Producto Economico"
    elif precio >= 200 and precio <= 500:
        categoria = "Producto Estandar"
    else:
        categoria = "Producto Premium"
    
    print(f"{prod}: ${precio} es {categoria}")
print("-" * 60)

print(Fore.YELLOW,"Listado de articulos con stock mas bajo".center(60, "-"))
for prod, cantidad in stock.items():
    if cantidad < 10:
        print(prod,":",cantidad,"unidades")
print()