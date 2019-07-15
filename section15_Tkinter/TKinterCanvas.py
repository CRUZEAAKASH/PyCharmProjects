from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=100)
canvas.pack()
lin1 = canvas.create_line(0, 0, 50, 100)
line2 = canvas.create_line(10, 90, 20, 0)

window.mainloop()
