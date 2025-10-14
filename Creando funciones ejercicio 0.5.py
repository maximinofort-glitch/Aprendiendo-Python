#Mini ejercicio propuesto

#Haz una función llamada resumen_alumno que reciba:
    #nombre (obligatorio)
    #edad (por defecto 18)
    #calificaciones (cualquier cantidad de números usando *args)
#Y que devuelva:
    #el promedio,
    #la mayor y la menor calificación.

def resumen_alumno(Nombre, Edad = "18",*Calificaciones):
    Calificaciones = list(Calificaciones)
    Promedio = sum(Calificaciones) / len(Calificaciones)
    MayorCalificacion = max(Calificaciones)
    MenorCalificacion = min(Calificaciones)
    return print(promedio, MayorCalificacion, MenorCalificacion)
while True:
    Datos = input("Escribe el nombre del alumno seguido por su edad y calificaciones: ")
    print(Datos)
    print(Datos.split())
    if len(Datos.split()) % 3 == 0:
        print(resumen_alumno(*Datos.split()))
        break
    else:
        continue


