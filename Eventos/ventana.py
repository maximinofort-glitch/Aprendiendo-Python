import tkinter as tk
def procesar():
    edad = int(entry.get())
    if edad >= 18:
        mayor = "si"
    else:
        mayor = "no"
    resultado.config(text=f"Tienes {edad} años, por lo que {'' if mayor == "si" else 'no'} eres mayor de edad")
    frame.pack_forget()
    frame2.pack()
def reinicio():
    frame2.pack_forget()
    frame.pack()
ventana = tk.Tk()
ventana.title("Solicitud de nombre")
ventana.geometry("1080x920")
frame = tk.Frame(ventana)
frame.pack()
label = tk.Label(frame, text="Ingresa tu edad")
label.pack()
entry = tk.Entry(frame)
entry.pack()
boton = tk.Button(frame, text="Continuar", command=procesar)
boton.pack()

frame2 = tk.Frame(ventana)
resultado = tk.Label(frame2, text="placeholder")
resultado.pack()
boton2 = tk.Button(frame2,text="regresar", command=reinicio)
ventana.mainloop()

