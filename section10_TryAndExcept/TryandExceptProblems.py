"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
 second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
 second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""

var1 = input("enter the first input")
var2 = input("Enter the seond input")

def div(a,b):
    try:
        division = int(a)/int(b)
        print(division)
    except ZeroDivisionError:
        print("Second Number should not be zero")
    except:
        print("enter integer number")

div(var1,var2)