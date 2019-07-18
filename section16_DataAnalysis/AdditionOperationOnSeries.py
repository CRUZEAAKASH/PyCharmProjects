from pandas import Series

# for equal values
series1 = Series([100, 200, 300, 400, 500])
series2 = Series([1, 2, 3, 4, 5])

series3 = series1 + series2

print(series3)

# for unequal values

series1 = Series([100, 200, 300, 400, 500])
series2 = Series([1, 2, 3, 4, 5, 6, 7])

series3 = series1 + series2

print(series3)
