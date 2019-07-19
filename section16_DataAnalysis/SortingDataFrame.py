from pandas import DataFrame

data = {'Name': ['John', 'Tom', 'Rob'],
        'Age': [10, 20, 30],
        'Salary': [2500, 35000, 4500]}

frame = DataFrame(data)
frame = frame.reindex([2, 0, 1])
print(frame)

# sorting on the basis of row in ascending order
frame2 = frame.sort_index()
print(frame2)

# Sorting on the basis of Columns
frame3 = frame.sort_index(axis=1)
print(frame3)

# Sorting rows on the basis of Values column wise
frame4 = frame.sort_values(['Salary'])
print(frame4)

# Sorting on the basis of values column wise descending
frame5 = frame.sort_values(['Salary'], ascending=False, ind)
print(frame5)
