from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from turtle import heading

from pyparsing import col

variables =[]
operacion= ""
def operandos(* args):
    textIn = args[0]
    print("args: ", args)
    numeros = [';','1','2','3','4','5','6','7','8','9','0']
    operaciones = [';','+','=','-','*','/']
    try:
        if numeros.index(textIn):
            var1 = entradaTxt.get()+textIn
            print("var1: ",var1)
            entradaTxt.set(var1)
    except ValueError:
        pass

        if operaciones.index(textIn):
            print("es una operacion")
            try:
                operacion = args[0]
                value = float(entradaTxt.get())
                print("operacion: ",operacion, "valor(float): ",value)
                variables.append(value)
                print(variables)
                entradaTxt.set("")
            except ValueError:
                pass
                if operacion == '+':
                    print("SUMA")

                    bandera = True
                if operacion == '=' :
                    print("RESULTADO")
                    print("valor 1: ", variables[0],'valor 2: ',variables[1])

                    resultado = variables[0]+ variables[1]
                    print(resultado)


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
# Numeros

btn7 = ttk.Button(marcoPrincipal,command=lambda: operandos("7",variables),text=valor[7], width=10,).grid(column = 1,row = 3,sticky=(W))
btn8 = ttk.Button(marcoPrincipal,command=lambda: operandos("8"),text='8',width=10).grid(column = 2,row = 3,sticky=(W))
btn9 = ttk.Button(marcoPrincipal,command=lambda: operandos("9"),text='9',width=10).grid(column = 3,row = 3,sticky=(W))
btn4 = ttk.Button(marcoPrincipal,command=lambda: operandos("4"),text='4',width=10).grid(column = 1,row = 4,sticky=(W))
btn5 = ttk.Button(marcoPrincipal,command=lambda: operandos("5"),text='5',width=10).grid(column = 2,row = 4,sticky=(W))
btn6 = ttk.Button(marcoPrincipal,command=lambda: operandos("6"),text='6',width=10).grid(column = 3,row = 4,sticky=(W))
btn1 = ttk.Button(marcoPrincipal,command=lambda: operandos("1"),text='1',width=10).grid(column = 1,row = 5,sticky=(W))
btn2 = ttk.Button(marcoPrincipal,command=lambda: operandos("2"),text='2',width=10).grid(column = 2,row = 5,sticky=(W))
btn3 = ttk.Button(marcoPrincipal,command=lambda: operandos("3"),text='3',width=10).grid(column = 3,row = 5,sticky=(W))
btn0 = ttk.Button(marcoPrincipal,command=lambda: operandos("0"),text='0',width=10).grid(column = 2,row = 6,sticky=(W))
#Operaciones
btnSum = ttk.Button(marcoPrincipal,command=lambda: operandos("+"),text='+', width=10,).grid(column = 4,row = 3,sticky=(W))
btnSum = ttk.Button(marcoPrincipal,command=lambda: operandos("="),text='=', width=10,).grid(column = 4,row = 4,sticky=(W))

root.mainloop()