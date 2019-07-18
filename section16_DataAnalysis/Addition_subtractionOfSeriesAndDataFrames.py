from pandas import DataFrame
from pandas import Series

data = {'Name': [123, 456, 789],
        'Age': [10, 20, 30],
        'Salary': [2500, 3500, 4500]}
frame = DataFrame(data)
print(frame)

series = Series([100, 200], index=['Age', 'Salary'])
print(series)

print(frame - series)
