while True:
    print()
    frase = input("Ingrese una frase de maximo 30 caracteres: ")
    print()
    solo_frase = [c for c in frase if c.isalpha()]
    frase_contada = len(solo_frase) 
    if frase_contada < 30:
        break
    else:
        print("La frase supera los 30 caracteres")
        
frase_mayus = frase.upper()
frase_minus = frase.lower()

letra_a_buscar = input("Ingrese una letra para saber cuantas veces aparece: ")

contador_letra = frase.count(letra_a_buscar)

print(f"la letra: {letra_a_buscar} aparece {contador_letra} veces en la frase")
print()
print(f"La longitud de la frase original es de: {frase_contada} caracteres")