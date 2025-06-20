grados_c = float(input("Ingrese la temperatura (°C) que desea convertir: "))

celcius_a_fahrenheit = ((grados_c * 9) / 5) + 32

celcius_a_kelvin = grados_c + 273.15

print(f"{grados_c}° celcius son = {celcius_a_fahrenheit}° grados Fahrenheit y {celcius_a_kelvin}° grados Kelvin")
