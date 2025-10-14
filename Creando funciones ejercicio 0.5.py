#Mini ejercicio propuesto

#Haz una función llamada resumen_alumno que reciba:
    #nombre (obligatorio)
    #edad (por defecto 18)
    #calificaciones (cualquier cantidad de números usando *args)
#Y que devuelva:
    #el promedio,
    #la mayor y la menor calificación.

def resumen_alumno(Nombre, Edad = "18",*Calificaciones)
    Promedio = sum(Calificaciones) / len(Calificaciones)

    
