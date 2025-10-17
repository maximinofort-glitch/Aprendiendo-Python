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
    try:
        int(Nombre)
        print("Error: El primer valor de la secuencia debe ser el nombre")
        return None

    except ValueError:
        try:    
            Calificaciones = [float(x) if x % 2 != 0] for x in Calificaciones 
        except ValueError:
            print("Error: A partir del tercer valor todos los valores deben ser numeros para ser calificaciones validas")
            return False
        try:
            int(Edad)
        except ValueError:
            Edad = 18
            print("Un caracter invalido ha sido introducido en la edad. Se a usado la edad predeterminada (18) como reemplazo.")
               

    Promedio = round((sum(Calificaciones)) / len(Calificaciones), 2)
    MayorCalificacion = max(Calificaciones)
    MenorCalificacion = min(Calificaciones)
    return (print(
            f"La calificacion promedio de {Nombre} fue de {round(Promedio,2)}"
            f"\nSu calificacion mas alta fue de {MayorCalificacion}"
            f"\nY su calificacion mas baja fue de {MenorCalificacion}"
            ))
    
while True:
    Datos = input("Escribe el nombre del alumno seguido por su edad y calificaciones: ")
    if len(Datos.split()) >= 3:
        Historial = resumen_alumno(*Datos.split())
    
    else:
        print("Los datos estan incompletos. Porfavor proporciona el nombre, edad y calificaciones del alumno")
        continue
    
    if not Historial:
        continue
        break