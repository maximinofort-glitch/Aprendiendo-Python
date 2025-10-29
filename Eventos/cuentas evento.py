from datetime import datetime 
from colorama import init, Fore, Style
import os

#os.chdir(r"C:\Users\maxim\OneDrive\Documentos\Codigos\Eventos")
os.chdir(r"C:\Users\maxim\Documents\Aprendiendo-Python\Eventos")
colores = {
    "amarillo" : Fore.YELLOW,
    "azul" : Fore.BLUE,
    "lazul" : Fore.LIGHTBLUE_EX,
    "rojo" : Fore.RED,
    "lrojo" : Fore.LIGHTRED_EX,
    "verde" : Fore.GREEN,
    "lverde" : Fore.LIGHTGREEN_EX,
    "cyan" : Fore.CYAN,
    "lcyan" : Fore.LIGHTCYAN_EX,
    "lmagenta" : Fore.LIGHTMAGENTA_EX,
    "magenta" : Fore.MAGENTA,
    "negro" : Fore.BLACK
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
    "papelera" : {},
    "total" : {
        "interior" : 0,
        "exterior" : 0
    }
    }
    for archivo in ("Ganancias", "Gastos", "Ganancias_Papelera", "Gastos_Papelera"):
        with open(f"{archivo}.txt", "r") as f:
            datos = [linea.strip() for linea in f.readlines()]
        if archivo in ("Ganancias_Papelera", "Gastos_Papelera"):
            lista = "papelera"
        else:
            lista = archivo.lower()
            
            
        print(len(datos))
        print(lista)
        if archivo in ("Ganancias", "Ganancias_Papelera"):
            rango = 9
        else:
            rango = 11
        for grupo in range(rango, len(datos) + 1, rango):
                
            for indice in range(grupo - (rango - 1), grupo + 1):
                    
                    
                if (indice - (rango * ((grupo / rango) - 1))) == 1:
                    clave = datos[indice - 1]
                    Diccionarios[lista][clave] = {}

                elif (indice - (rango * ((grupo / rango) - 1))) in (2, 4, 6, 8, 10):
                    dato = datos[indice - 1]
                            
                        
                elif (indice - (rango * ((grupo / rango) - 1))) in (3, 5, 7, 9, 11):
                    valor = datos[indice - 1]
                    Diccionarios[lista][clave][dato] = valor
                    print(Diccionarios[lista][clave])
                if (indice - (rango * ((grupo / rango) - 1))) == 3:
                    int(valor)
            #este metodo puede ser acortado haciendo que automaticamente se creen las claves "destino, cantidad, origen, retirante y fecha, de manera que no tienen que venir incluidos y repetidos por cada grupo dentro de los txt"
                    
            #agarra el ultimo indice de cada grupo, 7, 14, 21, usa ese indice / 7 para saber que numero de grupo es y resta (7 * numero de grupo - 1) a cada indice individual, ejemplo
            # 8 - (7 * ((indice / 7) - 1)) indice valdria 14 por lo que seria 8 - (7 * ((14 / 7 ) - 1)), 8 - (7 * (2 - 1) queda 8 - (7) = 1, el cual es el equivalente a el 1 del primer grupo, 
            # si es el caso lo va a traar igual que si fuera 1, solo que guardara el valor actual, el indice)
            #objetivo, primera libnenea es el nomrbe de la entrada, de ahi hay pared de tipo de dato y valor de dato, necesito que agarre grupos de 7 lineas, 
            # tome la primera como nombre de entrada, de ahi tipo de dato y valor, al empezar en 0, 0 sera el nombre de la entrada, de ahi 1 y los impares 
            # seran el tipo de dato y 2 junto con los pares seran valores, esto hasta el numero 7 donde comeinza un nuevo grupo, los grupos irian 
            # 0,1,2,3,4,5,6 de ahi 7,8,9,10,11,12,13 y comenzaroa por 14 el siguiente y termina en 20 
            # 1,2,3,4,5,6,7 de ahi 8,9,10,11,12,13,14
    with open("Indices.txt", "r") as i:
        indices = [int(linea.strip()) for linea in i.readlines()]


    with open("Total.txt", "r") as f:
        datos = [linea.strip() for linea in f.readlines()]
    Diccionarios["total"]["interior"] = int(datos[0])
    Diccionarios["total"]["exterior"] = int(datos[1])
    return Diccionarios, indices
#Empaqueta los diccionarios de Ganancias.txt, Gastos.txt y Total.txt, convirtiendolos en lineas ordenadas de manera especifica para ser desempaquetados en el futuro
def cerrar(Diccionarios):
    global indices
    for archivo in ("Ganancias", "Gastos", "Papelera"):
        empaquetado = []
        
        lista = archivo.lower()

        for entrada in Diccionarios[lista]:
            if archivo == "Papelera":
                if entrada[0] == "+":
                    archivo = "Ganancias_Papelera"
                elif entrada[0] == "-":
                    archivo = "Gastos_Papelera"
            clave = f"{entrada}"
            
            empaquetado.append(clave)

            for dato in Diccionarios[lista][entrada]:
                
                valor = f"{Diccionarios[lista][entrada][dato]}"
                
                empaquetado.append(dato)
                empaquetado.append(valor)
            
        with open(f"{archivo}.txt", "w") as f:
            try:
                for x in empaquetado[0:(len(empaquetado) - 1)]:
                    f.write(f"{x}\n")
                f.write(empaquetado[len(empaquetado) - 1])
            except IndexError:
                pass

    with open("Total.txt", "w") as t:
        t.write(str(Diccionarios["total"]["interior"]))
        t.write("\n")
        t.write(str(Diccionarios["total"]["exterior"]))

    with open("Indices.txt", "w") as i:
        try:
            for indice in indices[0:(len(indices) - 1)]:
                i.write(f"{indice}\n")
            i.write(str(indices[len(indices) - 1]))
        except IndexError:
            pass
    return True

#Dicta como se imprimen las distintas listas existentes. Es el menu para la funcion revisar en el menu principal
def revisar(Diccionarios):
    lista = ''
    ganancias = f"{color('verde','Ganancias')}: Muestra las entradas de las ganancias\n"
    gastos = f"{color('lrojo', 'Gastos')}: Muestra las entradas de los gastos\n"
    total = f"{color('lazul', 'Total')}: Muestra la cantidad de dinero total, la que hay dentro (con la maestra caro) y el exterior (dentro de la caja fuerte)\n"
    papelera = f"{color('negro', 'Papelera')}: Muestra las entradas que han sido borradas en el pasado\n"
    menu = f"{color('azul', 'Menu')}: Vuelve al menu"
    while lista != "menu":
        while True:
            print(
                f"Listas:\n\n"
                f"{ganancias if lista != 'ganancias' else ''}"
                f"{gastos if lista != 'gastos' else ''}"
                f"{total if lista != 'total' else ''}"
                f"{papelera if lista != 'papelera' else ''}\n"
                f"{menu}\n"
                )
            lista = ''
            accion = lista
            lista = input(color("amarillo", "Escribe la lista a revisar: "))
            if lista != '':
                break

        if lista in ("ganancias", "gastos"):
            for entrada in Diccionarios[lista]:
                imprimir_listas(lista, entrada, Diccionarios) 
                


        elif lista == "papelera":
            for entrada in sorted(Diccionarios[lista], key=lambda x: int(x[8:])):
                imprimir_listas(lista, entrada, Diccionarios)
            
            

        elif lista == "total":
            print(f"{color('amarillo','Diccionarios')}"     f"[{color('lcyan', f'{lista}')}]" + "{ ")
            print(
                f"{color('lrojo', 'Dinero en el interior' )} : {Diccionarios['total']['interior']}\n"
                f"{color('verde', 'Dinero en el exterior' )} : {Diccionarios['total']['exterior']}\n"
                f"{color('amarillo', 'Dinero total es')} : {(Diccionarios['total']['interior'] + Diccionarios['total']['exterior'])}\n"
                "}"
                )
            print("")
            input(color("amarillo", "Presiona enter para continuar"))
            lista = ''
            continue
            
            #introducir la funcion modificar en si, ya sea para borrar, editar y tal ves recuperar en esa misma funcion
        elif lista != "menu":
            print(color("amarillo", "porfavor introduce el nombre de una de las siguientes listas"))
            lista = ''
            continue

        if  lista != "menu":
            confirmacion = input(
                f"Escribe {color('verde', ''' 'si ' ''')} para modificar algun dato (cantidad, razon, origen, destino) de alguna entrada de la lista \n"
                f"En caso contrario presiona {color('amarillo', 'enter')}: "
                )
            if confirmacion == "si":  
                    modificar(lista, Diccionarios)
                    lista = ''
                    continue
        else:
            lista = ''
            continue

def modificar(lista, Diccionarios):
    if lista in ("ganancias", "gastos"):
        for entrada in Diccionarios[lista]:
            imprimir_listas(lista, entrada, Diccionarios) 


    elif lista == "papelera":
        for entrada in sorted(Diccionarios[lista], key=lambda x: int(x[12:])):
            imprimir_listas(lista, entrada, Diccionarios)

    
    seleccion = input("Selecciona una entrada basada en su numero")
    if lista == "papelera":
        while True:
            for entrada in Diccionarios["papelera"]:
                if seleccion == entrada[8:] and entrada[0] == "-":
                    entrada = f"-Entrada{seleccion}"
                    break
                elif seleccion == entrada[8:] and entrada[0] == "+":
                    entrada = f"+Entrada{seleccion}"
                    break
                else:
                    continue
            break
        
    else:
        entrada = f"Entrada{entrada}"
    print(f"Se ha seleccinado la entarda ' {entrada} ':")
    imprimir_listas(lista, entrada, Diccionarios)


    editar = f"{color('amarillo', 'Editar')}: Edita datos especificos de una entrada"
    borrar = f"{color('lrojo', 'Borrar')}: Borra una entrada existente y la agrega a la papelera"
    recuperar = f"{color('verde', 'Recuperar')}: Devuelve la entrada seleccionada a su lista original (Ganancias o gastos) con un nuevo numero de entrada\n"
    cancelar = f"{color('lcyan', 'Cancelar')}: Cancela la seleccion y vuelve a seleccionar una entrada"
    volver = f"{color('lmagenta', 'Volver')}: Vuelve a la lista de listas"
    menu = f"{color('azul', 'Menu')}: Vuelve al menu"

    while True:
        print("¿Que deseas hacer con la entrada?")
        
        accion = input(
        f"{editar}"
        f"{borrar}"
        f"{recuperar if lista == 'papelera' else ''}"
        f"{cancelar}"
        f"{volver}"
        f"{menu}"
        )
        if accion == "borrar":
            confirmacion = input(f"Escribe {color('lrojo', ''' 'borrar' ''')} para confirmar la eliminacion {color('rojo', {'DEFINITIVA' if lista == 'papelera' else ''})} de la entrada")
            if confirmacion == "borrar":
                if lista == "papelera":
                    del Diccionarios[lista][entrada]
                elif lista == "ganancias":
                    entrada_borrada = Diccionarios["ganancias"].pop(entrada)
                    Diccionarios["papelera"][entrada] = entrada_borrada
                elif lista == "gastos":
                    entrada_borrada = Diccionarios["gastos"].pop(entrada)
                    Diccionarios["papelera"][entrada] = entrada_borrada
                print(f"La entrada ha sido borrada {color('rojo', 'definitivamente' if lista == 'papelera' else '')} de manera exitosa")
                break


        elif accion == "editar":
            imprimir_listas(lista, f"Entrada{entrada}", Diccionarios)
            dato = input(f"Elige el dato a modificar (Cantidad, Origen, Destino{', Retirante' if lista == 'gastos' else ''})")
            valor = input(f"Escribe el nuevo valor de la clave {dato}")
            confirmacion = input(f"¿Estas seguro de reemplazar\n {dato} : {Diccionarios[lista][entrada]} por {dato} : {valor}?")
            if confirmacion == "si":
                Diccionarios[lista][entrada][dato] = valor
                break
            else:
                continue
        else:
            continue
#si quiero recuperar una entrada actualmente hay un+ o - al inicio del nombre de la clave ejemplo: "+Entrada200" necesito quitar el + o - al recuperar una entrada
#hice que independientemente de si la entrada tiene +, - o ninguna se guarde la enyrada en si como la variable entrada dependiendo unicamente de la lista de donde 
# se saco y suprimer valor en caso de haber llegado desde papelera, ahora mismmo estoy en el apso de confirmacion de sobreescritura del valor del dato que se selecciono,
#creo que ya lo hice pero puede que haya conflictos con si es - o + si viene de papelera, si noe s el caso toca hacer lasd funciones de recuperar, cancelar, volver y el menu
            
        

def imprimir_listas(lista, entrada, Diccionarios):
    if lista == "papelera":
        identificador = len(entrada)
    else:
        identificador = 0
    if lista == "ganancias" or identificador == 4:
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lverde', f'{lista}')}]"      f"[{color('verde', '+')}{color('amarillo', f'{entrada}')}] = " + "{ ")
        print(
            f"{'':<15}{color('verde', 'Valor de la ganancia')} : {Diccionarios[lista][entrada]['cantidad']}, \n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}Origen de la {color('verde', 'ganancia')} : {Diccionarios[lista][entrada]['origen']}, \n"
            f"{'':<15}{color('lcyan','Destino')} : {Diccionarios[lista][entrada]['destino']},"
            )
        
    elif lista == "gastos" or identificador == 5:
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('rojo', '-')}{color('amarillo', f'{entrada}')}] = " + "{ ")
        print(
            f"{'':<15}{color('lrojo', 'Valor del gasto')} : {Diccionarios[lista][entrada]['cantidad']},\n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}Origen del {color('lrojo', 'gasto')} : {Diccionarios[lista][entrada]['origen']},\n"
            f"{'':<15}{color('lmagenta','Origen del dinero')} : {Diccionarios[lista][entrada]['destino']}, \n"
            f"{'':<15}{color('lcyan', 'Nombre del retirante')} : {Diccionarios[lista][entrada]['retirante']}"
            )
    print(
        f"{'':<15}{Fore.BLUE}Fecha{Fore.RESET}: {Diccionarios[lista][entrada]['fecha']} = \n" + '}'
        )
    print("")


def entrada_definicion(accion, Diccionarios):
    accion = input(
                f"{Fore.LIGHTGREEN_EX}Deposito: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                f"{Fore.RED}Retiro: " f"{Fore.RESET}Quita dinero de la cuenta\n{Fore.RESET}"
                f"{Fore.YELLOW}\n\nEscribe tu accion: {Fore.RESET}"
                )
    retroceder(accion, "entrada_definicion")
    if accion == "deposito":
        lista = "ganancias"
    elif accion == "retiro":
        lista = "gastos"

    Diccionarios, indices = añadir_entrada(accion, lista, Diccionarios)
    return Diccionarios, indices

def añadir_entrada(accion, lista, Diccionarios):
    global indices
    if accion == "deposito":
            while True:
                try:
                    cantidad = input(color("verde", "Introduce el valor de la ganancia") + ": ")
                    int(cantidad)
                    break
                except TypeError:
                    print("Error: No se ha introducido un numero como cantidad")
                    continue
            origen = input(f"{color('lazul', 'Escribe el origen de la ')}{color('verde', 'ganancia')}: ")
            destino = input(f"{color('lmagenta', 'Introduce el destino del dinero (exterior o interior)')}: ")
            
            
    elif accion == "retiro":
            while True:
                try:
                    cantidad = input(color("lrojo", "Introduce el valor del gasto") + ": ")
                    cantidad = -int(cantidad)
                    break
                except TypeError:
                    print("Error: No se ha introducido un numero como cantidad")
                    continue
            origen = input(f"{color('lazul', 'Escribe el origen del ')}{color('lrojo', 'gasto')}: ")
            destino = input(f"{color('lmagenta', 'Introduce el origen del dinero (exterior o interior)')}: ")
            retirante = input(f"{color('lcyan', 'Introduce el nombre de quien retira el efectivo')}: ")
            

    indiceValor = 1
                
    for indice in sorted(indices):
        if indiceValor != int(indice):
            indices.append(indiceValor)
            break
        else:
            indiceValor += 1

    print("La entrada a introducir sera\n\n")

    if lista == "ganancias":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lverde', f'{lista}')}]"      f"[{color('verde', '+')}{color('amarillo', f'Entrada{indiceValor}')}] = " + "{ ")
        print(
            f"{'':<15}{color('verde', 'Valor de la ganancia')} : {cantidad}, \n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}Origen de la {color('verde', 'ganancia')} : {origen}, \n"
            f"{'':<15}{color('lcyan','Destino')} : {destino},"
            )
        
    elif lista == "gastos":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('rojo', '-')}{color('amarillo', f'Entrada{indiceValor}')}] = " + "{ ")
        print(
            f"{'':<15}{color('lrojo', 'Valor del gasto')} : {cantidad},\n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}Origen del {color('lrojo', 'gasto')} : {origen},\n"
            f"{'':<15}{color('lmagenta','Origen del dinero')} : {destino}, \n"
            f"{'':<15}{color('lcyan', 'Nombre del retirante')} : {retirante}"
            )
    print(
        f"{'':<15}{Fore.BLUE}Fecha{Fore.RESET}: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n" + f"{'':<15}" + '}'
        )
    print("")
                
    while True:
        confirmacion = input("¿Los datos son correctos?\n")
    
        if confirmacion == "si":
            Diccionarios[lista][f"Entrada{indiceValor}"] = {
                "cantidad" : f"{cantidad}",
                "origen" : f"{origen}",
                "destino" : f"{destino}",
                **({"retirante": f'retirante'} if accion == "retiro" else {}),
                "fecha" : f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                }
            indices.append(indiceValor)
            Diccionarios["total"][destino] += int(cantidad)
            print("")
            print(f"La entrada{indiceValor}:\n" 
                f"{Diccionarios[lista][f'Entrada{indiceValor}']}\n"
                )
            print("Se ha introducido exitosamente")
            print("Volviendo al menú...")
            return Diccionarios, indices
        
        elif confirmacion == "no":
            Diccionarios = añadir_entrada(accion, lista, Diccionarios)
            return Diccionarios, indices
        
        else:
            print("Error: Solo se acepta un si o un no como respuesta\n")
            continue

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
            entrada_definicion(Diccionarios)
                



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
    


#los indices no se guardan al borrar, se usa la funcion pop para unicamente tener los diccioanrios dentro de la entrada sin la entrada, 
# esto se guarda en una lista aparte como ganancias, total y gastos, si se quiere recuperar una entrada de usara una nueva funcion que 
# buscara un idnice disponible y confirmara la recuperacion de la entrada al mismo tiempo que menciona cual sera su nuevo nombre / indice