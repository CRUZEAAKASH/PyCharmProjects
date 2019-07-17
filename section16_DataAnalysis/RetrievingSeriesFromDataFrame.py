from pandas import DataFrame

data = {'Name': ['John', 'Tom', 'Rob'],
        'Age': [10, 20, 30],
        'Salary': [2500, 3500, 4500]}

frame = DataFrame(data)

# Printing Single Colum
print(frame['Salary'])

# Printing Single Column but in dataFrame style
print(frame[['Salary']])

# Printing Multiple Column
print(frame[['Salary', 'Name']])

# printing single row
print(frame.loc[0])

# printing single row in dataframe style
print(frame.loc[[0]])

# Printing Multiple ROws
print(frame.loc[[0, 1]])

# Printing top 2 records only
print(frame.head(3))
