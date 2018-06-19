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

1. 模块导入使用import，一个模块只会被导入一次，不管执行了多少次import
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
- ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None)该方法提供一个选择continue和cancel，相应的返回1或者0
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
- hasattr(object, name) 函数用于判断对象是否包含对应的属性

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

##1.迭代




