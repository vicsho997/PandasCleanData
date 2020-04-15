import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

print("1.Using a single column’s values to select data.")
print(df[df['A'] > 0])

print("2.Selecting values from a DataFrame where a boolean condition is met.")
print(df[df > 0])

print("!!!!!Using the isin() method for filtering:")
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

print(df2[df2['E'].isin(['two', 'four'])])
