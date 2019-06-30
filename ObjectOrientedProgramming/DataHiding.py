class MyClass:

    #Hiding the class variable
    __superHidden  = 7
    _semiHidden = 4

    def add(self, increment):
        self.__superHidden+= increment
        print(self.__superHidden)

mc = MyClass()

mc.add(5)
print(mc._semiHidden)
print(mc.__superHidden)
