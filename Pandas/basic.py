import pandas as pd #A library often used for data analysis
import numpy as np #A library for operation rules
from pandas import Series, DataFrame #two different data structure

#####################################################################
# 1. Create a series

s1 = pd.Series([20,30,40,50]) # assume index is 0,1,2,3...
print(s1)
s2 = pd.Series(data=[20,30,40,50],index=[2001,2002,2003,2004]) # can omit "data="
print(s2)
s3 = pd.Series({"Amy":23,"Candy":33,"Yara":40}) # create a series using list
print(s3)
s4 = pd.Series(range(4),index=list("abcd"))
print(s4)

#####################################################################
# 2. Creat a dataframe

d1 = pd.DataFrame(np.arange(9).reshape((3, 3)),index=["Amy","Candy","Yara"],columns=["Weight","Height","Age"])
print(d1) # note that there are two "()" for reshape

df = DataFrame(np.random.rand(16).reshape(4,4))
print(df)

d2 = pd.DataFrame({"Weight":[70,80,90],"Height":[150,160,170],"Age":[20,30,40]},index=["Amy","Candy","Yara"])
print(d2)

# 生成一个空的df，规定index和columns
d1 = pd.DataFrame(index=stock_list, columns=time_list) # stock_list & time_list 必须是list，或者是另一个dataframe的index/columns也可

# 以列填充df
d1['column_name'] = d2 # 此处会根据index自动进行对应，无法对应的地方会生成nan
d1['column_name'] = l1 # 此处list的长度必须和d1相同，否则会报错
d1['column_name'] = s1 # 此处也会根据index自动对应，同第一种情况

#####################################################################
# 3. Check info of your data

print("data info is "+str(d2.info()))
print("describe: "+str(d2.describe()))

print("data shape: "+str(d2.shape))
print(d2.head(2))
print("data index: "+str(d2.index))
print("column: "+str(d2.columns))

#####################################################################
# 4. Reindex (reindex是暂时性的，如果不存在新的容器里，原来的dataframe不会被改变)


StudentList = ["Amy","Bob","Candy","Yara"]
d3 = d2.reindex(index=StudentList)
print(d3)

d4 = d2.reindex(index=StudentList,method="ffill") #"ffill"means fill nan as forward column/row
print(d4)

d5 = d2.reindex(index=StudentList,method="bfill") #"bfill"means fill nan as back column/row
print(d5)

d6 = d2.reindex(columns=["Height","Weight1","Weight","Age"])
print(d6)

d6 = d2.reindex(columns=["Height","Weight1","Weight","Age"], method="ffill")
print(d6)
