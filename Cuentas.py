import math
SolicitudesFechas = [
     ("Introduce la primera fecha: "),
     ("Introduce la segunda fecha: "),
     ("Introduce la tercera fecha: ")
] 
def paga(vendedor):
     if vendedor in ("tere", "tola", "90", "27"):
          porcentaje = 0.7
     elif vendedor in ("carmen", "luis"):
          porcentaje = 0.75
     elif vendedor in ("lupe", "norma"):
          porcentaje = 0.72
     elif vendedor == "maribel":
          porcentaje = 0.77 
     elif vendedor == "elena":
          porcentaje = 0.71
     return porcentaje

Contador = 0
Fechas = []
SolicitudesVenta = [
     ("Escribe la venta de la primera fecha: "),
     ("Escribe el valor del primer premio: "),
     ("Escribe la venta de la segunda fecha: "),
     ("Escribe el valor del segundo premio: "),
     ("Escribe la venta de la tercera fecha: "),
     ("Escribe el valor del tercer premio: ")
]
Dias = {
     "dia1" : [0 , 0],
     "dia2" : [0 , 0],
     "dia3" : [0 , 0]
}
def SolicitudDatos(sorteos):
     global Dias
     Contador = 0
     Dias_input = []
     while Contador < sorteos * 2: 
          Dia = (input(SolicitudesVenta[Contador]))
          Dias_input.append(Dia)
          if Dia == "atras" and Contador > 0:
               Contador -= 1
          elif Dia == "exit":
               print("introducir fin del programa")
          else:
               Contador += 1
          if Contador % 2 == 0:
               Dias[f"dia{str(int(Contador/2))}"] = [int(Dias_input[Contador - 2]), int(Dias_input[Contador - 1])]
     return Dias
ExtraSorteo = 0
def ElenaExtra(ExtraSorteo):
     for dia in Dias:
          print(Dias[dia][0])
          if Dias[dia][0] > 0 :
               ExtraSorteo = ExtraSorteo + 35
          print(Dias[dia][0],ExtraSorteo)
     return ExtraSorteo

def imprimirDias(Dias, Fechas):
     global sorteos
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
     print(lineas)
     return lineas

def calculo(vendedor, deuda):
     global ExtraSorteo
     
     f1 = f2 = f3 = 0
     p1 = p2 = p3 = 0

     porcentaje = paga(vendedor)
     print(vendedor, "tiene una ganancia del", porcentaje,"%")

     SolicitudDatos(sorteos)

     if vendedor == "elena":
          ExtraSorteo = ElenaExtra(ExtraSorteo)


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
     total = resultado + deuda

     lineas = imprimirDias(Dias,Fechas)


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
     if restante >0:
          print(restantes)
     if vendedor == "elena":
          print(
          f"{' ':<5}-{ExtraSorteo}"
          f"\n{' ':<6}----"
          f"\n{' ':<6}{resultado}"
     )
     if deuda > 0:
          print(
               f"{' ':<5}+{deuda}"
               f"\n{' ':<6}-----"
               f"\n{' ':<6}{total}"
          )
          print(" ")
          print(" ") 

while True:
     try:
          sorteos = int(input("Cantidad de sorteos a calcular: "))
          print(" ")
          if sorteos in (1, 2, 3):
               break
          else:
               print("Valor no válido, escoge entre 1, 2 o 3.")
     except ValueError:
          print("Debes escribir un número válido (1, 2 o 3).")

while Contador < sorteos: 
     fecha = (input(SolicitudesFechas[Contador]))
     Fechas.append(fecha)
     if fecha == "atras" and Contador > 0:
          Contador -= 1
     elif fecha == "exit":
          print("introducir fin del programa")
     else:
          Contador += 1
print(
     f"{f'Fecha a trabajar: {Fechas[0]}' if Contador == 1 else ''}"
     f"{f'Fechas a trabajar: {", ".join(Fechas)}' if Contador >= 2 else ''}"
)


vendedor = " " 
while vendedor != "exit":
      while True:
          try:
              
           vendedor = str(input("Escribe el vendedor a calcular: "))
           if vendedor == "exit":
               print("Saliendo del programa...")
               break
           elif vendedor in ("tere","tola","maribel","luis","carmen","elena","90","27","lupe","norma"):
                deuda = int(input("Escribe la deuda pendiente: "))
                print(" ")
                calculo(vendedor, deuda)
           else:
                print("vendedor no encontrado, intenta de nuevo.")
          except ValueError:
                print("Debes escribir un dato valido.")