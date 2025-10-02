#Crea un programa que:
#Pida al usuario ingresar una lista de números separados por espacios.
#Detecte cuáles son negativos y los transforme a positivos usando abs().
#Verifique si al menos uno de los números originales era negativo usando any().
#Verifique si todos los números transformados son positivos usando all().
#Imprima los números en orden inverso usando reversed().
#Al final, muestre:
#Lista original
#Lista con valores absolutos
#Resultado de any() sobre negativos
#Resultado de all() sobre positivos
#Lista en orden inverso

negativos = []
numeros = []
positivos = []
while True:
    try:
        datos = input("Ingresa valores separados por espacios: ")
        valores = datos.split()
        for x in valores:
            numeros.append(int(x))
        break 
    except ValueError:
        print("Uno o mas datos no son validos (deben ser números), intenta nuevamente")
for x in numeros:
    positivos.append(abs(x))
    if x != abs(x):
        negativos.append(x)
print("Los valores originales son: ",datos)
print("La conversion a valores absolutos de la lista resulta en: ", ", ".join(str(x) for x in positivos))
if any(x < 0 for x in numeros):
    print("Por lo menos uno de los valores originales era negativo: ", " , ".join(str(x) for x in negativos))
else:
    print("No se encontraron valores negativos en los valores iniciales.    ")
if all(x > 0 for x in positivos):
    print("Todos los valores se han reescrito a su valor absoluto exitosamente.")
else:
    print("Ha ocurrido un problema, la conversion a valor absoluto no se ha ejecutado correctamente")
print("Los valores escritos de mayor a menor: ", end = "")
for x in reversed(range(len(positivos))):
    if positivos[x] != positivos[0]:
        print(sorted(positivos)[x], end = ", ")
    else:
        print(sorted(positivos)[x])