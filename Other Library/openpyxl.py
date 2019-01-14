import openpyxl
from openpyxl.chart import Reference, LineChart

# 读取已有的excel文件
existing_workbook = openpyxl.load_workbook(config.opt_des_path + '/alpha%s_results.xlsx'%self.alpha_number)
# 在load的workbook里找到对应的饿worksheet
current_worksheet = existing_workbook['净值序列']
# 初始化一个linechart
chart = LineChart()
# 选择一个style
chart.style = 2
# 可以限定x和y轴的最大最小值
chart.x_axis.scaling.min = 11
chart.y_axis.scaling.max = 1.5
# 指定作图的数据来源，范围一定要给全，min_row从1开始取-包括columns_names，min_col从第2列开始取（第1列为x-axis）
# 注意min_col、min_row、max_col、max_row参数的值都是从1开始而不是0
data = Reference(current_worksheet, min_col=2, min_row=1, max_col=7, max_row=self.end_point-self.start_point)
chart.add_data(data, titles_from_data=True)
# specify日期列
dates = Reference(current_worksheet, min_col=1, min_row=2, max_row=self.end_point-self.start_point)
chart.set_categories(dates)
# 将图加到指定的worksheet
current_worksheet.add_chart(chart, "I11")
# 最后一定要save，否则不会改变
existing_workbook.save(config.opt_des_path + '/alpha%s_results.xlsx'%self.alpha_number)

# 删除一个worksheet
existing_workbook.remove(current_worksheet)
