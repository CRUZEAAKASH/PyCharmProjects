class Students:
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

class scienceStudents(Students):
    def __init__(self,college):
        self.college = college
        print("Printing within the Init method of scienece student {}".format(self.college))

    def science(self):
        print("I am a sience student")

John = scienceStudents("KNIT")
John.science()
John.setData()
John.getData()

