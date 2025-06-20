# HECHO POR: Samir Arana y Matias Rain

from colorama import init, Fore
init()

# INICIANDO DICCIONARIO
columnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
tablero = {}

# FILA 1 (PIEZAS BLANCAS)
piezas_blancas_fila_1 = ["TorreB", "CaballoB", "AlfilB", "ReinaB", "ReyB", "AlfilB", "CaballoB", "TorreB"]
for posicion in range(8):
    casilla = columnas[posicion] + "1"
    tablero[casilla] = piezas_blancas_fila_1[posicion]

# PEONES BLANCOS
for letra_columna in columnas:
    tablero[letra_columna + "2"] = "PeonB"

# FILAS VACIAS
for numero_fila in range(3, 7):
    for letra_columna in columnas:
        casilla = letra_columna + str(numero_fila)
        tablero[casilla] = None

# FILA 8 (PIEZAS NEGRAS)
piezas_negras_fila_8 = ["TorreN", "CaballoN", "AlfilN", "ReinaN", "ReyN", "AlfilN", "CaballoN", "TorreN"]
for posicion in range(8):
    casilla = columnas[posicion] + "8"
    tablero[casilla] = piezas_negras_fila_8[posicion]

# PEONES NEGROS
for letra_columna in columnas:
    tablero[letra_columna + "7"] = "PeonN"

# SIMBOLOS (ASCII)
simbolos = {
    "TorreB": "R", "CaballoB": "N", "AlfilB": "B", "ReinaB": "Q", "ReyB": "K", "PeonB": "P",
    "TorreN": "r", "CaballoN": "n", "AlfilN": "b", "ReinaN": "q", "ReyN": "k", "PeonN": "p"
}

# LISTA PARA PIEZAS CAPTURADAS
piezas_capturadas = []
turno_blancas = True

while True:
    # IMPRIMIR EL TABLERO
    print(f"  {" ".join(columnas)}")
    for numero_fila in range(8, 0, -1):
        linea = f"{numero_fila} "
        for letra_columna in columnas:
            casilla = letra_columna + str(numero_fila)
            pieza = tablero[casilla]
            if pieza:
                linea += f"{simbolos.get(pieza, '?')} "
            else:
                linea += ". "
        print(f"{linea}{numero_fila}")
    print(f"  {" ".join(columnas)}")

    # MOSTRAR PIEZAS CAPTURADAS
    capturadas_str = [simbolos.get(p, "?") for p in piezas_capturadas]
    print(f"{Fore.CYAN}Capturadas: {capturadas_str}{Fore.RESET}")

    # TURNO
    jugador = "B" if turno_blancas else "N"
    print(f"Turno de {"Blancas" if turno_blancas else "Negras"}")

    # PEDIR CASILLA DE ORIGEN
    casilla_origen = input("Selecciona la casilla de origen (ej: e2) o escribe 'salir': ").lower()
    if casilla_origen == "salir":
        break
    if casilla_origen not in tablero or tablero[casilla_origen] is None:
        print(f"{Fore.YELLOW}No hay pieza en esa casilla. Intenta otra vez.{Fore.RESET}")
        continue

    pieza_seleccionada = tablero[casilla_origen]
    color_pieza = pieza_seleccionada[-1]
    tipo_pieza = pieza_seleccionada[:-1]

    if color_pieza != jugador:
        print(f"{Fore.RED}No es tu turno. Esa pieza no te pertenece.{Fore.RESET}")
        continue

    letra_columna_origen = casilla_origen[0]
    numero_fila_origen = int(casilla_origen[1])
    posibles_movimientos = []

    for fila in range(1, 9):
        for col in columnas:
            casilla_posible = col + str(fila)
            pieza_en_casilla = tablero.get(casilla_posible)
            if casilla_posible != casilla_origen and (pieza_en_casilla is None or pieza_en_casilla[-1] != color_pieza):
                posibles_movimientos.append(casilla_posible)

    if not posibles_movimientos:
        print(f"{Fore.YELLOW}Esa pieza no puede moverse.{Fore.RESET}")
        continue

    # PEDIR CASILLA DE DESTINO
    casilla_destino = input("¿A dónde quieres moverla?: ").lower()
    if casilla_destino not in posibles_movimientos:
        print(f"{Fore.RED}Movimiento invalido.{Fore.RESET}")
        continue

    # CAPTURA
    if tablero.get(casilla_destino):
        print(f"{Fore.MAGENTA}¡Capturo a {tablero[casilla_destino]} en {casilla_destino.upper()}!{Fore.RESET}")
        piezas_capturadas.append(tablero[casilla_destino])

    tablero[casilla_destino] = pieza_seleccionada
    tablero[casilla_origen] = None

    turno_blancas = not turno_blancas


""" En este ejercicio aprendimos nuevas funciones y nuevas formas de variables
    como por ejemplo: aprendimos a ocupar de una forma mas completa los (for), el .get() el cual nos sirve
    como para tener el valor de una CLAVE de nuestro diccionario, lo cual nos faltaba practicar por el poco uso de 
    diccionarios."""
    
""" el codigo corre y funciona, no sabemos porque pero funciona, gg ez """

