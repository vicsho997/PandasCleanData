import numpy as np
import pandas as pd

"""
print("pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.")
print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
df1 = df.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)

print("To drop any rows that have missing data.")
df1.dropna(thresh=1)
print(df1)
"""

df3 = {
    'Name':['George','Andrea','micheal','maggie','Ravi','Xien','Jalpa',np.nan],
    'State':['Arizona','Georgia','Newyork','Indiana','Florida','California',np.nan,np.nan],
    'Gender':["M","F","M","F","M","M",np.nan,np.nan],      
    'Score':[63,48,56,75,np.nan,77,np.nan,np.nan]
     
   }
 
df3 = pd.DataFrame(df3,columns=['Name','State','Gender','Score'])

print("1.)for any missing values")
print(df3.dropna(how='any'))

print("2.)Drop the rows even with single NaN or single missing values.")
print(df3.dropna())

print("3.)Drop the rows if that row has more than 2  NaN (missing) values")
print(df3.dropna(thresh=2))

print("4.)Drop rows with NaN in a specific column . here we are removing Missing values in Gender column")
print(df3.dropna(subset=['Score']))

print("5.)Filling missing data.")
print(df3.fillna(value=5))

print("6.)To get the boolean mask where values are nan.")
print(pd.isna(df3))