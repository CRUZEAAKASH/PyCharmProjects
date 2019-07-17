from pandas import Series

se1 = Series([1, 2, 3, 4, 5])
print(se1)

# Defining own Indexes
se2 = Series([100, 200, 300], index=['a', 'b', 'c'])
print(se2)

# Using pre-defined list
list1 = [1, 2, 3]
se3 = Series(list1)
print(se3)

# Using List Comprehension
list2 = [item for item in range(10)]
se4 = Series([item for item in range(10)])
print(se4)

minum = min(se4)
print(minum)