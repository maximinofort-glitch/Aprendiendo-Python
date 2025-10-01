negativos = []
numeros = []
while True:
    try:
        datos = input("Ingresa valores separados por espacios: ")
        valores = datos.split()
        for x in valores:
            numeros.append(int(x))
        break 
    except ValueError:
        print("Uno o mas datos no son validos (deben ser números), intenta nuevamente")
        break
for x in numeros:
    if x < 0:
        abs(x)
        negativos.append(x)
    else: 
        break
if any(datos):
    print("Por lo menos uno de los valores originales era negativo: ")
else:
    print("No se encontraron valores negativos en los valores iniciales.    ")
if all(numeros > 0):
    print("Todos los valores se han reescrito a su valor absoluto exitosamente.")
else:
    print("Ha ocurrido un problema, la conversion a valor absoluto no se ha ejecutado correctamente")
print("Los valores escritos de mayor a menor: ",reversed(sorted(numeros)))
negativos = []
numeros = []
while True:
    try:
        datos = input("Ingresa valores separados por espacios: ")
        valores = datos.split()
        for x in valores:
            numeros.append(int(x))
        break 
    except ValueError:
        print("Uno o mas datos no son validos (deben ser números), intenta nuevamente")
        break
for x in numeros:
    if x < 0:
        abs(x)
        negativos.append(x)
    else: 
        break
if any(datos):
    print("Por lo menos uno de los valores originales era negativo: ")
else:
    print("No se encontraron valores negativos en los valores iniciales.    ")
if all(numeros > 0):
    print("Todos los valores se han reescrito a su valor absoluto exitosamente.")
else:
    print("Ha ocurrido un problema, la conversion a valor absoluto no se ha ejecutado correctamente")
print("Los valores escritos de mayor a menor: ",reversed(sorted(numeros)))