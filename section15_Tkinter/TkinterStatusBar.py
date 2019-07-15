from tkinter import *

window = Tk()

status = Label(window, text="this is status bar", anchor=W, bd=1,relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

window.mainloop()
