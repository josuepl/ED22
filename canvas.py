from tkinter import *

from matplotlib.pyplot import fill

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

# Se crean dos lineas dentro del lienzo
#1er Linea ptInicial(10,10) ptFinal(80,80)
canvas.create_line(10, 10, 10, 70,fill='#FF0000',width=4)
#2a Liena ptInicial(10,80) ptFinal(80,10)
canvas.create_line(20, 10, 20, 70, fill='#00FF00', width=7)

# Ovalos - Circulos
canvas.create_oval(30,10,50,30,width=3, fill='#ff00ff' ,outline='#151590')
canvas.create_oval(60,10,100,30,width=3, fill='#00ffff' ,outline='#151590')
canvas.create_oval(90,10,150,130,width=3, fill='#888800' ,outline='#151590')

#Rectangulos - Cuadros
canvas.create_rectangle(30,10,50,30,width=1 ,outline='#151590')
canvas.create_rectangle(60,10,100,30,width=1, outline='#151590')
canvas.create_rectangle(90,10,150,130,width=1, outline='#151590')

#Arcos
canvas.create_arc( 160, 10, 200,40, fill='#007070')
canvas.create_arc( 200, 70, 160,30, fill='#007070')

#Textos
canvas.create_text(200,200,fill='#000000' , text="Dibujos en Canvas de TKinter",width=100)

#Imagenes

imagen = PhotoImage(file=r"C:\Users\usuario\Documents\GitHub\ED22\img.png",format='PNG')
canvas.create_image(0,200, image = imagen, anchor=NW)
mainloop()