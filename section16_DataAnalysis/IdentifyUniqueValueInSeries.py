from pandas import Series

series = Series([100, 200, 300, 400, 500], index=[1, 1, 2, 2, 3])
print(series)

print(series.index.is_unique)