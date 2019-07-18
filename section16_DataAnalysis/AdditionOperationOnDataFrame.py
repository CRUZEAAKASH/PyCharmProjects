from pandas import DataFrame

data1 = {'Name': ['John', 'Tom', 'Rob'],
         'Age': [10, 20, 30],
         'Salary': [2500, 3500, 4500]}
frame1 = DataFrame(data1)

data2 = {'Name': ['John', 'Tom', 'Tin'],
         'Sex': ['F', 'F', 'F'],
         'Salary': [2500, 4000, 5000]
         }
frame2 = DataFrame(data2)
frame3 = frame1 + frame2

print(frame3)
