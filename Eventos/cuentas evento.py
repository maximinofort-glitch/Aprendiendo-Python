from datetime import datetime 
from colorama import init, Fore, Style
import os

os.chdir(r"C:\Users\maxim\OneDrive\Documentos\Codigos\Eventos")

init(autoreset=True)

with open("Indices_de_Entrada.txt", "r") as f:
    indices = [indice.strip() for indice in f.readlines()]


def abrir(archivo, Diccionarios):
    with open(f"{archivo}.txt", "r") as f:
        datos = [linea.strip() for linea in f.readlines()]
        indice = 1
        lista = archivo.lower()
        for dato in datos:
            if indice % 2 != 0:
                clave = f"{dato}"
            elif indice % 2 == 0:
                valor = f"{dato}"
            Diccionarios[lista][clave] = valor
        indice += 1
    return Diccionarios



def retroceder(entrada, funcion):
    
    if entrada == "atras":
        return True
    elif entrada == "reinicio":
        return funcion()
    elif entrada == "menu":
        return main()
    return False

def añadir_entrada(accion, lista, Diccionarios):
    global indices
    if accion == "agregar":
        with open(f"{'Ganancias.txt' if accion == "agregar" else 'Gastos.txt'}", "a") as datos:
            cantidad = input(f"Introduce el valor {'de la ganancia: ' if accion == "agregar" else 'del gasto: '}")
            origen = input(f"Escribe el origen {'de la ganancia: ' if accion == "agregar" else 'del gasto: '}")
            if accion == "gastos":
                retirante = input(f"Escribe el nombre de quien retira el efectivo")
                cantidad = -int(cantidad)

            indiceValor = 1
            for entrada in sorted(indices):
                if indiceValor != entrada:
                    indices.append(indiceValor)
                    break
                else:
                    indiceValor += 1
            print(
                "La entrada a introducir sera\n\n"
                f"Diccionarios[{lista}][Entrada{indiceValor}] = Valor de ganancia: {cantidad}, Origen de la ganancia: {origen}, Fecha: {datetime.now()}" 
                )
            
            while True:
                accion_final = input("¿Los datos son correctos?\n")
                if accion_final == "si":
                    Diccionarios[lista][f"Entrada{indiceValor}"] = f"Valor de ganancia: {cantidad}, Origen de la ganancia: {origen}, Fecha: {datetime.now()}" 
                    print(f"La entrada{indiceValor}:\n" 
                        f"{Diccionarios[lista][f'Entrada{indiceValor}']}\n\n"
                        )
                    print("Se ha introducido exitosamente")
                    print("Volviendo al menú...")
                    return Diccionarios
                else:
                    print("Error: Solo se acepta un si o un no como respuesta\n")
                    continue

    return None

def agregar_dinero(entrada, Diccionarios):
    retroceder(entrada, agregar_dinero)
    lista = "ganancias"
    Diccionarios = añadir_entrada("agregar", lista, Diccionarios)
    return Diccionarios
#la idea para introducir datos es un diccionario, la primera linea sera el nombre mientras que las demas iran intercalando 
# entre clave y lista de datos (cantidad, razon, fecha)

#posible idea para nombre de las claves: 
# creo una lista de indices: 


#Cada entrada tendra su propio indice, la lista evita que se repitan y repone los numeros de entrada borrados anteriormente, 
# si hay 10 entradas y se borra la cuarta el codigo recorrera de uno en uno hasta que llegue a la 4, 
# detecte que no hay una entrada con el indice 4 y use el indice 4 pra crear la nueva entrada

Diccionarios = {
    "ganancias" : {},
    "gastos" : {},
    "total-Exterior-Interior" : {}
}
for lista in ("Ganancias", "Gastos", "Total-Exterior-Interior"):
    Diccionarios = abrir(lista, Diccionarios)
print(Diccionarios)
def main(Diccionarios):
    while True:
        accion = input(f"Bienvenido al {Fore.BLUE}menú\n\n"
                       

                       f"{Fore.LIGHTMAGENTA_EX}Entrada: {Fore.RESET}Introduce una entrada (agrega o quita dinero a la cuenta)\n"
                       f"{Fore.YELLOW}Revisar: {Fore.RESET}Revisa el dinero dentro y fuera de la cuenta\n"
                       f"{Fore.CYAN}Modificar: {Fore.RESET}Modifica una entrada anterior (cantidad de dinero, razon o fecha)\n"
                       f"{Fore.GREEN}Acpetar: {Fore.RESET}Aceptar y guardar cambios\n"
                       f"{Fore.LIGHTRED_EX}Salir: {Fore.RESET}Sale del programa\n"

                       f"La accion {Fore.BLUE}menu {Fore.RESET}siempre estara disponible"
                        
                       f"{Fore.YELLOW}\n\nEscribe tu accion: {Fore.RESET}"
                       )
        if accion == "entrada":
            accion = input(
                        f"{Fore.LIGHTGREEN_EX}Agregar: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                        f"{Fore.RED}Retirar: " f"{Fore.RESET}Quita dinero de la cuenta\n{Fore.RESET}"
                    )
            if accion == "agregar":
                Diccionarios = agregar_dinero(accion, Diccionarios)
                None
        elif accion == "retirar":
            #entrada
            None
        elif accion == "revisar":
            print(Diccionarios)
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
    Diccionarios = main(Diccionarios)
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