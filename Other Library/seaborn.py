import seaborn as sns 
# Seaborn 可以很方便的画出直方图，拟合曲线 (密度分布函数)
sns.distplot(data, rug=True, hist=False)
# 和用matplotlib画直方图类似
sns.distplot(df['column_name'], hist=True, kde=False, bins=80, color = 'blue',hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Histogram of Arrival Delays')
plt.xlabel('Delay (min)')
plt.ylabel('Flights')
