valor = 6

match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un número Par")
    case x if x % 2 != 0:
        print(f"{valor} es un número Impar")
