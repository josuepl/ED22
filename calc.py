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
root.columnconfigure(0, weight=1)                                                                                       # E Este - Derecho, S - Sur - Inferior
root.rowconfigure(0, weight=1)
styleF = ttk.Style()
styleF.configure('principal.TFrame',background = '#0059b3', borderwith = 5, relief='sunken')
marcoPrincipal = ttk.Frame(root,style="principal.TFrame",width=300, height=400)
marcoPrincipal.grid(column=0 , row=1,sticky=(N,W,E),padx=(5,5), pady=(2,2)) # N Norte - Superior, W - West - Oeste - Izquierdo
marcoEntrada = ttk.Frame(root,height=20,style="principal.TFrame")
marcoEntrada.grid(column=0,row=0,sticky=(N,E,W,S),padx=(5,5), pady=(2,2))

# Caja de entrada
entradaTxt = StringVar()
entrada = ttk.Entry(marcoEntrada, textvariable=entradaTxt,width=20).grid(column=0, row= 0,sticky=(N,E,W),padx=(6,6), pady=(2,2))

#Lista de Botones

btn7 = ttk.Button(marcoPrincipal,command=operandos,text='7',width=2,).grid(column = 1,row = 3,sticky=(W))
btn8 = ttk.Button(marcoPrincipal,command=operandos,text='8',width=2,).grid(column = 2,row = 3,sticky=(W))
btn9 = ttk.Button(marcoPrincipal,command=operandos,text='9',width=2,).grid(column = 3,row = 3,sticky=(W))
btn4 = ttk.Button(marcoPrincipal,command=operandos,text='4',width=2,).grid(column = 1,row = 4,sticky=(W))
btn5 = ttk.Button(marcoPrincipal,command=operandos,text='5',width=2,).grid(column = 2,row = 4,sticky=(W))
btn6 = ttk.Button(marcoPrincipal,command=operandos,text='6',width=2,).grid(column = 3,row = 4,sticky=(W))
btn1 = ttk.Button(marcoPrincipal,command=operandos,text='1',width=2,).grid(column = 1,row = 5,sticky=(W))
btn2 = ttk.Button(marcoPrincipal,command=operandos,text='2',width=2,).grid(column = 2,row = 5,sticky=(W))
btn3 = ttk.Button(marcoPrincipal,command=operandos,text='3',width=2,).grid(column = 3,row = 5,sticky=(W))
btn0 = ttk.Button(marcoPrincipal,command=operandos,text='0',width=2,).grid(column = 2,row = 6,sticky=(W))
root.mainloop()