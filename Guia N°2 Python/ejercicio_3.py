# HECHO POR: Samir Arana y Matias Rain

from colorama import init, Fore # IMPORTANDO COLORES
init() # INICIANDO LA BIBLIOTECA PARA LOS COLORES

ventas = { # DICCIONARIO
    "Pepitogamer": [120000, 240000, 33000, 67000, 69500], # VENTAS DIARIAS POR UNA SEMANA
    "Samirtralalerotralala": [500000, 190000, 150000, 220000, 0], 
    "bomboclap": [500000, 500000, 250000, 150000, 346700]
}


sueldo_base = 529000 # SUELDO BASE


bono_5 = sueldo_base * 0.05 # SACANDO PORCENTAJE DE BONO DESDE EL SUELDO BASE
bono_10 = sueldo_base * 0.10
bono_20 = sueldo_base * 0.20

print()
print(Fore.GREEN,"REPORTE SEMANAL DE VENTAS Y SUELDOS".center(60, "-")) # TITULO CENTRADO
print()
print(Fore.MAGENTA,"-" * 60)
print(Fore.MAGENTA,"Sueldo base (2025): ${}".format(sueldo_base),"pesos") # IMPRIMIENDO SUELDO BASE
print(Fore.MAGENTA,"-" * 60)
print()

# BUCLE CON RESULTADOS DE CADA VENDEDOR
for vendedor, ventas_dias in ventas.items():
    total = sum(ventas_dias)
    promedio = total / len(ventas_dias) # OBTENIENDO PROMEDIO DE VENTAS SEMANAL DE CADA VENDEDOR

    if total > 1500000:
        print(Fore.LIGHTRED_EX,"(El total sobrepasa el $1500000, (Aplica para bono 20% del sueldo base))")
        bono = bono_20
        porcentaje = "20%"
    elif total > 1000000:
        print(Fore.LIGHTRED_EX,"(EL total sobrepasa el $1000000, (Aplica para bono 10% del sueldo base))")
        bono = bono_10
        porcentaje = "10%"
    elif total > 500000:
        print(Fore.LIGHTRED_EX,"(El total sobrepasa los $500000, (Aplica para bono 5% del sueldo base))")
        bono = bono_5
        porcentaje = "5%"
    else:
        bono = 0
        porcentaje = "Sin bono"

    sueldo_total = total + bono
    # DATOS DE VENDEDOR, VENTAS SEMANALES, PROMEDIO DE VENTAS, PORCENTAJE DE BONO CORRESPONDIENTE Y SUELDO TOTAL A PAGAR
    print(Fore.YELLOW,"Vendedor: {}".format(vendedor))
    print(Fore.YELLOW,"Ventas semanales: ${}".format(total))
    print(Fore.YELLOW,"Promedio diario de ventas: ${:.0f}".format(promedio))
    print(Fore.YELLOW,"Bono aplicado: {} => ${:.0f}".format(porcentaje, bono))
    print(Fore.YELLOW,"Sueldo total a pagar: ${:.0f}".format(sueldo_total))
    print(Fore.GREEN,"-" * 60)