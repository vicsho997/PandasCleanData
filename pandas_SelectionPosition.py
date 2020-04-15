import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

print("1.Select via the position of the passed integers:")
print(df.iloc[3])

print("2.By integer slices, acting similar to numpy/python:")
print(df.iloc[3:5, 0:2])

print("3.By lists of integer position locations, similar to the numpy/python style:Rows then Columns")
print(df.iloc[[1, 2, 4], [0, 2]])

print("4.For slicing rows explicitly:")
print(df.iloc[1:3, :])

print("5.For slicing columns explicitly:")
print(df.iloc[:, 1:3])

print("6.For getting a value explicitly:")
print(df.iloc[1, 1])


print("7.For getting fast access to a scalar (equivalent to the prior method):")
print(df.iat[1, 1])

