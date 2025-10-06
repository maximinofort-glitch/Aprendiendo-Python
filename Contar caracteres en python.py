calificaciones = input("Escribe las calificaciones separadas por espacios: ")
calificaciones = calificaciones.split()
print("Las calificaciones son: ", ",".join(str(x) for x in calificaciones))
calificaciones = [int(x) for x in calificaciones]
print("La calificacion minima es: ", min(calificaciones))
print("La calificacion maxima es: ", max(calificaciones))
promedio = sum(calificaciones) / len(calificaciones)
redondeado = round(promedio, 2)
print("El promedio de las calificaciones (redondeado) es: ", redondeado)
print("El promedio de las calificaciones real es: ", promedio)
print(",".join(str(x) for x in sorted(calificaciones)))
print("Las calificaciones reprobadas son: ", end = "")
for x in calificaciones:
    if x < 6:
        print(x, end = " ")
