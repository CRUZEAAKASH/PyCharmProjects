from pandas import DataFrame

data = {'Name': ['John', 'Tom', 'Rob'],
        'Age': [10, 20, 30],
        'Salary': [2500, 3500, 4500]}

frame = DataFrame(data)
print(frame)

# Adding same values
frame['Profile'] = 'Doctor'
print(frame)

# Adding different values
list1 = ['Mumbai', 'Pune', 'Bangalore']

frame['City'] = list1
print(frame)

frame2 = frame.drop('Age', axis=1)
print(frame2)

frame3 = frame.drop([1])
print(frame3)
