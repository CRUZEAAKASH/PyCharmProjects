from tkinter import *

window = Tk()

window.title("GUIIIIIIIIIIIIIII")

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack(side=BOTTOM)

button1 = Button(frame1, text = "Click Here", fg = "Red")
button2 = Button(frame2, text = "Click Here", fg = "Blue")

button1.pack()
button2.pack()


window.mainloop()