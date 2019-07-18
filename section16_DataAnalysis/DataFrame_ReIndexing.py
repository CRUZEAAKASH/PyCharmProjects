from pandas import DataFrame

data = {'Name': ['John', 'Tom', 'Rob'],
        'Age': [10, 20, 30],
        'Salary': [2500, 3500, 4500]}

frame = DataFrame(data)
print(frame)

# reindex rows
frame = frame.reindex([2, 1, 0])
print(frame)

# reindex columns
frame = frame.reindex(columns=['Salary', 'Name', 'Age'])
print(frame)
