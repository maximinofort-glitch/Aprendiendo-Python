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
    #Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5
DatosListados = []
Alumnos = []
AlumnosTupla = []
while True:
    #Datos = input("Introduce los datos de los alumnos separados por espacios de la siguiente forma y orden: Nombre Edad Calificacion: ")
    Datos = "Ana 20 9.5 Luis 22 8.0 Pedro 19 6.5 Alejandro 22 10 Diego 19 10"
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
        Alumno = (Nombre, Edad, Calificacion)
        AlumnosTupla.append(Alumno)
        Alumnos[Nombre] = {"Edad" : Edad, "Calificacion" : Calificacion}
        #print("Calificacion actual", Calificacion, " y la calificacion mayor es: ", CalificacionMayor)
        if Calificacion == CalificacionMayor:
            CalificacionesMayores.append(x / 3)
        
        if Calificacion > CalificacionMayor:
            CalificacionMayor = Calificacion
            CalificacionesMayores = []
            CalificacionesMayores.append(x / 3)

        
        if Calificacion == CalificacionMenor:
            CalificacionesMenores.append(x / 3)

        if Calificacion < CalificacionMenor:
            CalificacionMenor = Calificacion
            CalificacionesMayenores = []
            CalificacionesMenores.append(x / 3)
    break
print(CalificacionesMayores)
if len(CalificacionesMayores) > 1:
    print("Los alumnos con la mayor calificacion son: ", end = "")
    for x in CalificacionesMayores[0:len(CalificacionesMayores) - 1]:
            print(f"{AlumnosTupla[x][0]},", end = "")



#for Alumno in Alumnos:
    #print(Alumno, f"(Edad: {Alumnos[Alumno]['Edad']}, Calificacion: {Alumnos[Alumno]['Calificacion']})")
print(CalificacionMayor)
print(CalificacionesMayores)
#print(f"{"El alumno" if Mayores == 1}{"Los Alumnos" if Mayores > 1} con la mayor calificacion fue {max(Alumnos, key = lambda x: Alumnos[x][Edad] )}")
#print("Funciona")