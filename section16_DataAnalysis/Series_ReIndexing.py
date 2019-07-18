from pandas import Series

series = Series([100, 200, 300, 400, 500], index = ['c', 'b', 'a', 'd', 'e'])
print(series)

series = series.reindex(['a','b', 'c', 'd', 'e'])
print(series)
