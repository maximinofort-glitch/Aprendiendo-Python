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
while True:
    Datos = input("Introduce los datos de los alumnos separados por espacios de la siguiente forma y orden: Nombre Edad Calificacion: ")
    DatosListados = Datos.split()
    if len(DatosListados) % 3 != 0:
        print("Error: Los datos ingresados estan incompletos. Los datos deben poderse emparejar en grupos de 3 de manera entera. Intenta ingresando los datos nuevamente")
        continue
    for x in range(0,len(DatosListados), 3):
        Nombre = DatosListados[x]
        Edad = DatosListados[x + 1]
        Calificaciones = DatosListados[x + 2]
        Alumno = (Nombre, Edad, Calificaciones)
        AlumnosTupla.append(Alumno)
        Alumnos = {
            
        }
    break
print("Funciona")