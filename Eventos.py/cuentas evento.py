from datetime import datetime 
from colorama import init, Fore, Style
init(autoreset=True)


def retroceder(entrada,funcion):
    if entrada == "atras":
        return None
    elif entrada == "reinicio":
        return funcion()
    return True

def añadir_entrada(archivo, accion):
    with open(archivo, "a") as datos:
        if archivo == "Ganancias.txt":
            ganancia = input("Introduce el valor de la ganancia: ")
            origen = input("Escribe el origen de la ganancia")
return (f"")


#la idea para introducir datos es un diccionario, la primera linea sera el nombre mientras que las demas iran intercalando 
# entre clave y lista de datos (cantidad, razon, fecha)

#posible idea para nombre de las claves: 
# creo una lista de indices: 
# indices = []
#añado la variable indices valiendo 0
# indices = 0
# while True:
#   for entrada in indices
#       if indice == int(entrada):
#           indices.append(indice)
#           return f"Entradas{indice}" : f"Valor de ganancia: {ganancia}, Origen de la ganancia: {origen}, Fecha: {datetime.now}" 

#Cada entrada tendra su propio indice, la lista evita que se repitan y repone los numeros de entrada borrados anteriormente, si hay 10 entradas y 
# se borra la cuarta el codigo recorrera de uno en uno hasta que llegue a la 4, detecte que no hay una entrada con el indice 4 y use el indice 4 pra crear la nueva entrada

#otra opcion que pense ahora es crear otra lista para cada indice borrado, de esa forma puedo checar si hay un indice libre debido a una entrada borrada y 
# si no es el caso puedo buscar cual fue el indice de mayor valor usado hasta ahora y usar el siguiente indice para la nueva entrada

def main():
    while True:
        accion = input(f"{Fore.LIGHTGREEN_EX}Agregar: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                       f"{Fore.RED}Retirar: " f"{Fore.RESET}Quita dinero de la cuenta\n"
                       f"{Fore.YELLOW}Revisar: " f"{Fore.RESET}Revisa el dinero dentro y fuera de la cuenta\n"
                       f"{Fore.CYAN}Modificar: " f"{Fore.RESET}Modifica una entrada anterior (cantidad de dinero, razon o fecha)\n"
                       f"{Fore.LIGHTRED_EX}Salir: " f"{Fore.RESET}Sale del programa\n"
                        
                       "\nEscribe tu accion:"
                       )
        if accion == "agregar":
            agregar_dinero()
            None
        elif accion == "retirar":
            #entrada
            None
        elif accion == "revisar":
            #entrada
            None
        elif accion == "modificar":
            #entrada
            None
        elif accion == "salir":
            #entrada
            None
        elif accion == "":
            #entrada
            None





def agregar_dinero():
    dinero = input("Escribe el dinero a agregar")
    accion_negativa = retroceder(dinero, agregar_dinero)
    if accion_negativa:
        pass
print("")
print("")
main()