from tkinter import *
from tkinter import ttk
from turtle import heading

from pyparsing import col

def operandos(* args):

    pass

root = Tk()
root.title("Calculadora básica")
root.geometry("300x400")
root.resizable(width=False, height=False)
styleF = ttk.Style()
styleF.configure('principal.TFrame',background = '#0059b3', borderwith = 5, relief='sunken')
marcoPrincipal = ttk.Frame(root,style="principal.TFrame",width=300, height=400).grid(column=0 , row=0,sticky=(N,W,E,S),padx=(5,5), pady=(2,2)) # N Norte - Superior, W - West - Oeste - Izquierdo
root.columnconfigure(0, weight=1)                                                                                       # E Este - Derecho, S - Sur - Inferior
root.rowconfigure(0, weight=1)
# Caja de entrada
entradaTxt = StringVar()
entrada = ttk.Entry(root, textvariable=entradaTxt,width=20).grid(column=0, row= 0,sticky=(N,E,W),padx=(6,6), pady=(2,2))

#Lista de Botones

btn0 = ttk.Button(marcoPrincipal,command=operandos,width=2,).grid(column = 1,row = 1)
btn1 = ttk.Button(marcoPrincipal,command=operandos,width=2,).grid(column = 2,row = 1)
btn2 = ttk.Button(marcoPrincipal,command=operandos,width=2,).grid(column = 3,row = 1)
btn3 = ttk.Button(marcoPrincipal,command=operandos,width=2,).grid(column = 1,row = 2)
btn4 = ttk.Button(marcoPrincipal,command=operandos,width=2,).grid(column = 2,row = 2)
root.mainloop()