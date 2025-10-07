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
    Datos = input("Ingresa los datos de los alumnos (nombre, edad, calificación) separados por espacios: ")
    #Datos = "max 22 8.7 sofia 21 9 tola 22 4.5"
    if len(Datos.split()) % 3 != 0:
            print("Error: Los datos estan incompletos, deben de poderse crear conjuntos de tres (Nombre, Edad, Calificacion), intenta nuevamente")
            continue
    else:
        for x in range(0, len(Datos.split()), 3):
            Nombre = Datos[x]
            Edad = Datos[x + 1]
            Calificacion = Datos[x + 2]
            try:
                Edad = int(Edad)
            except ValueError:
                print(Edad)
                Errores.append("si")
                print("Error: Se ha introducido un tipo de dato incorrecto. La edad debe ser un número entero.")
            try:
                Calificacion = float(Calificacion)
            except ValueError:
                Errores.append("Si")
                print("Error: La calificación debe ser un número decimal.")      
            if len(Errores < 1):
                ConjuntoDe3 = (Nombre, Edad, Calificacion)
                Alumnos.append(ConjuntoDe3)
        if len(Errores) > 0:
            Erorres = []
            continue

        break
    
print("funciona")
    
print(ConjuntoDe3)
