# 未知变量命名，常用于for循环，要将值赋给某个新创建的变量，而变量的名字是动态变化的
for i in range(0,len(other_list)):
  names = locals()
  names[other_list[i]] = pd.read_csv(other_factor_path + '/%s.csv'%other_list[i])
