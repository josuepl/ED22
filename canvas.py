from tkinter import *

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)

mainloop()