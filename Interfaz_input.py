from tkinter import *
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(True, True)
root.title('Suma')

def sumar():
    primero=int(caja1.get())
    segundo=int(caja2.get())
    resultado=(primero+segundo)
    return variable1.set(resultado)

variable1=StringVar()
etiqueta1=Label(root, text="Programa que suma 2 numeros") #etiqueta de texto
etiqueta3=Label(root, text="Ingrese primer valor") #etiqueta de texto
etiqueta4=Label(root, text="Ingrese segundo valor") #etiqueta de texto
caja1=Entry(root, text="primer número")  
caja2=Entry(root, text="segundo número")
caja3=Entry(root,textvariable=variable1)

#download_icon = tk.PhotoImage(file='./calculo.png')
boton_sumar = ttk.Button(root, text='Sumar',compound=tk.LEFT, command=sumar)

etiqueta1.pack()
etiqueta3.pack()
caja1.pack()
etiqueta4.pack()
caja2.pack()
boton_sumar.pack(ipadx=25,ipady=5,expand=FALSE)
caja3.pack()
root.mainloop()