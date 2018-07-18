#Python自带模块
总开发文档目录：https://docs.python.org/3/py-modindex.html#cap-s
##1.python学习基础
- random 生成伪随机数，该模块为各种分布实现伪随机数生成器。

	文档地址：https://docs.python.org/3/library/random.html#module-random
- sys 系统特定的参数和功能，该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数。它始终可用。

	文档地址：https://docs.python.org/3/library/sys.html#module-sys
- os 其他操作系统接口，该模块提供了一种使用操作系统相关功能的便携方式。如果您只想读取或写入文件，请参阅open()，如果要操作路径，请参阅os.path模块，如果要读取命令行上所有文件中的所有行，请参阅fileinput 模块。有关创建临时文件和目录的信息，请参阅tempfile 模块，有关高级文件和目录的处理，请参阅shutil 模块。

	文档地址：https://docs.python.org/3/library/os.html#module-os
- os.path 通用路径名操作，该模块在路径名上实现了一些有用的功能。

	文档地址：https://docs.python.org/3/library/os.path.html#module-os.path
- pickle Python对象序列化，该pickle模块实现了用于序列化和反序列化Python对象结构的二进制协议。用于存放（pickling）读取（unpickling）

	文档地址：https://docs.python.org/3/library/pickle.html#module-pickle
- calendar- 与日历相关的一般功能此模块允许您输出类似Unix cal程序的日历，并提供与日历相关的其他有用功能。

	文档地址：https://docs.python.org/3/library/calendar.html#module-calendar
- datetime- 基本日期和时间类型该datetime模块提供了以简单和复杂的方式操作日期和时间的类。虽然支持日期和时间算法，但实现的重点是有效的属性提取以进行输出格式化和操作。

	文档地址：https://docs.python.org/3/library/datetime.html#module-datetime
- time- 时间访问和转换该模块提供各种与时间相关的功能。

	文档地址：https://docs.python.org/3/library/time.html#module-time
- urllib- URL处理模块是一个收集几个模块以处理URL的包：

	文档地址：https://docs.python.org/3/library/urllib.html#module-urllib
	
	- urllib.request 用于打开和阅读URL
	- urllib.error 包含由...提出的例外 urllib.request
	- urllib.parse 用于解析URL
	- urllib.robotparser用于解析robots.txt文件

- json- JSON编码器和解码器，处理json格式文本

	文档地址：https://docs.python.org/3/library/json.html#module-json
- re- 正则表达式操作此模块提供与Perl中类似的正则表达式匹配操作。

	文档地址：https://docs.python.org/3/library/re.html#module-re
###1.1需另行安装模块
- Scrapy是一种用于抓取网站和提取结构化数据的应用程序框架，可用于广泛的有用应用程序，如数据挖掘，信息处理或历史存档。尽管Scrapy最初是为网络抓取而设计的，但它也可以用于使用API​​（例如Amazon Associates Web Services）或作为通用网络爬虫来提取数据。

	文档地址：https://docs.scrapy.org/en/latest/topics/api.html
- lxml - 使用Python的XML和HTML是功能最丰富且易于使用的库，用于处理Python语言中的XML和HTML。

	文档地址：https://lxml.de/index.html#documentation
- pyOpenSSL最初是由MartinSjögren创建的，因为Python 2.1中标准库中的SSL支持（当pyOpenSSL项目开始时Python的当代版本）受到严格限制。当时用于Python的其他OpenSSL包装器也有限，尽管方式不同。

	相关内容地址：https://pyopenssl.org/en/stable/introduction.html#development
##2.PythonGUI编程
主要有一个

- tkinter- Tcl / Tk的Python接口的tkinter封装（“TK接口”）是标准的Python接口Tk的GUI工具包。Tk和Tk tkinter都适用于大多数Unix平台以及Windows系统。（Tk本身不是Python的一部分;它在ActiveState中维护。）

	文档地址：https://docs.python.org/3/library/tkinter.html#module-tkinter
##3.Python游戏编程
使用python开发游戏需要用到pygame

- Pygame 

	文档地址：https://www.pygame.org/docs/
- traceback- 打印或检索堆栈追溯该模块提供了一个标准接口，用于提取，格式化和打印Python程序的堆栈跟踪。

	文档地址：https://docs.python.org/3/library/traceback.html#module-traceback
##4.PythonExcel处理
有一些python包可用于处理任何Python平台上运行的Excel文件，并且不需要使用Windows或Excel。它们快速，可靠且开源：
- openpyxl用于读取和写入Excel 2010文件的推荐包（即：.xlsx）

	文档地址：https://openpyxl.readthedocs.io/en/stable/
- xlsxwriter用于编写数据，格式化信息，特别是Excel 2010格式的图表的替代软件包（即：.xlsx）

	文档地址：https://xlsxwriter.readthedocs.org/
- xlrd此包用于从旧的Excel文件中读取数据和格式信息（即：.xls）

	文档地址：http://xlrd.readthedocs.io/en/latest/
- xlwt此包用于将数据和格式信息写入旧的Excel文件（即：.xls） 

	文档地址：http://xlwt.readthedocs.io/en/latest/
- xlutils该软件包收集需要xlrd和xlwt的实用程序，包括复制，修改或过滤现有excel文件的功能。注意： 一般来说，openpyxl现在涵盖了这些用例！

	文档地址：http://xlutils.readthedocs.io/en/latest/
##5.Python图片识别
- PIL全称：Python Imaging Library，python图像处理库，这个库支持多种文件格式，并提供了强大的图像处理和图形处理能力。由于PIL仅支持到Python 2.7，所以在PIL的基础上创建了Pillow库，支持最新Python 3.x。
- pytesseract图片识别工具

安装
		pip install pytesseract 
		pip install Pillow		//安装第一个后一般会自动安装该模块

使用百度OCR

	文档地址：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html
##6.Python操作手机
adb全名Andorid Debug Bridge. 顾名思义, 这是一个Debug工具。

- 官方文档：https://github.com/mzlogin/awesome-adb/blob/master/README.en.md#reference-links