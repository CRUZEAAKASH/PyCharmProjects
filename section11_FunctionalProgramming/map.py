# using map functionality with the help of method

def add(x):
    return x+2
newlist = [10,20,30,40,50]
output = list(map(add,newlist))
print(output)

#now we will use the map functionality using lamba

newlist = [1,2,3,4,5]
output = list(map(lambda x : x*2, newlist))
print(output)