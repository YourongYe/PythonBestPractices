# 初始化，只有当engine为openpyxl，mode才可以是amend模式
writer = pd.ExcelWriter('/Users/YoYo/Desktop/智能记账/Tencent.xlsx',engine='openpyxl',mode='a') 

# 开始写文件，可循环写入
df.to_excel(writer, sheet_name)
# 写完后要保存
writer.save() 和 writer.close() 两者功能一致
