import random  # PERMITE HACE ELECCIONES ALEATORIAS

opciones = ["piedra", "papel", "tijera"]  # LISTA DE LAS OPCIONES A ELEGIR

print("Bienvenido a piedra papel o tijera")

while True:  # INICIO DEL BUCLE
    # CON EL LOWER PERMITE QUE LA OPCION SEA EN MINUSCULA Y MAYUSCULAS
    jugador = input("Elige: Piedra, Papel o Tijera: ").lower()
    if jugador not in opciones:
        print("La opción no existe, intenta de nuevo")
        continue

    # PIDIENDO QUE LA COMPUTADO SEA IGUAL A UNA ELECCION RANDOM DE LA VARIABLE (OPCIONES)
    computadora = random.choice(opciones)
    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):  # OR \ SIGFICA (O) Y LA BARRA INVERTIDA (\) SIRVE PARA DECIRLE A PYTHON QUE LA CONTINUACION ESTA EN LA OTRA LINEA
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

    continuar = input("¿Quieres seguir jugando? (1=Sí, 2=No): ")
    if continuar != "1":  # != SIGNIFICA "DISTINDO DE" O "NO ES IGUAL A" EN ESTE CASO TAMBIEN SE PODRIAN USAR MAS IF YA QUE CON CUALQUIER OTRO CARACTER PUEDE TERMINAR SI NO ES EL UNO
        print("¡Gracias por jugar!")
        break  # FIN DEL BUCLE
