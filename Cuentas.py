import math
Fechas_input = [
     ("Introduce la primera fecha: "),
     ("Introduce la segunda fecha: "),
     ("Introduce la tercera fecha: ")
] 
Contador = 0
Fechas = []
Dia_input = [
     ("Escribe la venta de la primera fecha: "),
     ("Escribe el valor del primer premio: "),
     ("Escribe la venta de la segunda fecha: "),
     ("Escribe el valor del segundo premio: "),
     ("Escribe la venta de la tercera fecha: "),
     ("Escribe el valor del tercer premio: ")
]
Dias_input = []
Dias = {
     "dia1" : [0 , 0],
     "dia2" : [0 , 0],
     "dia3" : [0 , 0]
}

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
     fecha = (input(Fechas_input[Contador]))
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



def calculo(vendedor):
     global deuda
     global contador
     ExtraSorteo = 0
     if vendedor == "maribel":
          porcentaje = 0.77
     elif vendedor == "carmen" or vendedor == "luis":
          porcentaje = 0.75
     elif vendedor == "lupe" or vendedor == "norma":
          porcentaje = 0.72
     elif vendedor == "elena":
          porcentaje = 0.71
     elif vendedor == "tere" or vendedor == "tola" or vendedor == "90" or vendedor == "27":
          porcentaje = 0.7
     print(" ")
     print(vendedor, porcentaje,"%")
     print(" ")
     f1 = f2 = f3 = 0
     p1 = p2 = p3 = 0





   


     Contador = 0
     while Contador < sorteos * 2: 
          Dia = (input(Dia_input[Contador]))
          Dias_input.append(Dia)
          if fecha == "atras" and Contador > 0:
               Contador -= 1
          elif fecha == "exit":
               print("introducir fin del programa")
          else:
               Contador += 1
          if Contador % 2 == 0:

               Dias[f"dia{str(int(Contador/2))}"] = [int(Dias_input[Contador - 2]), int(Dias_input[Contador - 1])]
     print(Dias)
     print(Dias["dia1"][0], Dias["dia1"][1])
         


     if vendedor == "elena":
          if Dias["dia1"][0] > 0 :
               ExtraSorteo = ExtraSorteo + 35
          if sorteos >= 2:
               if Dias["dia2"][0] > 0:
                  ExtraSorteo = ExtraSorteo + 35
          if sorteos == 3:
               if Dias["dia3"][0] > 0:
                  ExtraSorteo = ExtraSorteo + 35
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
     linea1 = (
          f"{Fechas[0]}V="
          f"{Dias["dia1"][0]:<5}"
          f"{'p-' if Dias["dia1"][1] == 0 else ''}"
          f"{'p=' if Dias["dia1"][1] != 0 else ''}"
          f"{Dias["dia1"][1]}"
          f"{' -' if Dias["dia1"][1] == 0 else ''}"
     )
     linea2 = (
          f"{Fechas[1]}V="
          f"{Dias["dia2"][0]:<5}"
          f"{'p-' if Dias["dia2"][1] == 0 else ''}"
          f"{'p=' if Dias["dia2"][1] != 0 else ''}"
          f"{Dias["dia2"][1]}"
          f"{' -' if Dias["dia2"][1] == 0 else ''}"
     )
     linea3 = (
          f"{Fechas[2]}V="
          f"{Dias["dia3"][0]:<5}"
          f"{'p-' if Dias["dia3"][1] == 0 else ''}"
          f"{'p=' if Dias["dia3"][1] != 0 else ''}"
          f"{Dias["dia3"][1]}"
          f"{' -' if Dias["dia3"][1] == 0 else ''}"
     )
     restantes = (   
          f"{' ':<6}-{restante}"
          f"\n{' ':<6}-----"
         f"\n{' ':<6}{resto}"
     )
     print(" ")
     print(vendedor, porcentaje,"%")
     print(" ")
     if Dias["dia1"][0] != 0:
          print(linea1)
     if Dias["dia2"][0] != 0:
          print(linea2)
     if Dias["dia3"][0] != 0:
          print(linea3)

     print(
         f"{' ':<6}----"
          f"\n{' ':<6}{ventas}"
          f"\n{' ':<9}x"
          f"\n{' ':<6}----"
          f"\n{' ':<6}{pagado}"
     )
     if Dias["dia1"][1] > 0 or Dias["dia2"][1] > 0 or Dias["dia3"][1] > 0:
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
                calculo(vendedor)
           else:
                print("vendedor no encontrado, intenta de nuevo.")
          except ValueError:
                print("Debes escribir un dato valido.")