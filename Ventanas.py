import tkinter as tk



main = tk.Tk()
main.state("zoomed")
main.title("Calculdora de IMC")
info = tk.Frame()
info.pack(expand = True, fill="both")

peso = tk.Label(info, text= "Introduzca su peso")
peso.grid(row = 6, column =3, padx = (650,100), pady = (300, 0))
kilos = tk.Entry(info)
kilos.grid(row = 8, column = 3, padx = (650,100))
altura = tk.Label(info, text= "Introduzca su altura en metros")
altura.grid(row = 6, column = 5, padx = 100, pady = (300,0))
metros = tk.Entry(info)
metros.grid(row = 8, column = 5)
ims = tk.Button(info,text = "Calcular IMS", Calcular)



main.mainloop()
