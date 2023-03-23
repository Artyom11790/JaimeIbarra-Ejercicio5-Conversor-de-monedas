from tkinter import *
from tkinter import ttk

root=Tk()
root.title("EJERCICIO B")
#variables
moneda = IntVar()
CM = StringVar()
MA = StringVar()
#metodo
def Convertir():

    if MA.get()!=CM.get():

        if CM.get()=="MXN":

            if MA.get()=="USD":
                resultado = moneda.get()*19.00
                B.config(text=f'{resultado} MXN')

            if MA.get()=="EUR":
                resultado = moneda.get()*20.30
                B.config(text=f'{resultado} MXN')

        if CM.get()=="USD":

            if MA.get()=="MXN":
                resultado = moneda.get()*0.050
                B.config(text=f'{resultado} USD')

            if MA.get()=="EUR":
                resultado = moneda.get()*1.05
                B.config(text=f'{resultado} USD')

        if CM.get()=="EUR":

            if MA.get()=="MXN":
                resultado = moneda.get()*0.050
                B.config(text=f'{resultado} EUR')

            if MA.get()=="USD":
                resultado = moneda.get()*0.90
                B.config(text=f'{resultado} EUR')

    else:
        B.config(text=f'elige una opcion diferente')



ventanaPrincipal = Frame(root, bg="#E9967A")
ventanaPrincipal.grid()

#titulo de la raiz
titulo = Label(ventanaPrincipal, text="Convertidor de monedas", font=("Roboto",20,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=1, column=1, padx=10, columnspan=2)

#Etiqueta moneda actual
titulo = Label(ventanaPrincipal, text="Numero A", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=2, column=1, padx=10, pady=10)

textoNumeroA = Entry(ventanaPrincipal, font=("Roboto",10), textvariable=moneda).grid(row=2, column=2, padx=10, pady=10)

#moneda actual
titulo = Label(ventanaPrincipal, text="Valor actual", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=3, column=1, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable=MA).grid(row=4, column=1, padx=10, pady=10)

#moneda a convertir
titulo = Label(ventanaPrincipal, text="Convertir", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=3, column=2, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["USD", "MXN", "EUR"], state="readonly", textvariable = CM).grid(row=4, column=2, padx=10, pady=10)

#etiqueta resultado
titulo = Label(ventanaPrincipal, text="Resultado", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=5, column=1, padx=10, pady=10)

B = Label(ventanaPrincipal, text="$", font=("Roboto",10))
B.grid(row=5, column=2, padx=10, pady=10)

#Boton para convertir
botonConvertir = Button(ventanaPrincipal, text="Convertir", font=("Roboto",10), command=Convertir).grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()