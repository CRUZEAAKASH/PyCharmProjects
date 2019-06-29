#method1 using loop mechanism to show the genraror technique

def funct():
    counter = 0
    while counter < 5:
        yield counter
        counter +=1
for x in funct():
    print(x, end = " ")

print()
#method 2 to show the list
def even(x):
    for i in range(x):
        if i%2==0:
            yield i
newList = list(even(21))
print(newList)