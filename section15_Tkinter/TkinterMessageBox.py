from tkinter import Tk
from tkinter import messagebox

window = Tk()
messagebox.showinfo("title", "You are seeing message box")

response = messagebox.askquestion("Question 1", "Do you love Coffee?")
if (response == 'yes'):
    print("Here are your coffee loverrr!!!!!!!!!!!!!!!!!")
else:
    print("What do you love???")
window.mainloop()
