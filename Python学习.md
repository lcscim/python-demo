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
13. 加载模块使用import+模块，例如，然后才能使用模块内的内容

		import random
14. 单行注释#，多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来
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

- close()方法，关闭文件
- read



	
