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
#max 22 8.7 sofia 21 9 tola 22 4.5
Errores = []
Contador_Tuplas = 1
Alumnos = []
while True:
    #Datos = input("Ingresa los datos de los alumnos (nombre, edad, calificación) separados por espacios: ")
    Datos = "max 22 8.7 sofia 21 9 tola 22 4.5"
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
            print(Edad)
            print(Calificacion)
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
        if len(Errores) > 0:
            continue
        break
    
print("funciona")
CalificacionesMax = []
CalificacionesMin = []
for Nombre, Edad, Calificacion in Alumnos:
    print(f"{Nombre}, {Edad} años, calificación: {Calificacion}")
    Calificaciones.append(Calificacion)
for x in Calificaciones:
    if x == sorted(Calificaciones)[len(Calificaciones) - 1]
        CalificacionMax.append(x)
    elif x == sorted(Calificaciones)[0]
        CalificacionesMin.append(X)
if len(CalificacionesMax) == 1

elif len(CalificacionesMax) > 2

else:

if len(CalificacionesMin) == 1

elif len(CalificacionesMin) > 2

else: