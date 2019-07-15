from tkinter import *


def function1():
    print("Item clicked")


# Declares Object of TKinter
window = Tk()

# Creating object of Inbuilt MyMenu class
myMenu = Menu(window)

# Adding MyMenu to config part
window.config(menu=myMenu)

# Adding SubMenu to the first Menu we created
subMenu1 = Menu(myMenu)

# myMenu.add_cascade(label="File")
myMenu.add_cascade(label="File", menu=subMenu1)

subMenu1.add_command(label="Project", command=function1)
subMenu1.add_command(label="Save", command=function1)

subMenu1.add_separator()

subMenu1.add_command(label="Exit", command=function1)

subMenu2 = Menu(myMenu)
myMenu.add_cascade(label="Edit",menu=subMenu2)

subMenu2.add_command(label="Edit", command=function1)
subMenu2.add_command(label="Undo",command=function1)


window.mainloop()