import numpy as np
import pandas as pd

print("pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.")
print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
df1 = df.reindex(index=dates[0:4], columns=list(df1.columns))

print(df1)

s = pd.Series(np.random.randint(0, 7, size=10))

print(s)

print(s.value_counts())


print("The value_counts() Series method and top-level function computes a histogram of a 1D array of values. It can also be used as a function on regular arrays:")
data = np.random.randint(0, 7, size=50)
"""    ^
       np refers to numpy
"""
print("data")

s = pd.Series(data)
"""^^^pandas
     

     s refers to series
"""
print(s.value_counts())

"""
      pd refers to pandas
"""
print(pd.value_counts(data))
"""
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
Similarly, you can get the most frequently occurring value(s) (the mode) of the values in a Series or DataFrame:
Series
"""
s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])

print(s5.mode())
"""
Data Frame
"""
df5 = pd.DataFrame({"A": np.random.randint(0, 7, size=50),"B": np.random.randint(-10, 15, size=50)})

print(df5.mode())