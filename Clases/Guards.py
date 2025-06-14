# EJEMPLO DE GUARD
valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor}es un numero par")
    case x if x % 2 != 0:
        print(f"{valor} es un numero impar")