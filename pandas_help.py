import numpy as np
import pandas as pd

print("OBJECT CREATION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("Creating a Series by passing a list of values, letting pandas create a default integer index:")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print (s)


print ("Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns")

dates = pd.date_range('20130101', periods=6)
print (dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print (df)


print ("Creating a DataFrame by passing a dict of objects that can be converted to series-like.")

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})
print (df2)
print (df2.dtypes)


print("The columns of the resulting DataFrame have different dtypes.")
"""
df2.dtypes
If you’re using IPython, tab completion for column names (as well as public attributes) is automatically enabled. 
Here’s a subset of the attributes that will be completed:
In [12]: df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.consolidate
df2.applymap
df2.D
"""


