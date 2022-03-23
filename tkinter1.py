from tkinter import *
from tkinter import ttk
from turtle import width

from numpy import var

def calculate(*args):
    try:
        value = float(pie.get())
        metros.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def validaCheck(*args):
    try:
        print(opcion.get())
        print('Opcion 1',seleccion.get())
        print('Opcion 2',seleccion2.get())
        print('Opcion 3',seleccion3.get())
        
    except ValueError:
        pass

root = Tk()
root.title("Conversión de Metros a Pies")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#estilo frame
styleF = ttk.Style()
styleF.configure('cc.TFrame',background = 'blue', borderwith = 5, relief='sunken')

frameR = ttk.Frame(mainframe)
frameR.grid(column=1,row=4)
frameR['borderwidth'] = 10
frameR['relief'] = 'raised' # 'solid', 'sunken','flat', 'ridge', 'groove', 'ridge'
frameR['width']= 200
frameR['height'] = 50
frameR['style']= 'cc.TFrame'

frameO = ttk.Frame(mainframe,width=200,height= 50,relief='groove',style='cc.TFrame').grid(column=2, row=4)

#Checkbox

seleccion = StringVar()
seleccion2 = StringVar() 
seleccion3 = StringVar()
opcion = StringVar()
checkBox = ttk.Checkbutton(frameR, text='Opcion 1', command=validaCheck, variable= seleccion, onvalue= 'opc1',offvalue='NO').grid(column=1,row=1)
checkBox2 = ttk.Checkbutton(frameR, text='Opcion 2', command=validaCheck, variable= seleccion2, onvalue= 'opc2',offvalue='NO').grid(column=1,row=2)
checkBox3 = ttk.Checkbutton(frameR, text='Opcion 3', command=validaCheck, variable= seleccion3, onvalue= 'opc3',offvalue='NO').grid(column=1,row=3)

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