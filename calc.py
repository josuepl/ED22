from tkinter import *
from tkinter import ttk
from turtle import heading

from pyparsing import col

root = Tk()
root.title("Calculadora básica")
root.geometry("300x400")
styleF = ttk.Style()
styleF.configure('principal.TFrame',background = '#0059b3', borderwith = 5, relief='sunken')
marcoPrincipal = ttk.Frame(root,style="principal.TFrame",width=300, height=400).grid(column=0 , row=0,sticky=(N,W,E,S),padx=(5,5), pady=(2,2)) # N Norte - Superior, W - West - Oeste - Izquierdo
root.columnconfigure(0, weight=1)                                                                                       # E Este - Derecho, S - Sur - Inferior
root.rowconfigure(0, weight=1)


entradaTxt = StringVar()
entrada = ttk.Entry(marcoPrincipal, textvariable=entradaTxt,width=20).grid(column=0, row= 0,sticky=(N,E,W),padx=(6,6), pady=(2,2))

root.mainloop()