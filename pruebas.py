Alumnos = {
 'Ana': {'Edad': 20, 'Calificacion': 9.5}, 
 'Luis': {'Edad': 22, 'Calificacion': 8.0}, 
 'Pedro': {'Edad': 19, 'Calificacion': 6.5}, 
 'Alejandro': {'Edad': 22, 'Calificacion': 10.0}, 
 'Diego': {'Edad': 19, 'Calificacion': 10.0}, 
 'Abril': {'Edad': 20, 'Calificacion': 10.0}, 
 'tere': {'Edad': 24, 'Calificacion': 10.0}
 }
prueba = input()
Diccionarios = {
    "ganancias" : {},
    "gastos" : {},
    "total-Exterior-Interior" : {}
}

    with open("Ganancias.txt", "r") as f:
        datos = [linea.strip() for linea in f.readlines()]
        indice = 1
        lista = "ganancias"
        for dato in datos:
            if indice % 2 != 0:
                clave = dato
            else:
                valor = dato
                Diccionarios[lista][clave] = valor
            indice += 1
        


    lista = []
    for x in Diccionarios["ganancias"]:
        print(x)
        clave = x
        valor = Diccionarios["ganancias"][x]
        print(clave)
        print(valor)
        lista.append(clave)
        lista.append(valor)
        print(clave,"\n", valor,"\n")

    with open("Ganancias.txt", "w") as f:
        for x in lista:
            f.write(f"{x}\n")
