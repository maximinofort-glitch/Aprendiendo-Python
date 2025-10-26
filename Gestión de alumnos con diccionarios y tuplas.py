#Gestión de alumnos con diccionarios y tuplas
#Pide al usuario ingresar datos de varios alumnos en un solo input, en el formato:
#Nombre Edad Calificacion Nombre Edad Calificacion …
#Ejemplo:
    #Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5
#Convierte esos datos en:
    #Una lista de tuplas donde cada tupla tenga (nombre, edad, calificacion).
    #Un diccionario donde las claves sean los nombres de los alumnos y los valores sean diccionarios con {"edad":…, "calificacion":…}
#Muestra:
    #Todos los alumnos con su edad y calificación.
    #El alumno con la mejor calificación y el peor.
    #El promedio de calificaciones.
    #Quiénes tienen calificación mayor al promedio.
    #La lista de alumnos ordenada de mayor a menor calificación usando sorted(key=…).
#Ejemplo:
    #Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5 Alejandro 22 10 Diego 19 10 Abril 20 10 tere 24 10
DatosListados = []
Alumnos = []
AlumnosTupla = []
CalificacionesSuma = 0
ContadorCalificaciones = 0
while True:
    #Datos = input("Introduce los datos de los alumnos separados por espacios de la siguiente forma y orden: Nombre Edad Calificacion: ")
    Datos = "Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5 Alejandro 22 10 Diego 19 10 Abril 20 10 tere 24 10"
    DatosListados = Datos.split()
    if len(DatosListados) % 3 != 0:
        print("Error: Los datos ingresados estan incompletos. Los datos deben poderse emparejar en grupos de 3 de manera entera. Intenta ingresando los datos nuevamente")
        continue
    CalificacionesMayores = []
    CalificacionesMenores = []
    CalificacionMayor = float(DatosListados[2])
    CalificacionMenor = float(DatosListados[2])
    Alumnos = {}
    for x in range(0,len(DatosListados), 3):
        Nombre = DatosListados[x]
        Edad = int(DatosListados[x + 1])
        Calificacion = float(DatosListados[x + 2])
        Alumno = (Nombre, str(Edad), str(Calificacion))
        AlumnosTupla.append(Alumno)
        Alumnos[Nombre] = {"Edad" : Edad, "Calificacion" : Calificacion}
        #print("Calificacion actual", Calificacion, " y la calificacion mayor es: ", CalificacionMayor)
        if Calificacion == CalificacionMayor:
            CalificacionesMayores.append(int(x / 3))
        
        elif Calificacion > CalificacionMayor:
            CalificacionMayor = Calificacion
            CalificacionesMayores = []
            CalificacionesMayores.append(int(x / 3))

        if Calificacion == CalificacionMenor:
            CalificacionesMenores.append(int(x / 3))

        elif Calificacion < CalificacionMenor:
            CalificacionMenor = Calificacion
            CalificacionesMenores = []
            CalificacionesMenores.append(int(x / 3))
        CalificacionesSuma += Calificacion
        ContadorCalificaciones += 1
    break
CalificacionPromedio = CalificacionesSuma / ContadorCalificaciones
if len(CalificacionesMayores) > 1:
    print("Los alumnos con la mayor calificacion son:",AlumnosTupla[CalificacionesMayores[0]][0], end = "")
    for x in CalificacionesMayores[1:(len(CalificacionesMayores) - 1)]:
        print(f", {AlumnosTupla[x][0]}", end = " ")
    print(f"y {AlumnosTupla[CalificacionesMayores[len(CalificacionesMayores) - 1]][0]}", end = " ")
    print(f"con una calificacion de {(int(CalificacionMayor) if CalificacionMayor == (round(CalificacionMayor)) else CalificacionMayor)}")
    print("")
elif len(CalificacionesMayores) == 1:
    print("El alumno con la mayor calificacion es", AlumnosTupla[CalificacionesMayores[0]][0], "con una calificacion de", f"{(int(CalificacionMenor) if CalificacionMenor == (round(CalificacionMenor)) else CalificacionMenor)}")
    print("")


if len(CalificacionesMenores) > 1:
    print("Los alumnos con la menor calificacion son:",AlumnosTupla[CalificacionesMenores[0]][0], end = "")
    for x in CalificacionesMenores[1:(len(CalificacionesMenores) - 1)]:
        print(f", {AlumnosTupla[x][0]}", end = " ")
    print(f"y {AlumnosTupla[CalificacionesMenores[len(CalificacionesMenores) - 1]][0]}", end = " ")
    print(f"con una calificacion de {(int(CalificacionMenor) if CalificacionMenor == (round(CalificacionMenor)) else CalificacionMenor)}")
    print("")
elif len(CalificacionesMenores) == 1:
    print("El alumno con la mayor calificacion es", AlumnosTupla[CalificacionesMenores[0]][0], "con una calificacion de", f"{(int(CalificacionMenor) if CalificacionMenor == (round(CalificacionMenor)) else CalificacionMenor)}")
    print("")

print("La calificacion promedio es", round(CalificacionPromedio, 2))
print("")
CalificacionesSobrePromedio = []
for Nombre, Edad, Calificacion in AlumnosTupla:
    if float(Calificacion) > CalificacionPromedio:
        CalificacionesSobrePromedio.append(f"{Nombre} ({Edad} años) con una calificacion de {Calificacion}")
if len(CalificacionesSobrePromedio) > 1:
    print("La lista con los alumnos con una calificacion mayor al promedio es: ")
    print("\n".join(CalificacionesSobrePromedio))
else: 
    print("El alumno con una calificacion mayor al promedio fue:", CalificacionesSobrePromedio[0])

print(Alumnos)
print("")
print(sorted(AlumnosTupla, key = lambda x: x[2]))



#for Alumno in Alumnos:
    #print(Alumno, f"(Edad: {Alumnos[Alumno]['Edad']}, Calificacion: {Alumnos[Alumno]['Calificacion']})")
#print(f"{"El alumno" if Mayores == 1}{"Los Alumnos" if Mayores > 1} con la mayor calificacion fue {max(Alumnos, key = lambda x: Alumnos[x][Edad] )}")
#print("Funciona")