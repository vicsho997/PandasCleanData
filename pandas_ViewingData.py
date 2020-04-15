import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})


print("START OF VIEWING DATA!!!!!")

print("Show top or bottom rows of the frame")
print(df2.head(n=3))
print(df2.head(n=1))

print("display index columns")
print(df2.index)
print(df2.columns)
"""
DataFrame.to_numpy() gives a NumPy representation of the underlying data. 
Note that this can be an expensive operation when your DataFrame has columns
with different data types, which comes down to a fundamental difference between 
pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas 
DataFrames have one dtype per column. When you call DataFrame.to_numpy(), pandas 
will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This 
may end up being object, which requires casting every value to a Python object.

For df2, the DataFrame with multiple dtypes, DataFrame.to_numpy() is relatively expensive.
"""
print(df2.to_numpy())


"""
this is not sorting the df2 ex your using directly above
"""
print("describe() shows a quick statistic summary of your data:")
print(df.describe())

print("Transposing your data:")
print(df.T)

print("Sorting by an axis")
print(df.sort_index(axis=1, ascending=False))

print("Sorting by values")
print(df.sort_values(by='B'))