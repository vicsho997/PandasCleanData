import numpy as np
import pandas as pd

print("pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.")
print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
df1 = df.reindex(index=dates[0:4], columns=list(df1.columns))

print(df1)


"""Function application To apply your own or another library’s functions to pandas objects, you should be aware of the three methods below. The appropriate method to use depends on whether your function expects to operate on an entire DataFrame or Series, row- or column-wise, or elementwise. Tablewise Function Application: pipe() Row or Column-wise Function Application: apply() Aggregation API: agg() and transform() Applying Elementwise Functions: applymap() !!!!!https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-discretization"""


print("    ")
print(df1.apply(np.cumsum))

print(df.apply(lambda x: x.max() - x.min()))