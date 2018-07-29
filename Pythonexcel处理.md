#7.11
tips：

1. 在该网站查找相关模块信息http://www.python-excel.org/
2. xlsxwriter开发文档https://media.readthedocs.org/htmlzip/xlsxwriter/latest/xlsxwriter.zip
3. xlsxwriter在线开发文档https://xlsxwriter.readthedocs.io/
4. xlrd在线开发文档http://xlrd.readthedocs.io/en/latest/api.html


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
	2. 向XLSX文件添加格式,对示例1进行添加修改

			 import xlsxwriter
			 # Create a workbook and add a worksheet.
			 workbook = xlsxwriter.Workbook('Expenses02.xlsx')
			 worksheet = workbook.add_worksheet()
			 # Add a bold format to use to highlight cells.
			 bold = workbook.add_format({'bold': True})		//添加粗体格式以用于突出显示单元格。
			 # Add a number format for cells with money.
			 money = workbook.add_format({'num_format': '$#,##0'})	//为有钱的单元格添加数字格式。
			 # Write some data headers.
			 worksheet.write('A1', 'Item', bold)	
			 worksheet.write('B1', 'Cost', bold)	//向A1 B1 添加文字当做标题
			 # Some data we want to write to the worksheet.
			 expenses = (
			     ['Rent', 1000],
			     ['Gas',   100],
			     ['Food',  300],
			     ['Gym',    50],
			 )
			 # Start from the first cell below the headers.
			 row = 1
			 col = 0
			 # Iterate over the data and write it out row by row.
			 for item, cost in (expenses):
			     worksheet.write(row, col,     item)
			     worksheet.write(row, col + 1, cost, money)		//将money格式添加到对应单元格中
			     row += 1
			 # Write a total using a formula.
			 worksheet.write(row, 0, 'Total',       bold)		//设置字体
			 worksheet.write(row, 1, '=SUM(B2:B5)', money)		//设置格式
			 workbook.close()
		- 添加了两个Format对象，我们可以使用这些对象来格式化电子表格中的单元格。格式对象表示可应用于Excel中的单元格的所有格式设置属性，如字体，数字格式，颜色和边框。“格式类”部分对此进行了更详细的说明。https://xlsxwriter.readthedocs.io/format.html#format

			bold = workbook.add_format({'bold': True})
			money = workbook.add_format({'num_format': '$#,##0'})

		我们可以将这些格式作为可选的第三个参数传递给工作表，write()格式化单元格中数据：

			write(row, column, token, [format])
		就像：

			worksheet.write(row, 0,'Total',bold)
	3. 将不同类型的数据写入XLSX文件
	
			 from datetime import datetime	//导入时间模块
			 import xlsxwriter
			 # Create a workbook and add a worksheet.
			 workbook = xlsxwriter.Workbook('Expenses03.xlsx')
			 worksheet = workbook.add_worksheet()
			 # Add a bold format to use to highlight cells.
			 bold = workbook.add_format({'bold': 1})
			 # Add a number format for cells with money.
			 money_format = workbook.add_format({'num_format': '$#,##0'})
			 # Add an Excel date format.
			 date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})	//添加Excel日期格式
			 # Adjust the column width.
			 worksheet.set_column(1, 1, 15)		//调整列宽。
			 # Write some data headers.
			 worksheet.write('A1', 'Item', bold)
			 worksheet.write('B1', 'Date', bold)
			 worksheet.write('C1', 'Cost', bold)
			 # Some data we want to write to the worksheet.
			 expenses = (
			     ['Rent', '2013-01-13', 1000],		//多添加一列
			     ['Gas',  '2013-01-14',  100],
			     ['Food', '2013-01-16',  300],
			     ['Gym',  '2013-01-20',   50],
			 )
			 # Start from the first cell below the headers.
			 row = 1
			 col = 0
			 for item, date_str, cost in (expenses):
			     # Convert the date string into a datetime object.
			     date = datetime.strptime(date_str, "%Y-%m-%d")		//将日期字符串转换为datetime对象。
			     worksheet.write_string  (row, col,item)
			     worksheet.write_datetime(row, col + 1, date, date_format )
			     worksheet.write_number  (row, col + 2, cost, money_format)
			     row += 1
			 # Write a total using a formula.
			 worksheet.write(row, 0, 'Total', bold)
			 worksheet.write(row, 2, '=SUM(C2:C5)', money_format)
			 workbook.close()

		- write()几种更具体方法,根据具体数据类型分辨。如下

				write_string()
				write_number()
				write_blank()
				write_formula()
				write_datetime()
				write_boolean()
				write_url()
			在这个程序中使用了一些这些显式write_ 方法用于不同类型的数据：
				
				worksheet.write_string  (row, col,     item              )
				worksheet.write_datetime(row, col + 1, date, date_format )
				worksheet.write_number  (row, col + 2, cost, money_format)
		- Excel中的日期和时间是浮点数，应用数字格式以正确的格式显示它们。如果日期和时间是Python datetime对象，则XlsxWriter会自动进行所需的数字转换。但是，我们还需要添加数字格式以确保Excel将其显示为日期

				from datetime import datetime
				...
				date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
				...
				for item, date_str, cost in (expenses):
				    # Convert the date string into a datetime object.
				    date = datetime.strptime(date_str, "%Y-%m-%d")
				    ...
				    worksheet.write_datetime(row, col + 1, date, date_format )
				    ...
		- set_column()调整列'B'宽度的方法https://xlsxwriter.readthedocs.io/worksheet.html#set_column

				set_column（first_col，last_col，width，cell_format，options ）
					first_col（int） - 第一列（零索引）。
					last_col（int） - 最后一列（零索引）。可以与first_col相同。
					width（float） - 列的宽度。
					cell_format（Format） - 可选的Format对象。
					options（dict） - 可选参数：hidden，level，collapsed。
##2.工作簿类（Workbook类）
Workbook类是XlsxWriter模块公开的主类，它是您需要直接实例化的唯一类。文档https://xlsxwriter.readthedocs.io/workbook.html

- 构造函数，创建一个新的XlsxWriter Workbook对象。该Workbook()构造函数用于创建具有给定文件名的新Excel工作簿：

		Workbook（filename[，options]）
			filename（string） - 要创建的新Excel文件的名称。
			options（dict） - 可选的工作簿参数。见下文。

	options数选项是：

	- constant_memory：减少存储在内存中的数据量，以便有效地写入大文件：

			workbook = xlsxwriter.Workbook(filename, {'constant_memory': True})
	- tmpdir：XlsxWriter在汇编最终的XLSX文件之前，将工作簿数据存储在临时文件中。临时文件在系统的临时目录中创建。如果应用程序无法访问默认临时目录，或者包含的空间不足，则可以使用以下tempdir选项指定备用位置：

			workbook = xlsxwriter.Workbook(filename, {'tmpdir': '/home/user/tmp'})
	- in_memory：为避免在最终XLSX文件的程序集中使用临时文件，例如在不允许临时文件（如Google APP Engine）的服务器上，请将in_memory构造函数选项设置为True：

			workbook = xlsxwriter.Workbook(filename, {'in_memory': True})
		此选项会覆盖该constant_memory选项。

	- strings_to_numbers：启用 工作表。write()在可能的情况下，使用字符串将字符串转换为数字的方法，float()以避免出现关于“存储为文本的数字”的Excel警告。默认是False。要启用此选项，请使用：

			workbook = xlsxwriter.Workbook(filename, {'strings_to_numbers': True})
	- strings_to_formulas：启用 工作表。write()将字符串转换为公式的方法。默认是True。要禁用此选项，请使用：

			workbook = xlsxwriter.Workbook(filename, {'strings_to_formulas': False})
	- strings_to_urls：启用 工作表。write()将字符串转换为url的方法。默认是True。要禁用此选项，请使用：

			workbook = xlsxwriter.Workbook(filename, {'strings_to_urls': False})
	- nan_inf_to_errors：启用 工作表。write()和write_number() 方法，将nan，inf并-inf在Excel错误。Excel不处理NAN / INF的号码，因为它们映射到产生错误码公式解决方法#NUM!和#DIV/0!。默认是False。要启用此选项，请使用：

			workbook = xlsxwriter.Workbook(filename, {'nan_inf_to_errors': True})
	- default_date_format：此选项用于指定与工作表一起使用的默认日期格式字符串 。write_datetime()没有给出显式格式的方法。有关更多详细信息，请参阅使用日期和时间：

			xlsxwriter.Workbook(filename, {'default_date_format': 'dd/mm/yy'})
	- remove_timezone：Excel不支持日期时间/时间的时区，因此没有任何故障安全方式XlsxWriter可以将Python时区感知日期时间映射到Excel日期时间等函数中 write_datetime()。因此，用户应该根据他们的要求以某种有意义的方式转换和删除时区。或者，该remove_timezone选项可用于从datetime值中删除时区。默认是False。要启用此选项，请使用：

			workbook = xlsxwriter.Workbook(filename, {'remove_timezone': True})
		另请参阅XlsxWriter中的时区处理。

	- date_1904：Excel for Windows使用默认纪元1900而Excel for Mac使用1904纪元。但是，任一平台上的 Excel都将在一个系统和另一个系统之间自动转换。默认情况下，XlsxWriter以1900格式存储日期。如果要更改此设置，可以使用 date_1904工作簿选项。此选项主要用于增强与Excel的兼容性，通常不需要经常使用：

		workbook = xlsxwriter.Workbook(filename, {'date_1904': True})
- add_worksheet（[name]）将新工作表添加到工作簿。name（字符串） - 可选工作表名称，默认为Sheet1等。工作表名称必须是有效的Excel工作表名称，即它不能包含任何字符，并且必须少于32个字符。' [ ] : * ? / \ '
- add_format([properties])创建一个新的Format对象以格式化工作表中的单元格。
- add_chart（options）创建可以添加到工作表的图表对象。options（字典） - 图表类型选项的字典。
- add_chartsheet（[ sheetname ] ）将新的add_chartsheet添加到工作簿。sheetname（字符串） - 可选的图表表名称，默认为Chart1等。
- close（）关闭Workbook对象并编写XLSX文件。
- set_size（width，height）设置工作簿窗口的大小width（int） - 窗口的宽度（以像素为单位）。height（int） - 窗口的高度（以像素为单位）。
- set_properties（properties）设置文档属性，如标题，作者等。properties（dict） - 文档属性字典。
- set_custom_property（name，value [，property_type ] ）设置自定义文档属性。name（字符串） - 自定义属性的名称。value - 自定义属性的值（各种类型）。property_type（string） - 属性的类型。可选的。
- define_name（）在工作簿中创建定义的名称以用作变量。name（字符串） - 定义的名称。formula（string） - 定义的名称引用的单元格或范围。
- add_vba_project（vba_project [，is_stream ] ）将vbaProject二进制文件添加到Excel工作簿。vba_project - vbaProject二进制文件名。is_stream（bool） - vba_project是一个内存字节流。
- set_vba_name（name）设置工作簿的VBA名称。name（字符串） - 工作簿的VBA名称。
- worksheets（）返回工作簿中的工作表对象列表。
- get_worksheet_by_name（name）使用工作表返回工作簿中的工作表对象。name（字符串） - 要检索的工作表的名称。
- get_details_url_format（）返回格式对象
- set_calc_mode（mode）设置工作簿的Excel计算模式。mode（字符串） - 计算模式字符串
- use_zip64（）在编写xlsx文件zip容器时允许ZIP64扩展。

##3.工作表类（worksheet类）
工作表类表示Excel工作表。它处理诸如将数据写入单元格或格式化工作表布局等操作。工作表对象不直接实例化。而是通过add_worksheet()从Workbook() 对象调用方法来创建新工作表。	文档地址https://xlsxwriter.readthedocs.io/worksheet.html
##4.工作表类（页面设置）
##5.格式类
##6.图表类
##7.图表类
##8.使用单元格表示法
##9.使用公式
##10.使用日期和时间
##11.使用颜色
##12.使用图表
##13.使用自动过滤器
##14.使用数据验证
##15.使用条件格式
##16.使用工作表表
##17.使用文本框
##18.使用迷你图
##19.使用单元格注释
##20.使用大纲和分组
##21.使用内存和性能
##22.使用VBA宏
##23.使用Python Pandas和XlsxWriter


#7.29

##1.使用 Python 读写 Excel 文件（1）
openpyxl 模块简单易用、功能广泛，单元格格式/图片/表格/公式/筛选/批注/文件保护等功能应有尽有，图表功能是其一大亮点。

- 安装 openpyxl 模块

	打开 cmd 命令行窗口，输入 pip install openpyxl 命令即可 “一键安装”
- 示例创建并保存 Excel 文件

		import openpyxl
		# 新建工作表
		wb = openpyxl.Workbook()
		# 获取活跃的工作表
		ws = wb.active
		# 数据可以直接赋值给单元格
		ws['A1'] = 520
		# 可以整行添加
		ws.append([1, 2, 3])
		# Python 类型将自动转换
		import datetime
		ws['A3'] = datetime.datetime.now()
		# 保存文件
		wb.save("demo.xlsx")

- 爬取豆瓣数据并保存表格

		import requests		# 导入处理HTTP模块
		import bs4		# 导入提取xmls数据模块
		import re		# 正则表达式模块
		import openpyxl		# Excel处理模块
		
		def open_url(url):
		    # 使用代理
		    # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
		    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
		
		    # res = requests.get(url, headers=headers, proxies=proxies)
		    res = requests.get(url, headers=headers)	# 获取连接对象
		
		    return res
		
		def find_movies(res):
		    soup = bs4.BeautifulSoup(res.text, 'html.parser')
			# 对 连接对象读取内容，并使用html.parse python标准库解析
		    # 电影名
		    movies = []
		    targets = soup.find_all("div", class_="hd")	# 查找所有div标签并且class属性为hd
		    for each in targets:
		        movies.append(each.a.span.text)	# 遍历结果并添加到空集合中
		
		    # 评分
		    ranks = []
		    targets = soup.find_all("span", class_="rating_num")
		    for each in targets:
		        ranks.append(each.text)
		
		    # 资料
		    messages = []
		    targets = soup.find_all("div", class_="bd")
		    for each in targets:
		        try:
		            messages.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
		        except:
		            continue
		
		    result = []
		    length = len(movies)
		    for i in range(length):
		        result.append([movies[i], ranks[i], messages[i]])
		
		    return result
		
		# 找出一共有多少个页面
		def find_depth(res):
		    soup = bs4.BeautifulSoup(res.text, 'html.parser')
		    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text
		
		    return int(depth)
		
		def save_to_excel(result):
		    wb = openpyxl.Workbook()
		    ws = wb.active
		
		    ws['A1'] = "电影名称"
		    ws['B1'] = "评分"
		    ws['C1'] = "资料"
		
		    for each in result:
		        ws.append(each)
		
		    wb.save("豆瓣TOP250电影.xlsx")
		
		def main():
		    host = "https://movie.douban.com/top250"
		    res = open_url(host)
		    depth = find_depth(res)
		
		    result = []
		    for i in range(depth):
		        url = host + '/?start=' + str(25 * i)
		        res = open_url(url)
		        result.extend(find_movies(res))
		
		    '''
		    with open("test.txt", "w", encoding="utf-8") as f:
		        for each in result:
		            f.write(each)
		    '''
		
		    save_to_excel(result)
		    
		if __name__ == "__main__":
		    main()
	Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。

	下面是常见解析器：
	![](https://images2015.cnblogs.com/blog/997599/201706/997599-20170601215456586-1362956505.png)
##2.使用 Python 读写 Excel 文件（2）
- 打开 Excel 文件

	使用 openpyxl.load_workbook() 函数可以打开一个已存在的 Excel 文件。

		>>> import openpyxl
		>>> wb = openpyxl.load_workbook(r"C:\Users\goodb\Desktop\豆瓣TOP250电影.xlsx")
		>>> type(wb)
		
		<class 'openpyxl.workbook.workbook.Workbook'>
- 获取工作表

	上一节我们通过 active 属性可以获取当前激活的工作表。如果你想获取当期工作簿中所有的工作表，可以使用 get_sheet_names() 方法（不推荐使用）或者直接打印 sheetnames 属性

		>>> wb.get_sheet_names()
		['Sheet']
		>>> print(wb.sheetnames)
		['Sheet']
	通过 get_sheet_by_name() 方法可以找到指定名称对应的工作表（get_sheet_by_name() 方法已经不推荐使用，官方推荐使用更 Pythonic 的 wb["SheetName"] 方式来获取指定工作表）

		>>> print(wb['Sheet'])
		<Worksheet "Sheet">
	但如果传入一个不存在的工作表名称，程序会报错
- 创建和删除工作表

	利用 create_sheet() 和 remove_sheet() 方法可以创建和删除工作表。create_sheet() 默认创建的工作表是存放在现有工作表的后面，名字是 Sheet1,2,3 这样排下去。但我们可以通过参数来修改这一默认设置，index 参数指定新工作表插入的位置（0 表示第一个位置），title 参数指定工作表的名称

		>>> nws = wb.create_sheet(index = 0, title = "FishC Demo")
		>>> print(wb.get_sheet_names())
		['FishC Demo', 'Sheet']
	删除工作表使用 remove_sheet() 方法，该方法只有一个参数，就是制定待删除的工作表对象。这里需要注意一下，光给个名字是不够的，需要给它一个工作表对象.所以，删除名称为 “FishC Demo” 的工作表，应该这么写

		wb.remove_sheet(wb.get_sheet_by_name("FishC Demo"))
- 定位单元格

	获取工作表之后，可以通过像 Python 字典索引那样去定位单元格。单元格对象，拥有 row、column 和 coordinate 属性，代表单元格的行、列和坐标：

		>>> c = ws['A2']
		>>> c.row
		2
		>>> c.column
		'A'
		>>> c.coordinate
		'A2'
	通过 value 属性可以访问该单元格的值：
		
		>>> ws['A2'].value
		'肖申克的救赎'
	还可以通过 offset(row, column) 方法，定位距离该单元格 row 行 column 列偏移的另一个单元格：
	
		>>> d = c.offset(2, 0)
		>>> d.coordinate
		'A4'
		>>> d.value
		'这个杀手不太冷'
- 获取字母编号列数

	 Excel 工作表是以字母为编号，即 ABCDEFG...Z，到达 Z 之后就从 AA 开始继续编号，所以列的话是以二十六进制的形式来表示数据的。
	
	提供了 get_column_letter() 和 colunm_index_from_string() 方法来帮助大家进行转换。比如我们想知道第 496 列如何表示，可以使用 openpyxl.cell.cellget_column_letter(496) 方法进行转换（确实是有两个 cell 哈）
		
		>>> openpyxl.cell.cell.get_column_letter(496)
		'SB'
	如果我们知道列的编号是 “JB”，可以使用 openpyxl.cell.cell.column_index_from_string('JB') 方法得知其实际上位于第几列：
	
		>>> openpyxl.cell.cell.column_index_from_string('JB')
		262
- 访问多个单元格

	openpyxl 允许将工作表对象进行切片操作，即表示一个范围内的多个单元格

		>>> for each_movie in ws['A2':'B10']:
	        for each_cell in each_movie:
	                print(each_cell.value, end=' ')
	        print('\n')

		肖申克的救赎 9.6 
		
		霸王别姬 9.5 
		
		这个杀手不太冷 9.4 
		
		阿甘正传 9.4 
		
		美丽人生 9.5 
		
		千与千寻 9.2 
		
		辛德勒的名单 9.4 
		
		泰坦尼克号 9.2 
		
		盗梦空间 9.3
	对于一个范围内的多个单元格，openpyxl 是遵循 “先行后列” 的原则进行迭代的。我们还可以通过工作表的 rows 和 columns 属性获取当前工作表下所有行或列的迭代。

		>>> for each_row in ws.rows:
        print(each_row[0].value)

		电影名称
		肖申克的救赎
		霸王别姬
		这个杀手不太冷
		阿甘正传
		美丽人生
		千与千寻
		辛德勒的名单
		泰坦尼克号
		盗梦空间
		……
	如果不想一次性迭代所有的行或列，可以使用 iter_rows() 和 iter_columns() 方法进行控制

		>>> for each_row in ws.iter_rows(min_row=2, min_col=1, max_row=4, max_col=2):
        print(each_row[0].value)
		
		肖申克的救赎
		霸王别姬
		这个杀手不太冷
- 拷贝工作表

	拷贝整个工作表，可以使用工作簿对象的 copy_worksheet() 方法：

		>>> new = wb.copy_worksheet(ws)
		>>> wb.save(r"C:\Users\goodb\Desktop\豆瓣TOP250电影.xlsx")