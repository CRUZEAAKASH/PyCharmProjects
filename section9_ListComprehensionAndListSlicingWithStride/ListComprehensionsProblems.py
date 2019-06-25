"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""

expression1 = [num for num in range(8,-1,-2)]
print(expression1)

expression2 = [num**num for num in range(1,5)]
print(expression2)

expression3 = [num*(num+2) for num in range(4,7)]
print(expression3)

expression4 = [num for num in range(2,10) if num!=5 and num!=6]
print(expression4)

expression5 = [num for num in range(10,0,-1) if num>7 or num<4]
print(expression5)