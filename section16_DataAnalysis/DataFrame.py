from pandas import DataFrame

data = {'Name': ['John', 'Tom', 'Rob'],
        'Age': [10, 20, 30],
        'Salary': [2500, 3500, 4500]}

frame = DataFrame(data)

print(frame)
