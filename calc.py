from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from turtle import heading

from pyparsing import col

def operandos(* args):
    try:
        operando = args
        print(operando)
        #value = float(operando)
        print("value: ",args)
    except ValueError:
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
marcoPrincipal.grid(column=0 , row=1,sticky=(N,W,E,S),padx=(5,5), pady=(2,2)) # N Norte - Superior, W - West - Oeste - Izquierdo
marcoEntrada = ttk.Frame(root,height=20,style="principal.TFrame")
marcoEntrada.grid(column=0,row=0,sticky=(N,E,W,S),padx=(5,5), pady=(2,2))

# Caja de entrada
entradaTxt = StringVar()
entrada = ttk.Entry(marcoEntrada, textvariable=entradaTxt,width=20).grid(column=0, row= 0,sticky=(N,E,W),padx=(6,6), pady=(2,2))

#Lista de Botones

valor = StringVar()
valor = "0123456789"
btn7 = ttk.Button(marcoPrincipal,command=lambda: operandos("7"),text=valor[7], width=10,).grid(column = 1,row = 3,sticky=(W))
btn8 = ttk.Button(marcoPrincipal,command=lambda: operandos("8"),text='8',width=10).grid(column = 2,row = 3,sticky=(W))
btn9 = ttk.Button(marcoPrincipal,command=lambda: operandos("9"),text='9',width=10).grid(column = 3,row = 3,sticky=(W))
btn4 = ttk.Button(marcoPrincipal,command=lambda: operandos("4"),text='4',width=10).grid(column = 1,row = 4,sticky=(W))
btn5 = ttk.Button(marcoPrincipal,command=lambda: operandos("5"),text='5',width=10).grid(column = 2,row = 4,sticky=(W))
btn6 = ttk.Button(marcoPrincipal,command=lambda: operandos("6"),text='6',width=10).grid(column = 3,row = 4,sticky=(W))
btn1 = ttk.Button(marcoPrincipal,command=lambda: operandos("1"),text='1',width=10).grid(column = 1,row = 5,sticky=(W))
btn2 = ttk.Button(marcoPrincipal,command=lambda: operandos("2"),text='2',width=10).grid(column = 2,row = 5,sticky=(W))
btn3 = ttk.Button(marcoPrincipal,command=lambda: operandos("3"),text='3',width=10).grid(column = 3,row = 5,sticky=(W))
btn0 = ttk.Button(marcoPrincipal,command=lambda: operandos("0"),text='0',width=10).grid(column = 2,row = 6,sticky=(W))
root.mainloop()