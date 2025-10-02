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
while True:
    datos = input("Ingresa los nombres de los alumnos seguidos de su calificacion y por último su edad, todos los datos deben estar separados por espacios: ")
    DatosListados = datos.split()
    if (len(DatosListados) / 3) == (int(len(DatosListados) / 3)):
        for x in range(len(DatosListados)):
            try:
                if ((x + 3) / 3) == int(((x + 3) / 3)):
                    try:
                        int(DatosListados[x])
                        print("Error en el dato número",x, "\nLos valores númericos no son validos como nombres")
                    except ValueError:
                        Nombres.append(x)

                elif ((x + 2) / 3) == int((x + 2) / 3):
                       if DatosListados[x] == abs(DatosListados[x]):
                            Calificaciones.append(DatosListados[x])
                            print("Calificaciones son: ", DatosListados[x])
                       else:
                            print("Error en el dato número",x, "\nLos valores negativos no son validos como calificaciones")

                else:
                    if DatosListados[x] == abs(DatosListados[x]):
                        Edades.append(DatosListados[x])
                        print("Edades son: ", DatosListados[x])
                    else:
                        print("Error en el dato número",x, "\nLos valores negativos no son validos como edades")
                    
            except TypeError:
                Errores.append(x)
        break
    else:
        print("Los datos estan incompletos, deben de poder crearse una cantidad entera de trios de datos (Nombre, Calificacion, Edad). Intente nuevamente.")
if len(Errores) > 0:
    print("Se a introducido un tipo de dato incorrecto en los datos numeros: ", ",".join(str(x + 1) for x in Errores))




