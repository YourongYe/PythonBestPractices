1. check basic info about the dataframe
#查看每一列的类型
data.info()
#查看前三行
df.head(3)
#输出行索引  
print(data.index)
#输出列索引  
print(data.columns)
#输出DataFrame详细信息  
print(data.describe())

#############################################################################################
2. deal with the columns in dataframe
#改columns的顺序（也可以用来添加columns）
data.reindex_axis((timelist),axis=1)
data.reindex_axis(("1","2"),axis=1)
# reindex改columns的顺序
list = ['Inst_holding','Inst_num','PE_Actual','EPS_exp','EPS_actual']
result = result.reindex(columns=list)
# 去掉某一列或某几列的几种方法
1. del PanelData1['Mkt_cap']
2. PanelData1.drop('Inst_num',1)
3. PanelData1.drop('Inst_num',axis=1,inplace=True) # 默认inplace=False，表示原数组不会被替换
#重命名columns
data = data.rename(columns={"0": "StockNo."})
# 把某一列作为index，覆盖掉原来的自动索引Rangeindex
data.set_index('StockNo.')
d = data.set_index(["StockNo.","Datetime"]) # 设置多重索引
for x in self.other_factors:
  x = x.set_index('S_INFO_WINDCODE',inplace=True) # 在for循环中set_index的时候，要加inplace=true
# 统一datetime格式,如果原来的日期index是‘object’，可以用这个函数把它变为datetime格式
data['Datetime'] = pd.to_datetime(data['Datetime'])
data['Date'] = pd.to_datetime(data['Date'], format = '%d/%m/%Y')
# 提取datetime中的具体年月日
nvda['year']=nvda.index.year # 再建一列新的column等于对应的年份

#############################################################################################
3. deal with 'nan' in dataframe
# 删除缺失值
df.dropna()
# 删除表中含有任何NaN的行
df.dropna(axis=0,how='any')  # how='all' 表示 删除表中全部为NaN的行
# 删除表中含有任何NaN的列
df.dropna(axis=1,how='any') # how='all' 表示 删除表中全部为NaN的列
# 将所有行用各自的均值填充 
data_train.fillna(data_train.mean()) 

#############################################################################################
4. iloc and loc function
#截取某几列存入新的容器（-36是倒数第36行，不填就是默认最头或最尾）#[index1:index5, column1:column5]
holder_pctbyinst2 = holder_pctbyinst1.iloc[1:3, -36:]
#根据特定位置改变元素的值
data.iloc[1:3, 'portfolio'] = 1
# loc 函数
df_new.loc[list(["Canada"])] # 根据列中的元素，选取对应元素的数据集 
df_new.loc[df_new["duration"]>160] # 根据元素的选取条件来选取对应的数据集 
df_new.loc[((df_new["duration"] > 200) & (df_new["director_facebook_likes"] > 300 )),"flage"] =1 # 根据元素的选取条件来来选取对应的数据集，并在符合条件的数据行添加flage标签 
df_new.loc[df_new["duration"].isin([100])] # isin函数是series用来判断值是否在目标值是否在series
df_new.query("duration > 100 & index == 'UK'") # query函数中用来判断条件符合的数据集并返回

#############################################################################################
5. 统计：
# 按某一列的值进行升序排列
Data.sort_values(by='Inst_num',axis=0)
Data.sort_values(['column_1','column_2'],ascending = False) # 多重排列，是否按升序排列
# 按列或者行进行累积加和
data_new = np.cumsum(data,axis=0) # axis=0 按列，axis=1 按行
data.cumsum(0).plot() # 或者直接print出折线图
# 分组统计
group1 = d.groupby('Inst_num')
d2 = df.groupby([df['key1'],df['key2']]).mean() #多次分组统计，出来的是一个multiindex的df
group1.size()    #频率统计：这一列的每个值出现了多少次
group1.count()  #频率统计：按指定的列升序排列后，其他列的频数统计
#############################################################################################
6. stack() and unstack()
d = d.stack() # 原来的dataframe变为一个多重索引的只有一列对应数值的数据结构，所有的columns都会被作为第二重index来索引，原来的index为第一重索引
d = d.unstack() # 与上面的变化类似，唯一的不同就是原来的columns会变为第一重索引，而原来的index会变为第二重索引
#############################################################################################
7. 形式转换
# columns 和 index互换
data1 = Panel_industry.T
# transform dictionary to dataframe
table_list = DataFrame(table_list)
# df 变成 array
df.values
#############################################################################################
8. 合并表格
# 合并表格,axis=0为以行来合并（则两个df的columns要相同），axis=1为以列来合并（两个df的index要相同）
result = pd.concat([df1, df2],axis=1)
# 对于要合并的df中有一个要在新的df中进行复制（比如同一个股票同个时间点对应同一个industry），就用merge
result = df.merge(stock_price,industry,left_index=True,right_index=True)
#############################################################################################
9. 存取文件
#存在新的csv里面
data.to_csv(dir_path+"/holder_pctbyinst1.csv")
#读取csv文件
data = pd.read_csv(path + 'file_name.csv')
data = pd.read_csv(path + 'file_name.csv', index_col='stock_name')
#############################################################################################
10. 找出分位数
#只有当a是array的时候才可以用percentile，并且array中不能有str或者nan
np.percentile(a,95)#95%分位数
#专门给df求分位数的函数，默认是按列来求的
df.quantile(0.95)
df.quantile(0.95,axis=1)#按行来求
#如果想求整个df的分位数
df_stack = df.stack()
df_stack.quantile(0.99)
