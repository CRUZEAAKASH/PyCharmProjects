from tkinter import *

window = Tk()


def function1():
    print("Clicked on it")


toolbar = Frame(window, bg="pink")
insertButton = Button(toolbar, text="click", command=function1)
insertButton.pack(side=LEFT, padx=2, pady=2)

printButton = Button(toolbar, text="print", command=function1)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=LEFT)
window.mainloop()
