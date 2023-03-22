from tkinter import *
from tkinter import ttk

root=Tk()
root.title("EJERCICIO B")

#metodo
def Convertir():

    if MonedaAc.get()!=Convertirmoneda.get():

        if Convertirmoneda.get()=="$MXN":

            if MonedaAc.get()=="$USD":
                resultado = moneda.get()*19.00
                NUMEROB.config(text=f'{resultado} $MXN')

            if MonedaAc.get()=="EUR":
                resultado = moneda.get()*20.29
                NUMEROB.config(text=f'{resultado} $MXN')

        if Convertirmoneda.get()=="$USD":

            if MonedaAc.get()=="$MXN":
                resultado = moneda.get()*0.053
                NUMEROB.config(text=f'{resultado} $USD')

            if MonedaAc.get()=="$EUR":
                resultado = moneda.get()*1.07
                NUMEROB.config(text=f'{resultado} USD')

        if Convertirmoneda.get()=="$EUR":

            if MonedaAc.get()=="$MXN":
                resultado = moneda.get()*0.049
                NUMEROB.config(text=f'{resultado} EUR')

            if MonedaAc.get()=="$USD":
                resultado = moneda.get()*0.94
                NUMEROB.config(text=f'{resultado} EUR')

    else:
        NUMEROB.config(text=f'elige una opcion diferente')

#variables
moneda = IntVar()
Convertirmoneda = StringVar()
MonedaAc = StringVar()

Principal = Frame(root, bg="#E9967A")
Principal.grid()

#titulo de la raiz
titulo = Label(Principal, text="Convertidor de monedas", font=("Roboto",20,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=1, column=1, padx=10, columnspan=2)

#Etiqueta moneda actual
titulo = Label(Principal, text="Numero A", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=2, column=1, padx=10, pady=10)

NumeroA = Entry(Principal, font=("Roboto",10), textvariable=moneda).grid(row=2, column=2, padx=10, pady=10)

#moneda actual
titulo = Label(Principal, text="Valor actual", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=3, column=1, padx=10, pady=10)

Lista = ttk.Combobox(Principal,values=["USD", "MXN", "EUR"], state="readonly", textvariable=MonedaAc).grid(row=4, column=1, padx=10, pady=10)

#moneda a convertir
titulo = Label(Principal, text="Convertir", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=3, column=2, padx=10, pady=10)

Lista = ttk.Combobox(Principal,values=["USD", "MXN", "EUR"], state="readonly", textvariable = Convertirmoneda).grid(row=4, column=2, padx=10, pady=10)

#etiqueta resultado
titulo = Label(Principal, text="Resultado", font=("Roboto",10,"bold"), bg="#E9967A", fg="white")
titulo.grid(row=5, column=1, padx=10, pady=10)

NUMEROB = Label(Principal, text="", font=("Roboto",10))
NUMEROB.grid(row=5, column=2, padx=10, pady=10)

#Boton para convertir
botonConvertir = Button(Principal, text="Convertir", font=("Roboto",10), command=Convertir).grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()