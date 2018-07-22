#5.23
tips:

1. tab键在IDLE中是提示快捷键
2. 缩进是Python中很重要的相当于其他语言中的“{”
3. BIF = built-in function（内置函数）
4. 在IDLE中输入dir(__builtins__)出现小写的为内置函数bif
5. 输入help（input）即可查看内置函数input的详细信息
6. 会使用转义字符
7. 原始字符串在字符串引号的最前面加上字母r,例如：r"C:\\now"可将字符串原始内容显示出来，最后一个字符不能为\
8. 得到原本换行格式使用三引号，“”“内容”“”
9. 条件分支

		if 条件:
			结果为TRUE执行的
		else：
			结果为FALSE执行的			//可以嵌套使用
10. while循环

		while 条件:
			循环体			//条件为FALSE时跳出循环
11. 逻辑操作符and，or，not（与或非）
12. 产生随机数random模块，randint(a,b)产生一个a-b之间随机的整型
13. 加载模块使用
14. +模块，例如，然后才能使用模块内的内容

		import random
15. 单行注释#，多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来
##第一章
###1.第一个Python程序
####1.1 命令行模式
	在cmd中输入Python即可进入
####1.2 从IDLE（通过键入文本与程序交互）启动Python，
	Windows直接搜索IDLE
小结

1.在Python交互式模式下，可以直接输入代码，然后执行，并立刻得到结果。

2.在命令行模式下，可以直接运行.py文件。
###2.输出

	输入print("Hello,Python!") 输出 Hello,Python!
	输入print（5+3） 输出 8
	输入5+3 输出也是8			//可直接输出计算后的结果
	输入print("Hello"+"Python")输出HelloPython	//将其串联起来
	输入print("Hello"，"Python")输出Hello Python		//将逗号变为空格串联起来
	输入print("Hello,Python!"*8)输出8次Hello,Python!并将其串联起来
	输入print("Hello,Python!\n"*8)输出8次Hello,Python!并将其串联起来每次需要换行
###3.文字游戏

	print('-------------------大家好我是老长-------------------')
	temp = input("猜一个心里想一个数字：")		//打印一串字符并要求输入字符将输入字符赋值给temp，input就是内置函数（BIF）
	guess = int(temp)		//将temp强制转为int类型，int也是内置函数（BIF）
	if guess == 8:			//条件
	    print("猜对了")
	    print("猜对了也没有奖励")
	else:
	    print("猜错了，想的数字是8")
	print("game over")
练习：输入姓名年龄并将其打印出来

	print('-------------------输入显示姓名，年龄-------------------')
	name = input("请输入您的姓名：")
	age = input("请输入您的年龄：")
	print("您的姓名是"+name,"您的年龄是"+age)

加强版

	import random				//导入其他模块
	secret = random.randint(0,10)			//使用该模块中的方法生成一个在该范围内的随机整数，并将其赋予变量secret
	print('-------------------大家好我是老长-------------------')
	temp = input("猜一个心里想一个数字：")
	guess = int(temp)
	i = 1
	while guess != secret and i < 3:
	    i += 1
	    if guess > secret:
	        print("大了")
	    else:
	        print("小了")
	    temp = input("重新输入：")
	    guess = int(temp)
	if guess == secret:
	    print("猜对了也没有奖励")
	else:
	    print("超过" + str(i) + "次,game over")		//使用str（）将整型转化为str字符串型
#5.24
tips：

1. 运算符优先级，幂运算>正负号>算术操作符>比较操作符>逻辑运算符
2. break跳出循环
3. else if可缩写为elif 
4. 三元操作符 small = 结果为true执行的语句 if 条件 结果为false执行的语句 if
5. assert（断言），当跟在assert后的条件为假的时候，程序自动崩溃并抛出AssertionError异常，常用在确保程序某个条件一定为真时才让程序正常工作的情况下
6. 内置函数len(变量)，可以获得变量的字符长度
7. 内置函数range([start,]stop[,step = 1])中括号框起来的表示是可选参数，step = 1表示第三个参数默认为1表示步进，每次增加几。这个函数表示生成一个从start参数值开始到stop参数的值结束的数字序列（包含头不包含尾）
8. 内置函数list（参数）根据参数生成一个列表
9. continue语句，条件成立继续执行，不成立跳出循环。终止本轮循环开始下次循坏
##1.算术操作符
+，-，*，/，%（取模，就是取余数），**（幂a**b,就是a的b次方），//（取整，返回商的整数部分）	
##2.比较运算符,结果为布尔值
==，！=，>,<,>=,<=
##3.赋值运算符
=，+=，-=，*=，/=,%=,**=,//=
##4.逻辑操作符
and，or，not
##5.分支和循环
例子：打飞机游戏框架

		1.加载背景音乐
		2.播放背景音乐（设置单曲循环）
		3.我方飞机出现
		interval = 0
		while true：
			if 用户是否点击关闭按钮：
				退出程序
			interval += 1
			if interval == 50：
				interval = 0
				小飞机诞生
			小飞机移动一个位置
			屏幕刷新
			if 用户鼠标产生移动：
				我方飞机中心位置 = 用户鼠标位置
				屏幕刷新
			if我方飞机与小飞机发生肢体冲突：
				我放挂，播放背景音乐
				修改我方飞机图案
				打印“game over”
				停止背景音乐，最好淡出
for循环：语法

	for 目标 in 表达式：
		循环体
例子

	favorite = 'lcsim'
	for i in favorite:
		print(i,end = ' ')			//打印结果l c s c i m

	member = ['你好','我好','他好','大家好才是真的好']
	for each in member:
		print(each,len(each))
#5.25
tips:

1. 列表可以存储混合型数据
2. append(),向列表添加一个元素
3. extend(),向列表添加一个列表，都是在列表末尾添加
4. insert(),向指定位置添加数据
5. 成员关系操作符in，结果是布尔值。a in b判断a是否在b中。not in与in意思相反
6. 在IDLE中执行dir(list),可查看列表的所有方法
7. 使用=号只是添加了指向元素的标签，要获得拷贝需要使用切片slice。即[:]
8. type(元素名)，可以查看该元素的数据类型
9. 

##1.列表（加强型数组）
列表可以是普通列表，可以是混合列表，可以是空列表

- 向列表添加数据，append（）方法。例子：

		member = [1，2，3，4，5]
		member.append(6)
		member			//结果：123456
注意：append只接受一个参数，参数是值
- 向列表添加列表，extend()方法，例子：

		member = [1，2，3，4，5]
		member.extend([1,2,3])
		member			//结果：[1,2,3,4,5,1,2,3]
注意：extend只接受一个参数，参数是列表
- 向列表指定位置添加数据insert(),第一个参数是目的位置的索引，第二个参数是数据
		
		member = [1，2，3，4，5]
		member.insert(1，0)
		member			//结果：[1,0,2,3,4,5]
##2. 从列表中删除元素
- remove(),不需要知道元素在列表中的位置，需要知道元素的名字，只接受一个参数

		member = [1，2，3，4，5]
		member.remove(5)
		member			//结果：[1,0,2,3,4]
- del语句。del后跟一个带有索引的列表，列表中的索引

		member = [1，2，3，4，5]
		del member[1]
		member			//结果：[1,2,3,4,5]
- pop(),不加参数，表示从列表中提取最后一个元素。加参数表示从指定索引提取元素

		member = [1，2，3，4，5]
		member.pop(1）
		//结果：2
- slice切片，获取指定位置的列表，包含头不包含尾，语法如下

		member = [1，2，3，4，5]
		member[1:3]
		//结果是[2,3]
		member[:2]
		//结果是[1,2]
		member[3:]
		//结果是[3,4,5]
		member[:]
		//结果是[1，2，3，4，5]
- count(),参数在列表中出现的次数，接收一个参数，表示该参数在列表中出现的次数

		member = [1，2，3，4，5]
		member.count(1）
		//结果是1
- index(a,b,c),返回指定参数在列表中出现的索引,第一个参数是元素，第二个参数是列表起始位置索引，第三个参数为截至位置索引。第二个和第三个参数可省略

		member = [1，2，3，4，5]
		member.index(3，1，4）
		//结果是2
- reverse(),对列表元素进行颠倒顺序，没有参数

		member = [1，2，3，4，5]
		member.reverse()
		member   //结果是[5,4,3,2,1]
- sort(func,key,reverse),对列表进行排序第一个参数是函数，第二个参数是与函数有关的关键词，第三个参数默认为False，表示从小到大，值为True表示从大到小。True和False首字母要大写

		member = [1，2，3，4，5]
		member.sort(reverse=True)
		member   //结果是[5,4,3,2,1]
##3.常用操作符
- 成员关系操作符in，结果是布尔值。a in b判断a是否在b中。not in与in意思相反
##4.元组tuple,
元组和列表很相似，元组不能随意插入修改

- 元组使用小括号表示，元素之间必须有逗号,括号可以省略

		tuple1 = (1,2,3,4,5)
		tuple2 = 1,

		8*(8,)		//结果是(8,8,8,8,8,8,8,8)，*是重复操作符
		tuple3 = tuple1[:1]+(6,)+tuple1[3:]
		tuple3		//结果是(1, 6, 4, 5)
#5.26
tips:


##1.字符串内置函数
- capitalize()将字符串第一个字符转为大写
- casefold()将字符串所有字符改为小写
- center(width，fillchar)将字符串居中，并使用空格填充至width宽度,fillchar不指定的话默认为空格
- count(sub,start,end)返回字符串sub在字符串里出现的次数，start，end为指定在字符串中的起始位置。start和end可取消
- endswith（sub,start,end）检查字符串是否以sub字符串结束，如果是返回True，反之返回False。start和end标识起始位置可省略
- startswith（sub,start,end）检查字符串是否以sub字符串开始，如果是返回True，反之返回False。start和end标识起始位置可省略
- expandtabs(tabsize=8)把字符串中的tab符号转为空格，默认tab符号的空格数是8
- find（str，start，end）检测字符串str是否在字符串中，如果在返回开始位置的索引值，否则返回-1，start和end标识起始位置可省略
- rfind（str，start，end）和find类似，只不过从右边起查找
- index(str,start,end)和find相同，只不过不在字符串中会抛出一个异常
- rindex（str,start,end）和index类似，只不过从右边起查找
- isalnum()如果字符串中至少有一个字符都是字母或数字则返回True，否则返回False
- isalpha()如果字符串中至少有一个字符，并且都是字母则返回True，否则返回False
- isdecimal()如果字符串只包含十进制数字则返回True，否则返回False
- isdigit()如果字符串只包含数字则返回 True 否则返回 False
- islower()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
- isnumeric()如果字符串中只包含数字字符，则返回 True，否则返回 False
- isspace()如果字符串中只包含空白，则返回 True，否则返回 False.
- istitle()如果字符串是标题化的(首字母大写，其余所有字母都是小写)则返回 True，否则返回 False
- title()所有单词都是以大写开始，其余字母均为小写
- isupper()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
- join(sub)以指定字符串作为分隔符，将 sub 中所有的元素(的字符串表示)合并为一个新的字符串
- ljust(width，fillchar)返回一个左对齐的字符串其余以fillchar填满，fillchar默认为空格，可省略
- rjust（width，fillchar）返回一个右对齐的字符串其余以fillchar填满，fillchar默认为空格，可省略
- lower（）转换所有字符串中的字母大写改为小写
- upper()转换字符串中的小写字母为大写
- swapcase()将字符串中大写转换为小写，小写转换为大写
- lstrip（[chars]）截掉字符串左边的空格或指定字符。可以有参数，参数为指定字符
- rstrip([chars])删除字符串末尾的空格
- strip([chars])在字符串上执行 lstrip()和 rstrip()
- partition（sub）找到字符串sub，并把字符串分割并组成一个3元组，第二个是sub,第一个是sub之前，第三个是sub之后。如果找不到sub则返回（原字符串，‘’，‘’）
- rpartition（sub）类似于partition方法只不过从右查找
- replace（old，new，max）把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
- rstrip()删除字符串字符串末尾的空格.
- split(str="", num=string.count(str))以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串，如果都不指定则默认为空格切片
- splitlines([keepends])按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
- translate(table, deletechars="")根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

		str7='sssaaaasss'
		str7.translate(str.maketrans('s','b'))
		'bbbaaabbb'		//结果
		str.maketrans('s','b')结果为（115：98）
- maketrans(a,b)创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
- zfill (width)返回长度为 width 的字符串，原字符串右对齐，前面填充0

##2.字符串的格式化
- format（）方法

		"{0} love {1}.{2}".format("I","You","com")
		'I love You.com'	//仅限于数字
	
		"{a} love {b}.{c}".format(a="I",b="You",c="com")		//如果是字符的话如上，如果混用的话第一个必须是0
- 格式化符号

		  %c	 格式化字符及其ASCII码
	      %s	 格式化字符串
	      %d	 格式化整数
	      %u	 格式化无符号整型
	      %o	 格式化无符号八进制数
	      %x	 格式化无符号十六进制数
	      %X	 格式化无符号十六进制数（大写）
	      %f	 格式化浮点数字，可指定小数点后的精度默认六位小数
	      %e	 用科学计数法格式化浮点数
	      %E	 作用同%e，用科学计数法格式化浮点数
	      %g	 %f和%e的简写
	      %G	 %f 和 %E 的简写
	      %p	 用十六进制数格式化变量的地址
- 格式化操作符辅助指令:

			*	定义宽度或者小数点精度
			-	用做左对齐
			+	在正数前面显示加号( + )
		  <sp>	在正数前面显示空格
			#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
			0	显示的数字前面填充'0'而不是默认的空格
			%	'%%'输出一个单一的'%'
		  (var)	映射变量(字典参数)
		   m.n	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
- Python转义字符

		\(在行尾时)	续行符
		\\	反斜杠符号
		\'	单引号
		\"	双引号
		\a	响铃
		\b	退格(Backspace)
		\e	转义
		\000	空
		\n	换行
		\v	纵向制表符
		\t	横向制表符
		\r	回车
		\f	换页
		\oyy	八进制数，yy代表的字符，例如：\o12代表换行
		\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
		\other	其它的字符以普通格式输出
#5.27
tips：

1. 在max和min方法中只能对同种数据类型进行比较
2. 函数的默认属性以双下划綫开始以双下划綫结束，例如：abc.__doc__可查看函数的文档属性

##1.序列
列表，元组，字符串统称为序列

1. list(iterable),不带参数生成空列表，带参数，将该参数传入一个迭代器遍历，并将结果重新生成一个新列表并返回

		a = 'lcscim'
		b = list(a)
		b		//结果为['l', 'c', 's', 'c', 'i', 'm']

2. tuple()类似于list，只不过是操作元组的
3. str(obj)将obj对象转化为字符串
4. len(sub)返回sub参数的长度
5. max()返回参数的最大值如果参数是数字返回最大数字，如果是字符，则按照该字符的ASCII码进行对比
6. min()与max()方法类似是返回最小的
7. sum(iterable,start)返回序列iterable和可选参数start的总和
8. sorted()返回排序后的列表默认从小到大和列表的sort方法类似
9. reversed()返回迭代器对象，将其作为参数传入list方法中可得到列表的颠倒列表
10. enumerate()返回迭代器对象，将其作为参数传入list方法可得到新列表，列表内由元组构成，元组内有两个参数构成，第一个是序号，第二个是字符串的每个元素

		a = 'lcscim'
		list(enumerate(a))
		[(0, 'l'), (1, 'c'), (2, 's'), (3, 'c'), (4, 'i'), (5, 'm')]		//运行后的结果
11. zip(a,b)将列表a和b中的元素成对打包组成元组，再有元组组成新的迭代器对象，元组数量由两个参数最短的字符决定。使用list转为列表

		a = 'lcscim'
		b = 'LCSCIMIS'
		list(zip(a,b))
		[('l', 'L'), ('c', 'C'), ('s', 'S'), ('c', 'C'), ('i', 'I'), ('m', 'M')]		//结果
##2.函数
def关键字创建函数，语法如下

	def MyFirstFunction():			//函数名必须要有小括号
		print('这是我创建的第一个函数')
		print('我表示很鸡冻。。。')
调用时

	MyFirstFunction()
带有参数的函数

	def MySecondFunction(name):			//函数名必须要有小括号
		print(name +'这是我创建的第一个函数')
调用时

	MySecondFunction('lcscim')
参数可以有很多个，中间用逗号隔开

1. 函数的返回值使用return，示例

		def add(a,b):
			return a+b
		
		print(add(1,2))
		3		//返回值
##3.函数的参数
1. 形参（parameter）和实参（argument）

	例如MySecondFunction函数中，函数定义过程中的name是叫形参。传递进来的lcscim就是叫做实参

2. 函数文档

	函数的默认属性以双下划綫开始以双下划綫结束，例如：
		
		abc.__doc__可查看函数的文档属性。
		help（函数名）	//可以查看文档
		print.__doc__	//将未格式化的文档打印出来
		help(print)		//将文档格式化打印出来
3. 关键字参数

	给参数加上关键字，即使参数颠倒位置也不会出现问题
		
		def add(a,b):
			return a+b
		
		print(add(1,2))		//正常位置
		3
		print(add(2,1))		//结果虽然相同但如果是输出文字会顺序错乱
		print(add(b=2,a=1))		//给参数加上关键字即可避免
4. 默认参数

	定义了默认值的参数，使用过程中，如果没有指定函数就会使用定义函数时的默认值

		def add(a=1,b=2):
			return a+b
		print(add())		//结果是3
		print(add(2))		//结果是4
		print(add(2,3))		//结果是5
5. 收集参数

	不知道定义多少个参数，使用收集参数。在参数名最前面加个*号

		def add(*a):
			print('第二个参数是',a[1])
		add(0,1,2,3,4)		//结果是1
	如果知道其中一个特定的参数则需要使用关键字参数，或则使用默认参数，建议使用默认，否则会出现问题

		def add(*a,b=1):
			print('第二个参数是',a[1])
			print('特定参数是',b)
		add(0,1,2,3,4,b='我')	//结果是第二个参数是 1，特定参数是 我
#5.28
tips:

1. python只有函数没有过程
2. 有返回值的叫函数，没返回值的叫过程
3. 在函数内部不要修改全局变量，否则会创建一个新的局部变量
4. 把想要变成全局变量的局部变量前加上global关键字即可改变
5. 
##1.函数变量的作用域
变量分为局部变量(local variable)和全局变量(global variable)

1. 局部变量在函数中定义的变量，在函数外无法访问
2. 全局变量作用于整个代码块

##2.内嵌函数和闭包
把想要变成全局变量的局部变量前加上global关键字即可改变

	count = 5
	def MyFun():
		global count
		count = 10
		print(count)
	MyFun()		//结果为10
	count		//结果为10
- 定义在函数中的函数叫做函数嵌套，不过要注意缩进

		内嵌函数无法在函数外部使用
- 闭包对于内部函数访问外部作用域的变量进行引用，内部函数就是闭包

		def funX(x):
			def funY(y):
				return x*y
			return funY		//返回funY函数,加括号表示访问函数，不加括号访问函数对象
		funX(3)(5)		//结果15

	闭包访问外部作用域中的变量时需要使用nonlocal关键字，和global类似
		
		def fun1():
			x=5
			def fun2():
				nonlocal x
				x*=x
				return x
			return fun2()
##3.lambda表达式
示例

	def a(x):
		return 2 * x + 1
	a(5)		//正常方式
lambda表达式

	lambda x : 2 * x + 1		//是一个没有名字的函数对象

	a = lambda x : 2 * x + 1
	a(5)		//结果是11
	如果参数是两个的话
	a = lambda x,y : x + y
	a(1,2)		//在冒号前是参数
- 作用

	1. 执行一些简单脚本时，可适用lambda表达式，省下定义函数的过程，可是代码更精简
	2. 可解决一些抽象并且整个程序只调用一两次的的函数的命名问题
	3. 简化代码的可读性

- filter()内置函数。过滤器函数。

	语法：filter(function, iterable)<br/>
	该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

		list(filter(lambda x : x % 2,range(10)))
		结果[1,3,5,7,9]
- map(function, iterable, ...),映射。map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

		list(map(lambda x : x * 2,range(10)))
		运行结果[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#5.29
tips:

1. 设置递归深度多少层，需要导入sys模块然后设置递归的深度如

		import sys
		sys.setrecursionlimit(1000000)
2. 递归效率低，需要设置结束递归语句，需要合适的使用递归

##1.递归
函数调用自身时叫做递归,并且能正常返回值

	def funf(n):
		if n == 1:
			return 1
		else: 
			return n*funf(n-1)
	number = int(input('请输入一个数字'))
	result = funf(number)
	print("%d的阶乘是%d" % (number,result))
斐波那契数列的递归实现方式
	
	迭代实现;
		def funa(n):
			n1 = 1
			n2 = 1
			n3 = 1
			if n < 1:
				print('输入有误！')
				return -1
			while n - 2 > 0:
				n3 = n1 + n2
				n1 = n2
				n2 = n3
				n -= 1
			return n3
		result = funa(20)
		if result != -1:
			print('总共有%d对小兔子诞生'%result)
	递归实现
		def fab(n):
			if n < 1:
				print('输入有误！')
				return -1
			if n == 1 or n == 2:
				return 1
			else:
				return fab(n-1)+fab(n-2)
		result = fab(20)
		if result != -1:
			print('总共有%d对小兔子诞生'%result)
汉诺塔用递归实现

	def hanoi(n,x,y,z):
	    if n == 1:
	        print(x ,'-->',z )
    else:
        hanoi(n - 1 , x , z , y)
        print(x,'-->',z)
        hanoi(n - 1,y,x,z)

	n = int(input('请输入层数'))
	hanoi(n,'x','y','z')

1. 树结构的定义
2. 谢尔宾斯基三角形

#5.31
tips：

1. 创建空的字典用空括号标识
2. 

##1.字典，映射类型
键（key）和值（value）。字典用大括号表示：

	dict1 = {1:'one',2:'two','3：'three',4:'four'}	//大括号表示字典，每一项逗号隔开的是每项元素，每项冒号前面是键，冒号后是值
	print（4，dict1[4]）			//结果就是4 four

- dict()方法创建字典
		
		将同种类型的元组或序列
		dict2 = dict(((1,'l'),(2,'c'),(3,'s'),(4,'c'),(5,'i'),(6,'m')))
		dict2		//结果为{1: 'l', 2: 'c', 3: 's', 4: 'c', 5: 'i', 6: 'm'}
		另一种方法创建
		dict3 = dict(鲁迅='我没有这么说过',爱迪生='我也没有')
		dict3	//结果是{'鲁迅': '我没有这么说过', '爱迪生': '我也没有'}
		修改
		dict3['爱迪生'] = '这个真没有'	//单独调用并设置新内容，键是字符串类型必须加引号
		dict3	//新结果是{'鲁迅': '我没有这么说过', '爱迪生': '这个真没有'}
		当字典中没有要修改的键时会自动创建新的字典元素
#6.1
tips:

1. id(变量)可获取变量的地址值
2. 字典中没有顺序
3. 可直接用for循环对文件进行遍历读取

##1.字典2
方法

- fromkeys(seq[, value])用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

		dict1 = {}
		dict1.fromkeys((1,2,3))		//如果第二个参数是一个元组的的话，会把元组作为字典的值，不会一一对应
		{1: None, 2: None, 3: None}		//结果
- keys()以列表返回一个字典所有的键

		dict1 = dict1.formkeys(range(32),'赞')
		for eachKey in dict1.keys():
			print(eachKey)		//可得该字典中所有的键
- values()以列表返回字典中的所有值

		for eachValue in dict1.values():
			print(eachValue)	//可获取该字典所有的值
- items()以列表返回可遍历的(键, 值) 元组数组

		for eachItem in dict1.items():
			print(eachItem)	//可获取该字典的每一个键值对
- get(key，default=None)返回指定键的值，如果键不在字典中返回default值.第二个参数可为空，默认为none，也可以自己设置
- clear()清空一个字典。要清空一个字典务必使用
- copy()返回一个字典的浅复制。浅拷贝是值相同，变量所在的位置不同
- pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
- popitem()随机返回并删除字典中的一对键和值
- setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
- update(dict2)把字典dict2的键/值对更新到对应字典里

##2.集合
大括号表示字典，如果括号内没有键值对，那么就是集合，集合中元素是无序的

	num2 = {1，2，3，4}		//就是集合
- 集合具有唯一性，会自动删除集合中的重复项，每项在该集合中都是唯一的
- 集合是无序的不支持索引

使用set()工厂函数创建集合
		
	set1 = set([1,2,3,4,1,2])	//参数可以是列表，元组
	set1	//结果就是{1，2，3，4}

- add(num)向集合中添加num项
- remove（num）在集合中移除num

不可变集合，使用frozenset()创建不可变集合
	
	set2 = frozenset([1,2,3,4,5])	//创建集合后就不能对其进行修改
##3.文件
open() 方法用于打开一个文件，第一个参数名为必须。语法如下

	open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	- file -- 要打开的文件, 包含路径和文件名
	- mode -- 文件的操作模式
		- 'r'	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
		- 'w'	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
		- 'a'	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
		- 'x' 如果文件已存在，使用此模式打开将引发异常
		- 'b' 以二进制模式打开文件
		- 't' 以文本模式打开（默认）
		- '+' 可读写模式，可添加到其他模式中使用
		- 'U' 通用换行符支持 

- close()方法，关闭文件,关闭后不能再进行读写操作
- file.read([size])从文件读取指定的字节数，如果未给定或为负则读取所有。
- file.tell()返回文件当前位置。电脑光标位置
- file.readline([size])读取整行，包括 "\n" 字符。
- file.readlines([sizehint])读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
- file.write(str)将字符串写入文件，返回的是写入的字符长度。
- file.writelines(sequence)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
- file.seek(offset[, whence])设置文件当前位置，whence表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起偏移offset的字节数。

		f = open('E:\\test.txt','w')
		f.write('大家好我是老长')
		f.close（）
#6.2
tips:

1. 模块导入使用
2. ，一个模块只会被导入一次，不管执行了多少次import
2. 

##1.文件2
示例：

	def save_file(boy,girl,count):		//将保存方法提取出来成为一个函数，方便调用
	    file_name_boy = 'A_'+str(count)+'.txt'
	    file_name_girl = 'B_'+str(count)+'.txt'		//设置新文件名称
	    boy_file = open(file_name_boy,'w')
	    girl_file = open(file_name_girl,'w')		//
		新建文件
	    boy_file.writelines(boy)
	    girl_file.writelines(girl)		//将选取的内容保存到文件中
	    boy_file.close()
	    girl_file.close()		//关闭文件流
	
	def split_file(file_name):
	    f = open('text.txt')
	    boy = []
	    girl = []
	    count = 1
	    for each_line in f:
	        if each_line[:6] != '======':
	            (role,line_spoken) = each_line.split(':',1)
	            if role == 'A':
	                boy.append(line_spoken)
	            else:
	                girl.append(line_spoken)
	        else:
	            save_file(boy,girl,count)
	            boy = []
	            girl = []
	            count += 1
	    save_file(boy,girl,count)
	    f.close()
	split_file('text.txt')
##2.与文件有关模块
1.OS模块：操作系统模块
	
	模块方法：	
	os.getcwd()			返回当前工作目录
	os.chdir(path) 		改变当前工作目录，path为指定目录
	os.listdir(path)	返回path指定的文件夹包含的文件或文件夹的名字的列表。
	os.mkdir(path)		创建单层目录，如果存在就抛出异常
	os.makedirs(path)	递归创建多层目录，如果存在就抛出异常
	os.remove(path)		删除路径为path的文件
	os.rmdir(path)		删除单层目录，如果目录非空抛出异常
	os.removedirs(path)	递归删除目录，从子目录到父目录逐层删除，遇到目录非空则抛出异常
	os.rename(old, new)	重命名文件或目录,从old到new
	os.system(command)	运行系统的shell命令
	常用定义：
	os.curdir		指代当前目录('.')
	os.pardir		指代上一级目录('..')
	os.sep			输出操作系统特定的路径分隔符(win下为'\\',linux下为'/')
	os.linesep		当前平台使用的行终止符(win下为'\r\n',Linux下为'\n')
	os.name			指代当前的操作系统(posix代表Linux，nt代表Linux，mac代表苹果)
2.os.path模块

	os.path.basename(path)	去掉目录路径，单独返回文件名
	os.path.dirname(path) 	去掉文件名，单独返回目录路径
	os.path.join(path1[, path2[, ...]]) 	将path1和path2组合成一个路径
	os.path.split(path) 	将path分割成目录和文件名二元组返回。，如果最后一个为目录也会将其作为文件名与前面分开，不管是否为空
	os.path.splitext(path) 	分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
	os.path.getsize(path) 	返回path的文件的大小（字节）
	os.path.getatime(path) 	返回path所指向的文件或者目录的最后存取时间。(浮点型秒数，可用time模块的gmtime()或localtime()函数换算)
	os.path.getmtime(path) 	回path所指向的文件或者目录的最后修改时间。(浮点型秒数，可用time模块的gmtime()或localtime()函数换算)
	os.path.getctime(path)	回path所指向的文件的创建时间。(浮点型秒数，可用time模块的gmtime()或localtime()函数换算)
	os.path.exists(path) 	如果path存在，返回True；如果path不存在，返回False。
	os.path.isabs(path) 	如果path是绝对路径（包含盘符），返回True
	os.path.isdir(path) 	判断path是否是一个目录
	os.path.isfile(path)	判断path是否是一个文件
	os.path.islink(path)	判断path是否是一个符号链接（在Windows上是指快捷方式）
	os.path.ismount(path)	判断path是否是一个挂载点（盘符）
	os.path.samefile(path1,path2)	判断path1和path2是否指向同一个文件
#6.5
tips：

1. 如果需要，多个异常名用逗号连接用括号阔起except （EOFError，ImportError）：

##1.pickle模块
存放（pickling）读取（unpickling）
示例：

	import pickle		//导入模块
	my_list = [1,2,3,'你好','我好','大家好']
	pickle_file = open('C:\\Users\\asus\\Desktop\\kaifa\\python\\python-demo\\project\\my_list.pkl','wb')		//创建写入文件
	pickle.dump(my_list,pickle_file)	//将内容传入文件中
	pickle_file.close()		//关闭文件
	pickle_file = open('C:\\Users\\asus\\Desktop\\kaifa\\python\\python-demo\\project\\my_list.pkl','rb')		//打开文件
	my_list2 = pickle.load(pickle_file)		//读取打开文件内容
	print(my_list2)			//打印内容
- pickle.dump(内容，要传入的文件)		将内容传入文件
- pickle.load(要读取的文件)		读取文件内容

##2.异常exception
Python标准异常总结
	
	AssertionError		断言语句（assert）失败
	AttributeError		尝试访问未知的对象属性
	EOFError			用户输入文件末尾标志EOF（Ctrl+d）
	FloatingPointError	浮点计算错误
	GeneratorExit		generator.close()方法被调用的时候
	ImportError			导入模块失败的时候
	IndexError			索引超出序列的范围
	KeyError			字典中查找一个不存在的关键字
	KeyboardInterrupt	用户输入中断键（Ctrl+c）
	MemoryError			内存溢出（可通过删除对象释放内存）
	NameError			尝试访问一个不存在的变量
	NotImplementedError	尚未实现的方法
	OSError				操作系统产生的异常（例如打开一个不存在的文件）
	OverflowError		数值运算超出最大限制
	ReferenceError		弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
	RuntimeError		一般的运行时错误
	StopIteration		迭代器没有更多的值
	SyntaxError			Python的语法错误
	IndentationError	缩进错误
	TabError			Tab和空格混合使用
	SystemError			Python编译器系统错误
	SystemExit			Python编译器进程被关闭
	TypeError			不同类型间的无效操作
	UnboundLocalError	访问一个未初始化的本地变量（NameError的子类）
	UnicodeError		Unicode相关的错误（ValueError的子类）
	UnicodeEncodeError	Unicode编码时的错误（UnicodeError的子类）
	UnicodeDecodeError	Unicode解码时的错误（UnicodeError的子类）
	UnicodeTranslateError	Unicode转换时的错误（UnicodeError的子类）
	ValueError			传入无效的参数
	ZeroDivisionError	除数为零
Python 内置异常类的层次结构：
	
	BaseException
	+-- SystemExit
	+-- KeyboardInterrupt
	+-- GeneratorExit
	+-- Exception
	      +-- StopIteration
	      +-- ArithmeticError
	      |    +-- FloatingPointError
	      |    +-- OverflowError
	      |    +-- ZeroDivisionError
	      +-- AssertionError
	      +-- AttributeError
	      +-- BufferError
	      +-- EOFError
	      +-- ImportError
	      +-- LookupError
	      |    +-- IndexError
	      |    +-- KeyError
	      +-- MemoryError
	      +-- NameError
	      |    +-- UnboundLocalError
	      +-- OSError
	      |    +-- BlockingIOError
	      |    +-- ChildProcessError
	      |    +-- ConnectionError
	      |    |    +-- BrokenPipeError
	      |    |    +-- ConnectionAbortedError
	      |    |    +-- ConnectionRefusedError
	      |    |    +-- ConnectionResetError
	      |    +-- FileExistsError
	      |    +-- FileNotFoundError
	      |    +-- InterruptedError
	      |    +-- IsADirectoryError
	      |    +-- NotADirectoryError
	      |    +-- PermissionError
	      |    +-- ProcessLookupError
	      |    +-- TimeoutError
	      +-- ReferenceError
	      +-- RuntimeError
	      |    +-- NotImplementedError
	      +-- SyntaxError
	      |    +-- IndentationError
	      |         +-- TabError
	      +-- SystemError
	      +-- TypeError
	      +-- ValueError
	      |    +-- UnicodeError
	      |         +-- UnicodeDecodeError
	      |         +-- UnicodeEncodeError
	      |         +-- UnicodeTranslateError
	      +-- Warning
	           +-- DeprecationWarning
	           +-- PendingDeprecationWarning
	           +-- RuntimeWarning
	           +-- SyntaxWarning
	           +-- UserWarning
	           +-- FutureWarning
	           +-- ImportWarning
	           +-- UnicodeWarning
	           +-- BytesWarning
	           +-- ResourceWarning
##3.异常检测处理
try-except语句，语法：

	try：
		检测范围
	except Exception[as reason]:	//Exception是异常名，reason是指异常信息，
		c出现异常(Exception)后的处理代码
	finally：
		无论如何都会被执行的代码
	例如：
	try:
		f = open('nofile.txt')
		print(f.read())
		f.close()
	except OSError as reason:
		print('出错了，原因是：'+str(reason))

raise语句引发异常

	raise [异常名（'要显示异常的具体信息'）]
#6.6
tips:
1. 建议不要在IDLE上运行EasyGui
2. 对于函数而言前两个参数是消息和标题，几乎所有的组件都会显示一个标题和消息，标题默认空白字符串，信息是一个简单的默认值
3. 按钮组件可不带参数地调用它，当选择cancel或者关闭窗口的时候返回一个布尔值
4. msgbox(msg,title,ok_button,image,root)该方法显示一个消息和提供一个OK按钮，可以指定消息，标题，按钮，建议使用关键字参数调用
5. 

##1.else语句和with语句
- 丰富的else语句	

	1. if...else...语句
	2. else和while语句配合，当while语句全部被执行不会执行else语句，如果中途跳出执行else语句
	3. 跟在异常处理语句后，如果没有异常执行else中的语句

- 简洁的with语句

		try:
			with open('test.txt','w') as f	//会自动查看文件是否使用完毕，自动调用close方法
				for each_line in f:
					print(each_line)
		except OSError as reason:
			print('出错啦'+str(reason))	
##2.EasyGui图形界面入门
1. 安装easyGui

	下载安装包解压后，使用cmd命令切换到解压后的目录下使用命令Python setup.py install安装
2. 导入easyGui

		方法一：
		import easygui
		easygui.msgbox(...)		//使用此方法必须使用easygui开头才能调用其方法
		方法二：
		from easygui import *
		msgbox(...)		//导入全部包可省略开头，不建议使用
		方法三：
		import easygui as g
		g.msgbox(....)
3. 简单例子

		import easygui as f
		import sys
		
		while 1:
		    f.msgbox("欢迎进入游戏界面")		//对于函数而言前两个参数是消息和标题，几乎所有的组件都会显示一个标题和消息，									标题默认空白字符串，信息是一个简单的默认值

		    msg = "请问你想学什么呢？"
		    title = "小游戏互动"
		    choices = ["篮球","足球","乒乓球","网球"]		
		    choice = f.choicebox(msg,title,choices)		
		    f.msgbox("您的选择是："+str(choice),"结果")	//msgbox(msg,title,ok_button,image,root)该方法显示一个消息												和提供一个OK按钮，可以指定消息，标题，按钮，建议使用关键字参数调											用

		    msg = "您希望重新开始吗？"
		    title = "请选择"
		    if f.ccbox(msg,title):			//按钮组件可不带参数地调用它，当选择cancel或者关闭窗口的时候返回一个布尔值
											ccbox(msg,title,choices=('continue','cancel'),image)该方法提供一个选择continue和cancel，相应的返回1或者0
		        pass
		    else:
		        sys.exit(0)
- msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None)该方法显示一个消息	和提供一个OK按钮，可以指定消息，标题，按钮，建议使用关键字参数调用
- ccbox(msg='Shall I continue?', title=' ', 
- s=('Continue', 'Cancel'), image=None)该方法提供一个选择continue和cancel，相应的返回1或者0
- ynbox(msg,title,choices('yes','no'),image=none)和ccbox相同
- buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。如果用户取消取消或者关闭窗口，那么会返回默认选项（第一个选项）。
- indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None) 基本跟上面一样，区别就是当用户选择第一个按钮的时候返回序列号0，选择第二个按钮时候返回序列号1。
- boolbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None) 如果第一个按钮被选中则返回 1，否则返回 0。
- 当你调用一个 buttonbox 函数（例如 msgbox(), ynbox(), indexbox() 等等）的时候，你还可以为关键字参数 image 赋值，这是设置一个 .gif 格式的图像（注意仅支持 GIF 格式
- choicebox(msg='Pick something.', title=' ', choices=())为用户提供了一个可选择的列表，使用序列（元祖或列表）作为选项，这些选项显示前会按照不区分大小写的方法排好序。
- multchoicebox(msg='Pick as many items as you like.', title=' ', choices=(), **kwargs)multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。
- enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)为用户提供一个最简单的输入框，返回值为用户输入的字符串。默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。
- integerbox(msg='', title=' ', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入。
- multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=()) 为用户提供多个简单的输入框，要注意以下几点：

		如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
		如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
		如果用户取消操作，则返回域中的列表的值或者None值
- passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)passwordbox() 跟 enterbox() 样式一样，不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串
- multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（"*"）
- textbox(msg='', title=' ', text='', codebox=0)textbox() 函数默认会以比例字体（参数 codebox=1 设置为等宽字体）来显示文本内容（会自动换行哦），这个函数适合用于显示一般的书面文字。 
		
		注：text 参数（第三个参数）可以是字符串类型，列表类型，或者元祖类型。



#6.7
tips：

##1.类和对象
- 属性（变量）加方法（函数）统称对象
- class定义类，类名首字母大写
- 创建一个类的对象叫做类的实例化	

		class Text:
	    color = 'green'
	    weight = 10
	    legs = 4
	
	    def climb(self):
	        print('你好')
	    def run(self):
	        print('我好')
	    def bite(self):
	        print('大家好')
		调用
		tt = Text()
		tt.climb()
1. 封装，信息隐蔽技术
2. 继承，子类自动共享父类之间的数据和方法的机制

		class MyList1(list):	//括号内表示继承list
			pass
		list2 = MyList1()
		list2.append(3)
		list2.append(6)
		list2.append(9)
3. 多态，不同对象对同一方法响应不同的行动

		class A:
			def fun(self):
				print('我是A。。')
		class B:
			def fun(self):
				print('我是B。。')
		a = A()
		b = B()
		a.fun()
		b.fun()

#6.8
tips:

##1.面向对象编程
- Python中的self相当于Java中的this，对象的方法被调用时，对象会把自身作为第一个参数传递给方法
- __init__(self)是构造方法，前后两个


- 公有和私有的，公有的可直接使用.连接方法名使用，定义私有的需要在方法名或者变量名前加__(双
- )，私有的基本只能在内部引用，可使用_类名__属性名调用
- 

##2.继承
语法如下：

	class sonclassname(fatherclassname):	
	//sonclass子类，fatherclass又叫做基类父类或超类
		.......
- 子类重写父类方法，创建子类对象，调用该方法用的是子类方法
- 调用未绑定的父类方法和使用super()方法两种技术
- 支持多重继承,谨慎使用

		class sonclassname(name1,name2,name3...):
			......

示例

	import random as r

	class Fish:
	    def __init__(self):
	        self.x = r.randint(0,10)
	        self.y = r.randint(0,10)
	    def move(self):
	        self.x -= 1
	        print("我的位置是",self.x,self.y)
	        
	class Godfish(Fish):
	        pass
	class Carp(Fish):
	        pass
	class Salmon(Fish):
	        pass
	class Shark(Fish):
	    def _init_(self):
	        super()._init_() 
	        self.hungry = True
	    def eat(self):
	        if self.hungry:
	            print("那就吃了吧")
	        else:
	            print("吃不下")

##3.组合
就是把类的实例化放到新的类中，示例

	
	class Turtle:
	    def __init__(self,x):
	        self.num = x
	
	class Fish:
	    def __init__(self,x):
	        self.num = x
	
	class Pool:
	    def __init__(self,x,y):
	        self.turtle = Turtle(x)
	        self.fish = Fish(y)
	
	    def print_num(self):
	        print("水中有龟%d只，鱼%d条"%(self.turtle.num,self.fish.num)
- 不要在一个类里面定义所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
- 用不同词性的名词命名属性和方法	

##4.绑定
- Python严格要求方法需要有实例才能被调用，这种限制就是所谓绑定概念

- 定义一个类，使得产生一个这个类的实例，类的一个变量就自加

		class A(object):
		    count = 0
		
		    def __init__(self):
		        A.count += 1
			def print1(self):
				print(A.count)

#6.10-6.15
tips:

1. 名称前的单下划线（如：_shahriar）用于指定该名称属性为“私有”只供内部使用
2. 在参数名之前使用一个星号，就是让函数接受任意多的位置参数。

##1.相关内置函数BIF
- issubclass(class,classinfo)方法用于判断参数 class 是否是类型参数 classinfo 的子类
- isinstance(object, classinfo)函数来判断一个对象是否是一个已知的类型，类似 type()
	
	- object -- 实例对象。
	- classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组

			sinstance() 与 type() 区别：
			type() 不会认为子类是一种父类类型，不考虑继承关系。		
			isinstance() 会认为子类是一种父类类型，考虑继承关系
- hasattr(object, 
- ) 函数用于判断对象是否包含对应的属性

	- object -- 对象。
	- name -- 字符串，属性名。

- getattr(object, name[, default]) 函数用于返回一个对象属性值。

	- object -- 对象。
	- name -- 字符串，对象属性。
	- default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

- setattr(object, name, value)函数对应函数 getatt()，用于设置属性值，该属性必须存在。

	- object -- 对象。
	- name -- 字符串，对象属性。
	- value -- 属性值。
- delattr(object, name)函数用于删除属性

	- object -- 对象。
	- name -- 必须是对象属性。

- property([fget[, fset[, fdel[, doc]]]])函数的作用是在新式类中返回属性值。

	- fget -- 获取属性值的函数
	- fset -- 设置属性值的函数
	- fdel -- 删除属性值函数
	- doc -- 属性描述信息
##2.魔法方法
总被双下划线包围如__init__(self[,...])

1. 基本方法

		__new__(cls[,*argv]) cls：代表一个类的名称;  self：代表一个实例对象的名称
		
				1. __new__ 是在一个对象实例化的时候所调用的第一个方法
				2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法
				3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用
				4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string
		__init__(self[,*argv])构造器，当一个实例对象被定义时调用,类似于构造函数
		__del__(self)析构器，当删除一个实例对象时调用
		__call__(self[,*argv])允许一个类像函数一样被调用　　class_x(a,b)实际调用的是class_x.__call__(a,b) 
		__len__(self)	获得实例对象的长度 与调用函数 len(obj)一样的结果 
		__repr__(self)	将实例对象转化为字符串的形式。如 ls=[1,2,3], 则repr(ls)为 '[1,2,3]'，与函数repr(obj)功能相同
		__str__(self)	 将实例对象转化为字符串的形式	与repr()的区别在于：str(obj)的字符串是打印出来让人看的，更加亲民，而repr(obj)是给解释器看的；
		
				若 a = xxx(列表、字典、元祖或集合等)
				eval(repr(a)) == a  成立
				eval(str(a)) == a    不一定成立
		
		__int__(self)	定义当被 int() 调用时的行为	 
		__float__(self)　	定义当被 float() 调用时的行为	 
		__round__(self[, n])	当被round()调用时的行为	round(digit[, n]) 将digit数字保留n位精度
		__hash__(self)	定义能被 hash() 调用的行为 
		__bytes__(self)	 定义被 bytes() 调用的行为	 
		__bool__(self)	定义被 bool() 调用的行为 返回True(1) 或 False(0) 
		__format__(self, form)定义被 format()调用的行为 
 
2. 运算符方法
		
		__add__(self, other)加法：+ 
			
			class new_int(int):
				def __add__(self,other):
					return int(self) + int(other)	//必须这样做否则会出现递归异常
				def __sub__(self,other):
					return int(self) - int(other)
			a = new_int(3)
			b = new_int(5)
			a + b		//结果为8
		__sub__(self, other) 减法：-	 
		__mul__(self,other) 乘法：* 
		__truediv(self, other)	除法：/	注意是 truediv 
		__floordiv(self, other)	整数除法：//	 floor()即为向下取整的意思
		__mod__(self, other) 求余：%	 
		__pow__(self, other[, mod])	乘方：** 
				
				pow(x,y[,z]),
				若无Z，则为 return x**y
				若有Z，则为 return x**y%z
		
		__divmod__(self, other)	divmode() 返回值为元祖  (商值，余数) 
		__lshift__(self, other) 左移：<<	 
		__rshift__(self, other)	右移：>>  
		__and__(self, other)	按位与：&	注意以下均为按位操作，非逻辑操作 
		__or__(self, other)	按位或：| 
		__xor__(self, other)	按位异或：^	 

3. 反运算符方法  

		__radd__(self, other)加法，如a+b，当a不支持__add__()操作时，调用此函数； 即在运算符的基础上加上 'r' 即可，以下雷同

			class new_rint(int):
				 def __radd__(self,other):
					return int.__sub__(self,other)
			a = new_int(3)
			b = new_int(5)
			a + b		//结果为8
			1 + b		//结果为4
		__rsub__(self, other)	other - self  
		…………	 
	 
4. 增量赋值运算符方法  

		__iadd__(self, other)赋值加法：+=　　 即在赋值运算符之前加 'i' ,以下雷同 

			class new_rint(int):
				def __iadd__(self,other):
					return int.__sub__(self,other)
			a = new_int(3)
			b = new_int(5)
			a + b		//结果为8
			a += b		//结果为-2
		__isub__(self, other) 赋值减法：-=   self = self - other 
		………… 
 	 
5. 一元操作符方法  

		__pos__(self)	定义正号：+x	 
		__neg__(self)	定义负号：-x	 
		__abs__(self)	取绝对值,定义当被abs()方法调用时的行为
			class new_test(int):
				def __abs__(self):
					return int(self)+1
			a = abs(new_test(-1))		//a的值为0
		__invert__(self)	按位求反：~x	 

6. 比较操作符方法  

		__gt__(self, other)	大于：>	 
		__ge__(self, other)	大于等于：>=	 
		__lt__(self, other)	小于：<	 
		__le__(self, other)	小于等于：<=	 
		__eq__(self, other)	相等：==	 
		__ne__(self, other)	不等：！=	 

7. 属性操作  

描述符就是将某种特殊类型的类的实例指派给另一个类的属性，特殊类型是指至少实现__get__或__set__或__delete__的一类方法

		__getattr__(self, name)	当用户访问一个不存在的属性时调用	注意 object/super() (所有类的基类) 是无该方法的
		__getattribute(self, name)	访问存在的属性时调用	先调用此函数，如找不到该属性，再去调用上面的属性
		__setattr__(self, name, value)	设置属性时调用	 
		__delattr__(self, name)	删除一个属性时调用	 
		示例：	
			class Rectangle:
			    def __init__(self,width = 0,height = 0):
			        self.width = width
			        self.height = height
			
			    def __setattr__(self,nam,value):
			        if name == 'square':
			            self.width = value
			            self.height = value
			        else:
			            super().__setattr__(name,value)
			
			    def getArea(self):
			        return self.width * self.height

		property(fget=None, fset=None, fdel=None, doc=None)	是一个类，主要功能是为了方便类内部函数的调用	

示例
			
		class Celsius:
		    def __init__(self,value = 26):
		        self.value = float(value)
		
		    def __get__(self,instance,owner):
		        return self.value
		
		    def __set__(self,instance,value):
		        self.value = float(value)
		
		class Fahrenheit:
		    def __init__(self,value = 78.8):
		        self.value = float(value)
		        
		    def __get__(self,instance,owner):
		        return instance.cel * 1.8 + 32
		
		    def __set__(self,instance,value):
		        instance.cel = (float(value) - 32) / 1.8
					
		class Temperature:
		    cel = Celsius()
		    fah = Fahrenheit()

			x = Temperature()
			x.cel = 100
			x.fah		//结果为212
			x.fah = 100
			x.cel		//结果为86		

		__get__(self, instance, owner)	描述符被访问时调用	想详细了解，请点击这里
		__set__(self, instance, value)	描述符被改变时调用	 
		__delelte__(self, instance, value)删除描述符时调用	 

8. 容器类型操作  
定制的容器不可变的话，只需定义以下前两个，可变需定义前四个

		__len__(self)定义当被 len() 调用时的行为（返回容器中元素的个数）可变和非尅便容器均具备 __len__ 和 __getitem__
		__getitem__(self, key)	获取容器中指定元素的行为	相当于 self[key] 
		__setitem__(self, key, value)	设置容器中指定元素的行为	相当于 self[key] = value 只有可变容器拥有 __setitem__ 和 __delitem__
		__delitem__(self, key)	删除容器中指定元素的行为	del self[key] 


		__iter__(self)	定义迭代器中元素的行为	 ，调用到没有时会出现stopiteration异常 
		__reversed__(self)	当调用reversed()函数时	 
		__contains__(self, item)	成员运算符in/ not in的行为	 

示例：
		
		class CountList:
		    def __init__(self,*args):
		        self.values = [x for x in args]
		        self.count = {}.fromkeys(range(len(self.values)),0)
		
		    def __len__(self):
		        return len(self.values)
		
		    def __getitem__(self,key):
		        self.count[key] += 1
		        return self.values[key]
		
		>>> c1 = CountList(1,3,5,7,9)
		>>> c2 = CountList(2,4,6,8,10)
		>>> c1[1]
		3
		>>> c1[1]+c2[1]
		7
		>>> c1.count
		{0: 0, 1: 2, 2: 0, 3: 0, 4: 0}	//返回调用该键值的次数
		>>> c2.count
		{0: 0, 1: 1, 2: 0, 3: 0, 4: 0}

		
		class Fibs:
		    def __init__(self,n=10):
		        self.a = 0
		        self.b = 1
		        self.n = n
		
		    def __iter__(self):
		        return self
		
		    def __next__(self):
		        self.a,self.b = self.b,self.a+self.b
		        if self.a>self.n:
		            raise StopIteration
		
		        return self.a
		
		>>> fibs = Fibs()
		>>> for each in fibs:
			print(each)
		
			
		1
		1
		2
		3
		5
		8

		
 PS: ①.以上所有的魔法方法，君采用__xx__形式（__为双 "_"，双下划线）

　　 ②.以上魔法方法为Python解释器自动调用，当然也可以手动调用

　　 ③.魔法方法Python解释器自动给出默认的，因此除非需要改变其内部功能，其它时刻刻使用默认魔法方法

　　 ④.魔法方法是针对class而言的，脱离了”类“谈magic_method是没有意义的

　　 ⑤.*argv为可变的参数列表，类似C语言的va(variable argument),注意与指针的区别，python中暂时忘掉指针，因为python的内存机制都是解释器自动完成的
##3.time模块，时间的获取和转换
在 Python 中，与时间处理有关的模块包括：time，datetime 以及 calendar

- 时间戳（timestamp）的方式：通常来说，时间戳表示的是从 1970 年 1 月 1 日 00:00:00 开始按秒计算的偏移量（time.gmtime(0)）此模块中的函数无法处理 1970 纪元年以前的日期和时间或太遥远的未来（处理极限取决于 C 函数库，对于 32 位系统来说，是 2038 年）
- UTC（Coordinated Universal Time，世界协调时）也叫格林威治天文时间，是世界标准时间。在中国为 UTC+8
- DST（Daylight Saving Time）即夏令时的意思
- 一些实时函数的计算精度可能低于它们建议的值或参数，例如在大部分 Unix 系统，时钟一秒钟“滴答”50~100 次

时间元祖（time.struct_time）：gmtime()，localtime() 和 strptime() 以时间元祖（struct_time）的形式返回。

			索引值（Index）	属性（Attribute）	值（Values）
				0				tm_year（年）	（例如：2015）
				1				tm_mon（月）		1 ~ 12
				2				tm_mday（日）	1 ~ 31
				3				tm_hour（时）	0 ~ 23
				4				tm_min（分）		0 ~ 59
				5				tm_sec（秒）		0 ~ 61（60 代表闰秒，61 是基于历史原因保留。）
				6			tm_wday（星期几）		0 ~ 6（0 表示星期一）
				7			tm_yday（一年中的第几天）	1 ~ 366
				8			tm_isdst（是否为夏令时）	0， 1， -1（-1 代表夏令时）

1. time.altzone返回格林威治西部的夏令时地区的偏移秒数；如果该地区在格林威治东部会返回负值（如西欧，包括英国）；对夏令时启用地区才能使用。
2. time.asctime([t])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2015"（2015年12月11日 周二 18时07分14秒）的 24 个字符的字符串。
3. time.clock()用以浮点数计算的秒数返回当前的 CPU 时间。用来衡量不同程序的耗时，比 time.time() 更有用。
Python 3.3 以后不被推荐，由于该方法依赖操作系统，建议使用 perf_counter() 或 process_time() 代替（一个返回系统运行时间，一个返回进程运行时间，请按照实际需求选择）
4. time.ctime([secs]) 作用相当于 asctime(localtime(secs))，未给参数相当于 asctime()
5. time.gmtime([secs])接收时间辍（1970 纪元年后经过的浮点秒数）并返回格林威治天文时间下的时间元组 t（注：t.tm_isdst 始终为 0）
6. time.daylight如果夏令时被定义，则该值为非零。
7. time.localtime([secs])接收时间辍（1970 纪元年后经过的浮点秒数）并返回当地时间下的时间元组 t（t.tm_isdst 可取 0 或 1，取决于当地当时是不是夏令时）
8. time.mktime(t)接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）
9. time.perf_counter()返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
10. time.process_time() 返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。
11. time.sleep(secs)推迟调用线程的运行，secs 的单位是秒。
12. time.strftime(format[, t]) 把一个代表时间的元组或者 struct_time（如由 time.localtime() 和 time.gmtime() 返回）转化为格式化的时间字符串。如果 t 未指定，将传入 time.localtime()。如果元组中任何一个元素越界，将会抛出 ValueError 异常。

format 格式如下：

		格式	含义	备注
		%a	本地（locale）简化星期名称	
		%A	本地完整星期名称	
		%b	本地简化月份名称	
		%B	本地完整月份名称	
		%c	本地相应的日期和时间表示	
		%d	一个月中的第几天（01 - 31）	
		%H	一天中的第几个小时（24 小时制，00 - 23）	
		%l	一天中的第几个小时（12 小时制，01 - 12）	
		%j	一年中的第几天（001 - 366）	
		%m	月份（01 - 12）	
		%M	分钟数（00 - 59）	
		%p	本地 am 或者 pm 的相应符	注1
		%S	秒（01 - 61）	注2
		%U	一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周	注3
		%w	一个星期中的第几天（0 - 6，0 是星期天）	注3
		%W	和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始	
		%x	本地相应日期	
		%X	本地相应时间	
		%y	去掉世纪的年份（00 - 99）	
		%Y	完整的年份	
		%z	用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）	
		%Z	时区的名字（如果不存在为空字符）	
		%%	%号本身	

		注1：“%p”只有与“%I”配合使用才有效果。
		注2：范围真的是 0 ~ 61（你没有看错哦^_^）；60 代表闰秒，61 是基于历史原因保留。
		注3：当使用 strptime() 函数时，只有当在这年中的周数和天数被确定的时候 %U 和 %W 才会被计算。

		举个例子：
		# I love FishC.com!
		>>> import time as t
		>>> t.strftime("a, %d %b %Y %H:%M:%S +0000", t.gmtime())
		'a, 24 Aug 2014 14:15:03 +0000'

13. time.strptime(string[, format])把一个格式化时间字符串转化为 struct_time。实际上它和 strftime() 是逆操作。

		举个例子：
		# I really love FishC.com!
		>>> import time as t
		>>> t.strptime("30 Nov 14", "%d %b %y")
		time.struct_time(tm_year=2014, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=334, tm_isdst=-1)


14. time.time()返回当前时间的时间戳（1970 纪元年后经过的浮点秒数）
15. time.timezone 属性是当地时区（未启动夏令时）距离格林威治的偏移秒数（美洲 >0；大部分欧洲，亚洲，非洲 <= 0）
16. time.tzname 属性是包含两个字符串的元组：第一是当地非夏令时区的名称，第二个是当地的 DST 时区的名称。

#6.19
tips：

##1.Python的生成器
一般函数中使用yield关键字，可以实现一个最简单的生成器，此时这个函数变成一个生成器函数。yield与return返回相同的值，区别在于return返回后，函数状态终止，而yield会保存当前函数的执行状态，在返回后，函数又回到之前保存的状态继续执行

1. 生成器函数与一般函数的不同

	- 生成器函数包含一个或者多个yield
	- 当调用生成器函数时，函数将返回一个对象，但是不会立刻向下执行
	- 像__iter__()和__next__()方法等是自动实现的，所以我们可以通过next()方法对对象进行迭代
	- 一旦函数被yield，函数会暂停，控制权返回调用者
	- 局部变量和它们的状态会被保存，直到下一次调用
	- 函数终止的时候，StopIteraion会被自动抛出 

示例： 简单的生成器函数

	def my_gen():
		n = 1
		print("first")
		yield n
		n+=1
		print("second")
		yield n
		n+=1
		print("third")
		yield n

	>>> a=my_gen()
	>>> print(next(a))
	first
	1
	>>> print(next(a))
	second
	2
	>>> print(next(a))
	third
	3
	>>> print(next(a))
	Traceback (most recent call last):
	  File "<pyshell#15>", line 1, in <module>
	    print(next(a))
	StopIteration

使用循环的生成器

	def rev_str(my_str):
	    length=len(my_str)
	    for i in range(length-1,-1,-1):	//负数表示倒叙
	        yield my_str[i]
	
	for char in rev_str("hello"):
	    print(char)

2. 生成器的表达式
Python中，有一个列表生成方法，比如

		# 产生1,2,3,4,5的一个列表
		[x for x in range(5)]
		如果换成[]换成()，那么会成为生成器的表达式。
		
		(x for x in range(5))
		具体使用方式：
		
		a=(x for x in range(10))
		b=[x for x in range(10)]
		# 这是错误的，因为生成器不能直接给出长度
		# print("length a:",len(a))
		
		# 输出列表的长度
		print("length b:",len(b))
		
		b=iter(b)
		# 二者输出等价，不过b是在运行时开辟内存，而a是直接开辟内存
		print(next(a))
		print(next(b)) 

3. 为什么使用生成器

	- 更容易使用，代码量较小
	- 内存使用更加高效。比如列表是在建立的时候就分配所有的内存空间，而生成器仅仅是需要的时候才使用，更像一个记录
	- 代表了一个无限的流。如果我们要读取并使用的内容远远超过内存，但是需要对所有的流中的内容进行处理，那么生成器是一个很好的选择，比如可以让生成器返回当前的处理状态，由于它可以保存状态，那么下一次直接处理即可。
	- 流水线生成器。假设我们有一个快餐记录，这个记录的地4行记录了过去五年每小时售出的食品数量，并且我们要把所有的数量加在一起，求解过去5年的售出的总数。假设所有的数据都是字符串，并且不可用的数字被标记成N/A。那么可以使用下面的方式处理：
	
		with open('sells.log') as file:
		    pizza_col = (line[3] for line in file)
		    per_hour = (int(x) for x in pizza_col if x != 'N/A')  # 使用生成器进行自动迭代
		    print("Total pizzas sold = ",sum(per_hour))

#6.20-22
tips:


##1.模块

	容器：数据的封装
	函数：语句的封装
	类：方法和属性的封装
	模块：模块就是程序
导入模块三种方法：

	1. import 模块名
	2. from 模块名 import 函数名
	3. import 模块名 as 新名字（推荐第三种）

- if __name__ == '__main__'：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

		- __name__是内置变量，可用于反映一个包的结构。
		- __name__是内置变量，可用于表示当前模块的名字


- 搜索路径，使用sys模块的path方法，可获取文件可存放路径。

		>>> import sys
		>>> sys.path
		['', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages', 'C:\\Users\\lvqih\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\easygui-0.98.0_unreleased-py3.7.egg']
	由于可存放的路径是一个列表，所以我们可以向里面添加路径

		sys.path.append('D:\\Android\\python\\python-demo')

- 包（package）创建方法：

	1. 创建一个文件夹，用于存放相关的模块，文件夹的名字即报的名字
	2. 在文件夹中创建一个__init__.py的模块文件，内容可以为空
	3. 将相关模块放入到文件夹中

导入模块时，只需在模块前面加上(包名.)
##2.python标准库

##3.爬虫
- Python访问互联网，urllib包由urllib.request，urllib.error，urllib.parse，urllib.robotparser四个模块构成 

	- url的一般格式为（带[]的可选）：
	
			Protocol://hostname[:port]/path/[;parameters][?query]#fragment
	- url由三部分构成
			
		1. 第一部分是协议：http，https,ftp,file,ed2k...
		2. 第二部分是存放资源的服务器的域名系统或ip地址（有时候要包含端口号，各种协议都有默认的端口号，如http的默认端口号为80）
		3. 第三部分是资源的具体地址，如目录或文件名等

示例：

	>>> import urllib.request     //导入模块
	>>> response = urllib.request.urlopen("https://www.baidu.com/")     //加载链接地址
	>>> html = response.read()      //读取链接地址内容
	>>> print(html)      //打印
	b'<html>\r\n<head>\r\n\t<script>\r\n\t\tlocation.replace(location.href.replace("https://","http://"));\r\n\t</script>\r\n</head>\r\n<body>\r\n\t<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>\r\n</body>\r\n</html>'
	>>> html = html.decode("utf-8")      //将其内容进行重新编码
	>>> print(html)
	<html>	
	<head>	
		<script>	
			location.replace(location.href.replace("https://","http://"));	
		</script>	
	</head>	
	<body>	
		<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>	
	</body>	
	</html>
	
-  实战：

		import urllib.request

		req = urllib.request.Request('http://placekitten.com/g/500/600')
		response = urllib.request.urlopen(req)
		
		cat_img = response.read()
		
		with open('cat_500_600.jpg','wb') as f:
		    f.write(cat_img)
使用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。例如file的file.close()方法，无论with中出现任何错误，都会执行file.close（）方法其次with只有特定场合下才能使用。，这个特定场合只的是那些支持了上下文管理器的对象。这些对象有：

	file
	decimal.Context
	thread.LockType
	threading.Lock
	threading.RLock
	threading.Condition
	threading.Semaphore
	threading.BoundedSemaphore
上下文管理器就是在对象内实现了两个方法：__enter__() 和__exit__()

　　__enter__()方法会在with的代码块执行之前执行，__exit__（）会在代码块执行结束后执行。
　　__exit__()方法内会自带当前对象的清理方法。

这个urlopen函数总是返回一个对象，这个对象能被context manager（上下文管理器）中的一些方法使用，如：

	geturl() — 返回一个资源索引的URL，通常重定向后的URL照样能get到。
	info() — 返回页面的元信息，如头信息。像 email.message_from_string() 实例的格式一样。（请看 Quick Reference to HTTP Headers）
	getcode() – 返回响应后，HTTP的状态码。

- 实战2，有道翻译

		import urllib.request
		import urllib.parse
		import json				//导入json模块，处理数据结果需要使用
		
		content = input("请输入要翻译的内容")
		
		url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'		//翻译地址
		data = {}
		data['i'] = content
		data['from'] = 'AUTO'
		data['to'] = 'AUTO'
		data['smartresult'] = 'dict'
		data['client'] = 'fanyideskweb'
		data['salt'] = '1529660044390'
		data['sign'] = '093569408e9469545bafc4e72e1b06a3'
		data['doctype'] = 'json'
		data['version'] = '2.1'
		data['keyfrom'] = 'fanyi.web'
		data['action'] = 'FY_BY_CLICKBUTTION'
		data['typoResult'] = 'false'
		//以上为form Data内容
		data = urllib.parse.urlencode(data).encode('utf-8')		//将映射对象或两元素元组序列，可以包含str或字节对象，转换为百分号编码的ASCII文本字符串，并使用utf-8进行编码
		
		response = urllib.request.urlopen(url,data)		//加载地址，若本次HTTP请求要用POST方法，data必须有数据；若为GET方法时， data写None就行。data参数应该是一个标准的application/x-www-form-urlencoded 格式的缓冲区
		html = response.read().decode('utf-8')		//读取内容，并对其进行utf-8编码，是一个json格式文本
		
		target = json.loads(html)		//使用json进行加载读取
		print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

- 隐藏Python访问信息

	- 修改headers，通过request的headers参数修改或通过request.add_header()方法修改
	
		import urllib.request
		...
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
		...		
		data = urllib.parse.urlencode(data).encode('utf-8')
		req = urllib.request.Request(url,data,head)
		response = urllib.request.urlopen(req)
		...
		print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

		或者

		import urllib.request
		...
		
		data = urllib.parse.urlencode(data).encode('utf-8')
		
		req = urllib.request.Request(url,data)
		req.add_headers('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
		response = urllib.request.urlopen(req)
		...
		print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

	- 延迟提交时间，加入time模块

		import urllib.request
		import urllib.parse
		import json
		import time
		
		while True:
		    content = input("请输入要翻译的内容(输入'q!'退出程序)")
		    if content == 'q!':
		        break
		    .....
		    time.sleep(5)
	- 使用代理，步骤
		
		1. 参数是一个字典{'类型':'代理ip:端口号'}

			proxy_support=urllib.request.ProxyHandler({})
		2. 定制，创建一个opener

			opener=urllib.request.build_opener(proxy_support)
		3. 安装.调用opener

			urllib.request.intall_opener(opener)
			opener.open(url)

		import urllib.request
		import random
		
		url = 'http://www.whatismyip.com.tw/'		//查询地址
		
		iplist = ['60.216.177.152:8118','118.190.95.26:9001','171.12.133.160:47102']
		
		proxy_support = urllib.request.ProxyHandler({'https':random.choice(iplist)})
		
		opener = urllib.request.build_opener(proxy_support)
		opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')]
		
		urllib.request.install_opener(opener)
		
		response = urllib.request.urlopen(url)
		html = response.read().decode('utf-8')
		
		print(html)

#6.23-26
tips:
1. 元字符在方括号中不会触发“特殊功能”，在字符类中，它们只匹配自身。例如 [akm$] 会匹配任何字符 'a'，'k'，'m' 或 '$'，'$' 是一个元字符，但在方括号中它不表示特殊含义，它只匹配 '$' 字符本身。
2. 

##1.爬取图片
实例（目前不能用）：

	import urllib.request
	import os
	import random
	
	def url_open(url):			//隐藏信息相关方法
	    req = urllib.request.Request(url)
	    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
	
	    proxies = ['118.190.95.43:9001','61.135.217.7:80','110.83.172.124:28214']
	    proxy = random.choice(proxies)
	
	    proxy_support = urllib.raquest.ProxyHandler({'http':proxy})
	    opener = urllib.request.build_opener(proxy_support)
	    urllib.request.install_opener(opener)
	
	    response = urllib.request.urlopen(url)
	    html = response.read()
	
	    return html
	
	def get_page(url):
	    html = url_open(url).decode('utf-8')
	
	    a = html.find('current-comment-page') + 23
	    b = html.find(']',a)
	
	    return html[a:b]
	
	def find_imgs(url):
	    html = url_open(url).decode('utf-8')
	    img_addrs = []
	
	    a = html.find('image src=')
	
	    while a != -1:
	        b = html.find('.jpg',a,a+255)
	        if b != -1:
	            img_addrs.append(html[a+9,b+4])
	        else:
	            b = a + 9
	
	        a = html.find('img src=',b)
	
	    return img_addrs
	
	def save_img(folder.img_addrs):
	    for each in img_addrs:
	        filename = each.split('/')[-1]
	        with open(filename,'wb') as f:
	            img = url_open(each)
	            f.write(image)
	
	def download_mm(folder='ooxx',pages=10):
	    os.mkdir(folder)
	    os.chdir(folder)
	
	    url = "http://jandan.net/ooxx/"
	    page_num = int(get_page(url))
	
	    for i in range(pages):
	        page_num -= i
	        page_url = url+'page-'+str(page_num)+'#comments'
	        img_addrs = find_imgs(page_url)
	        save_image(folder,img_addrs)
	
	if __name__ == '__main__':
	    download_mm()

##2.正则表达式
正则表达式（Regular expressions 也称为 REs，或 regexes 或 regex patterns）本质上是一个微小的且高度专业化的编程语言。它被嵌入到 Python 中，并通过 re 模块提供给程序猿使用。

	import re
	re.search(r'FishC','I love FishC.com')		//第一个参数为表达式，必须以r开头，后跟表达式，表达式用单引号括起，第二个参数被查找的目标
- 字符匹配，有少数特殊的字符我们称之为元字符（metacharacter），它们并不能匹配自身，它们定义了字符类、子组匹配和模式重复次数等。有以下几个：'.','^','$','*','+','?','{ }','[ ]','\','|','( )'

	1. 括号 [ ]，它们指定一个字符类用于存放你需要匹配的字符集合。可以单独列出需要匹配的字符，也可以通过两个字符和一个横杆 - 指定匹配的范围。例如 [abc] 会匹配字符 a，b 或 c；[a-c] 可以实现相同的功能。后者使用范围来表示与前者相同的字符集合。如果你想只匹配小写字母，你的 RE 可以写成 [a-z]。可以匹配方括号中未列出的所有其他字符。做法是在类的开头添加一个脱字符号 ^ ，例如 [^5] 会匹配除了 '5' 之外的任何字符。
	2. 反斜杠 \ 了。跟 Python 的字符串规则一样，如果在反斜杠后边紧跟着一个元字符，那么元字符的“特殊功能”也不会被触发。例如你需要匹配符号 [ 或 \，你可以在它们前面加上一个反斜杠，以消除它们的特殊功能：\[，\\。
		
		特殊字符             含义
		\d 				匹配任何十进制数字；相当于类 [0-9]
		\D 				与 \d 相反，匹配任何非十进制数字的字符；相当于类 [^0-9]
		\s 				匹配任何空白字符（包含空格、换行符、制表符等）；相当于类 [ \t\n\r\f\v]
		\S 				与 \s 相反，匹配任何非空白字符；相当于类 [^ \t\n\r\f\v]
		\w 				匹配任何单词字符，相当于字符类 [a-zA-Z0-9_]
		\W 				于 \w 相反
		\b 				匹配单词的开始或结束
		\B 				与 \b 相反
	3. * 这个元字符它用于指定前一个字符匹配零次或者多次.例如 ca*t 将匹配 ct（0 个字符 a），cat（1 个字符 a），caaat（3 个字符 a），等等
	4. + 元字符,用于指定前一个字符匹配一次或者多次。和 + 的区别：* 匹配的是零次或者多次，所以被重复的内容可能压根儿不会出现；+ 至少需要出现一次。
	5. ? 用于指定前一个字符匹配零次或者一次。例如 小?甲鱼 可以匹配 小甲鱼，也可以匹配 甲鱼。
	6. 最灵活的应该是元字符 {m,n}（m 和 n 都是十进制整数），上边讲到的几个元字符都可以使用它来表达，它的含义是前一个字符必须匹配 m 次到 n 次之间。例如 a/{1,3}b 会匹配 a/b，a//b 和 a///b。但不会匹配 ab（没有斜杠）；也不会匹配 a////b（斜杠超过三个）。可以省略 m 或者 n，这样的话，引擎会假定一个合理的值代替。省略 m，将被解释为下限 0；省略 n 则会被解释为无穷大（事实上是上边我们提到的 20 亿）。
	
	import re
	re.search(r'(([01]？\d？\d|2[0-4]\d|25[0-5])\.){3}([01]？\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
	//此方法匹配IP地址
- Python3 正则表达式特殊符号及用法（详细列表）

		字符			含义
		.
				表示匹配除了换行符外的任何字符
				注：通过设置 re.DOTALL 标志可以使 . 匹配任何字符（包含换行符）
		|
				A | B，表示匹配正则表达式 A 或者 B
		^
				1. （脱字符）匹配输入字符串的开始位置,只有在开始位置时才能匹配
				2. 如果设置了 re.MULTILINE 标志，^ 也匹配换行符之后的位置
		$
				1. 匹配输入字符串的结束位置
				2. 如果设置了 re.MULTILINE 标志，$ 也匹配换行符之前的位置
		\
				1. 将一个普通字符变成特殊字符，例如 \d 表示匹配所有十进制数字
				2. 解除元字符的特殊功能，例如 \. 表示匹配点号本身
				3. 引用序号对应的子组所匹配的字符串
				4. 详见下方列举
		[...]
				字符类，匹配所包含的任意一个字符
				注1：连字符 - 如果出现在字符串中间表示字符范围描述；如果如果出现在首位则仅作为普通字符
				注2：特殊字符仅有反斜线 \ 保持特殊含义，用于转义字符。其它特殊字符如 *、+、? 等均作为普通字符匹配
				注3：脱字符 ^ 如果出现在首位则表示匹配不包含其中的任意字符；如果 ^ 出现在字符串中间就仅作为普通字符匹配
		{M,N}
				M 和 N 均为非负整数，其中 M <= N，表示前边的 RE 匹配 M ~ N 次
				注1：{M,} 表示至少匹配 M 次
				注2：{,N} 等价于 {0,N}
				注3：{N} 表示需要匹配 N 次
		*
				匹配前面的子表达式零次或多次，等价于 {0,}
		+
				匹配前面的子表达式一次或多次，等价于 {1,}
		?
				匹配前面的子表达式零次或一次，等价于 {0,1}
		*?, +?, ??
				默认情况下 *、+ 和 ? 的匹配模式是贪婪模式（即会尽可能多地匹配符合规则的字符串）；*?、+? 和 ?? 表示启用对应的非贪婪模式。
				举个栗子：对于字符串 "FishCCC"，正则表达式 FishC+ 会匹配整个字符串，而 FishC+? 则匹配 "FishC"。
		{M,N}?
				同上，启用非贪婪模式，即只匹配 M 次
		(...)
				匹配圆括号中的正则表达式，或者指定一个子组的开始和结束位置
				注：子组的内容可以在匹配之后被 \数字 再次引用 
				举个栗子：(\w+) \1 可以字符串 "FishC FishC.com" 中的 "FishC FishC"（注意有空格）
		(?...)
				(? 开头的表示为正则表达式的扩展语法（下边这些是 Python 支持的所有扩展语法）
		(?aiLmsux)
				1. (? 后可以紧跟着 'a'，'i'，'L'，'m'，'s'，'u'，'x' 中的一个或多个字符，只能在正则表达式的开头使用
				2. 每一个字符对应一种匹配标志：re-A（只匹配 ASCII 字符），re-I（忽略大小写），re-L（区域设置），re-M（多行模式）, re-S（. 匹配任何符号），re-X（详细表达式），包含这些字符将会影响整个正则表达式的规则
				3. 当你不想通过 re.compile() 设置正则表达式标志，这种方法就非常有用啦
				注意，由于 (?x) 决定正则表达式如何被解析，所以它应该总是被放在最前边（最多允许前边有空白符）。如果 (?x) 的前边是非空白字符，那么 (?x) 就发挥不了作用了。
		(?:...)
				非捕获组，即该子组匹配的字符串无法从后边获取
		(?P<name>...)
				命名组，通过组的名字（name）即可访问到子组匹配的字符串
		(?P=name)
				反向引用一个命名组，它匹配指定命名组匹配的任何内容
		(?#...)
				注释，括号中的内容将被忽略
		(?=...)
				前向肯定断言。如果当前包含的正则表达式（这里以 ... 表示）在当前位置成功匹配，则代表成功，否则失败。一旦该部分正则表达式被匹配引擎尝试过，就不会继续进行匹配了；剩下的模式在此断言开始的地方继续尝试。
				举个栗子：love(?=FishC) 只匹配后边紧跟着 "FishC" 的字符串 "love"
		(?!...)
				前向否定断言。这跟前向肯定断言相反（不匹配则表示成功，匹配表示失败）。
				举个栗子：FishC(?!\.com) 只匹配后边不是 ".com" 的字符串 "FishC"
		(?<=...)
				后向肯定断言。跟前向肯定断言一样，只是方向相反。
				举个栗子：(?<=love)FishC 只匹配前边紧跟着 "love" 的字符串 "FishC"
		(?<!...)
				后向否定断言。跟前向肯定断言一样，只是方向相反。
				举个栗子：(?<!FishC)\.com 只匹配前边不是 "FishC" 的字符串 ".com"
		(?(id/name)yes-pattern|no-pattern)
				1. 如果子组的序号或名字存在的话，则尝试 yes-pattern 匹配模式；否则尝试 no-pattern 匹配模式
				2. no-pattern 是可选的
				举个栗子：(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$) 是一个匹配邮件格式的正则表达式，可以匹配 <user@fishc.com> 和 'user@fishc.com'，但是不会匹配 '<user@fishc.com' 或 'user@fishc.com>'
		\
				下边列举了由字符 '\' 和另一个字符组成的特殊含义。注意，'\' + 元字符的组合可以解除元字符的特殊功能
		\序号
				1. 引用序号对应的子组所匹配的字符串，子组的序号从 1 开始计算
				2. 如果序号是以 0 开头，或者 3 个数字的长度。那么不会被用于引用对应的子组，而是用于匹配八进制数字所表示的 ASCII 码值对应的字符
				举个栗子：(.+) \1 会匹配 "FishC FishC" 或 "55 55"，但不会匹配 "FishCFishC"（注意，因为子组后边还有一个空格）
		\A
				匹配输入字符串的开始位置
		\Z
				匹配输入字符串的结束位置
		\b
				匹配一个单词边界，单词被定义为 Unidcode 的字母数字或下横线字符
				举个栗子：\bFishC\b 会匹配字符串 "love FishC"、FishC." 或 "(FishC)"
		\B
				匹配非单词边界，其实就是与 \b 相反
				举个栗子：py\B 会匹配字符串 "python"、"py3"  或 "py2"，但不会匹配 "py  "、"py." 或  "py!"
		\d
				1. 对于 Unicode（str 类型）模式：匹配任何一个数字，包括 [0-9] 和其他数字字符；如果开启了 re.ASCII 标志，就只匹配 [0-9]
				2. 对于 8 位（bytes 类型）模式：匹配 [0-9] 中任何一个数字
		\D
				匹配任何非 Unicode 的数字，其实就是与 \d 相反；如果开启了 re.ASCII 标志，则相当于匹配 [^0-9]
		\s
				1. 对于 Unicode（str 类型）模式：匹配 Unicode 中的空白字符（包括 [ \t\n\r\f\v] 以及其他空白字符）；如果开启了 re.ASCII 标志，就只匹配 [ \t\n\r\f\v]
				2. 对于 8 位（bytes 类型）模式：匹配 ASCII 中定义的空白字符，即 [ \t\n\r\f\v]
		\S
				匹配任何非 Unicode 中的空白字符，其实就是与 \s 相反；如果开启了 re.ASCII 标志，则相当于匹配 [^ \t\n\r\f\v]
		\w
				1. 对于 Unicode（str 类型）模式：匹配任何 Unicode 的单词字符，基本上所有语言的字符都可以匹配，当然也包括数字和下横线；如果开启了 re.ASCII 标志，就只匹配 [a-zA-Z0-9_]
				2. 对于 8 位（bytes 类型）模式：匹配 ASCII 中定义的字母数字，即 [a-zA-Z0-9_]
		\W
				匹配任何非 Unicode 的单词字符，其实就是与 \w 相反；如果开启了 re.ASCII 标志，则相当于 [^a-zA-Z0-9_]
				转义符号
				正则表达式还支持大部分 Python 字符串的转义符号：\a，\b，\f，\n，\r，\t，\u，\U，\v，\x，\\
		注1：\b 通常用于匹配一个单词边界，只有在字符类中才表示“退格”
		注2：\u 和 \U 只有在 Unicode 模式下才会被识别
		注3：八进制转义（\数字）是有限制的，如果第一个数字是 0，或者如果有 3 个八进制数字，那么就被认为是八进制数；其他情况则被认为是子组引用；至于字符串，八进制转义总是最多只能是 3 个数字的长度

- 编译正则表达式，如果需要重复的使用某个正则表达式，那么可以将该正则表达式编译成模式对象

	1. 使用re.compile(pattern, flags=0)编译,也可以接受 flags 参数，用于开启各种特殊功能和语法变化

		>>> import re
		>>> p = re.compile('ab*')
		>>> p  
		<_sre.SRE_Pattern object at 0x...>
		>>>p.search('lcscim')

- 实现匹配,将正则表达式编译之后，就得到一个模式对象.模式对象拥有很多方法和属性

		方法										功能
		match(pattern, string, flags=0)		判断一个正则表达式是否从开始处匹配一个字符串
		search(pattern, string, flags=0)	遍历字符串，找到正则表达式匹配的第一个位置
		findall(pattern, string, flags=0)	遍历字符串，找到正则表达式匹配的所有位置，并以列表的形式返回
		finditer(pattern, string, flags=0)	遍历字符串，找到正则表达式匹配的所有位置，并以迭代器的形式返回

例子：
	
		>>> import re
		>>> p = re.compile('[a-z]+')
		>>> p.match("")
		>>> print(p.match(""))
		None
		>>> m = p.match('fishc')
		>>> m  
		<_sre.SRE_Match object; span=(0, 5), match='fishc'>
		>>> m.group()
		'fishc'
		>>> m.start()
		0
		>>> m.end()
		5
		>>> m.span()
		(0, 5)
match() 返回一个匹配对象，我们将其存放在变量 m 中,匹配对象包含了很多方法和属性，以下几个是最重要的：

		方法				功能
		group()		返回匹配的字符串
		start()		返回匹配的开始位置
		end()		返回匹配的结束位置
		span()		返回一个元组表示匹配位置（开始，结束）
由于 match() 只检查正则表达式是否在字符串的起始位置匹配，所以 start() 总是返回 0。

- 编译标志,编译标志让你可以修改正则表达式的工作方式。在flags中定义。在 re 模块下，编译标志均有两个名字：完整名和简写，例如 IGNORECASE 简写是 I（如果你是 Perl 的粉丝，那么你有福了，因为这些简写跟 Perl 是一样的，例如 re.VERBOSE 的简写是 re.X）。另外，多个标志还可以同时使用（通过“|”），如：re.I | re.M 就是同时设置 I 和 M 标志。

		标志								含义
		ASCII, A					使得转义符号如 \w，\b，\s 和 \d 只能匹配 ASCII 字符
		DOTALL, S					使得 . 匹配任何符号，包括换行符
		IGNORECASE, I				匹配的时候不区分大小写
		LOCALE, L					支持当前的语言（区域）设置
		MULTILINE, M				多行匹配，影响 ^ 和 $
		VERBOSE, X (for 'extended')	启用详细的正则表达式


下面我们来详细讲解一下它们的含义：

	A
	ASCII
	使得 \w，\W，\b，\B，\s 和 \S 只匹配 ASCII 字符，而不匹配完整的 Unicode 字符。这个标志仅对 Unicode 模式有意义，并忽略字节模式。
	
	S
	DOTALL
	使得 . 可以匹配任何字符，包括换行符。如果不使用这个标志，. 将匹配除了换行符的所有字符。
	
	I
	IGNORECASE
	字符类和文本字符串在匹配的时候不区分大小写。举个例子，正则表达式 [A-Z] 也将会匹配对应的小写字母，像 FishC 可以匹配 FishC，fishc 或 FISHC 等。如果你不设置 LOCALE，则不会考虑语言（区域）设置这方面的大小写问题。
	
	L
	LOCALE
	使得 \w，\W，\b 和 \B 依赖当前的语言（区域）环境，而不是 Unicode 数据库。
	
	区域设置是 C 语言的一个功能，主要作用是消除不同语言之间的差异。例如你正在处理的是法文文本，你想使用 \w+ 来匹配单词，但是 \w 只是匹配 [A-Za-z] 中的单词，并不会匹配 'é' 或 'ç'。如果你的系统正确的设置了法语区域环境，那么 C 语言的函数就会告诉程序 'é' 或 'ç' 也应该被认为是一个字符。当编译正则表达式的时候设置了 LOCALE 的标志，\w+ 就可以识别法文了，但速度多少会受到影响。
	
	M
	MULTILINE
	（^ 和 $ 我们还没有提到，别着急，后边我们有细讲...）
	
	通常 ^ 只匹配字符串的开头，而 $ 则匹配字符串的结尾。当这个标志被设置的时候，^ 不仅匹配字符串的开头，还匹配每一行的行首；& 不仅匹配字符串的结尾，还匹配每一行的行尾。
	
	X
	VERBOSE
	这个标志使你的正则表达式可以写得更好看和更有条理，因为使用了这个标志，空格会被忽略（除了出现在字符类中和使用反斜杠转义的空格）；这个标志同时允许你在正则表达式字符串中使用注释，# 符号后边的内容是注释，不会递交给匹配引擎（除了出现在字符类中和使用反斜杠转义的 #）。

使用正则表达式的下载实例

	import urllib.request
	import re
	
	def open_url(url):
	    req = urllib.request.Request(url)
	    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
	    page = urllib.request.urlopen(req)
	    html = page.read().decode('utf-8')
	
	    return html
	
	def get_img(html):
	    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'	
	    imglist = re.findall(p,html)		//如果匹配的内容中含有词组（用括号阔住的内容），就单独返回该词组，如果有多个，将所有词组组成元组并返回
	    '''
	    for each in imglist:
	        print(each)
	    '''
	    for each in imglist:
	        filename = each.split("/")[-1]
	        urllib.request.urlretrieve(each,filename,None)
	if __name__ == '__main__':
	    url = "https://tieba.baidu.com/p/3563409202"
	    get_img(open_url(url))
仅在findall（）方法中，如果正则表达式匹配的内容中含有词组（用括号阔住的内容），就单独返回该词组，如果有多个，将所有词组组成元组并返回.如果不需要自动完成，需要使用(?:...),即，左侧括号后紧跟'？'和'：'，例子如下

	import urllib.request
	import re
	
	def open_url(url):
	    req = urllib.request.Request(url)
	    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
	    page = urllib.request.urlopen(req)
	    html = page.read().decode('utf-8')
	
	    return html
	
	def get_img(html):
	    p = r'(?:(?:2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(?:2[0-4]\d|25[0-5]|[01]?\d\d?)'
	    iplist = re.findall(p,html)
	
	    for each in iplist:
	        print(each)
	        
	if __name__ == '__main__':
	    url = "https://www.kuaidaili.com/free/intr/"
	    get_img(open_url(url))

#6.26
tips：


##1.异常处理
这里介绍urlerror，HTTPError 是 URLError 的子类，服务器上每一个 HTTP 的响应都包含一个数字的“状态码”。</b>
有时候状态码会指出服务器无法完成的请求类型，一般情况下 Python 会帮你处理一部分这类响应（例如，响应的是一个“重定向”，要求客户端从别的地址来获取文档，那么 urllib 会自动为你处理这个响应。）；但是呢，有一些无法处理的，就会抛出 HTTPError 异常。这些异常包括典型的：404（页面无法找到），403（请求禁止）和 401（验证请求）。</b>

因为 Python 默认会自动帮你处理重定向方面的内容（状态码 300 ~ 399 范围），状态码 100 ~ 299 的范围是表示成功，所以你需要关注的是 400 ~ 599 这个范围的状态码（因为它们代表响应出了问题）。</b>

其中，出现 4xx 的状态码，说明问题来自客户端，就是你自己哪里做错了；出现 5xx 的状态码，那就表示与你无关了，是来自服务器的问题</b>

	状态码				内容					详细内容
  
	1xx 			这一类型的状态码，代表请求已被接受，需要继续处理。
	  
	100 			Continue 				收到请求，客户端应当继续发送请求。
	  
	101 		Switching  Protocols 		服务器通过 Upgrade 消息头通知客户端采用不同的协议来完成这个请求。
	  
	2xx 			成功 | 这一类型的状态码，代表请求已成功被服务器接收、理解、并接受。
	  
	200 			OK 						请求已成功，请求的响应头或数据体将随此响应返回。
	  
	201 		Created 					请求已经被实现，而且有一个新的资源已经依据请求的需要而创建，且其 URI 已经随 Location  头信息返回。
	  
	202 		Accepted 					服务器已接受请求，但尚未处理。正如它可能被拒绝一样，最终该请求可能会也可能不会被执行。
	  
	203 	Non-Authoritative  Information 	服务器已成功处理了请求，但返回的实体头部元信息不是在原始服务器上有效的确定集合，而是来自本地或者第三方的拷贝。
	  
	204 		No  Content 				服务器成功处理了请求，但没有返回任何实体内容。
	  
	205 		Reset  Content 				服务器成功处理了请求，且没有返回任何内容。但是与204响应不同，返回此状态码的响应要求请求者重置文档视图。
	  
	206 		Partial  Content 			服务器已经成功处理了部分 GET 请求。
	  
	3xx 		重定向 | 这类状态码代表需要客户端采取进一步的操作才能完成请求。通常，这些状态码用来重定向，后续的请求地址（重定向目标）在本次响应的 Location 域中指明。
	  
	300 		Multiple  Choices 			被请求的资源有一系列可供选择的回馈信息，每个都有自己特定的地址和浏览器驱动的商议信息。用户或浏览器能够自行选择一个首选的地址进行重定向。
	  
	301 		Moved  Permanently 			被请求的资源已永久移动到新位置，并且将来任何对此资源的引用都应该使用本响应返回的若干个 URI 之一。
	  
	302 		Found 						请求的资源现在临时从不同的 URI 响应请求。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。
	  
	303 		See  Other 					对应当前请求的响应可以在另一个 URI 上被找到，而且客户端应当采用 GET 的方式访问那个资源。
	  
	304 		Not  Modified 				如果客户端发送了一个带条件的 GET 请求且该请求已被允许，而文档的内容（自上次访问以来或者根据请求的条件）并没有改变，则服务器应当返回这个状态码。
	  
	305 		Use  Proxy 					被请求的资源必须通过指定的代理才能被访问。Location  域中将给出指定的代理所在的URI信息，接收者需要重复发送一个单独的请求，通过这个代理才能访问相应资源。
	  
	307 		Temporary  Redirect 		请求的资源现在临时从不同的 URI 响应请求。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。
	  
	4xx 		客户端错误 | 这类的状态码代表了客户端看起来可能发生了错误，妨碍了服务器的处理。
	  
	400 		Bad  Request 				由于包含语法错误，当前请求无法被服务器理解。
	  
	401 		Unauthorized 				当前请求需要用户验证。
	  
	402 		Payment  Required 			该状态码是为了将来可能的需求而预留的。
	  
	403 		Forbidden 					服务器已经理解请求，但是拒绝执行它。
	  
	404 		Not  Found 					请求失败，请求的资源在服务器上找不到。
	  
	405 		Method  Not Allowed 		请求中指定的请求方法不能被用于请求相应的资源。
	  
	406 		Not  Acceptable 			请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。
	  
	407 	Proxy  Authentication Required 	与 401 状态码类似，只不过客户端必须在代理服务器上进行身份验证。
	  
	408 		Request  Timeout 			请求超时。客户端没有在服务器预备等待的时间内完成一个请求的发送。
	  
	409 		Conflict 					由于和被请求的资源的当前状态之间存在冲突，请求无法完成。
	  
	410 		Gone 						被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址。
	  
	411 		Length  Required 			服务器拒绝在没有定义  Content-Length 头的情况下接受请求。
	  
	412 		Precondition  Failed 		服务器在验证在请求的头字段中给出先决条件时，没能满足其中的一个或多个。
	  
	413 		Request  Entity Too Large 	服务器拒绝处理当前请求，因为该请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。
	  
	414 		Request-URI  Too Long 		请求的 URI 长度超过了服务器能够解释的长度，因此服务器拒绝对该请求提供服务。
	  
	415 		Unsupported  Media Type 	对于当前请求的方法和所请求的资源，请求中提交的实体并不是服务器中所支持的格式，因此请求被拒绝。
	  
	416 Requested  Range Not Satisfiable 	如果请求中包含了 Range 请求头，并且 Range 中指定的任何数据范围都与当前资源的可用范围不重合，同时请求中又没有定义 If-Range 请求头，那么服务器就应当返回 416 状态码。
	  
	417 		Expectation  Failed 		在请求头 Expect 中指定的预期内容无法被服务器满足，或者这个服务器是一个代理服务器，它有明显的证据证明在当前路由的下一个节点上，Expect 的内容无法被满足。
	  
	5xx 		服务器错误 | 这类状态码代表了服务器在处理请求的过程中有错误或者异常状态发生。
	  
	500 		Internal  Server Error 		服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。
	  
	501 		Not  Implemented 			服务器不支持当前请求所需要的某个功能。
	  
	502 		Bad  Gateway 				作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
	  
	503 		Service  Unavailable 		由于临时的服务器维护或者过载，服务器当前无法处理请求。
	  
	504 		Gateway  Timeout 			作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI 标识出的服务器，例如 HTTP、FTP、LDAP）或者辅助服务器（例如 DNS）收到响应。
	  
	505 	HTTP  Version Not Supported 	服务器不支持，或者拒绝支持在请求中使用的HTTP版本。
处理异常的第一种写法：

	from urllib.request import Rquest,urlopen
	from urllib.error imort URLError,HTTPError
	req = Request(someurl)
	try:
		response = urlopen(req)
	except HTTPError as e:
		print('The server couldn\'t fulfill the request.')
		print('Error code: ',e.code)
	except URLError as e:
		print('We failed to reach a server.')
		print('Reason: ',e.reason)
	else:
		#everything is fine
处理异常的第二种写法（推荐）：

	from urllib.request import Rquest,urlopen
	from urllib.error imort URLError,HTTPError
	req = Request(someurl)
	try:
		response = urlopen(req)
	except URLError as e:
		if hasattr(e,'reason'):
			print('We failed to reach a server.')
			print('Reason: ',e.reason)
		elif hasattr(e,'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code: ',e.code)		
	else:
		#everything is fine
##2.安装scrapy
1. 下载安装pywin32,要对应Python版本，地址如下

		https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/
2. 安装pip,一般会自带，在Python安装目录下的scrips文件夹下

3. 安装lxml，在cmd中输入以下，等待完成即可

		pip install lxml
4. 安装OpenSSL，在cmd中输入以下，等待即可完成

		pip install pyOpenSSL
5. 安装Scrapy，在cmd中输入以下，等待即可完成

		pip install Scrapy
注意：可能需要更新pip,更新方法

	Python -m pip install --upgrade pip
提示：microsoft visual c++ 14.0 is required，需要在https://www.lfd.uci.edu/~gohlke/pythonlibs/下载对应版本的pymssql-2.1.4.dev5-cp36-cp36m-win32.whl,，然后放到Python安装目录下的scrips文件夹下，再执行以下语句

	pip install C:\Users\asus\AppData\Local\Programs\Python\Python36-32\Scripts\numpy-1.14.5+mkl-cp36-cp36m-win32.whl
##3.Scrapy框架
- 使用Scrapy抓取一个网站一共需要四个步骤：

	- 创建一个Scrapy项目

			在cmd中执行以下语句，会创建项目。Scrapy startproject tutorial
	- 定义item容器

			item是保存爬取到的数据的容器，其使用方法和Python字典类似，并提供了额外的保护机制来避免拼写错误导致的未定义字段错误，重写items文件
			import scrapy
			class DmozItem(scrapy.Item):
			    title = scrapy.Field()

	- 编写爬虫
	- 存储内容



编写爬虫类spider，spider是用户编写用于从网站上爬取数据的类。包含了一个用于下载初始URL，然后是如何跟进网页中的连接以及如何分析页面中的内容，还有提取生成item的方法，例如在C:\Users\asus\tutorial\tutorial\spiders中新建dmoz_spider.py。内容如下
	
	import scrapy
	class DmozSpider(scrapy.Spider):
	    name = "dmoz"
	    allowed_domains = ['docs.python.org']
	    start_urls = [
	        'https://docs.python.org/3/',
	        'https://docs.python.org/3/reference/index.html'
	        ]
	    def parse(self,response):
	        filename = response.url.split("/")[-2]
	        with open(filename,'wb') as f:
	            f.write(response.body)
在cmd中输入cd tutorial切换路径到创建的工程目录下，再输入Scrapy crawl dmoz（dmoz就是上方的name的值），会在目录下生成URL地址所指定的网页内容

	接下来对所保存的内容进行筛选，这时需要进行筛选selector。selector是一个选择器，有四个基本方法
	xpath():传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
	css():传入css表达式，返回该表达式所对应的所有节点的selector list列表
	extract():序列化该节点为Unicode字符串并返回list
	re():根据传入的正则表达式对数据进行提取，返回Unicode字符串list列表

在cmd中，输入scrapy shell "https://docs.python.org/3/reference/index.html"，用于进入shell模式，这时可以使用response.headers获取header，respons.body可以获取网页内容。response后跟xpath等可使用其方法。

1. xpath表达式：根据节点查找

		/html/head/title:选择HTML文档中<head>标签内的<title>元素
		/html/head/title/text():选择上面提到的<title>内的文字
		//td:选择所有的<td>元素
		//div[@class="mine"]:选择所有具有class=“mine”属性 的div元素

response.xpath() == response.selector.xpath()
2. 将列表字符串化使用extract()方法

		response.xpath('//title').extract()
3. 获取标签中具体的内容

		response.xpath('//title/text()').extract()

- shell会根据内容自动生成一个变量sel。

		sel.xpath('//ul/li')		//匹配ul/li
		sel.xpath('//ul/li/text()')		//获取内容
		sel.xpath('//ul/li/text()').extract()  //获取字符串
		sel.xpath('//ul/li/ul/li/a/@href').extract()	//获取链接地址

		sites = sel.xpath('//ul/li/ul/li/a/@href').extract()
		for site in sites:
			title = "https://docs.python.org/3/reference/"+site
			print(title)			//打印出找到的每一项

使用exit()退出shell模式，然后修改dmoz_spider.py文件

	import scrapy

	from tutorial.items import DmozItem			//关联模块文件
	
	class DmozSpider(scrapy.Spider):
	    name = "dmoz"
	    allowed_domains = ['docs.python.org']
	    start_urls = [
	        'https://docs.python.org/3/',
	        'https://docs.python.org/3/reference/index.html'
	        ]
	    def parse(self,response):
	        sel = scrapy.selector.Selector(response)
	        sites = sel.xpath('//ul/li/ul/li/a/@href').extract()
	        items = []
	        for site in sites:
	            item = DmozItem()
	            item['title'] = "https://docs.python.org/3/reference/"+site
	            items.append(item)
	
	        return items

最后在cmd中使用一下语句将查找内容导出为json格式文本

	Scrapy crawl dmoz -o items.json -t json

#7.20
##1.抓取抖音app视频并下载

	from splinter.driver.webdriver.chrome import Options, Chrome
	from splinter.browser import Browser
	from contextlib import closing
	import requests, json, time, re, os, sys, time
	from bs4 import BeautifulSoup
	 
	class DouYin(object):
	        def __init__(self, width = 500, height = 300):
			"""
			抖音App视频下载
			"""
			# 无头浏览器
			chrome_options = Options()
			chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"')
			self.driver = Browser(driver_name='chrome', executable_path='D:/chromedriver', options=chrome_options, headless=True)
	 
		def get_video_urls(self, user_id):
			"""
			获得视频播放地址
			Parameters:
				user_id：查询的用户ID
			Returns:
				video_names: 视频名字列表
				video_urls: 视频链接列表
				nickname: 用户昵称
			"""
			video_names = []
			video_urls = []
			unique_id = ''
			while unique_id != user_id:
				search_url = 'https://api.amemv.com/aweme/v1/discover/search/?cursor=0&keyword=%s&count=10&type=1&retry_type=no_retry&iid=17900846586&device_id=34692364855&ac=wifi&channel=xiaomi&aid=1128&app_name=aweme&version_code=162&version_name=1.6.2&device_platform=android&ssmix=a&device_type=MI+5&device_brand=Xiaomi&os_api=24&os_version=7.0&uuid=861945034132187&openudid=dc451556fc0eeadb&manifest_version_code=162&resolution=1080*1920&dpi=480&update_version_code=1622' % user_id
				req = requests.get(url = search_url, verify = False)
				html = json.loads(req.text)
				aweme_count = html['user_list'][0]['user_info']['aweme_count']
				uid = html['user_list'][0]['user_info']['uid']
				nickname = html['user_list'][0]['user_info']['nickname']
				unique_id = html['user_list'][0]['user_info']['unique_id']
			user_url = 'https://www.douyin.com/aweme/v1/aweme/post/?user_id=%s&max_cursor=0&count=%s' % (uid, aweme_count)
			req = requests.get(url = user_url, verify = False)
			html = json.loads(req.text)
			i = 1
			for each in html['aweme_list']:
				share_desc = each['share_info']['share_desc']
				if '抖音-原创音乐短视频社区' == share_desc:
					video_names.append(str(i) + '.mp4')
					i += 1
				else:
					video_names.append(share_desc + '.mp4')
				video_urls.append(each['share_info']['share_url'])
	 
			return video_names, video_urls, nickname
	 
		def get_download_url(self, video_url):
			"""
			获得带水印的视频播放地址
			Parameters:
				video_url：带水印的视频播放地址
			Returns:
				download_url: 带水印的视频下载地址
			"""
			req = requests.get(url = video_url, verify = False)
			bf = BeautifulSoup(req.text, 'lxml')
			script = bf.find_all('script')[-1]
			video_url_js = re.findall('var data = \[(.+)\];', str(script))[0]
			video_html = json.loads(video_url_js)
			download_url = video_html['video']['play_addr']['url_list'][0]
			return download_url
	 
		def video_downloader(self, video_url, video_name, watermark_flag=False):
			"""
			视频下载
			Parameters:
				video_url: 带水印的视频地址
				video_name: 视频名
				watermark_flag: 是否下载不带水印的视频
			Returns:
				无
			"""
			size = 0
			if watermark_flag == True:
				video_url = self.remove_watermark(video_url)
			else:
				video_url = self.get_download_url(video_url)
			with closing(requests.get(video_url, stream=True, verify = False)) as response:
				chunk_size = 1024
				content_size = int(response.headers['content-length']) 
				if response.status_code == 200:
					sys.stdout.write('  [文件大小]:%0.2f MB\n' % (content_size / chunk_size / 1024))
	 
					with open(video_name, "wb") as file:  
						for data in response.iter_content(chunk_size = chunk_size):
							file.write(data)
							size += len(data)
							file.flush()
	 
							sys.stdout.write('  [下载进度]:%.2f%%' % float(size / content_size * 100) + '\r')
							sys.stdout.flush()
	 
	 
		def remove_watermark(self, video_url):
			"""
			获得无水印的视频播放地址
			Parameters:
				video_url: 带水印的视频地址
			Returns:
				无水印的视频下载地址
			"""
			self.driver.visit('http://douyin.iiilab.com/')
			self.driver.find_by_tag('input').fill(video_url)
			self.driver.find_by_xpath('//button[@class="btn btn-default"]').click()
			html = self.driver.find_by_xpath('//div[@class="thumbnail"]/div/p')[0].html
			bf = BeautifulSoup(html, 'lxml')
			return bf.find('a').get('href')
	 
		def run(self):
			"""
			运行函数
			Parameters:
				None
			Returns:
				None
			"""
			self.hello()
			user_id = input('请输入ID(例如40103580):')
			video_names, video_urls, nickname = self.get_video_urls(user_id)
			if nickname not in os.listdir():
				os.mkdir(nickname)
			print('视频下载中:共有%d个作品!\n' % len(video_urls))
			for num in range(len(video_urls)):
				print('  解析第%d个视频链接 [%s] 中，请稍后!\n' % (num+1, video_urls[num]))
				if '\\' in video_names[num]:
					video_name = video_names[num].replace('\\', '')
				elif '/' in video_names[num]:
					video_name = video_names[num].replace('/', '')
				else:
					video_name = video_names[num]
				self.video_downloader(video_urls[num], os.path.join(nickname, video_name))
				print('\n')
	 
			print('下载完成!')
	 
		def hello(self):
			"""
			打印欢迎界面
			Parameters:
				None
			Returns:
				None
			"""
			print('*' * 100)
			print('\t\t\t\t抖音App视频下载小助手')
			print('\t\t作者:Jack Cui')
			print('*' * 100)
	 
	 
	if __name__ == '__main__':
		douyin = DouYin()
		douyin.run()

##2.Fiddler之手机APP爬取
https://blog.csdn.net/c406495762/article/details/76850843
##2.1什么是Fiddler?
Fiddler是位于客户端和服务器端的HTTP代理，也是目前最常用的http抓包工具之一 。 它能够记录客户端和服务器之间的所有 HTTP请求，可以针对特定的HTTP请求，分析请求数据、设置断点、调试web应用、修改请求的数据，甚至可以修改服务器返回的数据，功能非常强大，是web调试的利器。

既然是代理，也就是说：客户端的所有请求都要先经过Fiddler，然后转发到相应的服务器，反之，服务器端的所有响应，也都会先经过Fiddler然后发送到客户端，基于这个原因，Fiddler支持所有可以设置http代理为127.0.0.1:8888的浏览器和应用程序。使用了Fiddler之后，web客户端和服务器的请求如下所示：
![](https://img-blog.csdn.net/20170807155427297?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYzQwNjQ5NTc2Mg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
利用可以设置代理的这个特点，我们就可以对手机APP进行抓包了。

电脑上安装fiddler：https://www.telerik.com/fiddler，下载地址：https://telerik-fiddler.s3.amazonaws.com/fiddler/FiddlerSetup.exe

##2.1抓取守望先锋APP队伍logo并命名

	import requests
	from urllib.request import urlretrieve	//导入该模块方法
	
	if __name__ == '__main__':
	    headers = {'Host': 'api.overwatchleague.cn',
	               'Connection': 'Keep-Alive',
	               'Accept-Encoding': 'gzip',
	               'User-Agent': 'okhttp/3.6.0'
	               }
	    heros_url = "https://api.overwatchleague.cn/ranking"
	    req = requests.get(url=heros_url, headers=headers).json().get('content')
	    print('一共有%d个队伍' %len(req))
	    for i in req:
	        filename = i.get('competitor').get('name')+'.jpg'
	        logo_url = i.get('competitor').get('logo')
	        urlretrieve(url = logo_url, filename = filename)
urllib.request.urlretrieve（url，filename = None，reporthook = None，data = None ）

将URL表示的网络对象复制到本地文件。如果URL指向本地文件，则除非提供filename，否则不会复制该对象。返回一个元组，其中filename是可以在其下找到对象的本地文件名，而headers是返回的对象返回方法（对于远程对象）。

前两个参数都已知，第三个参数（如果存在）是一个可调用的，在建立网络连接时将调用一次，之后在每个块读取之后调用一次。callable将传递三个参数; 到目前为止传输的块数，块大小（以字节为单位）以及文件的总大小。第三个参数可能是-1旧的FTP服务器，它们不会返回文件大小以响应检索请求。

	

	
    



