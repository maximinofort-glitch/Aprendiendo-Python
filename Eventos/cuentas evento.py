from datetime import datetime 
from colorama import Fore, Style
import textwrap
import os

os.chdir(r"C:\Users\maxim\OneDrive\Documentos\Codigos\Eventos")
#os.chdir(r"C:\Users\maxim\Documents\Aprendiendo-Python\Eventos")

#Toda esta seccion de colores es para aplicar colores al texto con el formato color("color", "texto a colorear")
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
#EJEMPLO:
#print(f"Probando un {color('azul', 'color')}, en este caso el azul")

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
                if (indice - (rango * ((grupo / rango) - 1))) == 3:
                    float(valor)
            #este metodo puede ser acortado haciendo que automaticamente se creen las claves "ubicacion, monto, concepto, retirante y fecha, de manera que no tienen que venir incluidos y repetidos por cada grupo dentro de los txt"
                    
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
    Diccionarios["total"]["interior"] = float(datos[0])
    Diccionarios["total"]["exterior"] = float(datos[1])
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

#Dicta como se imprimen las distintas listas existentes. Es la introduccion al menu de modificaciones
def revisar(Diccionarios):
    lista = ''
    ganancias = f"{color('verde','Ganancias')}: Muestra las entradas de las ganancias"
    gastos = f"{color('lrojo', 'Gastos')}: Muestra las entradas de los gastos"
    total = f"{color('lazul', 'Total')}: Muestra el monto de dinero total, la que hay dentro (con la maestra caro) y el exterior (dentro de la caja fuerte)"
    papelera = f"{color('negro', 'Papelera')}: Muestra las entradas que han sido borradas en el pasado"
    main = f"{color('azul', 'Menu')}: Vuelve al menu"
    while lista != "menu":
        while True:
            print(textwrap.dedent(f"""
                Listas:
                                  
                {ganancias if lista != 'ganancias' else ''}
                {gastos if lista != 'gastos' else ''}
                {total if lista != 'total' else ''}
                {papelera if lista != 'papelera' else ''}

                {main}

                """))
            lista = ''
            lista = input(f"{color('amarillo', 'Escribe la lista a revisar')} \n>>>>>>>> ")
            lista = lista.lower()
            if lista != '':
                break

        if lista in ("ganancias", "gastos"):
            for entrada in Diccionarios[lista]:
                imprimir_listas(lista, entrada, Diccionarios) 
                


        elif lista == "papelera":
            print(Diccionarios[lista])
            for entrada in sorted(Diccionarios[lista], key=lambda x: int(x[8:])):
                imprimir_listas(lista, entrada, Diccionarios)
            
            

        elif lista == "total":
            print(f"{color('amarillo','Diccionarios')}"     f"[{color('lcyan', f'{lista}')}]" + "{ ")
            print(
                f"      {color('lrojo', 'Dinero en el interior' )} : {Diccionarios['total']['interior']}\n"
                f"      {color('verde', 'Dinero en el exterior' )} : {Diccionarios['total']['exterior']}\n"
                f"      {color('amarillo', 'Dinero total es')} : {(Diccionarios['total']['interior'] + Diccionarios['total']['exterior'])}\n"
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
            while True:
                confirmacion = input(
                    f"Escribe {color('verde', ''' 'si ' ''')} para modificar algun dato (monto, concepto, ubicacion) de alguna entrada de la lista \n"
                    f"En caso contrario presiona {color('amarillo', 'enter')}: "
                    )
                confirmacion = confirmacion.lower()
                if confirmacion == "si":  
                        menu = modificar(lista, Diccionarios)
                        break
                elif confirmacion == "":
                    menu = False
                    break
                else: 
                    continue

            if menu:
                break
            lista = ''
            continue
        else:
            break

def modificar(lista, Diccionarios):
    global indices
    if lista in ("ganancias", "gastos"):
        for entrada in Diccionarios[lista]:
            imprimir_listas(lista, entrada, Diccionarios) 


    elif lista == "papelera":
        for entrada in sorted(Diccionarios[lista], key=lambda x: int(x[8:])):
            imprimir_listas(lista, entrada, Diccionarios)

    while True:
        seleccion = input(f"Selecciona una entrada basada en su {color('azul', 'numero')}: ")
        seleccion = seleccion.lower()
        if f"+Entrada{seleccion}" in Diccionarios[lista]:
            entrada = f"+Entrada{seleccion}"
            break
        elif f"-Entrada{seleccion}" in Diccionarios[lista]:
            entrada = f"-Entrada{seleccion}"
            break
        else:
            print(f"No se ha encontrado la {color('amarillo',f'Entrada{seleccion}')}")
            continue
    

    print(f"Se ha seleccinado la ' {entrada[1:]} ':")
    imprimir_listas(lista, entrada, Diccionarios)


    editar = f"{color('amarillo', 'Editar')}: Edita datos especificos de una entrada\n"
    borrar = f"{color('lrojo', 'Borrar')}: Borra una entrada existente y la agrega a la papelera\n"
    recuperar = f"{color('verde', 'Recuperar')}: Devuelve la entrada seleccionada a su lista original (Ganancias o gastos) con un nuevo numero de entrada\n\n"
    cancelar = f"{color('lcyan', 'Cancelar')}: Cancela la seleccion y vuelve a seleccionar una entrada\n"
    volver = f"{color('lmagenta', 'Volver')}: Vuelve a la lista de listas\n"
    menu = f"{color('azul', 'Menu')}: Vuelve al menu\n"

    while True:
        print(
            f"{editar}"
            f"{borrar}"
            f"{recuperar if lista == 'papelera' else ''}"
            f"{cancelar}"
            f"{volver}"
            f"{menu}"
            )
        
        
        accion = input(f"{color('amarillo', '¿Que deseas hacer con la entrada?')}\n>>>>>>>> ")
        accion = accion.lower()
        if accion == "borrar":
            if lista == "papelera":
                confirmacion = input(f"Escribe {color('lrojo', ''' 'borrar' ''')} para confirmar la eliminacion {color('rojo', 'DEFINITIVA')} de la entrada")
            else:
                confirmacion = input(f"Escribe {color('lrojo', ''' 'borrar' ''')} para confirmar la eliminacion de la entrada")
            confirmacion = confirmacion.lower()
            if confirmacion == "borrar":
                if lista == "papelera":
                    del Diccionarios[lista][entrada]
                elif lista in ("ganancias", "gastos"):
                    
                    indices_nuevos = []
                    for indice in indices:
                        if str(indice) != str(entrada[8:]):
                            indices_nuevos.append(indice)
                    indices = indices_nuevos
                    Diccionarios['total'][Diccionarios[lista][entrada]["ubicacion"]] -=  int(Diccionarios[lista][entrada]["monto"])
                    entrada_borrada = Diccionarios[lista].pop(entrada)
                    Diccionarios["papelera"][entrada] = entrada_borrada
                    
                
                print(f"La entrada ha sido borrada {color('rojo', 'definitivamente' if lista == 'papelera' else '')} de manera exitosa")
                break


        elif accion == "editar":
            imprimir_listas(lista, entrada, Diccionarios)
            dato = input(f"Elige el dato a modificar")
            dato = dato.lower()
            valor = input(f"Escribe el nuevo valor de la clave {dato}")
            valor = valor.lower()
            confirmacion = input(f"Escribe si para confirmar el cambio\n {dato} : {Diccionarios[lista][entrada][dato]} por {dato} : {valor}\n ")
            confirmacion = confirmacion.lower()
            
            if confirmacion == "si":
                if dato == "monto":
                    Diccionarios["total"][Diccionarios[lista][entrada]["ubicacion"]] -= float(Diccionarios[lista][entrada]["monto"])
                Diccionarios[lista][entrada][dato] = valor
                if dato == "monto":
                    Diccionarios["total"][Diccionarios[lista][entrada]["ubicacion"]] += float(Diccionarios[lista][entrada]["monto"])
                break
            else:
                continue

        elif accion == "recuperar" and lista == "papelera":
            
            indiceValor = 1
            for indice in sorted(indices):
                        if indiceValor != int(indice):
                            break
                        else:
                            indiceValor += 1
            
            confirmacion = input(f"Escribe {color('verde', 'confirmar')} para recuperar la entrada y devolverla a la lista '{lista}' con el indice {indiceValor}")
            confirmacion = confirmacion.lower()
            if confirmacion == "confirmar":
                
                entrada_borrada = Diccionarios["papelera"].pop(entrada)

                if entrada[0] == "+":
                    lista = "ganancias"


                elif entrada[0] == "-":
                    lista == "gastos"

                
                indices.append(indiceValor)
                entrada = f"{entrada[0:8]}{indiceValor}"

                Diccionarios[lista][entrada] = entrada_borrada
                Diccionarios["total"][Diccionarios[lista][entrada]["ubicacion"]] += int(Diccionarios[lista][entrada]["monto"])
                print(f"La entrada {entrada} se ha recuperado con exito")
                break
            else: 
                continue

        elif accion == "cancelar":
            vuelta = modificar(lista, Diccionarios)
            return vuelta
        elif accion == "volver":
            return False
        elif accion == "menu":
            return True
        else:
            continue

            

def imprimir_listas(lista, entrada, Diccionarios):
    if entrada[0] == "+":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lverde', f'{lista}')}]"      f"[{color('verde', f'{entrada[0]}')}{color('amarillo', f'{entrada[1:]}')}] = " + "{ ", end = "")
        print(f"""
            {'':<5}{color('verde', 'Monto de la ganancia')} : {Diccionarios[lista][entrada]['monto']},
            {'':<5}{Fore.LIGHTMAGENTA_EX}Concepto de la {color('verde', 'ganancia')} : {Diccionarios[lista][entrada]['concepto']}, 
            {'':<5}{color('lcyan','Ubicacion')} : {Diccionarios[lista][entrada]['ubicacion']},
            """, end = "")
        
    elif entrada[0] == "-":
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('rojo', f'{entrada[0]}')}{color('amarillo', f'{entrada[1:]}')}] = " + "{ ", end = "")
        print(f"""
            {'':<5}{color('lrojo', 'Monto del gasto')} : {Diccionarios[lista][entrada]['monto']},
            {'':<5}{Fore.LIGHTMAGENTA_EX}Concepto del {color('lrojo', 'gasto')} : {Diccionarios[lista][entrada]['concepto']},
            {'':<5}{color('lcyan','Ubicacion del dinero')} : {Diccionarios[lista][entrada]['ubicacion']}, 
            {'':<5}{color('magenta', 'Nombre del retirante')} : {Diccionarios[lista][entrada]['retirante']}
            """, end = "")
    print(
        f"{'':<5}{Fore.BLUE}Fecha{Fore.RESET}: {Diccionarios[lista][entrada]['fecha']}  \n" + f"{'':<17}" + '}'
        )
    print("")


def entrada_definicion(accion, Diccionarios):
    while True:
        accion = input(
                    f"{Fore.LIGHTGREEN_EX}Deposito: " f"{Fore.RESET}Añade dinero a la cuenta\n"
                    f"{Fore.RED}Retiro: " f"{Fore.RESET}Quita dinero de la cuenta\n{Fore.RESET}"
                    f"{Fore.YELLOW}\n\nEscribe tu accion: {Fore.RESET}"
                    )
        accion = accion.lower()
        retroceder(accion, "entrada_definicion")
        if accion == "deposito":
            lista = "ganancias"
            break
        elif accion == "retiro":
            lista = "gastos"
            break
        else:
            print("Error: No se ha introducido una accion valida")
            continue

    Diccionarios, indices = añadir_entrada(accion, lista, Diccionarios)
    return Diccionarios, indices

def añadir_entrada(accion, lista, Diccionarios):
    global indices
    if accion == "deposito":
            while True:
                try:
                    monto = input(color("verde", "Introduce el valor de la ganancia") + ": ")
                    float(monto)
                    break
                except ValueError:
                    print("Error: No se ha introducido un numero valido como monto")
                    continue
            concepto = input(f"{color('lazul', 'Escribe el concepto de la ')}{color('verde', 'ganancia')}: ")
            ubicacion = input(f"{color('lmagenta', 'Introduce la ubicacion del dinero (exterior o interior)')}: ")
            ubicacion = ubicacion.lower()
            
            
    elif accion == "retiro":
            while True:
                try:
                    monto = input(color("lrojo", "Introduce el monto del gasto") + ": ")
                    monto = -int(monto)
                    break
                except TypeError:
                    print("Error: No se ha introducido un numero como monto")
                    continue
            concepto = input(f"{color('lazul', 'Escribe el concepto del ')}{color('lrojo', 'gasto')}: ")
            ubicacion = input(f"{color('lmagenta', 'Introduce la ubicacion del dinero (exterior o interior)')}: ")
            ubicacion = ubicacion.lower()
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
        entrada = f"+Entrada{indiceValor}"
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lverde', f'{lista}')}]"      f"[{color('verde', f'{entrada[0]}')}{color('amarillo', f'{entrada[1:]}')}] = " + "{ ")
        print(
            f"{'':<15}{color('verde', 'Monto de la ganancia')} : {monto}, \n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}concepto de la {color('verde', 'ganancia')} : {concepto}, \n"
            f"{'':<15}{color('lcyan','Ubicacion')} : {ubicacion},"
            )
        
    elif lista == "gastos":
        entrada = f"-Entrada{indiceValor}"
        print(f"{color('amarillo','Diccionarios')}"     f"[{color('lrojo', f'{lista}')}]"      f"[{color('rojo', f'{entrada[0]}')}{color('amarillo', f'{entrada[1:]}')}] = " + "{ ")
        print(
            f"{'':<15}{color('lrojo', 'Monto del gasto')} : {monto},\n"
            f"{'':<15}{Fore.LIGHTMAGENTA_EX}concepto del {color('lrojo', 'gasto')} : {concepto},\n"
            f"{'':<15}{color('lmagenta','Ubicacion del dinero')} : {ubicacion}, \n"
            f"{'':<15}{color('lcyan', 'Nombre del retirante')} : {retirante}"
            )
    print(
        f"{'':<15}{Fore.BLUE}Fecha{Fore.RESET}: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n" + f"{'':<15}" + '}'
        )
    print("")
                
    while True:
        confirmacion = input("¿Los datos son correctos?\n")
        confirmacion = confirmacion.lower()
        if confirmacion == "si":
            Diccionarios[lista][f'{entrada}'] = {
                "monto" : f"{monto}",
                "concepto" : f"{concepto}",
                "ubicacion" : f"{ubicacion}",
                **({"retirante": f'retirante'} if accion == "retiro" else {}),
                "fecha" : f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                }
            indices.append(indiceValor)
            Diccionarios["total"][ubicacion] += float(monto)
            print("")
            print(f"La Entrada{indiceValor}:\n" 
                f"{Diccionarios[lista][f'{entrada}']}\n"
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
    global indices
    while True:
        accion = input(textwrap.dedent(f"""
                       Bienvenido al {Fore.BLUE}menú
                       
                       {color('magenta', 'Entrada')}: Introduce una entrada (agrega o quita dinero a la cuenta)
                       {color('amarillo', 'Revisar')}: Revisa el dinero dentro y fuera de la cuenta
                       {color('verde', 'Guardar')}: Salir del programa guardando los cambios
                       {color('lrojo', 'Salir')}: Salir del programa {color('lrojo', 'SIN GUARDAR')} los cambios
                       {color('rojo', 'Reiniciar')}: Reinicia {color('rojo', 'TODOS')} los datos almacenados
                       
                       Escribe {Fore.BLUE}menu {Fore.RESET}en cualquier momento para cancelar y volver a esta pagina
                        
                       {color('amarillo', 'Escribe tu accion')}
                       >>>>>>> """))
        print("")
        accion = accion.lower()
        if accion == "entrada":
            Diccionarios, indices = entrada_definicion(accion, Diccionarios)
                

        elif accion == "revisar":
            revisar(Diccionarios)
            return True
            
        elif accion == "guardar":
            Diccionarios = cerrar(Diccionarios)
            return False
            
        elif accion == "salir":
            accion_final = input(f"¿Estas seguro de querer salir {Fore.LIGHTRED_EX}SIN GUARDAR{Fore.RESET} tus cambios?: ")
            accion_final = accion_final.lower()
            if accion_final == "si":
                return False
            else:
                return True
            
        elif accion == "reiniciar":
            confirmacion = input(f"¿Estas seguro de querer {color('rojo', 'REINCIAR TODOS')} los datos almacenados?\nEsta accion no es reversible una ves guardado el cambio\n>>>>>>>>>>>>>>>>> ")
            confirmacion = confirmacion.lower()
            if confirmacion == "si":
                Diccionarios = {
                    "ganancias" : {},
                    "gastos" : {},
                    "papelera" : {},
                    "total" : {
                        "interior" : 0,
                        "exterior" : 0
                        }
                    }
                indices = []
                print("Todos los datos han sido borrados con exito")
        else:
            print("No se ha introducido una opcion valida. Favor de intentar nuevamente")

Diccionarios, indices = abrir()
  
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