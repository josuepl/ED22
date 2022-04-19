from tkinter import *

from pyparsing import col
  
root = Tk() 
  
  
def hide_button(widget):    
    widget.grid_remove()
  
def show_button(widget):
    widget.grid(row=0,column=0)  
    #widget.pack() 
  
B1 = Button(root, text="Button 1") 
B1.grid(column=0, row=0) 

  
B2 = Button(root, text="Ocultar", command=lambda: hide_button(B1)) 
B2.grid(row=0,column=1) 
  
B3 = Button(root, text="Mostrar", command=lambda: show_button(B1)) 
B3.grid(row=0,column=2)
  
root.mainloop() 