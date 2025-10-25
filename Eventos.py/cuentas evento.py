from datetime import datetime 
from colorama import init, Fore, Style
init(autoreset=True)


def abrir(archivo):
    with open(f"{archivo}.txt", r) as f:
        lista = f.readlines()
        indice = 1
        f"{archivo}" = {}
        for dato in lista:
            if indice % 2 != 0:
                clave = f"{dato}"
            elif indice % 2 != 0:
                valor = f"{dato}"
            f"{archivo}"[f"{clave}"] : f"{valor}"
    return f"{archivo}"



def retroceder(entrada, funcion):
    
    if entrada == "atras":
        return True
    elif entrada == "reinicio":
        return funcion()
    elif entrada == "menu":
        return main()
    return False

def revisar(Lista)
    if lista == Ganancias:
        print(entrada for entrada in Ganancias)
        open(f"{lista}", )
        print()

def añadir_entrada(accion):
    global Entradas
    if accion == "agregar":
        with open(f"{'Ganancias.txt' if accion == "agregar" else 'Gastos.txt'}", "a") as datos:
            ganancia = input(f"Introduce el valor {'de la ganancia: ' if accion == "agregar" else 'del gasto: '}")
            origen = input(f"Escribe el origen {'de la ganancia: ' if accion == "agregar" else 'del gasto: '}")
            indices = []
            indiceValor = 1
            for entrada in sorted(indices):
                if indiceValor != entrada:
                    indices.append(indiceValor)
                    break
                else:
                    indiceValor += 1
            temporal = {}
            temporal[f"entrada{indiceValor}"] = f"Valor de ganancia: {ganancia}, Origen de la ganancia: {origen}, Fecha: {datetime.now}" 
            print("La entrada a introducir sera\n\n"
                  f"{temporal[f'entrada{indiceValor}']}\n\n")
            while True:
                accion_final = input("¿Los datos son correctos?\n")
                if accion_final == "si":
                    print(f"La entrada{indiceValor}:\n"
                          f"{Entradas[f"entrada{indiceValor}"] = f"Valor de ganancia: {ganancia}, Origen de la ganancia: {origen}, Fecha: {datetime.now()}}")
                    print("Se ha introducido exitosamente")
                    print("Volviendo al menú...")
                    break
                    return menu()
                else:
                    print("Error: Solo se aceota un si o un no como respuesta\n")
                    continue

    return Entradas
def agregar_dinero():
    global Entradas
    dinero = input(
        f"{Fore.YELLOW}Escribe el dinero a agregar\n"
        f"En caso de querer volver al menu escriba {Fore.BLUE}'menu'"
    )
    retroceder(dinero, agregar_dinero)
    Entradas = añadir_entrada("agregar")
    return Entradas
#la idea para introducir datos es un diccionario, la primera linea sera el nombre mientras que las demas iran intercalando 
# entre clave y lista de datos (cantidad, razon, fecha)

#posible idea para nombre de las claves: 
# creo una lista de indices: 


#Cada entrada tendra su propio indice, la lista evita que se repitan y repone los numeros de entrada borrados anteriormente, 
# si hay 10 entradas y se borra la cuarta el codigo recorrera de uno en uno hasta que llegue a la 4, 
# detecte que no hay una entrada con el indice 4 y use el indice 4 pra crear la nueva entrada


def main():
    while True:
        accion = input(f"Bienvenido al {Fore.BLUE}menú\n\n"
                       
                       f"{Fore.LIGHTGREEN_EX}Agregar: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                       f"{Fore.RED}Retirar: " f"{Fore.RESET}Quita dinero de la cuenta\n"
                       f"{Fore.YELLOW}Revisar: " f"{Fore.RESET}Revisa el dinero dentro y fuera de la cuenta\n"
                       f"{Fore.CYAN}Modificar: " f"{Fore.RESET}Modifica una entrada anterior (cantidad de dinero, razon o fecha)\n"
                       f"{Fore.GREEN}Acpetar: " f"{Fore.RESET}Aceptar y guardar cambios\n"
                       f"{Fore.LIGHTRED_EX}Salir: " f"{Fore.RESET}Sale del programa\n"

                       f"La accion {Fore.BLUE}menu " f"{Fore.RESET}siempre estara disponible"
                        
                       f"{Fore.YELLOW}\n\nEscribe tu accion:"
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
        elif accion == "aceptar":
            #entrada
            None
        elif accion == "salir":
            #entrada
            None
        else:
            print("No se ha introducido una opcion valida. Favor de intentar nuevamente")






print("")
print("")
while True:
    main()
    if not main:
        print("saliendo...")
        break
    else:
        continue
    


#ultimo error
#Traceback (most recent call last):
#  File "c:\Users\maxim\Documents\Aprendiendo-Python\Eventos.py\cuentas evento.py", line 99, in <module>
#    main()
#    ~~~~^^
#  File "c:\Users\maxim\Documents\Aprendiendo-Python\Eventos.py\cuentas evento.py", line 73, in main
#    agregar_dinero()
#    ~~~~~~~~~~~~~~^^
#  File "c:\Users\maxim\Documents\Aprendiendo-Python\Eventos.py\cuentas evento.py", line 41, in agregar_dinero
#    añadir_entrada()
#    ~~~~~~~~~~~~~~^^
#TypeError: añadir_entrada() missing 3 required positional arguments: 'lista_datos', 'archivo', and 'accion'