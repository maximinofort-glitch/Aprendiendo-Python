import tkinter as tk

def calcular():
    a = int(entry1.get())
    b = int(entry2.get())
    resultado_label.config(text=f"Resultado: {a + b}")

ventana = tk.Tk()
ventana.title("Mi Calculadora")

entry1 = tk.Entry(ventana)
entry1.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack()

resultado_label = tk.Label(ventana, text="Resultado:")
resultado_label.pack()

ventana.mainloop()