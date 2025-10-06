#Pida al usuario que ingrese nombres y edades en un solo input (ejemplo: Ana 20 Luis 25 Pedro 30).
#Convierta los datos en dos listas: una con nombres y otra con edades (los inválidos se descartan).

#Muestre:

#    Todos los nombres en una sola línea separados por comas.
#    La edad más alta y la edad más baja, indicando a qué persona corresponden.
#    El promedio de edades, redondeado a 2 decimales.
#    La lista de nombres con sus edades, numerada (ejemplo: 1. Ana (20 años)).
#    Qué personas tienen una edad mayor al promedio.
nombres = []
edades = []
NombreEdad = []
while True:
    datos = input("Ingresa los nombres con las edades separados por espacios: ")
    lista = datos.split()
    for x in lista:
        try:
            edades.append(int(x))
        except ValueError:
            nombres.append(x)
    if len(nombres) != len(edades):
        print("La cantidad de nombres y edades no coincide, revisa los datos ingresados.")
    elif len(nombres) < 1:
        print("No se han encontrado nombres validos, intenta de nuevo.")
    elif len(edades) < 1:
        print("No se han encontrado edades validas, intenta de nuevo.")
    else:
        break
print("Los nombres ingresados son: ",", ".join(str(x) for x in nombres))
edadpromedio = round((sum(edades))/len(edades),2)
edadesM = []
nombreM = nombres[0]
edadM = edades[0]
nombreX = nombres[0]
edadX = edades[0]
for nombre, edad in zip(nombres, edades):
    if edad < edadM:
        edadM = edad
        nombreM = nombre
    if edad > edadX:
        edadX = edad
        nombreX = nombre
    if edad > edadpromedio:
        edadesM.append(nombre)
    par = (nombre + " " + str(edad))
    NombreEdad.append(par)
print(f'La persona con la mayor edad es {nombreX}, con {edadX}')
print(f'La persona con la menor edad es {nombreM}, con {edadM}')
print("El promedio de las edades ingresadas es: ", edadpromedio)
for x, y in enumerate(NombreEdad, start = 1):
    print(f'{x}. {y}')
print("Las personas con una edad mayor al promedio son: ", " ".join(edadesM))