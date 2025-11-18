#Arroz:20:True, Frijoles:15:False, Aceite:30:True, 

datos = input("Introduce los objetos con su precio y disponibilidad con el formato producto:precio:True/False")
datos_listados = datos.split(":")
objetos = []

objetos = [i for x in datos_listados if objetos.index(x) % 3 == 0]
print(objetos)

    