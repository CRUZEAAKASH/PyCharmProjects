# Example1: Using the simple class method to unserstand the concept

class Parrot:
    #class attributes
    species = "bird"

    #instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

#Instantiate the Parrot class
blu = Parrot("blu", 10)
woo = Parrot("woo", 15)

#Access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

#Access the instance attriutes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name, woo.age))

