# Histogram 为最常用的查看密度分布可视化方法，利用matplotlib 中 hist 函数即可
plt.hist(data, bins=50, color='steelblue', normed=True )
plt.show()
# python会自动帮你分出每组的频率有多少个，然后再画图就可以了。bins 指的是直方条的个数
plt.hist(df['column_name'], color = 'blue', edgecolor = 'black', bins = 100)
plt.show()

for i in range(0,len(self.alpha_list)):
  plotdata.index = pd.to_datetime(plotdata.index)
  plotdata.plot() # dataframe也有画图的函数，这是画曲线图
  plt.close('all') # 循环画图要注意关掉，否则会画在同一个图上
  plt.savefig(dir_path + '/alpha%d.png'%self.alpha_list[i]) # 直接存起来，可以是jpg

