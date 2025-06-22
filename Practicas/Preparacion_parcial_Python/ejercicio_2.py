"""Escribir un programa que cuente del 1 al 50 y se salte el 40"""

for i in range(1, 51, 1):
    if i == 40:
        continue
    print(i)