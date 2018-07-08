1. 移动窗口函数，滚动算平均值、总和、数量、标准差等

arg : 为Series或DataFrame 
window : 窗口的大小 
min_periods : 最小的观察数值个数 
freq : 
center : 布尔型，默认为False, 指取中间的 
how : 取值的方式，默认为None

std = pd.rolling_std(data[1:], window=5)
sum = pd.rolling_mean(arg, window, min_periods=None, freq=None, center=False, how=None, **kwargs)
count = pd.rolling_count(df, window=10, freq=None, center=False, how=None)
variance = pd.rolling_var(arg, window, min_periods=None, freq=None, center=False, how=None, **kwargs)
median = pd.rolling_median(arg, window, min_periods=None, freq=None, center=False, how='median', **kwargs)
# 移动窗口的相关系数
pd.rolling_corr(arg1, arg2=None, window=None, min_periods=None, freq=None, center=False, pairwise=None, how=None)
# 移动窗口的协方差
pd.rolling_cov(arg1, arg2=None, window=None, min_periods=None, freq=None, center=False, pairwise=None, how=None, ddof=1)

##################################################################################################

2. 创建html的历史数据图

# 库
from pyecharts import Grid, Bar, Line, Kline, Overlap, Page

# 画k线图，y轴数据必须是open、close、high、low 4列
self.price = self.data[['open', 'close', 'high', 'low']]
self.price_list = [self.price.ix[i].tolist() for i in range(len(self.price))]

# 显示滑块：is_datazoom_show=True，有多图的时候是否share一个滑块：datazoom_type='both'，有几个图就几个元素：datazoom_xaxis_index=[0, 1, 2]
kline = Kline('图的标题')
kline.add('线的名字', x轴数据, y轴数据, is_datazoom_show=True, datazoom_type='both', datazoom_xaxis_index=[0, 1, 2])

# 画一般的折线图，是否可以滑动：is_smooth=True，这条线的标题写在整个网页的从上往下的55%的位置：legend_top="55%"
line = Line()
line.add('线的名字', x轴数据, y轴数据, is_fill=False, line_opacity=0.8, is_smooth=True)
line_trend.add('1-5MA', self.timeline, self.data['1-5 MA'], is_fill=False, line_opacity=0.8, is_smooth=True,  legend_top="55%")

# 多线同图
overlap = Overlap() #画在同一个图上
overlap.add(kline) #kline是一个图的名字

# 设置页面的大小，add后面的第一个是某一个图
grid = Grid(width=1400, height=1100)
grid.add(line_trend, grid_top="55%",grid_bottom="25%")

# 当页面中有多个图的时候，应该用page（）
page = Page()
page.add(grid)
page.render() #将这个page转为html

# 当一个文件里有class的时候，通常在执行main的时候要写这个
if __name__=='__main__':
  print(data)

##################################################################################################

3. dataframe 统计各列的参数

def stats(x):
    return pd.Series([x.count(),x.min(),x.idxmin(),
    x.quantile(.25),x.median(),
    x.quantile(.75),x.mean(),
    x.max(),x.mad(),x.var(),x.std()],
    index = ['Count','Min','Whicn_Min',
    'Q1','Median','Q3','Mean',
    'Max','Which_Max','Var','Std'])
  
df.apply(stats)
