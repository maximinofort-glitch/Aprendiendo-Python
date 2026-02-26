import tkinter as tk

def verificar():
    edad = int(entry1.get())

    if edad  >= 18:
        confirmacion = True
    else:
        confirmacion = False
    
    resultado_label.config(text=f"Tienes {edad} años, {'' if confirmacion else 'no '}eres mayor de edad")
    frame1.pack_forget()
    frame2.pack(expand=True)

def volver():
    frame2.pack_forget()
    frame1.pack()

ventana = tk.Tk()
ventana.state("zoomed")
ventana.title("Mi Calculadora")


frame1 = tk.Frame(ventana)
frame1.pack(expand=True)
frame2 = tk.Frame(ventana)


edad = tk.Label(frame1, text="Introduce tu edad")
edad.pack()

entry1 = tk.Entry(frame1)
entry1.pack()


boton = tk.Button(frame1, text="Verificar", command=verificar)
boton.pack()


resultado_label = tk.Label(frame2, text="placeholder")
resultado_label.pack()


boton2 = tk.Button(frame2, text="Volver", command=volver)
boton2.pack()

ventana.mainloop()