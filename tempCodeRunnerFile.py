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