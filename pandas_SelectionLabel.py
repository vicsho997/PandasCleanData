import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

print("1.For getting a cross section using a label:")
print(df.loc[dates[0]])

print("2.Selecting on a multi-axis by label:")
print(df.loc[:, ['A', 'B']])

print("3.Showing label slicing, both endpoints are included:")
print(df.loc['20130102':'20130104', ['A', 'B']])

print("4.Reduction in the dimensions of the returned object:")
print(df.loc['20130102', ['A', 'B']])

print("5.For getting a scalar value:")
print(df.loc[dates[0], 'A'])

print("6.For getting fast access to a scalar (equivalent to the prior method):")
print(df.at[dates[0], 'A'])
