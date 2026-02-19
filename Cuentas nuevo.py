import math
SolicitudesFechas = [
     ("Introduce la primera fecha: "),
     ("Introduce la segunda fecha: "),
     ("Introduce la tercera fecha: ")
]
SolicitudesVenta = [
    ("Escribe la venta de la primera fecha: "),
    ("Escribe el valor del primer premio: "),
    ("Escribe la venta de la segunda fecha: "),
    ("Escribe el valor del segundo premio: "),
    ("Escribe la venta de la tercera fecha: "),
    ("Escribe el valor del tercer premio: ")
]

def CantidadSorteos():
    while True:
        try:
            Sorteos = int(input("""
                Introduce la cantidad de sorteos a calcular
                >>>>>>>>>>>>> """))
            print(" ")
            if Sorteos in (1, 2, 3):
                break
            else:
                print("Valor no válido, escoge entre 1, 2 o 3.")
        except ValueError:
            print("Debes escribir un número válido (1, 2 o 3).")
    return Sorteos

def Fechas(Sorteos):
    Fechas = []
    Contador = 0
    while Contador < Sorteos: 
        fecha = input(f"""{SolicitudesFechas[Contador]}
            >>>>>>>>> """)
        if fecha == "atras":
            if Contador == 0:
                print("No es posible retroceder más")
            else:
                Contador -= 1
                Fechas.remove(Fechas[Contador])
        else:
            Fechas.append(fecha)
            Contador += 1
    print(
    f"{f'Fecha a trabajar: {Fechas[0]}' if Contador == 1 else ''}"
    f"{f'Fechas a trabajar: {", ".join(Fechas)}' if Contador >= 2 else ''}"
    )
    return Fechas

def Deudas():
    Deudores = {}
    for vendedor in ("tere", "tola", "90", "27","carmen", "luis", "lupe", "norma", "maribel", "elena"):
        Deudores[vendedor] = 0
    while True:
        Deudor = input("""
            Escribe el nombre de un vendedor con deuda, en caso de no haber presiona enter
            >>>>>>>>>>>>>>>>>>> """)
        if Deudor in Deudores:
            Deuda = input(f"""
            Escribe la deuda de {Deudor}
            >>>>>>>>>>>>>>>>>>> """)
            try:
                Deudores[Deudor] = int(Deuda)
                print(f"{' ':<12}Se le ha aplicado una deuda de {Deuda} a {Deudor}")
            except ValueError:
                print("Error: Se ha introducido un tipo de dato incorrecto, intenta nuevamente.")
            continue
        elif Deudor != "":
            print(f"{' ':<12}El vendedor '{Deudor}' no ha sido encontrado")
            continue
        break
    return Deudores
        
def ElenaExtra(ExtraSorteo, Dias):
    ExtraSorteo = 0
    for dia in Dias:
        print(Dias[dia][0])
        if Dias[dia][0] > 0 :
            ExtraSorteo = ExtraSorteo + 35
        print(Dias[dia][0],ExtraSorteo)
    return ExtraSorteo
 
def imprimirDias(Dias, Fechas, sorteos):
    lineas = {}
    indice = 1
    while indice <= sorteos:
        lineas[f"linea{indice}"] = (
            f"{Fechas[indice - 1]}V="
            f"{Dias[f'dia{indice}'][0]:<5}"
            f"{'p-' if Dias[f'dia{indice}'][1] == 0 else ''}"
           f"{'p=' if Dias[f'dia{indice}'][1] != 0 else ''}"
           f"{Dias[f'dia{indice}'][1]}"
           f"{' -' if Dias[f'dia{indice}'][1] == 0 else ''}"
           )
        indice += 1
    return lineas

def Datos(Sorteos, Solicitudes):
    Dias = {
    "dia1" : [0 , 0],
    "dia2" : [0 , 0],
    "dia3" : [0 , 0]
    }
    indice = 1
    solicitud = 0
    while solicitud < (Sorteos * 2):
        Dia = input(Solicitudes[solicitud])
        if Dia == "atras" and solicitud != 0:
            if indice % 2 == 0:
                indice -= 1
                solicitud -= 1
            else:
                indice += 1
                solicitud -= 1
            continue
        elif Dia == "atras" and solicitud == 0:
            return False
        else:
            solicitud += 1.5
            dia = round(solicitud / 2)
            Dias[f"dia{dia}"][indice - 1] = int(Dia)
            if indice % 2 == 0:
                indice -= 1
            else:
                indice += 1
        solicitud = int(solicitud - 0.5)
    return Dias

def paga(vendedor):
     if vendedor in ("tere", "tola", "90", "27"):
          porcentaje = 0.7
     elif vendedor in ("carmen", "luis"):
          porcentaje = 0.75
     elif vendedor in ("lupe", "norma"):
          porcentaje = 0.72
     elif vendedor == "maribel":
          porcentaje = 0.73 
     elif vendedor == "elena":
          porcentaje = 0.71
     return porcentaje

def calculo(vendedor, deuda, ExtraSorteo):
    

    porcentaje = paga(vendedor)
    print(vendedor, "tiene una ganancia del", porcentaje,"%")

    Dias = Datos(Sorteos, SolicitudesVenta)
    if not Dias:
        return None
    if vendedor == "elena":
        ExtraSorteo = ElenaExtra(ExtraSorteo, Dias)


    ventas = Dias["dia1"][0] + Dias["dia2"][0] + Dias["dia3"][0]
    pagado = ventas * porcentaje
    decimal = pagado - int(pagado)
    if decimal <= 0.5:
        pagado = math.floor(pagado)
    else:
        pagado = math.ceil(pagado)
    restante = Dias["dia1"][1] + Dias["dia2"][1] + Dias["dia3"][1]
    resto = pagado - restante
    resultado = resto - ExtraSorteo
    total = resultado + Deudores[vendedor]

    lineas = imprimirDias(Dias, Fechas, Sorteos)


    restantes = (   
        f"{' ':<6}-{restante}"
        f"\n{' ':<6}-----"
        f"\n{' ':<6}{resto}"
    )
    print(" ")
    print(vendedor, porcentaje,"%")
    print(" ")
    
    indice = 1
    while indice <= 3:
        if Dias[f"dia{indice}"][0] != 0:
            print(lineas[f"linea{indice}"])
        indice += 1

    print(
        f"{' ':<6}----"
        f"\n{' ':<6}{ventas}"
        f"\n{' ':<9}x"
        f"\n{' ':<6}----"
        f"\n{' ':<6}{pagado}"
    )
    if restante > 0:
        print(restantes)
    if vendedor == "elena":
        print(
        f"{' ':<5}-{ExtraSorteo}"
        f"\n{' ':<6}----"
        f"\n{' ':<6}{resultado}"
    )
    if Deudores[vendedor] > 0:
        print(
            f"{' ':<5}+{Deudores[vendedor]}"
            f"\n{' ':<6}-----"
            f"\n{' ':<6}{total}"
        )
        print(" ")
        print(" ") 

Sorteos = CantidadSorteos()
Fechas = Fechas(Sorteos)
Deudores = Deudas()

vendedor = " " 
ExtraSorteo = 0
while vendedor != "exit":
      while True:
            vendedor = input("""Escribe el vendedor a calcular
                >>>>>>>>>>>> """)
            if vendedor == "exit":
                print("Saliendo del programa...")
                break
            elif vendedor in Deudores:
                calculo(vendedor, Deudores, ExtraSorteo)
            else:
                print("vendedor no encontrado, intenta de nuevo.")



