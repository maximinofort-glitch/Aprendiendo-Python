#Pedir al usuario que ingrese los gastos diarios de la semana en un solo input, separados por espacios.
#Convertir los gastos a una lista de números, ignorando cualquier entrada no válida.
#Mostrar:
##Todos los gastos originales en una línea, separados por comas.
#El gasto más alto de la semana.
#El gasto más bajo de la semana.
#El promedio de gastos, redondeado a dos decimales.
#La lista de gastos ordenada de menor a mayor.
#Cuáles gastos fueron altos, es decir, mayores al promedio.
gastosV = []
descartados = []
gastos =[]
mayores = []
while True:
    datos = input("Ingresa los gastos de la semana separados por espacios: ")
    gastos = datos.split()
    for x in gastos:
        try:
            gastosV.append(int(x))
        except ValueError:
            descartados.append(x)
    if len(gastosV) < 1:
        print("No se han encontrado datos validos, intenta de nuevo.")
    else:     
        break
print("Se encontraron datos no validos: ",descartados)
print("Los datos ingresados fueron: ",gastos)
print("El gasto de menor valor fue: ", min(gastosV))
print("El gasto de mayor valor fue: ", max(gastosV))
promedio = round(sum(gastosV) / len(gastosV),2)
print("Los gastos de menor a mayor son: ",sorted(gastosV))
for x in gastosV:
    if x > promedio:
        mayores.append(x)
print("Los gastos mayores son: ",mayores)