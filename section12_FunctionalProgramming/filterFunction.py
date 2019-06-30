#using function methodology to see the filter functionality
def oddNum(x):
    if x%2!=0:
        return x
newList = [1,2,3,4,5,6,7,8,9,10]
results = list(filter(oddNum, newList))
print(results)

#using lambda functionality to see the filter functionality
#results = list(filter(lambda x : x%2==0, newList))

results = list(filter(lambda x: x%2==0, newList))
print(results)

