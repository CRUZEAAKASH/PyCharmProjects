from tkinter import*

window = Tk()

label1 = Label(window, text="Firstname", bg="Red", fg="White")
label1.pack(fill=X)

label2 = Label(window, text="LastName", bg="Blue", fg="White")
label2.pack(side=LEFT, fill=Y)

window.mainloop()

