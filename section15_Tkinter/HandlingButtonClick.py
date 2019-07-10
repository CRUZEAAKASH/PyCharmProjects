from tkinter import *

window = Tk()

counter = 0


def dosomething():
    print("You clicked on it")
    button1 = Button(window, text="You clicked on it....Yeahhhhhhh")
    button1.grid(row=0, column=1)


button = Button(window, text="Click Here!!!!!!!!!!!!!", command=dosomething)
button.grid(row=0, column=0)
window.mainloop()
