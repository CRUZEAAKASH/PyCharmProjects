from tkinter import *


class MyButton:

    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.printButton = Button(frame, text="Click to print", command=self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame, text="Exit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Printing this button")


window = Tk()

b = MyButton(window)

window.mainloop()
