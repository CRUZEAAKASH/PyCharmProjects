"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

def function1():
    print("printing Method 1")

var1 = 5

def function2(a):
    print(a)
    function1()

function2(var1)


"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

var1 = 10
var2 = 20
var3 = 30

def function3(a,b):
    print(abs(a-b))

def function4(a,b,c):
    print(a * b * c)

function3(var1,var2)

function4(var1,var2,var3)



"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

flt1 = 10.0
flt2 = 20.0
flt3 = 30.0

def function5(a,b):
    return a/b

def function6(a,b,c):
    return((function5(a,b))/c)
flat4 = function5(flt1,flt2)
print(flat4)

print(function6(flt2,flt1,flt3))