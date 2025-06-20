# HECHO POR: Samir Arana y Matias Rain

import time
from colorama import init, Fore

print(Fore.YELLOW,"RELOJ DIGITAL".center(60, "-"))
print()

hora = 0
minuto = 0
segundos = 0

for hora in range(23): # LA HORA COMIENZA EN 0 HASTA 24
    for minuto in range(59): # EL MINUTO VA DE 0 HASTA 60
        for segundos in range(59): # LOS SEGUNDOS VAN DE 0 HASTA 60
            print(f"{hora:02}:{minuto:02}:{segundos:02}".center(60), end="\r")
            # IMPRIMIENDO LA HORA, MINUTOS Y SEGUNDOS
            # {hora:02} 
            time.sleep(1)
            
            
# ESTE EJERCICIO ESTA HECHO DE ACUERDO A LO QUE SE PIDE EN LA GUIA PROFE (HICIMOS 2 PERO ESTE ES EL QUE CUADRA MAS CON LA GUIA)
