from pandas import Series

series = Series([4400, 200, 3300, 400, 500], index=[3, 5, 2, 4, 1])
print(series)

# sort by indexes
series = series.sort_index()
print(series)

# sort by values ascending
series = series.sort_values()
print(series)

# sort by values descending
series = series.sort_values(ascending=False)
print(series)
