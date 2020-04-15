import numpy as np
import pandas as pd

print("pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.")
print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
df1 = df.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)


print("1.)performing a desciptive statistic")
print(df1.mean())

print("2.)same operation on the other axis")
print(df1.mean(1))

print("3.)Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension.")
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)

print(df.sub(s, axis='index'))