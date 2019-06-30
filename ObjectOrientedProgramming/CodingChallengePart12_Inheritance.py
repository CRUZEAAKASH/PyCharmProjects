class Computer:
    def __init__(self,ram, processor,memory):
        self.ram = ram
        self.processor = processor
        self.memory = memory

    def getspecs(self):
        print('Enter the Details')
        self.ram = input('Enter the RAM')
        self.processor = input('Enter Processor Speed')
        self.memory = input('Enter the Memory Size')

    def displaySpecs(self):
        print("Here are the specs of the computer")
        print(' RAM size is {} and memory size is {}'.format(self.ram, self.memory))


class Desktop(Computer):
    def __init__(self, caseColor):
        self.caseColor = caseColor

    def get_case_details(self):
        self.caseColor = input('Enter the case details')

    def disply_case_details(self):
        print('Case details of Desktop are {}'.format(self.caseColor))

class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input('Enter the weight details of laptop')

    def display_weight(self):
        print('Weght of laptop is {}'.format(self.weight))

comp = Laptop(' ')
comp.getspecs()
comp.get_weight()
comp.display_weight()
comp.displaySpecs()