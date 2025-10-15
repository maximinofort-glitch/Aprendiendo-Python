# sMini ejercicio propuesto

# Haz una función llamada resumen_alumno que reciba:
    #nombre (obligatorio)
    #edad (por defecto 18)
    #calificaciones (cualquier cantidad de números usando *args)
# Y que devuelva:
    #el promedio,
    #la mayor y la menor calificación.
# max 22 10 9.7 7.9

def resumen_alumno(Nombre, Edad = "18", *Calificaciones):
    Calificaciones = [float(x) for x in Calificaciones]
    Promedio = (sum(Calificaciones)) / len(Calificaciones)
    MayorCalificacion = max(Calificaciones)
    MenorCalificacion = min(Calificaciones)
    return print(round(Promedio), MayorCalificacion, MenorCalificacion)
    
while True:
    Datos = input("Escribe el nombre del alumno seguido por su edad y calificaciones: ")
    if len(Datos.split()) >= 3:
        print(resumen_alumno(*Datos.split()))

        break
    else:
        continue


