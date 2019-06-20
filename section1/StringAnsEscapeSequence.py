"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
# type your code for "string and escape sequences" in between this single line comment and the one below it ------------
# ----------------------------------------------------------------------------------------------------------------------

a = "Tday is Wednesday"
b= 'Today is Thursday'
c = "Today's weather \"is\" good"
d = "Today's atmosphere \'is\' good"

print(a)
print (b)
print (c)
print(d)

"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""
# type your code for "accessing values by index and string slicing" in between this comment and the one below it-------
# ----------------------------------------------------------------------------------------------------------------------

lannisters = "JaimeCerseiTyrion"
var1 = lannisters[1:2]
var2 = lannisters[:1]
var3 = lannisters[:5]
var4 = lannisters[5:11]
var5 = lannisters[11:]

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)