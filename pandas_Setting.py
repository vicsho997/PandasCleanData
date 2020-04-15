import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'),'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})


print("1.Setting a new column automatically aligns the data by the indexes.")


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
s1
df['F'] = s1

print(s1)
print(df)

print("2.Setting values by label:")
df.at[dates[0], 'A'] = 0

print("3.Setting values by position:")
df.iat[0, 1] = 0


print("4.Setting by assigning with a NumPy array:")
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)

print("A where operation with setting.")
df2 = df.copy()
df2[df2 > 0] = -df2

print(df2)