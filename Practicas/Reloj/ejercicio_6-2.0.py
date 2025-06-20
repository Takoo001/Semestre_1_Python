import time # PARA CONTROLAR TIEMPO 
from colorama import init, Fore
from datetime import datetime # PARA USAR HORAS O FECHAS REALES DEL SISTEMA


print(Fore.YELLOW,"RELOJ DIGITAL".center(60, "-"))
print()

while True:
    ahora = datetime.now() # OBTENIENDO LA HORA DE NUESTRO SISTEMA
    hora = ahora.hour # IMPORTANDO LA VARIABLE (AHORA) Y PIDIENDOLE QUE TOME LA HORA
    minuto = ahora.minute # IMPORTANDO LA VARIABLE (AHORA) Y PIDIENDOLE QUE TOME LOS MINUTOS
    segundo = ahora.second # IMPORTANDO LA VARIABLE (AHORA) Y PIDIENDOLE QUE TOME LOS SEGUNDOD

    print(f"{hora:02}:{minuto:02}:{segundo:02}".center(60), end="\r") 
    # IMPRIMIENDO LA HORA Y USANDO [.center()] PARA CENTRARLO Y (end="\r") PARA QUE SE REFRESQUE EN LA MISMA LINEA
    time.sleep(1) # MAS QUE NADA ES COMO DANDO UNA PAUSA DE (1) SEGUNDOS PARA REFRESCAR
