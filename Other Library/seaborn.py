import seaborn as sns 
1. draw histogram
# Seaborn 可以很方便的画出直方图，并且可以选择同时画出拟合曲线rug (密度分布函数)
sns.distplot(data, rug=True, hist=False)
# 和用matplotlib画直方图类似
sns.distplot(df['column_name'], hist=True, kde=False, bins=80, color = 'blue',hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Histogram of Arrival Delays')
plt.xlabel('Delay (min)')
plt.ylabel('Flights')

2. draw regression
sns.pairplot(df, x_vars=['column1','column2'], y_vars='column3', size=7, aspect=0.8, kind='reg')
