#Pida al usuario ingresar nombres, calificaciones y edades en un solo input
#(ejemplo: Ana 9 20 Luis 5 22 Pedro 8 19).
#La entrada siempre vendrá en el orden nombre → calificación → edad.
#Los inválidos (ejemplo: calificación no numérica o edad negativa) se descartan.
#Convierta los datos en tres listas:
#nombres
#calificaciones
#edades
#Muestre:
    #Todos los nombres en una sola línea separados por comas.
    #El alumno con la mejor calificación y el alumno con la peor calificación.
    #El promedio de calificaciones (redondeado a 2 decimales).
    #El promedio de edades.
    #La lista numerada de estudiantes en el formato:
        #1. Ana (20 años, calificación 9)
    #Quiénes reprobaron (nota < 6).
    #Si todos aprobaron (all).
    #Si al menos uno es mayor de 21 años (any).
    #Los estudiantes ordenados por calificación de mayor a menor.

Nombres = []
Edades = []
Calificaciones = []
Errores = []
Negativos = []
LideresNombres = []
Conjunto = []
ResagadosNombres = []

while True:
    datos = input("Ingresa los nombres de los alumnos seguidos de su calificacion y por último su edad.\nTodos los datos deben estar separados por espacios: ")

    if len(datos) < 0:
        print("\nNo se han introducido datos, intente nuevamente\n")

    DatosListados = datos.split()


    if (len(DatosListados) / 3) == (int(len(DatosListados) / 3)):

        for x in range(len(DatosListados)):
           
                if ((x + 3) / 3) == int(((x + 3) / 3)):
                    try:
                        int(DatosListados[x])
                        Errores.append(x)
                        print("\nError en el dato número",(x + 1), "\nLos valores númericos no son validos como nombres\n")
                    except ValueError:
                        Nombres.append(DatosListados[x])

                elif ((x + 2) / 3) == int((x + 2) / 3):
                        try:
                            DatosListados[x] = int(DatosListados[x])
                            if DatosListados[x] == abs(DatosListados[x]):
                                Calificaciones.append(DatosListados[x])
                            else:
                                print("\nError en el dato número",(x + 1), "\nLos valores negativos no son validos como calificaciones\n")
                                Negativos.append(x)
                        except ValueError:
                            Errores.append(x)

                else:
                    try:
                        DatosListados[x] = int(DatosListados[x])
                        if DatosListados[x] == abs(DatosListados[x]):
                            Edades.append(DatosListados[x])
                        else:
                            print("\nError en el dato número",(x + 1), "\nLos valores negativos no son validos como edades\n")
                            Negativos.append(x)
                    except ValueError:
                        Errores.append(x)


    else:
        print("\nLos datos estan incompletos, deben de poder crearse una cantidad entera de trios de datos (Nombre, Calificacion, Edad). Intente nuevamente.\n")

    if len(Errores) > 0:
        print("\nSe a introducido un tipo de dato incorrecto en los datos numeros: ", ", ".join(str(x + 1) for x in Errores), "\n")
        Errores = []
        Nombres = []
        Edades = []
        Negativos = []
        calificacines = []

    elif len(Negativos) > 0:
        Errores = []
        Nombres = []
        Edades = []
        Negativos = []
        calificacines = []

    else:
        break
    
print("\nAlumnos ingresados: ", ", ".join(str(x)for x in Nombres), "\n")


for x in range(len(Calificaciones)):
    if Calificaciones[x] == sorted(Calificaciones)[(len(Calificaciones)) - 1]:
        LideresNombres.append(Nombres[x])
  

for x in range(len(Calificaciones)):
    if Calificaciones[x] == sorted(Calificaciones)[0]:
        ResagadosNombres.append(Nombres[x])


if len(ResagadosNombres) != 0:
     if len(ResagadosNombres) == 1:
          print(f"\nEl alumno con la menor calificacion es {ResagadosNombres[0]} con una calificacion de {sorted(Calificaciones)[0]}\n")
     else:
        print(f"\nLos alumnos con la menor calificaion son ", end = "")
        for x in range(len(ResagadosNombres)):
            if x < (len(ResagadosNombres) - 2):
                print(ResagadosNombres[x] + ", ", end = "")

            elif x == (len(ResagadosNombres) - 1):
                print(" y " + ResagadosNombres[x], end = "")

            else:
                print(ResagadosNombres[x], end = "")

if len(LideresNombres) != 0:
    if len(LideresNombres) == 1:
          print(f"\nEl alumno con la mayor calificacion es {LideresNombres[0]} con una calificacion de {sorted(Calificaciones)[(len(Calificaciones)) - 1]}\n")
    else:
        print(f"\nLos alumnos con la mayor calificaion son ", end = "")
        for x in range(len(LideresNombres)):
            if x < (len(LideresNombres) - 2):
                print(LideresNombres[x] + ", ", end = "")

            elif x == (len(LideresNombres) - 1):
                print(" y " + LideresNombres[x], end = "")

            else:
                print(LideresNombres[x], end = "")

print(f"\nEl promedio de las calificaiones es: {sum(Calificaciones) / len(Calificaciones)}\n")
print(f"\nEl promedio de las edades es: {sum(Edades) / len(Edades)}\n")
print("\nLista de alumnos, sus edades y calificacion ordenados de mayor calificacion a menor\n")

Union = []
Conjunto = []
Usados = []
for x in reversed(sorted(range(len(Calificaciones)))):
    Contador = (len(Calificaciones) - 1)
    while True:
        if Contador < 0:
            break
        else:
            if sorted(Calificaciones)[x] ==  Calificaciones[Contador]:
                try:
                    if sorted(Calificaciones)[x] != sorted(Calificaciones)[x + 1]:
                            Usados.append(Contador)
                            if Calificaciones[Contador] > 5:
                                Union = f"{Nombres[Contador]} ({Edades[Contador]} años, calificacion {Calificaciones[Contador]})"
                                Conjunto.append(Union)
                            else:
                                Union = f"{Nombres[Contador]} ({Edades[Contador]} años, calificacion {Calificaciones[Contador]}) |Reprobado|"
                                Conjunto.append(Union)
                except IndexError:
                    Usados.append(Contador)
                    if Calificaciones[Contador] > 5:
                        Union = f"{Nombres[Contador]} ({Edades[Contador]} años, calificacion {Calificaciones[Contador]})"
                        Conjunto.append(Union)
                    else:
                        Union = f"{Nombres[Contador]} ({Edades[Contador]} años, calificacion {Calificaciones[Contador]}) |Reprobado|"
                        Conjunto.append(Union)
        Contador -= 1
for x, y in enumerate(Conjunto, start = 1):
    print(f"#{x}. {y} ")


if all(x < 6 for x in Calificaciones):
    print("\nTodos los alumnos han reprobado\n")

if any(x > 21 for x in Edades):
    MayoresDe21 = []
    for x in range(len(Edades)):
        if Edades[x] > 21:
            MayoresDe21.append(Edades[x])
    print("\nLos alumnos mayores de 21 son: ", end = "")
    for x in range(len(MayoresDe21)):
        if x < (len(MayoresDe21) - 2):
            print(Nombres[x] + " (" + str(Edades[x]) + " años), ", end = "")

        elif x == (len(MayoresDe21) - 1):
            print(" y " + Nombres[x] + " (" + str(Edades[x]) + " años)", end = "")

        else:
            print(Nombres[x] + " (" + str(Edades[x]) + " años)", end = "")
print("")



#print("\nLas calificaciones de mayor a menor son: " ", ".join(str(x) for x in reversed(sorted(Calificaciones))),"\n")

#Muestre:
    #Todos los nombres en una sola línea separados por comas.
    #El alumno con la mejor calificación y el alumno con la peor calificación.
    #El promedio de calificaciones (redondeado a 2 decimales).
    #El promedio de edades.
    #La lista numerada de estudiantes en el formato:
        #1. Ana (20 años, calificación 9)
    #Quiénes reprobaron (nota < 6).
    #Si todos aprobaron (all).
    #Si al menos uno es mayor de 21 años (any).
    #Los estudiantes ordenados por calificación de mayor a menor.
#Emiliano -8 20 lisa 10 -21 sofia1 9 22
#Emiliano 8 20 sebastian 8 22 lisa 10 21 alejandro 10 20 sofia 9 22 julio 3 18