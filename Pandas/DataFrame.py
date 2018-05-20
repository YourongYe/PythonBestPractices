import pandas as pd
import numpy as np
from pandas import Series,DataFrame

############################ index ##################################
# 1. set_index
df = DataFrame()
data.set_index('column_name') # specify a column to be index
data.index = range(0,len(data)) # note that range(a,b) means a <= x & x < b.
data.
