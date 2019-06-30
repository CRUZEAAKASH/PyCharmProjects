class students:
    company = "amdocs"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getData(self):
        print("My name is {} and my age is {}".format(self.name,self.age))

    def setData(self):
        print("Accepting Data")
        self.name = input("Enter Name")
        self.age = input("Enter Age")

John = students("blank", 0)
John.setData()
John.getData()

