import numpy as np
import pandas as pd
"""
Continuous values can be discretized using the cut() 
(bins based on values) and qcut() (bins based on sample quantiles)
 functions:
"""
arr = np.random.randn(20)
factor = pd.cut(arr, 4)
print(factor)
print(" ")
factor1 = pd.cut(arr, [-5, -1, 0, 1, 5])
print(factor1)

"""
qcut() computes sample quantiles. For example, we could slice up some
 normally distributed data into equal-size quartiles like so:
"""
print(" ")
arr = np.random.randn(30)
factor2 = pd.qcut(arr, [0, .25, .5, .75, 1])
print(factor2)
print(" ")
print(pd.value_counts(factor2))
print(" ")
"""
We can also pass infinite values to define the bins:
"""
arr = np.random.randn(20)
factor4 = pd.cut(arr, [-np.inf, 0, np.inf])

print(factor4)

