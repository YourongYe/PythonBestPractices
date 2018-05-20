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
# 统一datetime格式,如果原来的日期index是‘object’，可以用这个函数把它变为datetime格式
data['Datetime'] = pd.to_datetime(data['Datetime'])
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
PanelData1.sort_values(by='Inst_num',axis=0)
# 分组统计
group1 = d.groupby('Inst_num')
group1.size()    #频率统计：这一列的每个值出现了多少次
group1.count()  #频率统计：按指定的列升序排列后，其他列的频数统计
#############################################################################################
6. stack() and unstack()
d = d.stack() # 原来的dataframe变为一个多重索引的只有一列对应数值的数据结构，所有的columns都会被作为第二重index来索引，原来的index为第一重索引
d = d.unstack() # 与上面的变化类似，唯一的不同就是原来的columns会变为第一重索引，而原来的index会变为第二重索引



# 合并表格
result = pd.concat([d, d1],axis=1)

# 找出分位数
np.percentile(a,95)#95%分位数

# columns 和 index互换
data1 = Panel_industry.T

#存在新的csv里面
holder_pctbyinst1.to_csv(dir_path+"/holder_pctbyinst1.csv")