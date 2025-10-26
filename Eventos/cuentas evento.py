from datetime import datetime 
from colorama import init, Fore, Style
import os

os.chdir(r"C:\Users\maxim\OneDrive\Documentos\Codigos\Eventos")
colores = {
    "amarillo" : Fore.YELLOW,
    "azul" : Fore.BLUE,
    "lazul" : Fore.LIGHTBLUE_EX,
    "rojo" : Fore.RED,
    "lrojo" : Fore.LIGHTRED_EX,
    "verde" : Fore.GREEN,
    "cyan" : Fore.CYAN,
    "lcyan" : Fore.LIGHTCYAN_EX,
    "lmagenta" : Fore.LIGHTMAGENTA_EX,
    "magenta" : Fore.MAGENTA
}
def color(color_escogido, texto):
    global colores
    texto_coloreado = f"{colores[color_escogido]}{texto}{Fore.RESET}"
    return texto_coloreado

init(autoreset=True)
#Desempaqueta las lineas de Ganancias.txt, Gastos.txt y Total.txt, convirtiendolas en diccionarios dentro del diccioanrio Diccionarios
def abrir():
    Diccionarios = {
    "ganancias" : {},
    "gastos" : {},
    "total" : {
        "interior" : 0,
        "exterior" : 0
    }
    }
    for archivo in ("Ganancias", "Gastos"):
        with open(f"{archivo}.txt", "r") as f:
            datos = [linea.strip() for linea in f.readlines()]
        lista = archivo.lower()
            
            
        print(len(datos))
        print(lista)
        for grupo in range(7, len(datos) + 1, 7):
                
            for indice in range(grupo - 6, grupo + 1):
                    
                    
                if (indice - (7 * ((grupo / 7) - 1))) == 1:
                    clave = datos[indice - 1]
                    Diccionarios[lista][clave] = {}

                elif (indice - (7 * ((grupo / 7) - 1))) in (2, 4, 6,):
                    dato = datos[indice - 1]
                            
                        
                elif (indice - (7 * ((grupo / 7) - 1))) in (3, 5, 7):
                    valor = datos[indice - 1]
                    Diccionarios[lista][clave][dato] = valor
                    print(Diccionarios[lista][clave])
                if (indice - (7 * ((grupo / 7) - 1))) == 3:
                    int(valor)
                    
            #agarra el ultimo indice de cada grupo, 7, 14, 21, usa ese indice / 7 para saber que numero de grupo es y resta (7 * numero de grupo - 1) a cada indice individual, ejemplo
            # 8 - (7 * ((indice / 7) - 1)) indice valdria 14 por lo que seria 8 - (7 * ((14 / 7 ) - 1)), 8 - (7 * (2 - 1) queda 8 - (7) = 1, el cual es el equivalente a el 1 del primer grupo, 
            # si es el caso lo va a traar igual que si fuera 1, solo que guardara el valor actual, el indice)
            #objetivo, primera libnenea es el nomrbe de la entrada, de ahi hay pared de tipo de dato y valor de dato, necesito que agarre grupos de 7 lineas, 
            # tome la primera como nombre de entrada, de ahi tipo de dato y valor, al empezar en 0, 0 sera el nombre de la entrada, de ahi 1 y los impares 
            # seran el tipo de dato y 2 junto con los pares seran valores, esto hasta el numero 7 donde comeinza un nuevo grupo, los grupos irian 
            # 0,1,2,3,4,5,6 de ahi 7,8,9,10,11,12,13 y comenzaroa por 14 el siguiente y termina en 20 
            # 1,2,3,4,5,6,7 de ahi 8,9,10,11,12,13,14

    with open(f"Total.txt", "r") as f:
        datos = [linea.strip() for linea in f.readlines()]
    Diccionarios["total"]["interior"] = int(datos[0])
    Diccionarios["total"]["exterior"] = int(datos[1])
    

    with open("Indices.txt", "r") as f:
        indices = [indice.strip() for indice in f.readlines()]
   
    return Diccionarios, indices
#Empaqueta los diccionarios de Ganancias.txt, Gastos.txt y Total.txt, convirtiendolos en lineas ordenadas de manera especifica para ser desempaquetados en el futuro
def cerrar(Diccionarios):
    global indices
    for archivo in ("Ganancias", "Gastos"):
        empaquetado = []
        lista = archivo.lower()
        for entrada in Diccionarios[lista]:
            clave = f"{entrada}"
            
            empaquetado.append(clave)

            for dato in Diccionarios[lista][entrada]:
                
                valor = f"{Diccionarios[lista][entrada][dato]}"
                
                empaquetado.append(dato)
                empaquetado.append(valor)
            
        with open(f"{archivo}.txt", "w") as f:
            for x in empaquetado[0:(len(empaquetado) - 1)]:
                f.write(f"{x}\n")
            f.write(empaquetado[len(empaquetado) - 1])

    with open("Total.txt", "w") as t:
        f.write(Diccionarios["total"]["interior"])
        f.write(Diccionarios["total"]["exterior"])

    with open("Indices.txt", "w") as i:
        for indice in indices:
            i.write(indice)
    return True

#Dicta como se imprimen las distintas listas existentes. Es el menu para la funcion revisar en el menu principal
def revisar(Diccionarios):
    lista = ''
    while lista != "menu":
        ganancias = f"{color('verde','Ganancias')}: muestra las entradas de las ganancias\n"
        gastos = f"{color('lrojo', 'Gastos')}: Muestra las entradas de los gastos\n"
        total = f"{color('lazul', 'Total')}: Muestra la cantidad de dinero total, la que hay dentro (con la maestra caro) y el exterior (dentro de la caja fuerte)\n"
        modificar = f"{color('cyan', 'Modificar')}: Modifica una entrada anterior (cantidad de dinero, razon o fecha)\n"
        menu = f"{color('azul', 'Menu')}: Vuelve al menu"
        while lista == '':
            print(
                f"Listas:\n\n"
                f"{ganancias if lista != 'ganancias' else ''}"
                f"{gastos if lista != 'gastos' else ''}"
                f"{total if lista != 'total' else ''}\n"
                f"{modificar if lista != '' else ''}"
                f"{menu}\n"
                )
            lista = input(color("amarillo", "Escribe la lista a revisar: "))

        if lista in ("ganancias", "gastos"):
            for entrada in Diccionarios[lista]:
                if lista == "ganancias":
                    print(f"{color('amarillo','Diccionarios')}"     f"[{color('verde', f'{lista}')}]"      f"[{color('amarillo', f'{entrada}')}] = " + "{ ", end = "")
                    print(f"{color('verde', 'Valor de la ganancia: ')} {Diccionarios[lista][entrada]['cantidad']}, "
                        f"{Fore.LIGHTMAGENTA_EX}Origen de la {color('verde', 'ganancia:')} {Diccionarios[lista][entrada]['origen']}, ", end = ""
                        )
                    
                elif lista == "gastos":
                    print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('amarillo', f'{entrada}')}] = " + "{ ", end = "")
                    print(f"{color('lrojo', 'Valor del gasto: ')} {Diccionarios[lista][entrada]['cantidad']}, "
                        f"{Fore.LIGHTMAGENTA_EX}Origen del {color('lrojo', 'ganancia:')} {Diccionarios[lista][entrada]['origen']}, "
                        f"{color('lcyan', 'Nombre del retirante: ')}{Diccionarios[lista][entrada]['retirante']}", end = ""
                        )
                print(
                    f"{Fore.BLUE}Fecha{Fore.RESET}: {Diccionarios[lista][entrada]['fecha']} " + '}'
                    )
            print("")
            input(color("amarillo", "Presiona enter para continuar"))

        elif lista == "total":
            #introducir prints para el total
            None
        
        else:
            print(color("amarillo", "porfavor introduce el nombre de una de las siguientes listas"))
            lista = ''
            continue

def añadir_entrada(accion, lista, Diccionarios):
    global indices
    if accion == "agregar":
            cantidad = input(color("verde", "Introduce el valor de la ganancia") + ": ")
            origen = input(Fore.LIGHTBLUE_EX + "Escribe el origen de la ", color("verde", "ganancia") + ": ")
            destino = input(f"{color('lmagenta', 'Introduce el destino del dinero (exterior o interior)')}: ")
            
            
    elif accion == "retirar":
            cantidad = input(f"{Fore.LIGHTRED_EX}Introduce el valor del gasto{Fore.RESET}: ")
            origen = input(f"{Fore.LIGHTBLUE_EX}Introduce el origen del {Fore.LIGHTRED_EX}gasto{Fore.RESET}: ")
            destino = input(f"{color('lmagenta', 'Introduce el origen del dinero (exterior o interior)')}: ")
            retirante = input(f"{Fore.LIGHTCYAN_EX}Introduce el nombre de quien retira el efectivo{Fore.RESET}: ")
            cantidad = -int(cantidad)

    indiceValor = 1
                
    for indice in sorted(indices):
        if indiceValor != int(indice):
            indices.append(indiceValor)
            break
        else:
            indiceValor += 1

    print("La entrada a introducir sera\n\n")

    if lista == "ganancias":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('verde', f'{lista}')}]"      f"[{color('amarillo', f'Entrada{indiceValor}')}] = " + "{ ", end = "")
        print(
            f"{color('verde', 'Valor de la ganancia: ')} {cantidad}, "
            f"{Fore.LIGHTMAGENTA_EX}Origen de la {color('verde', 'ganancia:')} {origen}, "
            f"{color('lmagenta','Destino')}: {destino}", end = ""
            )
        
    elif lista == "gastos":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('amarillo', f'Entrada{indiceValor}')}] = " + "{ ", end = "")
        print(
            f"{color('lrojo', 'Valor del gasto: ')} {cantidad}, "
            f"{Fore.LIGHTMAGENTA_EX}Origen del {color('lrojo', 'gasto:')} {origen}, "
            f"{color('lmagenta','Destino')}: {destino}"
            f"{color('lcyan', 'Nombre del retirante: ')}{retirante}", end = ""
            )
    print(
        f"{Fore.BLUE}Fecha{Fore.RESET}: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} " + '}'
        )
    print("")
                
    while True:
        confirmacion = input("¿Los datos son correctos?\n")
    
        if confirmacion == "si":
            Diccionarios[lista][f"Entrada{indiceValor}"] = {
                "cantidad" : f"{cantidad}",
                "origen" : f"{origen}",
                "destino" : f"{destino}",
                **({"retirante": f'retirante'} if accion == "retirar" else {}),
                "fecha" : f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                }
            Diccionarios["total"][destino] -= cantidad
            print("")
            print(f"La entrada{indiceValor}:\n" 
                f"{Diccionarios[lista][f'Entrada{indiceValor}']}\n"
                )
            print("Se ha introducido exitosamente")
            print("Volviendo al menú...")
            return Diccionarios
        
        elif confirmacion == "no":
            Diccionarios = añadir_entrada(accion, lista, Diccionarios)
            return Diccionarios
        
        else:
            print("Error: Solo se acepta un si o un no como respuesta\n")
            continue

def entrada_definicion(accion, Diccionarios):
    retroceder(accion, "entrada_definicion")
    if accion == "agregar":
        lista = "ganancias"
    elif accion == "retirar":
        lista = "gastos"

    Diccionarios = añadir_entrada(accion, lista, Diccionarios)
    return Diccionarios

def retroceder(entrada, funcion):
    
    if entrada == "atras":
        return None
    elif entrada == "reinicio":
        return funcion()
    elif entrada == "menu":
        return main()
    return False



def main():
    global Diccionarios
    while True:
        accion = input(f"Bienvenido al {Fore.BLUE}menú\n\n"
                       

                       f"{Fore.LIGHTMAGENTA_EX}Entrada: {Fore.RESET}Introduce una entrada (agrega o quita dinero a la cuenta)\n"
                       f"{Fore.YELLOW}Revisar: {Fore.RESET}Revisa el dinero dentro y fuera de la cuenta\n"
                       f"{Fore.GREEN}Guardar: {Fore.RESET}Salir del programa guardando los cambios\n"
                       f"{Fore.LIGHTRED_EX}Salir: {Fore.RESET}Salir del programa {Fore.LIGHTRED_EX}SIN GUARDAR{Fore.RESET} los cambios\n\n"
                       
                       f"Escribe {Fore.BLUE}menu {Fore.RESET}en cualquier momento para cancelar y volver a esta pagina"
                        
                       f"{Fore.YELLOW}\n\nEscribe tu accion: {Fore.RESET}"
                       )
        print("")
        if accion == "entrada":
            accion = input(
                        f"{Fore.LIGHTGREEN_EX}Agregar: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                        f"{Fore.RED}Retirar: " f"{Fore.RESET}Quita dinero de la cuenta\n{Fore.RESET}"
                        f"{Fore.YELLOW}\n\nEscribe tu accion: {Fore.RESET}"
                    )
            if accion in ("agregar" , "retirar"):
                entrada_definicion(accion, Diccionarios)
                
            elif accion == "retirar":
                
                None



        elif accion == "revisar":
            revisar(Diccionarios)
            return True
            
        elif accion == "guardar":
            Diccionarios = cerrar(Diccionarios)
            return False
            
        elif accion == "salir":
            accion_final = input(f"¿Estas seguro de querer salir {Fore.LIGHTRED_EX}SIN GUARDAR{Fore.RESET} tus cambios?: ")
            if accion_final == "si":
                return False
            else:
                return True
        else:
            print("No se ha introducido una opcion valida. Favor de intentar nuevamente")





Diccionarios, indices = abrir()


    
print("")
print("")
while True:
    accion_final = main()
    if not accion_final:
        print("saliendo...")
        break
    else:
        continue
    