from tkinter import *
from tkinter import ttk
from turtle import width

def calculate(*args):
    try:
        value = float(pie.get())
        metros.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Conversión de Metros a Pies")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#estilo frame
styleF = ttk.Style()
styleF.configure('CuadroControl',background = 'blue', borderwith = 5, relief='sunken')
frameR = ttk.Frame(mainframe)
frameR.grid(column=1,row=4)
frameR['borderwidth'] = 3
frameR['relief'] = 'solid'

frameR['width']= 200
frameR['height'] = 50
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

pie = StringVar()
pieEntrada = ttk.Entry(mainframe, width=7, textvariable=pie)
pieEntrada.grid(column=2, row=1, sticky=(W, E))

metros = StringVar()
ttk.Label(mainframe, textvariable=metros).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Convertir ...", command=calculate).grid(column=2, row=3, sticky=W)

ttk.Label(mainframe, text="Pies").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="su conversión a metros es: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

pieEntrada.focus()
root.bind("<Return>", calculate)

root.mainloop()