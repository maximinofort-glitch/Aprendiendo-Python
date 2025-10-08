#Crea un programa que:
#Pida al usuario ingresar alumnos con nombre, edad y calificación, en un solo input.
#Ejemplo:
    #Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5
#Convierta los datos en una lista de tuplas, donde cada tupla tenga (nombre, edad, calificación).
#Muestre:
    #Todos los alumnos con su edad y calificación.
    #El alumno con la mejor calificación y el peor.
    #El promedio de calificaciones.
    #Qué alumnos tienen una nota mayor al promedio.
#max 22 8.7 sofia 21 9 tola 22 4.5 diego 20 9
Errores = []
Alumnos = []
Calificaciones = []
while True:
    Datos = input("Ingresa los datos de los alumnos (nombre, edad, calificación) separados por espacios: ")
    
    if len(Datos.split()) % 3 != 0:
            print("Error: Los datos estan incompletos, deben de poderse crear conjuntos de tres (Nombre, Edad, Calificacion), intenta nuevamente")
            continue
    else:
        DatosListados = Datos.split()
        for x in range(0, len(DatosListados), 3):
            Errores = []
            Nombre = DatosListados[x]
            Edad = DatosListados[x + 1]
            Calificacion = DatosListados[x + 2]
            try:
                Edad = int(Edad)
            except ValueError:
                print(Edad)
                Errores.append("si")
                print("Error: Se ha introducido un tipo de dato incorrecto en la posicion ",(x + 1),". La edad debe ser un número entero.")
            try:
                Calificacion = float(Calificacion) 
            except ValueError:
                Errores.append("Si")
                print("Error: Se ha introducido un tipo de dato incorrecto en la posicion ",(x + 2),". La calificación debe ser un número decimal.")      
            Conjunto = (Nombre, Edad, Calificacion)
            Alumnos.append(Conjunto)
            Calificaciones.append(Calificacion)
            print(f"{Nombre}, {Edad} años, calificación: {Calificacion}")
        if len(Errores) > 0:
            Conjunto = []
            Alumnos = []
            Calificaciones = []
            continue
        break
    
PromedioCalificacion = sum(Calificaciones) / len(Calificaciones)
CalificacionesMayores = []
CalificacionesMax = []
CalificacionesMin = []
    
for x in range(len(Calificaciones)):
    if Calificaciones[x] == sorted(Calificaciones)[len(Calificaciones) - 1]:
        CalificacionesMax.append(x)
    elif Calificaciones[x] == sorted(Calificaciones)[0]:
        CalificacionesMin.append(x)
    if Calificaciones[x] > PromedioCalificacion:
        CalificacionesMayores.append(Calificaciones[x])


if len(CalificacionesMax) == 1:
    print(f"El alumno con la mayor calificacion es {Alumnos[CalificacionesMax[0]][0]} con una calificacion de {Alumnos[CalificacionesMax[0]][2]}")

else:
    print(f"Los alumnos con la mayor calificacion son ", end = "")
    for x in range(len(CalificacionesMax)):
        if x < (len(CalificacionesMax) - 2):
            print(f"{Alumnos[CalificacionesMax[x]][0]}, ", end = "")

        elif x == (len(CalificacionesMax) - 1):
            print(f" y {Alumnos[CalificacionesMax[x]][0]} ", end = "")
        
        else:
            print(f"{Alumnos[CalificacionesMax[x]][0]}", end = "")
    print("con una calificacion de", Alumnos[CalificacionesMax[0]][2])

print("")

if len(CalificacionesMin) == 1:
    print(f"El alumno con la menor calificacion es {Alumnos[CalificacionesMin[0]][0]} con una calificacion de {Alumnos[CalificacionesMin[0]][2]}")

else:
    print(f"Los alumnos con la menor calificacion son ", end = "")

    for x in range(len(CalificacionesMin)):
        if x < (len(CalificacionesMin) - 2):
            print(f"{Alumnos[CalificacionesMin[x]][0]}, ", end = "")

        elif x == (len(CalificacionesMin) - 1):
            print(f" y {Alumnos[CalificacionesMin[x]][0]} ", end = "")
        
        else:
            print(f"{Alumnos[CalificacionesMin[x]][0]}", end = "")
        
    print("con una calificacion de",Alumnos[CalificacionesMin[0]][2])
if len(CalificacionesMayores) == 1:
    print(f"Solo un alumno obtuvo una calificacion mayor al promedio y fue {Alumnos[CalificacionesMayores[0]][0]} con una calificacion de {Alumnos[CalificacionesMayores[0]][2]}")

else:
    print(f"Los alumnos con una calificacion mayor al promedio son: ", end = "")

    for x in range(len(CalificacionesMayores)):
        if x < (len(CalificacionesMayores) - 2):
            print(f"{Alumnos[x][0]} (Calificacion: {Alumnos[x][2]}), ", end = "")
        elif x == (len(CalificacionesMayores) - 1):
            print(f" y {Alumnos[x][0]} (Calificacion: {Alumnos[x][2]}) ", end = "")
        
        else:
            print(f"{Alumnos[x][0]} (Calificacion: {Alumnos[x][2]})", end = "")