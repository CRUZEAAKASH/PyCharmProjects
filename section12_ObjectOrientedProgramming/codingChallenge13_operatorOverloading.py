class Number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return  x

    def __add__(self, other):
        x = self.x * other.x
        return x

number_a = Number(3)
number_b = Number(4)

print(number_a * number_b)
print(number_a + number_b)