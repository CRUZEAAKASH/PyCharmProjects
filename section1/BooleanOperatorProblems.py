"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it.---------------------------------
# ----------------------------------------------------------------------------------------------------------------------

print(True and True)
print(True and False)
print(True or True)
print(False or False)
print (not False)
print (not True)

"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one\below it. --------
var1 = not 3 > 1 and 5 != 2 or 6 == 6
var2 = 4 * 2 != 6 and not 7 % 6 == 1
# ----------------------------------------------------------------------------------------------------------------------

print(not 3 > 1 and 5 != 2 and 6 == 6)
print(4 * 2 != 6 and  7 % 6 == 1)