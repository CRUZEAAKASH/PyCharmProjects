from tkinter import *

window = Tk()

label1 = Label(window, text = "FirstName")
label2 = Label(window, text = "LastName")

entry1 = Entry(window)
entry2 = Entry(window)

button1 = Button(window, text = "Cick Here!!!!", fg="Red")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button1.grid(row=2, column=1)

window.mainloop()