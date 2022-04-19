from tkinter import *

root = Tk()

for r in range(0, 5):
    for c in range(0, 5):
        cell = Entry(root, width=10)
        cell.grid(padx= 5, pady =5, row=r, column=c)
        cell.insert(0, '({}, {})'.format(r, c))
Label(root, text="Nombre:").grid(pady=5, row=0, column=0)
Label(root, text="Apellido:").grid( pady=5, row=1, column=0)

Entry(root, width=40).grid(padx=5, row=0, column=1)
Entry(root, width=40).grid(padx=5, row=1, column=1)

Button(root, text="Aceptar", width=50).grid(padx=10, pady=10, row=2, column=0, columnspan=2)


root.mainloop()