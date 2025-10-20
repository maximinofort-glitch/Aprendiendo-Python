import math
Fechas_input = [
("Introduce la primera fecha: "),
("Introduce la segunda fecha: "),
("Introduce la tercera fecha: ")
]
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
contador = 0
Fechas = []
while contador <= sorteos: 
        fecha = (input(Fechas_input[contador]))
        Fechas.append(fecha)
        if fecha == "atras" and contador > 0:
            if contador == 0:
               contador += 1
            contador -= 1
        elif fecha == "exit":
          print("introducir fin del programa")
        else:
          contador += 1
print(
     f"{f'Fecha a trabajar: {Fechas[0]}' if contador == 1 else ''}"
     f"{f'Fechas a trabajar: {", ".join(Fechas)}' if contador >= 2 else ''}"
)
print(contador)
print("aqui acaba")
    
fecha1 = input("Introduce la primera fecha: ")
if sorteos == 1:
     fecha2 = 0
     fecha3 = 0
     print("Fecha a trabajar: ", fecha1)
     print(" ")
elif sorteos >= 2:
     fecha2 = input("Introduce la segunda fecha: ")
     if sorteos == 2:
          fecha3 = 0
          print("fechas a trabajar: ", fecha1, fecha2)
          print(" ")
     elif sorteos == 3:
          fecha3 = input("Introduce la tercera fecha: ")
          print(" ")
          print("fechas a trabajar: ", fecha1, fecha2, fecha3)
          print(" ")
def calculo(vendedor):
    global deuda
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
    f1 = int(input("Escribe la venta de la primera fecha: "))
    print(" ")
    p1 = int(input("Escribe el valor del primer premio: "))
    print(" ")
    if sorteos >= 2:
        f2 = int(input("Escribe la venta de la segunda fecha: "))
        print(" ")
        p2 = int(input("Escribe el valor del segundo premio: "))
        print(" ")
    if sorteos == 3:
         f3 = int(input("Escribe la venta de la tercera fecha: "))
         print(" ")
         p3 = int(input("Escribe el valor del tercer premio: "))
         print(" ")
    if vendedor == "elena":
        if f1 > 0 :
           ExtraSorteo = ExtraSorteo + 35
        if sorteos >= 2:
             if f2 > 0:
                 ExtraSorteo = ExtraSorteo + 35
        if sorteos == 3:
             if f3 > 0:
                 ExtraSorteo = ExtraSorteo + 35
    ventas = f1 + f2 + f3
    pagado = ventas * porcentaje
    decimal = pagado - int(pagado)
    if decimal <= 0.5:
      pagado = math.floor(pagado)
    else:
      pagado = math.ceil(pagado)
    restante = (p1 + p2 + p3)
    resto = pagado - restante
    resultado = resto - ExtraSorteo
    total = resultado + deuda
    linea1 = (
      f"{fecha1}V="
      f"{f1:<5}"
      f"{'p-' if p1 == 0 else ''}"
      f"{'p=' if p1 != 0 else ''}"
      f"{p1}"
      f"{' -' if p1 == 0 else ''}"
    )
    linea2 = (
      f"{fecha2}V="
      f"{f2:<5}"
      f"{'p-' if p2 == 0 else ''}"
      f"{'p=' if p2 != 0 else ''}"
      f"{p2}"
      f"{' -' if p2 == 0 else ''}"
    )
    linea3 = (
      f"{fecha3}V="
      f"{f3:<5}"
      f"{'p-' if p3 == 0 else ''}"
      f"{'p=' if p3 != 0 else ''}"
      f"{p3}"
      f"{' -' if p3 == 0 else ''}"
    )
    restantes = (   
      f"{' ':<6}-{restante}"
      f"\n{' ':<6}-----"
      f"\n{' ':<6}{resto}"
    )
    print(" ")
    print(vendedor, porcentaje,"%")
    print(" ")
    if f1 != 0:
       print(linea1)
    if f2 != 0:
       print(linea2)
    if f3 != 0:
       print(linea3)

    print(
    f"{' ':<6}----"
    f"\n{' ':<6}{ventas}"
    f"\n{' ':<9}x"
    f"\n{' ':<6}----"
    f"\n{' ':<6}{pagado}"
    )
    if p1 > 0 or p2 > 0 or p3 > 0:
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