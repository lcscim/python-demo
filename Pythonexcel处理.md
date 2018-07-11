#7.11
tips：

1. 在该网站查找相关模块信息http://www.python-excel.org/
2. https://media.readthedocs.org/htmlzip/xlsxwriter/latest/xlsxwriter.zip为xlsxwriter开发文档


##1.相关模块
- openpyxl 用于读取和写入Excel 2010文件的推荐包（即：.xlsx）
注意： 一般来说，openpyxl现在涵盖了这些用例！
- xlsxwriter 用于编写数据，格式化信息，特别是Excel 2010格式的图表的替代软件包（即：.xlsx）
- xlrd 此包用于从旧的Excel文件中读取数据和格式信息（即：.xls）
- xlwt 此包用于将数据和格式信息写入旧的Excel文件（即：.xls）
- xlutils 该软件包收集需要xlrd和xlwt的实用程序，包括复制，修改或过滤现有excel文件的功能。注意： 一般来说，openpyxl现在涵盖了这些用例！

目前常用xlrd和xlsxwriter

##1.1 xlrd
1. 安装xlrd

		pip install xlrd


##1.2 xlsxwriter
1. 安装xlsxwriter

		pip install xlsxwriter
2. 教程

	1. 假设我们有一些关于每月支出的数据，我们希望将其转换为Excel XLSX文件：

			expenses = (
			    ['Rent', 1000],
			    ['Gas',   100],
			    ['Food',  300],
			    ['Gym',    50],
			)
		
		程序代码如下

			import xlsxwriter
			# Create a workbook and add a worksheet.
			workbook = xlsxwriter.Workbook('Expenses01.xlsx')	//创建工作簿
			worksheet = workbook.add_worksheet()	//向工作簿中添加工作表
			# Some data we want to write to the worksheet.
			expenses = (		//需要写入的数据
			    ['Rent', 1000],
			    ['Gas',   100],
			    ['Food',  300],
			    ['Gym',    50],
			)
			# Start from the first cell. Rows and columns are zero indexed.
			row = 0
			col = 0		//设置索引从第一行第一列开始
			# Iterate over the data and write it out row by row.
			for item, cost in (expenses):	//迭代数据并向表中添加
			    worksheet.write(row, col,     item)
			    worksheet.write(row, col + 1, cost)
			    row += 1
			# Write a total using a formula.
			worksheet.write(row, 0, 'Total')	//向第一列追加
			worksheet.write(row, 1, '=SUM(B1:B4)')	//向第二列追加并用公式求
			workbook.close()
	
	程序方法详解：

	- import xlsxwriter	导入模块
	- Workbook() 构造函数创建新的工作簿对象。XlsxWriter只能创建新文件。它无法读取或修改现有文件。采用一个非可选的参数，它是我们想要创建的文件名：

			workbook = xlsxwriter.Workbook('Expenses01.xlsx')
	- add_worksheet() 添加新工作表 ：详细https://xlsxwriter.readthedocs.io/workbook.html#add_worksheet

			worksheet = workbook.add_worksheet()	//向工作簿中添加工作表
	
			worksheet1 = workbook.add_worksheet()        //添加表1，默认名称Sheet1.
			worksheet2 = workbook.add_worksheet('Data')  //添加表2，指定名称Data.
			worksheet3 = workbook.add_worksheet()        //添加表3，默认名称Sheet3.
	- write() 方法写入数据：详细文档https://xlsxwriter.readthedocs.io/worksheet.html#write
	
			worksheet.write(row, col, *args)	//三个参数分别是行，列，附加方法。附加方法可以是值也可以是方法。默认A1的行列									（0,0）。示例如下
		
			for item, cost in (expenses):
			    worksheet.write(row, col,     item)
			    worksheet.write(row, col + 1, cost)
			    row += 1

			worksheet.write(row, 1, '=SUM(B1:B4)')
	- close()方法关闭Excel文件：详细文档https://xlsxwriter.readthedocs.io/workbook.html#close

			workbook.close()		
		除非您使用with上下文管理器，否则应始终在结束前close()文件