#6.28
tips:


##1.图形界面GUI编程
###1.1Tkinter
实例1：

	import tkinter as tk
	app = tk.Tk()			//实例化一个tk用于容纳整个对象
	app.title("lcscim")		//设置图形化界面标题栏	
	theLabel = tk.Label(app,text="我的第一个程序！")		//label方法用于显示文本，图标，图片等
	theLabel.pack()			//pack方法用于自动调节窗口的尺寸和位置	
	app.mainloop()			//mainloop方法用于显示界面，一般位于程序最后一行代码

实例2：

	import tkinter as tk
	class APP:
	    def __init__(self,master):
	        frame = tk.Frame(master)
	        frame.pack(side=tk.LEFT,padx=10,pady=10)	//对框架frame进行包装，并设置位置
	
	        self.hi_there = tk.Button(frame,text="打招呼",bg="black",fg="white",command=self.say_hi)	//设置按钮并同时设置相关参数，command设置按钮的点击事件
	        self.hi_there.pack()	//对按钮进行包装
	
	    def say_hi(self):	//点击按钮方法
	        print("大家好我是老长")	
	root = tk.Tk()		//实例化一个tk用于容纳整个对象
	app = APP(root)		//创建类对象并将tk对象传入
	root.mainloop()

###1.2Tkinter 组件
Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。目前有15种Tkinter的部件。

	控件					描述
	Button			按钮控件；在程序中显示按钮。
	Canvas			画布控件；显示图形元素如线条或文本
	Checkbutton		多选框控件；用于在程序中提供多项选择框
	Entry			输入控件；用于显示简单的文本内容
	Frame			框架控件；在屏幕上显示一个矩形区域，多用来作为容器
	Label			标签控件；可以显示文本和位图
	Listbox			列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
	Menubutton		菜单按钮控件，由于显示菜单项。
	Menu			菜单控件；显示菜单栏,下拉菜单和弹出菜单
	Message			消息控件；用来显示多行文本，与label比较类似
	Radiobutton		单选按钮控件；显示一个单选的按钮状态
	Scale			范围控件；显示一个数值刻度，为输出限定范围的数字区间
	Scrollbar		滚动条控件，当内容超过可视化区域时使用，如列表框。.
	Text			文本控件；用于显示多行文本
	Toplevel		容器控件；用来提供一个单独的对话框，和Frame比较类似
	Spinbox			输入控件；与Entry类似，但是可以指定输入范围值
	PanedWindow		PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
	LabelFrame		labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
	tkMessageBox	用于显示 你应用程序的消息框。
标准属性，标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。

	属性				描述
	Dimension	控件大小；
	Color		控件颜色；
	Font		控件字体；
	Anchor		锚点；
	Relief		控件样式；
	Bitmap		位图；
	Cursor		光标；
几何管理，Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置

	几何方法		描述
	pack()		包装；
	grid()		网格；
	place()		位置；	

- label标签，用于在屏幕上显示文本或图像。Label 组件仅能显示单一字体的文本，但文本可以跨越多行。另外，还可以为其中的个别字符加上下划线（例如用于表示键盘快捷键）。
		
		from tkinter import *
		root = Tk()
		textLabel = Label(root,
		                  text="您所下载的影片包含有成人信息，\n年满18周岁才可观看",		//可使用换行符对文本进行换行
		                  justify=LEFT,			//指定多行文本对齐方式，默认为居中
		                  padx=10)				//设置文本偏移
		textLabel.pack(side=LEFT)				//设置文本居左
		photo = PhotoImage(file="18.gif")		//不支持JPG格式
		imgLabel = Label(root,image=photo)		//设置图片标签
		imgLabel.pack(side=RIGHT)				//设置图片居右
		mainloop()
		//该方法设置文本居左，图片居右

		from tkinter import *
		root = Tk()
		photo = PhotoImage(file="timg.gif")		//图片对象
		theLabel = Label(root,
		                 text="大家好我是老长，\n各位下午好",		//文本
		                 justify=LEFT,			//多行文本对齐
		                 image=photo,			//指定图片背景
		                 compound=CENTER,		//混合模式设置为居中
		                 font=("微软雅黑",20),
		                 fg="white")
		theLabel.pack()
		mainloop()
		//将图片设置为背景

语法：

	Label(master=None, **options) (class)
		master -- 父组件
		**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

	选项								含义
	activebackground	1. 设置当 Label 处于活动状态（通过 state 选项设置状态）的背景色
						2. 默认值由系统指定
						
	activeforeground	1. 设置当 Label 处于活动状态（通过 state 选项设置状态）的前景色
						2. 默认值由系统指定
	
	anchor				1. 控制文本（或图像）在 Label 中显示的位置
						2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN 代表东西南北，上北下南左西右东）
						3. 默认值是 CENTER
	
	background			1. 设置背景颜色
						2. 默认值由系统指定
	
	bg					跟 background 一样
	
	bitmap				1. 指定显示到 Label 上的位图
						2. 如果指定了 image 选项，则该选项被忽略
	
	borderwidth			1. 指定 Label 的边框宽度
						2. 默认值由系统指定，通常是 1 或 2 像素
	
	bd					跟 borderwidth 一样
	
	compound			1. 控制 Label 中文本和图像的混合模式
						2. 默认情况下，如果有指定位图或图片，则不显示文本
						3. 如果该选项设置为 CENTER，文本显示在图像上（文本重叠图像）
						4. 如果该选项设置为 BOTTOM，LEFT，RIGHT 或 TOP，那么图像显示在文本的旁边（如 BOTTOM，则图像在文本的下方）
						5. 默认值是 NONE
	
	cursor				1. 指定当鼠标在 Label 上飘过的时候的鼠标样式
						2. 默认值由系统指定
	
	disabledforeground	1. 指定当 Label 不可用的时候前景色的颜色
						2. 默认值由系统指定
	
	font				1. 指定 Label 中文本的字体
						2. 一个 Label 只能设置一种字体
						3. 默认值由系统指定
	
	foreground			1. 设置 Label 的文本和位图的颜色
						2. 默认值由系统指定
	
	fg					跟 foreground 一样
	
	height				1. 设置 Label 的高度
						2. 如果 Label 显示的是文本，那么单位是文本单元
						3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
						4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出高度
	
	highlightbackground	1. 指定当 Label 没有获得焦点的时候高亮边框的颜色
						2. 默认值由系统指定，通常是标准背景颜色
	
	highlightcolor		1. 指定当 Label 获得焦点的时候高亮边框的颜色
						2. 默认值由系统指定
	
	highlightthickness	1. 指定高亮边框的宽度
						2. 默认值是 0（不带高亮边框）
	
	image				1. 指定 Label 显示的图片
						2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
						3. 该选项优先于 text 和 bitmap 选项
	
	justify				1. 定义如何对齐多行文本
						2. 使用 LEFT，RIGHT 或 CENTER
						3. 注意，文本的位置取决于 anchor 选项
						4. 默认值是 CENTER
	
	padx				1. 指定 Label 水平方向上的额外间距（内容和边框间）
						2. 单位是像素
	
	pady				1. 指定 Label 垂直方向上的额外间距（内容和边框间）
						2. 单位是像素
	
	relief				1. 指定边框样式
						2. 默认值是 FLAT
						3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
	
	state				1. 指定 Label 的状态
						2. 这个标签控制 Label 如何显示
						3. 默认值是 NORMAL
						4. 另外你还可以设置 ACTIVE 或 DISABLED
	
	takefocus			1. 如果是 True，该 Label 接受输入焦点
						2. 默认值是 False
	
	text				1. 指定 Label 显示的文本
						2. 文本可以包含换行符
						3. 如果设置了 bitmap 或 image 选项，该选项则被忽略
	
	textvariable		1. Label 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
						2. 如果变量被修改，Label 的文本会自动更新
	
	underline			1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键） 
						2. 默认值是 -1
						3. 例如设置为 1，则说明在 Button 的第 2 个字符处画下划线
	
	width				1. 设置 Label 的宽度
						2. 如果 Label 显示的是文本，那么单位是文本单元
						3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
						4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出宽度
	
	wraplength			1. 决定 Label 的文本应该被分成多少行
						2. 该选项指定每行的长度，单位是屏幕单元
						3. 默认值是 0

- Button按钮，用于在 Python 应用程序中添加按钮，按钮上可以放上文本或图像，按钮可用于监听用户行为，能够与一个 Python 函数关联，当按钮被按下时，自动调用该函数。

		from tkinter import *
		def callback():
		    var.set("吹得")
		root = Tk()
		frame1 = Frame(root)
		frame2 = Frame(root)	
		var = StringVar()
		var.set("您所下载的影片包含有成人信息，\n年满18周岁才可观看")
		textLabel = Label(frame1,
		                  textvariable=var,
		                  justify=LEFT)
		textLabel.pack(side=LEFT)
		photo = PhotoImage(file="18.gif")
		imgLabel = Label(frame1,image=photo)
		imgLabel.pack(side=RIGHT)
		theButton = Button(frame2,text="我已满18周岁",command=callback)
		theButton.pack()
		frame1.pack(padx=10,pady=10)
		frame2.pack(padx=10,pady=10)
		mainloop()

语法格式如下：

	w = Button ( master, option=value, ... )
		master: 按钮的父容器。
		options: 可选项，即该按钮的可设置的属性。这些选项可以用键 = 值的形式设置，并以逗号分隔。

	序号			可选项 							描述
	1 		activebackground 			当鼠标放上去时，按钮的背景色
	
	2	 	activeforeground 			当鼠标放上去时，按钮的前景色
	
	3	 	bd 							按钮边框的大小，默认为 2 个像素
	
	4 		bg 							按钮的背景色
	
	5	 	command 					按钮关联的函数，当按钮被点击时，执行该函数
	
	6 		fg 							按钮的前景色（按钮文本的颜色）
	
	7 		font 						文本字体
	
	8 		height 						按钮的高度
	
	9	 	highlightcolor 				要高亮的颜色
	
	10	 	image 						按钮上要显示的图片
	
	11	 	justify 					显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
	
	12	 	padx 						按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离
	
	13	 	pady 						按钮在y轴方向上的内边距(padding)
	
	14	 	relief 						边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
	
	15	 	state 						设置按钮组件状态,可选的有NORMAL、ACTIVE、 DISABLED。默认 NORMAL。
	
	16	 	underline 					下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
	
	17	 	width 						按钮的宽度，如未设置此项，其大小以适应按钮的内容（文本或图片的大小）
	
	18	 	wraplength 					限制按钮每行显示的字符的数量
	
	19	 	text 						按钮的文本内容
	
	19	 	anchor 						锚选项，控制文本的位置，默认为中心
	
	
	以下为组件常用的方法：

	方法						描述
	deselect()		清除单选按钮的状态
	flash()			在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
	invoke()		可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
	select()		设置单选按钮为选中。
- checkbutton

	1. 实例1

			from tkinter import *
			root = Tk()
			v = IntVar()		//variable主要用于传参和绑定变量
			c = Checkbutton(root,text="测试一下",variable=v)		//设置checkbutton，variable为值，选中为1未选中为0
			c.pack()
			l = Label(root,textvariable=v)
			l.pack()
			mainloop()
	2. 实例2

			from tkinter import *
			root = Tk()
			GIRLS = ["西施","貂蝉","王昭君","杨玉环"]
			v = []
			for girl in GIRLS:
			    v.append(IntVar())
			    b = Checkbutton(root,text=girl,variable=v[-1])
			    b.pack(anchor=W)		//anchor值为E，W，S,N,和地图方位类似
			mainloop()
语法格式如下：

	w = Checkbutton ( master, option=value, ... )	
		master: 按钮的父容器。
		options: 可选项，即该按钮的可设置的属性。这些选项可以用键 = 值的形式设置，并以逗号分隔。

	序号			可选项     			描述
	1	 activebackground 		当鼠标放上去时，按钮的背景色
	2	 activeforeground 		当鼠标放上去时，按钮的前景色
	3 	 		bg 				按钮的背景色
	4	 	  bitmap 			位图
	5	 		bd 				边框的大小，默认为 2 个像素
	6	 		command 		关联的函数，当按钮被点击时，执行该函数
	7	 		cursor 			光标的形状设定，如arrow, circle, cross, plus 等
	8	 disabledforeground 	禁用选项的前景色
	9	 		font 			文本字体
	10	 		fg 				选项的前景色
	11	 		height 			复选框文本行数，默认为 1。
	12	 	highlightcolor 		聚焦的高亮颜色
	13	 		image 			是否使用图标
	14	 		justify 		显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
	15	 		offvalue 		Checkbutton 的值不仅仅是 1 或 0，可以是其他类型的数值，可以通过 onvalue 和 offvalue 属性							设置 Checkbutton 的状态值。
	16	 		onvalue 		Checkbutton 的值不仅仅是 1 或 0，可以是其他类型的数值，可以通过 onvalue 和 offvalue 属性							设置 Checkbutton 的状态值。
	17	 		padx 			按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离，默认为 1 像素。
	18	 		pady 			按钮在y轴方向上的内边距(padding)，默认为 1 像素。
	19	 		relief 			边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
	20	 	selectcolor 		选中后的颜色，默认为 selectcolor="red"。
	21	 	selectimage 		选中后的图片
	22	 		state 			状态，默认为 state=NORMAL
	23	 		text 			显示的文本，使用 "\n" 来对文本进行换行。
	24	 		underline       下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
	25	 		variable 		变量，variable 的值为 1 或 0，代表着选中或不选中	
	26	 		width 			默认宽度是复选框的文本或图像决定的，你可以设置指定字符数。	
	27	 		wraplength 		是否设置包裹。
	
		以下为常用的方法：

	序号				方法 			描述
	1			deselect() 		清除复选框选中选项。	
	2	 		flash() 		在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。	
	3 			invoke() 		可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作	
	4	 		select() 		设置按钮为选中。	
	5	 		toggle()  		选中与没有选中的选项互相切换
- Radiobutton与checkbutton类似

	1. 实例1

		from tkinter import *
		root = Tk()
		v = IntVar()
		Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)	//anchor值为E，W，S,N,和地图方位类似指定位置
		Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
		Radiobutton(root,text="Three",variable=v,value=3).pack(anchor=W)
		mainloop()
	2. 实例2

		from tkinter import *
		root = Tk()		
		LANGES = [
		    ("Python",1),
		    ("Perl",2),
		    ("Ruby",3),
		    ("Lua",4)]		
		v = IntVar()
		v.set(1)		
		for lang,num in LANGES:
		    b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)	//indicatoron=False指定radiobutton的形状，取消前面的点状选择点
		    b.pack(fill=X)		//指定fill参数布满窗口
		mainloop()
- labelFrame，是一个简单的容器控件

	- 实例
		
		from tkinter import *
		root = Tk()
		group = LabelFrame(root,text="最好的脚本语言是？",padx=10,pady=10)
		group.pack(padx=10,pady=10)
		LANGES = [
		    ("Python",1),
		    ("Perl",2),
		    ("Ruby",3),
		    ("Lua",4)]
		v = IntVar()
		for lang,num in LANGES:
		    b = Radiobutton(group,text=lang,variable=v,value=num)
		    b.pack(anchor=W)
		mainloop()

- entry输入控件

	- 实例1

		from tkinter import *
		root = Tk()		
		e = Entry(root)
		e.pack(padx=20,pady=20)		
		e.delete(0,END)
		e.insert(0,"默认...")		
		mainloop()
	- 实例2，由于IDLE由python编写，所以指定command点击事件为quit在IDLE中产生冲突退不出来，直接运行py文件可以

		from tkinter import *
		root = Tk()		
		Label(root,text="作品：").grid(row=0,column=0)	//grid用于修改控件布局，以表格形式，row表示行，column表示列
		Label(root,text="作者：").grid(row=1,column=0)		
		e1 = Entry(root)
		e2 = Entry(root)
		e1.grid(row=0,column=1,padx=10,pady=5)		//同理
		e2.grid(row=1,column=1,padx=10,pady=5)		
		def show():
		    print("作品：《%s》"% e1.get())
		    print("作者：%s"% e2.get())		
		Button(root,text="获取信息",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)	//sticky用于指定对齐
		Button(root,text="退出",width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)	
		mainloop()
	- 实例3

		from tkinter import *
		root = Tk()		
		Label(root,text="账号：").grid(row=0,column=0)
		Label(root,text="密码：").grid(row=1,column=0)		
		v1 = StringVar()
		v2 = StringVar()		
		e1 = Entry(root,textvariable=v1)
		e2 = Entry(root,textvariable=v2,show="*")		//用*代替密码显示
		e1.grid(row=0,column=1,padx=10,pady=5)
		e2.grid(row=1,column=1,padx=10,pady=5)		
		def show():
		    print("账号：%s"% e1.get())
		    print("密码：%s"% e2.get())				
		Button(root,text="芝麻开门",width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
		Button(root,text="退出",width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)		
		mainloop()

语法：

	Entry(master=None, **options) (class)
		master -- 父组件
		**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

		选项						含义
	background				1. 设置 Entry 的背景颜色
							2. 默认值由系统指定
	bg						跟 background 一样
	borderwidth				1. 设置 Entry 的边框宽度
							2. 默认值是 1 或 2 像素
	bd						跟 borderwidth 一样
	cursor					1. 指定当鼠标在 Entry 上飘过的时候的鼠标样式
							2. 默认值由系统指定
	exportselection			1. 指定选中的文本是否可以被复制到剪贴板
							2. 默认值是 True
							3. 可以修改为 False 表示不允许复制文本
	font					1. 指定 Entry 中文本的字体
							2. 默认值由系统指定
	foreground				1. 设置 Entry 的文本颜色
							2. 默认值由系统指定
	fg	跟 foreground 一样
	highlightbackground		1. 指定当 Entry 没有获得焦点的时候高亮边框的颜色
							2. 默认值由系统指定
	highlightcolor			1. 指定当 Entry 获得焦点的时候高亮边框的颜色
							2. 默认值由系统指定
	highlightthickness		1. 指定高亮边框的宽度
							2. 默认值是 1 或 2 像素
	insertbackground		指定输入光标的颜色
	insertborderwidth		1. 指定输入光标的边框宽度
							2. 如果被设置为非 0 值，光标样式会被设置为 RAISED
							3. 小甲鱼温馨提示：将 insertwidth 设置大一点才能看到效果哦
	insertofftime			1. 该选项控制光标的闪烁频率（灭）
							2. 单位是毫秒
	insertontime			1. 该选项控制光标的闪烁频率（亮）
							2. 单位是毫秒
	insertwidth				1. 指定光标的宽度
							2. 默认值是 1 或 2 像素
	invalidcommand			1. 指定当输入框输入的内容“非法”时调用的函数
							2. 也就是指定当 validateCommand 选项指定的函数返回 False 时的函数
							3. 详见本内容最下方小甲鱼关于验证详解
	invcmd					跟 invalidcommand 一样
	justify					1. 定义如何对齐输入框中的文本
							2. 使用 LEFT，RIGHT 或 CENTER
							3. 默认值是 LEFT
	relief					1. 指定边框样式
							2. 默认值是 SUNKEN
							3. 其他可以选择的值是 FLAT，RAISED，GROOVE 和 RIDGE
	selectbackground		1. 指定输入框的文本被选中时的背景颜色
							2. 默认值由系统指定
	selectborderwidth		1. 指定输入框的文本被选中时的边框宽度（选中边框）
							2. 默认值由系统指定
	selectforeground		1. 指定输入框的文本被选中时的字体颜色
							2. 默认值由系统指定
	show					1. 设置输入框如何显示文本的内容
							2. 如果该值非空，则输入框会显示指定字符串代替真正的内容
							3. 将该选项设置为 "*"，则是密码输入框
	state					1. Entry 组件可以设置的状态：NORMAL，DISABLED 或 "readonly"（注意，这个是字符串。它跟 DISABLED 相似，但它支持选中和拷贝，只是不能修改，而 DISABLED 是完全禁止）
							2. 默认值是 NORMAL
							3. 注意，如果此选项设置为 DISABLED 或 "readonly"，那么调用 insert() 和 delete() 方法都会被忽略
	takefocus				1. 指定使用 Tab 键可以将焦点移动到输入框中
							2. 默认是开启的，可以将该选项设置为 False 避免焦点在此输入框中
	textvariable			1. 指定一个与输入框的内容相关联的 Tkinter 变量（通常是 StringVar）
							2. 当输入框的内容发生改变时，该变量的值也会相应发生改变
	validate				1. 该选项设置是否启用内容验证 
							2. 详见本内容最下方小甲鱼关于验证详解
	validatecommand			1. 该选项指定一个验证函数，用于验证输入框内容是否合法
							2. 验证函数需要返回 True 或 False 表示验证结果
							3. 注意，该选项只有当 validate 的值非 "none" 时才有效
							3. 详见本内容最下方小甲鱼关于验证详解
	vcmd					跟 validatecommand 一样
	width					1. 设置输入框的宽度，以字符为单位
							2. 默认值是 20
							3. 对于变宽字体来说，组件的实际宽度等于字体的平均宽度乘以 width 选项的值
	xscrollcommand			1. 与 scrollbar（滚动条）组件相关联
							2. 如果你觉得用户输入的内容会超过该组件的输入框宽度，那么可以考虑设置该选项
							3. 使用方法可以参考：Scrollbar 组件

方法：

		delete(first, last=None)
			-- 删除参数 first 到 last 范围内（包含 first 和 last）的所有内容
			-- 如果忽略 last 参数，表示删除 first 参数指定的选项
			-- 使用 delete(0, END) 实现删除输入框的所有内容		
		get()
			-- 获得当前输入框的内容		
		icursor(index)
			-- 将光标移动到 index 参数指定的位置
			-- 这同时也会设置 INSERT 的值
		index(index)
			-- 返回与 index 参数相应的选项的序号（例如 e.index(END)）
		insert(index, text)
			-- 将 text 参数的内容插入到 index 参数指定的位置
			-- 使用 insert(INSERT, text) 将 text 参数指定的字符串插入到光标的位置
			-- 使用 insert(END, text) 将 text 参数指定的字符串插入到输入框的末尾
		scan_dragto(x)
			--  见下方 scan_mark(x)
		scan_mark(x)
			-- 使用这种方式来实现输入框内容的滚动
			-- 需要将鼠标按下事件绑定到 scan_mark(x) 方法（x 是鼠标当前的水平位置），然后再将 <motion> 事件绑定到 scan_dragto(x) 方法（x 是鼠标当前的水平位置），就可以实现输入框在当前位置和 sacn_mack(x) 指定位置之间的水平滚动
		select_adjust(index)
			-- 与 selection_adjust(index) 相同，见下方解释
		select_clear()
			-- 与 selection_clear() 相同，见下方解释
		select_from(index)
			-- 与 selection_from(index) 相同，见下方解释
		select_present()
			-- 与 selection_present() 相同，见下方解释
		select_range(start, end)
			-- 与 selection_range(start, end) 相同，见下方解释
		select_to(index)
			-- 与 selection_to(index) 相同，见下方解释
		selection_adjust(index)
			-- 该方法是为了确保输入框中选中的范围包含 index 参数所指定的字符
			-- 如果选中的范围已经包含了该字符，那么什么事情也不会发生
			-- 如果选中的范围不包含该字符，那么会从光标的位置将选中的范围扩展至该字符
		selection_clear()
			-- 取消选中状态
		selection_from(index)
			-- 开始一个新的选中范围
			-- 会设置 ANCHOR 的值
		selection_present()
			-- 返回输入框是否有处于选中状态的文本
			-- 如果有则返回 True，否则返回 False
		selection_range(start, end)
			-- 设置选中范围
			-- start 参数必须必 end 参数小
			-- 使用 selection_range(0, END) 选中整个输入框的所有内容
		selection_to(index)
			-- 选中 ANCHOR 到 index 参数的间的所有内容
		xview(index)
			-- 该方法用于确保给定的 index 参数所指定的字符可见
			-- 如有必要，会滚动输入框的内容
		xview_moveto(fraction)
			-- 根据 fraction 参数给定的比率调整输入框内容的可见范围
			-- fraction 参数的范围是 0.0 ~ 1.0，0.0 表示输入框的开始位置，1.0 表示输入框的结束位置
		xview_scroll(number, what)
			-- 根据给定的参数水平滚动输入框的可见范围
			-- number 参数指定滚动的数量，如果是负数则表示反向滚动
			-- what 参数指定滚动的单位，可以是 UNITS 或 PAGES（UNITS 表示一个字符单元，PAGES 表示一页）
- 关于验证

	- Entry 组件是支持验证输入内容的合法性的，实现该功能，需要通过设置 validate、validatecommand 和 invalidcommand 选项。首先启用验证的“开关”是 validate 选项，该选项可以设置的值有：

			值					含义
			'focus'			当 Entry 组件获得或失去焦点的时候验证
			'focusin'		当 Entry 组件获得焦点的时候验证
			'focusout'		当 Entry 组件失去焦点的时候验证
			'key'			当输入框被编辑的时候验证
			'all'			当出现上边任何一种情况的时候验证
			'none'			1. 关闭验证功能
							2. 默认设置该选项（即不启用验证）
							3. 注意，是字符串的 'none'，而非 None

			from tkinter import *
			master = Tk()			
			def test():
			    if e1.get() == "小甲鱼":
			        print("正确！")
			        return True
			    else:
			        print("错误！")
			        e1.delete(0, END)
			        return False			
			v = StringVar()			
			e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=test)
			e2 = Entry(master)
			e1.pack(padx=10, pady=10)
			e2.pack(padx=10, pady=10)			
			mainloop()

	- 其次是为 validatecommand 选项指定一个验证函数，该函数只能返回 True 或 False 表示验证的结果。一般情况下验证函数只需要知道输入框的内容即可，可以通过 Entry 组件的 get() 方法获得该字符串。下边的例子中，在第一个输入框输入“小甲鱼”并通过 Tab 键将焦点转移到第二个输入框的时候，验证功能被成功触发

			from tkinter import *
			master = Tk()			
			def test():
			    if e1.get() == "小甲鱼":
			        print("正确！")
			        return True
			    else:
			        print("错误！")
			        e1.delete(0, END)
			        return False			
			v = StringVar()
			e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=test)
			e2 = Entry(master)
			e1.pack(padx=10, pady=10)
			e2.pack(padx=10, pady=10)			
			mainloop()
	- 然后，invalidcommand 选项指定的函数只有在 validatecommand 的返回值为 False 的时候才被调用。下边的例子中，在第一个输入框输入“小鱿鱼”，并通过 Tab 键将焦点转移到第二个输入框，validatecommand 指定的验证函数被触发并返回 False，接着 invalidcommand 被触发：

			from tkinter import *
			master = Tk()	
			v = StringVar()
			def test1():
			    if v.get() == "小甲鱼":
			        print("正确！")
			        return True
			    else:
			        print("错误！")
			        e1.delete(0, END)
			        return False
			def test2():
			    print("我被调用了......")
			    return True
			e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=test1, invalidcommand=test2)
			e2 = Entry(master)
			e1.pack(padx=10, pady=10)
			e2.pack(padx=10, pady=10)	
			mainloop()
	- 	最后，其实 Tkinter 还有隐藏技能，不过需要冷却才能触发。Tkinter 为验证函数提供一些额外的选项：

			额外选项				含义
			'%d'		操作代码：0 表示删除操作；1 表示插入操作；2 表示获得、失去焦点或 textvariable 变量的值被修改
			'%i'		1. 当用户尝试插入或删除操作的时候，该选线表示插入或删除的位置（索引号）
						2. 如果是由于获得、失去焦点或 textvariable 变量的值被修改而调用验证函数，那么该值是 -1
			'%P'		1. 当输入框的值允许改变的时候，该值有效
						2. 该值为输入框的最新文本内容
			'%s'		该值为调用验证函数前输入框的文本内容
			'%S'		1. 当插入或删除操作触发验证函数的时候，该值有效
						2. 该选项表示文本被插入和删除的内容
			'%v'		该组件当前的 validate 选项的值
			'%V'		1. 调用验证函数的原因
						2. 该值是 'focusin'，'focusout'，'key' 或 'forced'（textvariable 选项指定的变量值被修改）中的一个
			'%W'		该组件的名字

为了使用这些选项，你可以这样写：

	validatecommand=(f, s1, s2, ...)

其中，f 就是你“冷却后”的验证函数名，s1、s2、s3 这些是额外的选项，这些选项会作为参数依次传给 f 函数。我们刚刚说了，使用隐藏技能前需要冷却，其实就是调用 register() 方法将验证函数包装起来：

	from tkinter import *
	master = Tk()	
	v = StringVar()	
	def test(content, reason, name): 
	    if content == "小甲鱼":
	        print("正确！")
	        print(content, reason, name)
	        return True
	    else:
	        print("错误！")
	        print(content, reason, name)
	        return False	
	testCMD = master.register(test)
	e1 = Entry(master, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'))
	e2 = Entry(master)
	e1.pack(padx=10, pady=10)
	e2.pack(padx=10, pady=10)	
	mainloop()

- 实战，简单加法计算器

		from tkinter import *
		master = Tk()		
		frame = Frame(master)
		frame.pack(padx=10,pady=10)		
		v1 = StringVar()
		v2 = StringVar()
		v3 = StringVar()		
		def test(content):
		    return content.isdigit()		
		testCMD = master.register(test)		
		e1 = Entry(frame,width=10,textvariable=v1,validate="key",validatecommand=(testCMD,'%P')).grid(row=0,column=0)
		Label(frame,text="+").grid(row=0,column=1)
		e2 = Entry(frame,width=10,textvariable=v2,validate="key",validatecommand=(testCMD,'%P')).grid(row=0,column=2)
		Label(frame,text="=").grid(row=0,column=3)
		e3 = Entry(frame,width=10,textvariable=v3,state="readonly").grid(row=0,column=4)	
		def calc():
		    result = int(v1.get()) + int(v2.get())
		    v3.set(str(result))
		Button(frame,text="计算结果",command=calc).grid(row=1,column=2,pady=5)	
		mainloop()

#6.30
tips：


##1.listbox
Listbox 组件通常被用于显示一组文本选项，Listbox 组件跟 Checkbutton 和 Radiobutton 组件类似，不过 Listbox 是以列表的形式来提供选项的（后两个是通过按钮的形式）。创建一个 Listbox 组件的时候，它是空的,我们使用 insert() 方法添加文本，该方法有两个参数：第一个参数是插入的索引号，第二个参数是插入的字符串。索引号通常是项目的序号（0 是列表中第一项的序号）。

	from tkinter import *
	master = Tk()	
	# 创建一个空列表
	theLB = Listbox(master)
	theLB.pack()	
	# 往列表里添加数据
	for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
	    theLB.insert(END, item)			//第一个参数是插入的索引号，第二个参数是插入的字符串
		//listbox.delete(0, END)
	theButton = Button(master, text="删除", command=lambda x=theLB: x.delete(ACTIVE))	//lambda表达式表示删除活动部分
	theButton.pack()
	mainloop()
	
- 语法：

		Listbox(master=None, **options) (class)
			master -- 父组件
			**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

			选项							含义
		background					1. 设置背景颜色
									2. 默认值由系统指定
		bg							跟 background 一样
		borderwidth					1. 指定 Listbox 的边框宽度
									2. 默认值由系统指定，通常是 2 像素
		bd							跟 borderwidth 一样
		cursor						1. 指定当鼠标在 Listbox 上飘过的时候的鼠标样式
									2. 默认值由系统指定
		exportselection				1. 指定选中的项目文本是否可以被复制到剪贴板
									2. 默认值是 True
									3. 可以修改为 False 表示不允许复制项目文本
		font						1. 指定 Listbox 中文本的字体
									2. 默认值由系统指定
		foreground					1. 设置 Listbox 的文本颜色
									2. 默认值由系统指定
		fg							跟 foreground 一样
		height						1. 设置 Listbox 显示的行数（不是像素）
									2. 默认值是 10
		highlightbackground			1. 指定当 Listbox 没有获得焦点的时候高亮边框的颜色
									2. 默认值由系统指定，通常是标准背景颜色
		highlightcolor				1. 指定当 Listbox 获得焦点的时候高亮边框的颜色
									2. 默认值由系统指定
		highlightthickness			1. 指定高亮边框的宽度
									2. 默认值是 1
		listvariable				1. 指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目
									2. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("鸡蛋 鸭蛋 鹅蛋 李狗蛋")
		relief						1. 指定边框样式
									2. 默认值是 SUNKEN
		selectbackground			1. 指定当某个项目被选中的时候背景颜色
									2. 默认值由系统指定
		selectborderwidth			1. 指定当某个项目被选中的时候边框的宽度
									2. 默认是由 selectbackground 指定的颜色填充，没有边框
									3. 如果设置了此选项，Listbox 的每一项会相应变大，被选中项为 RAISED 样式
		selectforeground			1. 指定当某个项目被选中的时候文本颜色
									2. 默认值由系统指定
		selectmode					1. 决定选择的模式
									2. 四种不同的选择模式：SINGLE（单选）、BROWSE（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、MULTIPLE（多选）和 EXTENDED（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）
									3. 默认是 BROWSE
		setgrid						1. 指定一个布尔类型的值，决定是否启用网格控制
									2. 默认值是 False
		takefocus					1. 指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来）
									2. 默认值是 True
		width						1. 设置 Listbox 的宽度（单位是文本单元）
									2. 文本单元是英文字母的平均宽度（所以如果该选项设置为 2，那么是无法容纳"ww"这两个宽度大于平均宽度的字母的）
									3. 默认值是 20
		xscrollcommand				1. 为 Listbox 组件添加一条水平滚动条
									2. 将此选项与 Scrollbar 组件相关联即可
		yscrollcommand				1. 为 Listbox 组件添加一条垂直滚动条
									2. 将此选项与 Scrollbar 组件相关联即可
		

- ListBox相关方法
	
		activate(index)			-- 将给定索引号对应的选项激活（在其文本下方画一条下划线）
		bbox(index) 			-- 返回给定索引号对应的选项的边框
								-- 返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)
								-- xoffset 和 yoffset 表示距离左上角的偏移位置
								-- 返回的 width 是文本的实际宽度（像素为单位）
								-- 如果指向的选项是不可见的，那么返回值是 None
		curselection() 			-- 返回一个元组，包含被选中的选项的序号（从 0 开始）
								-- 如果没有选中任何选项，返回一个空元组
		delete(first, last=None)-- 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项
								-- 如果忽略 last 参数，表示删除 first 参数指定的选项
		get(first, last=None) 	-- 返回一个元组，包含参数 first 到 last 范围内（包含 first 和 last）的所有选项的文本
								-- 如果忽略 last 参数，表示返回 first 参数指定的选项的文本
		index(index) 			-- 返回与 index 参数相应的选项的序号（例如 lb.index(END)）
		insert(index, *elements)-- 添加一个或多个项目到 Listbox 中
								-- 使用 lb.insert(END) 添加新选项到末尾
		itemcget(index, option) -- 获得 index 参数指定的项目对应的选项（由 option 参数指定）
		itemconfig(index, **options)-- 设置 index 参数指定的项目对应的选项（由可变参数 **option 指定）
		nearest(y)				-- 返回与给定参数 y 在垂直坐标上最接近的项目的序号
		scan_dragto(x, y) 		-- 见下方 scan_mark(x, y)
		scan_mark(x, y) 		-- 使用这种方式来实现 Listbox 内容的滚动
								-- 需要将鼠标按钮事件及当前鼠标位置绑定到 scan_mark(x, y) 方法，然后再将 <motion> 事件及当前鼠标位置绑定到 scan_dragto(x, y) 方法，就可以实现 Listbox 在当前位置和 sacn_mack(x, y) 指定的位置 (x, y) 之间滚动
		see(index) 				-- 调整列表框的位置，使得 index 参数指定的选项是可见的
		select_anchor(index) 	-- 与 selection_anchor(index) 相同，见下方解释
		select_clear(first, last=None)-- 与 selection_clear(first, last=None) 相同，见下方解释
		select_includes(index) 	-- 与 selection_includes(index) 相同，见下方解释
		select_set(first, last=None)-- 与 selection_set(first, last=None) 相同，见下方解释
		selection_anchor(index)	-- 在 index 参数的位置下一个锚点，此后你就可以通过特殊索引 ANCHOR 访问
		selection_clear(first, last=None)-- 取消参数 first 到 last 范围内（包含 first 和 last）选项的选中状态
										-- 如果忽略 last 参数，则只取消 first 参数指定选项的选中状态
		selection_includes(index) 	-- 返回 index 参数指定的选项的选中状态
									-- 返回 1 表示选中，返回 0 表示未选中
		selection_set(first, last=None) -- 设置参数 first 到 last 范围内（包含 first 和 last）选项为选中状态
										-- 如果忽略 last 参数，则只设置 first 参数指定选项为选中状态
		size() 					-- 返回 Listbox 组件中选项的数量
		xview(*args) 			-- 该方法用于在水平方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
								-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
								-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：xview(SCROLL, 3, UNITS) 表示向右滚动三行
		xview_moveto(fraction) 	-- 跟 xview(MOVETO, fraction) 一样
		xview_scroll(number, what)-- 跟 xview(SCROLL, number, what) 一样
		yview(*args)			-- 该方法用于在垂直方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
								-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最顶端，1.0 表示最底端
								-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：yview(SCROLL, 3, PAGES) 表示向下滚动三页
		yview_moveto(fraction) 	-- 跟 yview(MOVETO, fraction) 一样
		yview_scroll(number, what) 	-- 跟 yview(SCROLL, number, what) 一样

##2.Scrollbar
在某个组件上安装垂直滚动条Scrollbar

1. 设置该组件的yscrollbarcommand选项为Scrollbar组建的set()方法
2. 设置Scrollbar组建的command选项为该组件的yview()方法

示例：

	from tkinter import *
	root = Tk()		
	sb = Scrollbar(root)
	sb.pack(side=RIGHT,fill=Y)	
	lb = Listbox(root,yscrollcommand=sb.set)	
	for i in range(1000):
	    lb.insert(END,i)	
	lb.pack(side=LEFT,fill=BOTH)
	sb.config(command=lb.yview)		    
	mainloop()

##3.scale
Scale范围控件，显示一个数值刻度，为输出限定范围的数字区间,样式和scrollbar类似

	from tkinter import *
	root = Tk()
	s1 = Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200)
	s1.pack()
	s2 = Scale(root,from_=0,to=200,tickinterval=20,orient=HORIZONTAL,length=600)
	s2.pack()
	def show():
	    print(s1.get(),s2.get())
	Button(root,text="获取位置",command=show).pack()
	mainloop()

	tickinterval   			--指定刻度间距
	resolution				--指定显示精度，就是每一步走多少
	length					--指定Scrollbar的长度

#7.1
tips：


##1.Text组件
该组件用于显示和处理多行文本，主要用于显示多行文本，也常常作为简单的文字编辑器和浏览器使用

- 创建Text组件，它里面是没有内容的，需要insert()方法为其插入内容

		from tkinter import *
		root = Tk()		
		text = Text(root,width=30,height=2)
		text.pack()		
		text.insert(INSERT,"I love you \n")		//在开始处插入
		text.insert(END,"Do you know")			//在结尾处插入
		mainloop()

- 可以插入其他组件，用window_create()方法

		from tkinter import *
		root = Tk()	
		text = Text(root,width=30,height=5)
		text.pack()
		text.insert(INSERT,"I love you \n")
		text.insert(END,"Do you know")	
		def show():
		    print("被点击了")	
		b1 = Button(text,text="click",command=show)
		text.window_create(INSERT,window=b1)		//window窗口组件
		mainloop()

- 可以插入图片image_create()方法

		from tkinter import *
		root = Tk()	
		text = Text(root,width=30,height=30)
		text.pack()
		photo = PhotoImage(file="18.gif")
		def show():
		    text.image_create(END,image=photo)	
		b1 = Button(text,text="click",command=show)
		text.window_create(INSERT,window=b1)
		mainloop()
##1.1Indexes(索引)用法
Indexes（索引）是用来指向 Text 组件中文本的位置，跟 Python 的序列索引一样，Text 组件索引也是对应实际字符之间的位置。Tkinter 提供一系列不同的索引类型：

	"line.column"（行/列）
	"line.end"（某一行的末尾）
	INSERT				对应插入光标的位置。	
	CURRENT				对应与鼠标坐标最接近的位置。不过，如果你紧按鼠标任何一个按钮，它会直到你松开它才响应。
	END					对应 Text 组件的文本缓冲区最后一个字符的下一个位置。
	user-defined marks			user-defined marks 是对 Text 组件中位置的命名。INSERT 和 CURRENT 是两个预先命名好的 marks，除此之外你可以自定义 marks（请参考下方【Marks 用法】
	user-defined tags（"tag.first"，"tag.last"）				User-defined tags 代表可以分配给 Text 组件的特殊事件绑定和风格（请参考下方【Tags 用法】）
	selection（SEL_FIRST，SEL_LAST）				selection 是一个名为 SEL（或 "sel"）的特殊 tag，表示当前被选中的范围，你可以使用  SEL_FIRST 到 SEL_LAST 来表示这个范围。如果没有选中的内容，那么 Tkinter 会抛出一个TclError 异常。
	window coordinate（"@x,y"）
	embedded object name（window，images）			embedded object name 用于指向在 Text 组件中嵌入的 window 和 image 对象。要引用一个 window，只要简单地将一个 Tkinter 组件实例作为索引即可。引用一个嵌入的 image，只需使用相应的 PhotoImage 和 BitmapImage 对象。
	expressions			expressions 用于修改任何格式的索引，用字符串的形式实现修改索引的表达式。
- "line.column"行/列 是最基础的索引方式，它们将索引位置的行号和列号以字符串的形式表示出来（中间以 "." 分隔，例如 "1.0"）。需要注意的是，行号以 1 开始，列号则以 0 开始。使用 index() 方法可以将所有支持的“索引”格式转换为“行/列”格式的索引号。

		text.insert(INSERT, "I love FishC")
		print(text.get("1.2", 1.6))		//打印从第一行第三个字母开始到第一行第七个字母结束
- "line.end"行号加上字符串 ".end" 的格式表示为该行最后一个字符的位置

		text.insert(INSERT, "I love FishC")
		print(text.get("1.2", "1.end"))
- expressionsexpressions 用于修改任何格式的索引，用字符串的形式实现修改索引的表达式。具体表达式实现如下：

		表达式				含义
		"+ count chars"	1. 将索引向前（->）移动 count 个字符
		2. 可以越过换行符，但不能超过 END 的位置
		"- count chars"	1. 将索引向后（<-）移动 count 个字符
		2. 可以越过换行符，但不能超过 "1.0" 的位置
		"+ count lines"	1. 将索引向前（->）移动 count 行
		2. 索引会尽量保持与移动前在同一列上，但如果移动后的那一行字符太少，将移动到该行的末尾
		"- count lines"	1. 将索引向后（<-）移动 count 行
		2. 索引会尽量保持与移动前在同一列上，但如果移动后的那一行字符太少，将移动到该行的末尾
		" linestart"	1. 将索引移动到当前索引所在行的起始位置
		2. 注意，使用该表达式前边必须有一个空格隔开
		" lineend"	1. 将索引移动到当前索引所在行的末尾
		2. 注意，使用该表达式前边必须有一个空格隔开
		" wordstart"	1. 将索引移动到当前索引指向的单词的开头
		2. 单词的定义是一系列字母、数字、下划线或任何非空白字符的组合
		3. 注意，使用该表达式前边必须有一个空格隔开
		" wordend"	1. 将索引移动到当前索引指向的单词的末尾
		2. 单词的定义是一系列字母、数字、下划线或任何非空白字符的组合
		3. 注意，使用该表达式前边必须有一个空格隔开

TIPS：只要结果不产生歧义，关键字可以被缩写，空格也可以省略。例如："+ 5 chars" 可以简写成 "+5c"

##1.2Marks 用法
Marks（标记）通常是嵌入到 Text 组件文本中的不可见对象。事实上 Marks 是指定字符间的位置，并跟随相应的字符一起移动。Marks 有 INSERT，CURRENT 和 user-defined marks（用户自定义的 Marks）。其中，INSERT 和 CURRENT 是 Tkinter 预定义的特殊 Marks，它们不能够被删除。<br/>
INSERT（或 "insert"）用于指定当前插入光标的位置，Tkinter 会在该位置绘制一个闪烁的光标（因此并不是所有的 Marks 都不可见）。<br/>
CURRENT（或 "current"）用于指定与鼠标坐标最接近的位置。不过，如果你紧按鼠标任何一个按钮，它会直到你松开它才响应。<br/>
你还可以自定义任意数量的 Marks，Marks 的名字是由普通字符串组成，可以是除了空白字符外的任何字符（为了避免歧义，你应该起一个有意义的名字）。使用 mark_set() 方法创建和移动 Marks。<br/>

如果你在一个 Mark 标记的位置之前插入或删除文本，那么 Mark 跟着一并移动。删除 Marks 你需要使用 mark_unset() 方法，删除 Mark 周围的文本并不会删除 Mark 本身。<br/>

1. 例1，Mark 事实上就是索引，用于表示位置：

		text.insert(INSERT, "I love FishC")
		text.mark_set("here", "1.2")
		text.insert("here", "插")
2. 例2，如果 Mark 前边的内容发生改变，那么 Mark 的位置也会跟着移动

		text.insert(INSERT, "I love FishC")
		text.mark_set("here", "1.2")
		text.insert("here", "插")
		text.insert("here", "入")
3. 如果 Mark 周围的文本被删除了，Mark 仍然还在

		text.insert(INSERT, "I love FishC")
		text.mark_set("here", "1.2")
		text.insert("here", "插")
		
		text.delete("1.0", END)
		text.insert("here", "入")
4. 只有 mark_unset() 方法可以解除 Mark 的封印：
		
		text.insert(INSERT, "I love FishC")
		text.mark_set("here", "1.2")
		text.insert("here", "插")
		
		text.mark_unset("here")
		
		text.delete("1.0", END)
		text.insert("here", "入")
5. 默认插入内容到 Mark，是插入到它的左侧（就是说插入一个字符的话，Mark 向后移动了一个字符的位置）。那能不能插入到 Mark 的右侧呢？其实是可以的，通过 mark_gravity() 方法就可以实现。

		text.insert(INSERT, "I love FishC")

		text.mark_set("here", "1.2")
		text.mark_gravity("here", LEFT)
		
		text.insert("here", "插")
		text.insert("here", "入")
##1.3Tags用法
Tags（标签）通常用于改变 Text 组件中内容的样式和功能。你可以修改文本的字体、尺寸和颜色。另外，Tags 还允许你将文本、嵌入的组件和图片与键盘和鼠标等事件相关联。除了 user-defined tags（用户自定义的 Tags），还有一个预定义的特殊 Tag：SEL。<br/>
SEL（或 "sel"）用于表示对应的选中内容（如果有的话）。<br/>
你可以自定义任意数量的 Tags，Tags 的名字是由普通字符串组成，可以是除了空白字符外的任何字符。另外，任何文本内容都支持多个 Tags 描述，任何 Tag 也可以用于描述多个不同的文本内容。<br/>
- 为指定文本添加 Tags 可以使用 tag_add() 方法：

		text.insert(INSERT, "I love FishC.com!")
		text.tag_add("tag1", "1.7", "1.12", "1.14")
		text.tag_config("tag1", background="yellow", foreground="red")
- 使用 tag_config() 方法可以设置 Tags 的样式。下边罗列了 tag_congif() 方法可以使用的选项：

		选项								含义
		background				1. 指定该 Tag 所描述的内容的背景颜色
								2. 注意：bg 并不是该选项的缩写，在这里 bg 被解释为 bgstipple 选项的缩写
		bgstipple				1. 指定一个位图作为背景，并使用 background 选项指定的颜色填充
								2. 只有设置了 background 选项该选项才会生效
								3. 默认的标准位图有：'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question' 和 'warning'
		borderwidth				1. 指定文本框的宽度
								2. 默认值是 0
								3. 只有设置了 relief 选项该选项才会生效
								4. 注意：该选项不能使用 bd 缩写
		fgstipple				1. 指定一个位图作为前景色
								2. 默认的标准位图有：'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question' 和 'warning'
		font					指定该 Tag 所描述的内容使用的字体
		foreground				1. 指定该 Tag 所描述的内容的前景色
								2. 注意：fg 并不是该选项的缩写，在这里 fg 被解释为 fgstipple 选项的缩写
		justify					1. 控制文本的对齐方式
								2. 默认是 LEFT（左对齐），还可以选择 RIGHT（右对齐）和 CENTER（居中）
								3. 注意：需要将 Tag 指向该行的第一个字符，该选项才能生效
		lmargin1				1. 设置 Tag 指向的文本块第一行的缩进
								2. 默认值是 0
								3. 注意：需要将 Tag 指向该文本块的第一个字符或整个文本块，该选项才能生效
		lmargin2				1. 设置 Tag 指向的文本块除了第一行其他行的缩进
								2. 默认值是 0
								1. 注意：需要将 Tag 指向整个文本块，该选项才能生效
		offset					1. 设置 Tag 指向的文本相对于基线的偏移距离
								2. 可以控制文本相对于基线是升高（正数值）或者降低（负数值）
								3. 默认值是 0
		overstrike				1. 在 Tag 指定的文本范围画一条删除线
								2. 默认值是 False
		relief					1. 指定 Tag 对应范围的文本的边框样式
								2. 可以使用的值有：SUNKEN, RAISED, GROOVE, RIDGE 或 FLAT
								3. 默认值是 FLAT（没有边框）
		rmargin					1. 设置 Tag 指向的文本块右侧的缩进
								2. 默认值是 0
		spacing1				1. 设置 Tag 所描述的文本块中每一行与上方的空白间隔
								2. 注意：自动换行不算
								3. 默认值是 0
		spacing2				1. 设置 Tag 所描述的文本块中自动换行的各行间的空白间隔
								2. 注意：换行符（'\n'）不算
								3. 默认值是 0
		spacing3				1. 设置 Tag 所描述的文本块中每一行与下方的空白间隔 
								2. 注意：自动换行不算
								3. 默认值是 0
		tabs					1. 定制 Tag 所描述的文本块中 Tab 按键的功能
								2. 默认 Tab 被定义为 8 个字符的宽度
								3. 你还可以定义多个制表位：tabs=('3c', '5c', '12c') 表示前 3 个 Tab 宽度分别为 3厘米，5厘米，12厘米，接着的 Tab 按照最后两个的差值计算，即：19厘米，26厘米，33厘米
								4. 你应该注意到了，它上边 'c' 的含义是“厘米”而不是“字符”，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
								5. 如果是一个整型值，则单位是像素
		underline				1. 该选项设置为 True 的话，则 Tag 所描述的范围内文本将被画上下划线
								2. 默认值是 False
		wrap					1. 设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行
								2. 该选项的值可以是：NONE（不自动换行），CHAR（按字符自动换行）和 WORD（按单词自动换行）
- 如果你对同一个范围内的文本加上多个 Tags，并且设置相同的选项，那么新创建的 Tag 样式会覆盖比较旧的 Tag.
- 可以使用 tag_raise() 和 tag_lower() 方法来提高和降低某个 Tag 的优先级：
- Tags 还支持事件绑定，使用的是 tag_bind() 的方法

		from tkinter import *
		import webbrowser		//导入浏览器模块
		root = Tk()		
		text = Text(root, width=30, height=5)				//设置Text大小
		text.pack()											//打包text
		text.insert(INSERT, "I love FishC.com!")			//插入内容
		text.tag_add("link", "1.7", "1.16")					//在第一行7-16列之间添加tag
		text.tag_config("link", foreground="blue", underline=True)		//设置tag格式
		def show_hand_cursor(event):
		    text.config(cursor="arrow")				
		def show_arrow_cursor(event):
		    text.config(cursor="xterm")		
		def click(event):
		    webbrowser.open("http://www.fishc.com")			//浏览器打开网址
		text.tag_bind("link", "<Enter>", show_hand_cursor)		//当鼠标进入该文本段的时候，鼠标样式切换为 "arrow" 形态
		text.tag_bind("link", "<Leave>", show_arrow_cursor)		//离开文本段的时候切换回 "xterm" 形态
		text.tag_bind("link", "<Button-1>", click)			//当触发鼠标“左键点击操作”事件的时候，使用默认浏览器打开连接		
		mainloop()

##1.4text参数方法

	Text(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：
	选项								含义
	autoseparators			1. 指定实现“撤销”操作的时候是否自动插入一个“分隔符”（用于分隔操作记录）
							2. 默认值是 True
							3. 详见上方用法【“撤销”和“恢复”操作】
	background				1. 设置 Text 组件的背景颜色
							2. 注意：通过使用 Tags 可以使 Text 组件中的文本支持多种背景颜色显示（请参考上方【Tags 用法】）
	bg						跟 background 一样
	borderwidth				1. 设置 Entry 的边框宽度
							2. 默认值是 1 像素
	bd						跟 borderwidth 一样
	cursor					1. 指定当鼠标在 Text 组件上飘过的时候的鼠标样式
							2. 默认值由系统指定
	exportselection			1. 指定选中的文本是否可以被复制到剪贴板
							2. 默认值是 True
							3. 可以修改为 False 表示不允许复制文本
	font					1. 设置 Text 组件中文本的默认字体
							2. 注意：通过使用 Tags 可以使 Text 组件中的文本支持多种字体显示（请参考上方【Tags 用法】）
	foreground				1. 设置 Text 组件中文本的颜色
							2. 注意：通过使用 Tags 可以使 Text 组件中的文本支持多种颜色显示（请参考上方【Tags 用法】）
	fg						跟 foreground 一样
	height					1. 设置 Text 组件的高度
							2. 注意：单位是行数，不是像素噢
	highlightbackground		1. 指定当 Text 组件没有获得焦点的时候高亮边框的颜色
							2. 默认值由系统指定
	highlightcolor			1. 指定当 Text 组件获得焦点的时候高亮边框的颜色
							2. 默认值由系统指定
	highlightthickness		1. 指定高亮边框的宽度
							2. 默认值是 0
	insertbackground		1. 设置插入光标的颜色
							2. 默认是 BLACK（或 "black"）
	insertborderwidth		1. 设置插入光标的边框宽度
							2. 默认值是 0
							3. 提示：你得设置 insertwidth 选项为比较大的数值才能看出来噢
	insertofftime			1. 该选项控制光标的闪烁频率（灭）
							2. 单位是毫秒
	insertontime			1. 该选项控制光标的闪烁频率（亮）
							2. 单位是毫秒
	insertwidth				1. 指定光标的宽度
							2. 默认值是 2 像素
	maxundo					1. 设置允许“撤销”操作的最大次数
							2. 默认值是 0
							3. 设置为 -1 表示不限制
	padx					1. 指定水平方向上的额外间距（内容和边框间）
							2. 默认值是 1
	pady					1. 指定垂直方向上的额外间距（内容和边框间）
							2. 默认值是 1
	relief					1. 指定边框样式
							2. 默认值是 SUNKEN
							3. 其他可以选择的值是 FLAT，RAISED，GROOVE 和 RIDGE
	selectbackground		1. 指定被选中文本的背景颜色
							2. 默认值由系统指定
	selectborderwidth		1. 指定被选中文本的边框宽度
							2. 默认值是 0
	selectforeground		1. 指定被选中文本的字体颜色
							2. 默认值由系统指定
	setgrid					1. 指定一个布尔类型的值，确定是否启用网格控制
							2. 默认值是 False
	spacing1				1. 指定 Text 组件的文本块中每一行与上方的空白间隔
							2. 注意：自动换行不算
							3. 默认值是 0
	spacing2				1. 指定 Text 组件的文本块中自动换行的各行间的空白间隔
							2. 注意：换行符（'\n'）不算
							3. 默认值是 0
	spacing3				1. 指定 Text 组件的文本中每一行与下方的空白间隔 
							2. 注意：自动换行不算
							3. 默认值是 0
	state					1. 默认情况下 Text 组件响应键盘和鼠标事件（NORMAL）
							2. 如果将该选项的值设置为 DISABLED，那么上述响应就不会发生，并且你无法修改里边的内容
	tabs					1. 定制 Tag 所描述的文本块中 Tab 按键的功能
							2. 默认 Tab 被定义为 8 个字符的宽度
							3. 你还可以定义多个制表位：tabs=('3c', '5c', '12c') 表示前 3 个 Tab 宽度分别为 3厘米，5厘米，12厘米，接着的 Tab 按照最后两个的差值计算，即：19厘米，26厘米，33厘米
							4. 你应该注意到了，它上边 'c' 的含义是“厘米”而不是“字符”，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
							5. 如果是一个整型值，则单位是像素
	takefocus				1. 指定使用 Tab 键可以将焦点移动到 Text 组件中
							2. 默认是开启的，可以将该选项设置为 False 避免焦点在此 Text 组件中
	undo					1. 该选项设置为 True 开启“撤销”功能
							2. 该选项设置为 False 关闭“撤销”功能
							3. 默认值是 False
	width					1. 设置 Text 组件的宽度
							2. 注意：单位是字符数，因此 Text 组件的实际宽度还取决于字体的大小
	wrap					1. 设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行
							2. 该选项的值可以是：NONE（不自动换行），CHAR（按字符自动换行）和 WORD（按单词自动换行）
	xscrollcommand			1. 与 scrollbar（滚动条）组件相关联（水平方向）
							2. 使用方法可以参考：Scrollbar 组件
	yscrollcommand			1. 与 scrollbar（滚动条）组件相关联（垂直方向）
							2. 使用方法可以参考：Scrollbar 组件

方法

	bbox(index)
				-- 返回给定索引指定的字符的边界框
				-- 返回值是一个 4 元组：(x, y, width, height)
				-- 如果该字符是不可见的，那么返回 None
				-- 注意：只有当 Text 组件被更新的时候该方法才有效，可以使用 update_idletasks() 方法先更新 Text 组件
	compare(index1, op, index2)
					-- 返回对比 index1 和 index2 指定的两个字符的结果
					-- op 是操作符：'<', '<=', '==', '>=', '>' 或 '!='（不支持 Python 的 '<>' 操作符）
					-- 返回布尔类型的值表示对比的结果	
	debug(boolean=None)
					-- 开启或关闭 Debug 状态	
	delete(start, end=None)
					-- 删除给定范围的文本或嵌入对象
					-- 如果在给定范围内有任何 Marks 标记的位置，则将 Marks 移动到 start 参数开始的位置	
	dlineinfo(index)
					-- 返回给定索引指定的字符所在行的边界框
					-- 返回值是一个 5 元组：(x, y, width, height, offset)，offset 表示从该行的顶端到基线的偏移
					-- 如果该行不可见，则返回 None
					-- 注意：只有当 Text 组件被更新的时候该方法才有效，可以使用 update_idletasks() 方法先更新 Text 组件	
	dump(index1, index2=None, command=None, **kw)
					-- 返回 index1 和 index2 之间的内容
					-- 返回的值是一个由 3 元组（关键词，值，索引）组成的列表，关键词参数的顺序为：all, image, mark, tag, text, window
					-- 默认关键词是 'all'，表示全部关键词均为选中状态
					-- 如果需要筛选个别关键词，可以用 dump(index1, index2, image=True, text=True) 这样的形式调用
					-- 如果指定了 command 函数，那么会为列表中的每一个三元组作为参数调用一次该函数（这种情况下，dump() 不返回值）	
	edit_modified(arg=None)
					-- 该方法用于查询和设置 modified 标志（该标标志用于追踪 Text 组件的内容是否发生变化）
					-- 如果不指定 arg 参数，那么返回 modified 标志是否被设置
					-- 你可以传递显式地使用 True 或 False 作为参数来设置或清除 modified 标志
					-- 任何代码或用户的插入或删除文本操作，“撤销”或“恢复”操作，都会是的 modified 标志被设置	
	edit_redo(self)
					-- “恢复”上一次的“撤销”操作
					-- 如果 undo 选项为 False，该方法无效
					-- 详见上方用法【“撤销”和“恢复”操作】	
	edit_reset()
					-- 清空存放操作记录的栈	
	edit_separator()
					-- 插入一个“分隔符”到存放操作记录的栈中，用于表示已经完成一次完整的操作
					-- 如果 undo 选项为 False，该方法无效
					-- 详见上方用法【“撤销”和“恢复”操作】
	edit_undo()
					-- 撤销最近一次操作
					-- 如果 undo 选项为 False，该方法无效
					-- 详见上方用法【“撤销”和“恢复”操作】
	get(index1, index2=None)
					-- 返回 index1 到 index2（不包含）之间的文本
					-- 如果 index2 参数忽略，则返回一个字符
					-- 如果包含 image 和 window 的嵌入对象，均被忽略
					-- 如果包含有多行文本，那么自动插入换行符（'\n'）
	image_cget(index, option)
					-- 返回 index 参数指定的嵌入 image 对象的 option 选项的值
					-- 如果给定的位置没有嵌入 image 对象，则抛出 TclError 异常
	image_configure(index, **options)
					-- 修改 index 参数指定的嵌入 image 对象的一个或多个 option 选项的值
					-- 如果给定的位置没有嵌入 image 对象，则抛出 TclError 异常	
	image_create(index, cnf={}, **kw)
					-- 在 index 参数指定的位置嵌入一个 image 对象
					-- 该 image 对象必须是 Tkinter 的 PhotoImage 或 BitmapImage 实例
					-- 可选选项 align：设定此图像的垂直对齐，可以是 TOP、CENTER、BOTTOM 或 BASELINE
					-- 可选选项 image：PhotoImage 或 BitmapImage 对象
					-- 可选选项 name：你可以为该图像实例命名，如果你忽略此选项，那么 Tkinter 会自动为其取一个独一无二的名字。
					-- 可选选项 padx：设置水平方向上的额外间距
					-- 可选选项 pady：设置垂直方向上的额外间距	
	image_names()
					-- 返回 Text 组件中嵌入的所有 image 对象的名字	
	index(index)
					-- 将 index 参数指定的位置以 "line.column" 的索引形式返回
					-- index 参数支持任何格式的索引	
	insert(index, text, *tags)
					-- 在 index 参数指定的位置插入字符串
					-- 可选参数 tags 用于指定文本的样式
					-- 详见上方【Tags 用法】	
	mark_gravity(self, markName, direction=None)
					-- 设置 Mark 的方向，可以是 LEFT 或 RIGHT（默认是 RIGHT，即如果在 Mark 处插入文本的话，Mark 将发生相应的移动以保持在插入文本的右侧）
					-- 如果设置为 LEFT，那么在 Mark 处插入文本并不会移动 Mark（因为 Mark 在插入文本的左侧）
					-- 如果忽略 direction 参数，则返回指定 Mark 的方向
					-- 详见上方【Marks 用法】	
	mark_names()
					-- 返回 Text 组件中所有 Marks 的名字
					-- 包括两个特殊 Mark：INSERT 和 CURRENT
					-- 注意：END 是特殊的索引，不是 Mark
	mark_next(index)
					-- 返回在 index 指定的位置后边的一个 Mark 的名字
					-- 如果不存在则返回空字符串
	mark_previous(index)
					-- 返回在 index 指定的位置前边的一个 Mark 的名字
					-- 如果不存在则返回空字符串
	mark_set(markName, index)
					-- 移动 Mark 到 index 参数指定的位置
					-- 如果 markName 参数指定的 Mark 不存在，则创建一个新的 Mark
	mark_unset(*markNames)
					-- 删除 markNames 指定的 Marks
					-- 不能删除预定义的 INSERT 和 CURRENT
	replace(index1, index2, chars, *args)
					-- 将 index1 到 index2 之间的内容替换为 chars 参数指定的字符串
					-- 如果需要为替换的内容添加 Tag，可以在 args 参数指定 Tag
					-- 详见上方【Tags 用法】
	scan_dragto(x, y)
					-- 详见下方 scan_mark(x, y)
	scan_mark(x, y)
					-- 使用这种方式来实现 Text 组件内容的滚动
					-- 需要将鼠标按钮事件以及鼠标当前位置绑定到 scan_mark(x, y) 方法，然后将 <motion> 事件及当前鼠标位置绑定到 scan_dragto(x, y) 方法，就可以实现 Text 组件的内容在当前位置和 scan_mark(x, y) 指定的位置 (x, y) 之间滚动
	search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None)
					-- 从 index 开始搜索 pattern，到 stopindex 结束（不指定表示搜索到末尾）
					-- 如果成功找到，以 "line.column" 返回第一个匹配的字符；否则返回空字符串
					-- forwards 参数设置为 True 表示向前（->）搜索
					-- backwards 参数设置为 True 表示向后（<-）搜索
					-- exact 参数设置为 True 表示搜索与 pattern 完全匹配的结果
					-- regexp 参数设置为 True，则 pattern 被解释为 Tcl 格式的正则表达式
					-- nocase 参数设置为 True 是忽略大小写，默认是区分大小写的搜索
					-- count 参数指定为一个 IntVar 的 Tkinter 变量，用于存放当找到匹配的字符个数（如果匹配结果中没有嵌入的 image 或 window 对象的话，一般该值等于 pattern 的字符个数）
	see(index)
					-- 滚动内容，确保 index 指定的位置可见
	tag_add(tagName, index1, index2=None)
					-- 为 index1 到 index2 之间的内容添加一个 Tag（tagName 参数指定）
					-- 如果 index2 参数忽略，则单独为 index1 指定的内容添加 Tag
					-- 详见上方【Tags 用法】
	tag_bind(tagName, sequence, func, add=None)
					-- 为 Tag 绑定事件
					-- 详见上方【Tags 用法】
	tag_cget(tagName, option)
					-- 返回 tagName 指定的 option 选项的值
	tag_config(tagName, cnf=None, **kw)
					-- 跟 tag_configure(tagName, cnf=None, **kw) 一样
	tag_configure(tagName, cnf=None, **kw)
					-- 设置 tagName 的选项
					-- 详见上方【Tags 用法】
	tag_delete(*tagNames)
					-- 删除 tagNames 指定的 Tags
	tag_lower(tagName, belowThis=None)
					-- 降低 Tag 的优先级
					-- 如果 belowThis 参数不为空，则表示 tagName 需要比 belowThis 指定的 Tag 优先级更低
					-- 详见上方【Tags 用法】
	tag_names(index=None)
					-- 如果不带参数，表示返回 Text 组件中所有 Tags 的名字
					-- index 参数表示返回该位置上所有的 Tags 的名字
	tag_nextrange(tagName, index1, index2=None)
					-- 在 index1 到 index2 的范围内第一个 tagName 的位置
					-- 如果没有则返回空字符串
	tag_prevrange(tagName, index1, index2=None)
					-- tag_nextrange() 的反向查找，也就是查找范围是 index2 到 index1
	tag_raise(tagName, aboveThis=None)
					-- 提高 Tag 的优先级
					-- 如果 aboveThis 参数不为空，则表示 tagName 需要比 aboveThis 指定的 Tag 优先级更高
					-- 详见上方【Tags 用法】
	tag_ranges(tagName)
					-- 返回所有 tagName 指定的文本，并将它们的范围以列表的形式返回
	tag_remove(tagName, index1, index2=None)
					-- 删除 index1 到 index2 之间所有的 tagName
					-- 如果忽略 index2 参数，那么只删除 index1 指定的那个字符的 tagName（如果有的话）
	tag_unbind(tagName, sequence, funcid=None)
					-- 解除与 tagName 绑定的事件（sequence 指定）
	window_cget(index, option)
					-- 返回 index 参数指定的嵌入 window 对象的 option 选项的值
					-- 如果给定的位置没有嵌入 window 对象，则抛出 TclError 异常
	window_config(index, cnf=None, **kw)
					-- 跟 window_configure(index, cnf=None, **kw) 一样
	window_configure(index, cnf=None, **kw)
					-- 修改 index 参数指定的嵌入 window 对象的一个或多个 option 选项的值
					-- 如果给定的位置没有嵌入 window 对象，则抛出 TclError 异常
	window_create(index, **options)
					-- 在 index 参数指定的位置嵌入一个 window 对象
					-- 支持两种方式在 Text 组件中嵌入 window 对象：请看下方 create 选项和 window 选项的描述
					-- 可选选项 align：设定此图像的垂直对齐，可以是 TOP、CENTER、BOTTOM 或 BASELINE
					-- 可选选项 create：指定一个回调函数用于创建嵌入的 window 组件，该函数没有参数，并且必须创建 Text 的子组件并返回
					-- 可选选项 padx：设置水平方向上的额外间距
					-- 可选选项 pady：设置垂直方向上的额外间距
					-- 可选选项 stretch：该选项控制当行的高度大于嵌入组件的高度时，嵌入组件是否延伸。默认值是 False，表示组件保持原形；设置为 True 表示将该组件垂直部分延伸至行的高度
					-- 可选选项 window：指定一个已经创建好的 window 组件，该组件必须是 Text 组件的子组件
	window_names()
					-- 返回 Text 组件中嵌入的所有 window 对象的名字
	xview(*args)
					-- 该方法用于在水平方向上滚动 Text 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
					-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
					-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：xview(SCROLL, 3, UNITS) 表示向右滚动三行
	xview_moveto(fraction)
					-- 跟 xview(MOVETO, fraction) 一样
	xview_scroll(number, what)
					-- 跟 xview(SCROLL, number, what) 一样
	yview(*args)
					-- 该方法用于在垂直方向上滚动 Text 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
					-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最顶端，1.0 表示最底端
					-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：yview(SCROLL, 3, PAGES) 表示向下滚动三页
	yview_moveto(fraction)
					-- 跟 yview(MOVETO, fraction) 一样
	yview_scroll(number, what)
					-- 跟 yview(SCROLL, number, what) 一样

- 实例1.

		from tkinter import *
		import hashlib			//导入hash模块
		root = Tk()			
		text = Text(root, width=30, height=5)
		text.pack()			
		text.insert(INSERT, "I love FishC.com!")		
		contents = text.get("1.0",END)	
		def getsig(contents):
		    m = hashlib.md5(contents.encode())			//获取text的hash值
		    return m.digest()				//获取md5值加密后的结果用二进制表示
		sig = getsig(contents)	
		def check():
		    contents=text.get("1.0",END)
		    if sig != getsig(contents):
		        print("内容发生变动")
		    else:
		        print("风平浪静~")	
		Button(root,text="检查",command=check).pack()	
		mainloop()
- 示例2

		from tkinter import *
		import hashlib	
		root = Tk()			
		text = Text(root, width=30, height=5)
		text.pack()			
		text.insert(INSERT, "I love FishC.com!")
		def getIndex(text,index):
		    return tuple(map(int,str.split(text.index(index),".")))		//返回元祖，将行列对剪切，并将其转为int类型组成元祖
		start = "1.0"
		while True:
		    pos = text.search("o",start,stopindex=END)
		    if not pos:
		        break
		    print("找到啦，位置是：",getIndex(text,pos))
		    start = pos+"+1c"		//将start向右移动一个位置
		mainloop()
- 示例3

		from tkinter import *
		import hashlib
		root = Tk()		
		text = Text(root, width=30, height=5,undo=True)	//undo设置为TRUE
		text.pack()			
		text.insert(INSERT, "I love FishC.com!")	
		def show():
		    text.edit_undo()		//使用该方法撤销操作
		Button(root,text="撤销",command=show).pack()	
		mainloop()

##1.5“恢复”和“撤销”操作
Text 组件还支持“恢复”和“撤销”操作，这使得 Text 组件显得相当高大上。通过设置 undo 选项为 True 可以开启 Text 组件的“撤销”功能。然后用 edit_undo() 方法实现“撤销”操作，用 edit_redo() 方法实现“恢复”操作，这是因为 Text 组件内部有一个栈专门用于记录内容的每次变动，所以每次“撤销”操作就是一次弹栈操作，“恢复”就是再次压栈。<br/>

默认情况下，每一次完整的操作将会放入栈中。但怎么样算是一次完整的操作呢？Tkinter 觉得每次焦点切换、用户按下 Enter 键、删除\插入操作的转换等之前的操作算是一次完整的操作。也就是说你连续输入“FishC 是个 P”的话，一次的“撤销”操作就会将所有的内容删除。<br/>

那我们能不能自定义呢？比如我希望插入一个字符就算一次完整的操作，然后每次点击“撤销”就去掉一个字符。<br/>

当然可以！做法就是先将 autoseparators 选项设置为 False（因为这个选项是让 Tkinter 在认为一次完整的操作结束后自动插入“分隔符”），然后绑定键盘事件，每次有输入就用 edit_separator() 方法人为地插入一个“分隔符”：

	from tkinter import *
	root = Tk()	
	text = Text(root, width=30, height=5, autoseparators=False, undo=True, maxundo=10)
			//设置 undo 选项为 True 可以开启 Text 组件的“撤销”功能
	text.pack()	
	def callback(event):
	    text.edit_separator()
	text.bind('<Key>', callback)
	text.insert(INSERT, "I love FishC")
	def show():
	    text.edit_undo()
	Button(root, text="撤销", command=show).pack()
	mainloop()

#7.2
tips


##1.Canvas
Canvas（画布）组件为 Tkinter 的图形绘制提供了基础。Canvas 是一个高度灵活的组件，你可以用它绘制图形和图表，创建图形编辑器，并实现各种自定义的小部件。<br/>
- 在 Canvas 组件上绘制对象，可以用 create_xxx() 的方法（xxx 表示对象类型，例如线段 line，矩形 rectangle，文本 text 等）：

		from tkinter import *
		root = Tk()	
		w = Canvas(root, width=200, height=100)		//设置画框大小
		w.pack()	
		# 画一条黄色的横线
		w.create_line(0, 50, 200, 50, fill="yellow")		//两两组成两个坐标，绘制颜色为黄色的直线
		# 画一条红色的竖线（虚线）
		w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))		//dash设置虚线,4像素短线，4像素间隔
		# 中间画一个蓝色的矩形
		w.create_rectangle(50, 25, 150, 75, fill="blue")	
		mainloop()
- 注意，添加到 Canvas 上的对象会一直保留直着。如果你希望修改它们，你可以使用 coords()，itemconfig() 和 move() 方法来移动画布上的对象，或者使用 delete() 方法来删除：
	
		line1 = w.create_line(0, 50, 200, 50, fill="yellow")
		line2 = w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
		rect1 = w.create_rectangle(50, 25, 150, 75, fill="blue")
		w.coords(line1, 0, 25, 200, 25)		//将line1移动到相应坐标
		w.itemconfig(rect1, fill="red")		//设置对象的属性
		w.delete(line2)				//删除某个对象
		Button(root, text="删除全部", command=(lambda x=ALL : w.delete(x))).pack()
- 还可以在 Canvas 上显示文本，使用的是 create_text() 方法：

		w.create_line(0, 0, 200, 100, fill="green", width=3)
		w.create_line(200, 0, 0, 100, fill="green", width=3)
		w.create_rectangle(40, 20, 160, 80, fill="green")
		w.create_rectangle(65, 35, 135, 65, fill="yellow")
		w.create_text(100, 50, text="FishC",anchor=W)		//可同时设置text的位置
- 用 create_oval() 方法绘制椭圆形（或圆形），参数是指定一个限定矩形（Tkinter 会自动在这个矩形内绘制一个椭圆）：

		w.create_rectangle(40, 20, 160, 80, dash=(4, 4))
		w.create_oval(40, 20, 160, 80, fill="pink")			//给定矩形可限定椭圆
		w.create_text(100, 50, text="FishC")

- 绘制多边形，可以使用 create_polygon() 方法：

		from tkinter import *
		import math as m
		root = Tk()
		w = Canvas(root, width=200, height=100, background="red")
		w.pack()
		center_x = 100
		center_y = 50
		r = 50
		points = [
		    # 左上点
		    center_x - int(r * m.sin(2 * m.pi / 5)),
		    center_y - int(r * m.cos(2 * m.pi / 5)),
		    # 右上点
		    center_x + int(r * m.sin(2 * m.pi / 5)),
		    center_y - int(r * m.cos(2 * m.pi / 5)),
		    # 左下点
		    center_x - int(r * m.sin(m.pi / 5)),
		    center_y + int(r * m.cos(m.pi / 5)),
		    # 顶点
		    center_x,
		    center_y - r,
		    # 右下点
		    center_x + int(r * m.sin(m.pi / 5)),
		    center_y + int(r * m.cos(m.pi / 5)),
		    ]
		w.create_polygon(points, outline="green", fill="yellow")	//outline轮廓线，fill填充颜色，不指定fill默认为黑，fill值为空，填充颜色为透明
		mainloop()

- Tkinter 并没有提供画“点”的方法。不过，我们可以通过绘制一个超小的椭圆形来表示一个“点”。下边例子中，通过响应“鼠标左键按住拖动”事件（<B1-Motion>），我们在鼠标拖动的同时获取鼠标的实时位置（x, y），并绘制一个超小的椭圆来代表一个“点”：

		from tkinter import *
		root = Tk()
		w = Canvas(root, width=400, height=200)
		w.pack()
		def paint(event):			//event表示当前被鼠标点下的坐标
		    x1, y1 = (event.x - 1), (event.y - 1)
		    x2, y2 = (event.x + 1), (event.y + 1)
		    w.create_oval(x1, y1, x2, y2, fill="red")   
		w.bind("<B1-Motion>", paint)			//<B1-Motion>为鼠标左键
		Label(root, text="按住鼠标左键并移动，开始绘制你的理想蓝图吧......").pack(side=BOTTOM)
		mainloop()

##1.1Canvas 组件支持对象

	arc（弧形、弦或扇形）
	bitmap（内建的位图文件或 XBM 格式的文件）
	image（BitmapImage 或 PhotoImage 的实例对象）
	line（线）
	oval（圆或椭圆形）
	polygon（多边形）
	rectangle（矩形）
	text（文本）
	window（组件）
其中，弦、扇形、椭圆形、圆形、多边形和矩形这些“封闭式”图形都是由轮廓线和填充颜色组成的，但都可以设置为透明（传入空字符串表示透明）。
- 坐标系，由于画布可能比窗口大（带有滚动条的 Canvas 组件），因此 Canvas 组件可以选择使用两种坐标系：

	窗口坐标系：以窗口的左上角作为坐标原点
	画布坐标系：以画布的左上角作为坐标原点
	将窗口坐标系转换为画布坐标系，可以使用 canvasx() 或 canvasy() 方法：

		def callback(event):
	    canvas = event.widget
	    x = canvas.canvasx(event.x)
	    y = canvas.canvasy(event.y)
	    print canvas.find_closest(x, y)
- 画布对象显示的顺序

	Canvas 组件中创建的画布对象都会被列入显示列表中，越接近背景的画布对象位于显示列表的越下方。显示列表决定当两个画布对象重叠的时候是如何覆盖的（默认情况下新创建的会覆盖旧的画布对象的重叠部分，即位于显示列表上方的画布对象将覆盖下方那个）。当然，显示列表中的画布对象可以被重新排序。
- 指定画布对象，Canvas 组件提供几种方法让你指定画布对象：

		Item handles
		Tags
		ALL
		CURRENT
	Item handles 事实上是一个用于指定某个画布对象的整型数字（也成为画布对象的 ID）。当你在 Canvas 组件上创建一个画布对象的时候，Tkinter 将自动为其指定一个在该 Canvas 组件中独一无二的整型值。然后各种 Canvas 的方法可以通过这个值操纵该画布对象。

	Tags 是附在画布对象上的标签，Tags 由普通的非空白字符串组成。一个画布对象可以与多个 Tags 相关联，一个 Tag 也可用于描述多个画布对象。然而，与 Text 组件不同，没有指定画布对象的 Tags 不能进行事件绑定和配置样式。也就是说，Canvas 组件的 Tags 是仅为画布对象所拥有。
	
	Canvas 组件预定义了两个 Tags：ALL 和 CURRENT
	
	ALL（或 "all"）表示 Canvas 组件中的所有画布对象
	
	CURRENT（或 "current"）表示鼠标指针下的画布对象（如果有的话）
##1.2参数和方法
参数：

	Canvas(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

		选项							含义
	background					指定 Canvas 的背景颜色
	bg							跟 background 一样
	borderwidth					指定 Canvas 的边框宽度
	bd							跟 borderwidth 一样
	closeenough					1. 指定一个距离，当鼠标与画布对象的距离小于该值时，鼠标被认为在画布对象上
								2. 该选项是一个浮点类型的值
	confine						1. 指定 Canvas 组件是否允许滚动超出 scrollregion 选项指定的范围
								2. 默认值是 True
	cursor						指定当鼠标在 Canvas 上飘过的时候的鼠标样式
	height						1. 指定 Canvas 的高度
								2. 单位是像素
	highlightbackground			指定当 Canvas 没有获得焦点的时候高亮边框的颜色
	highlightcolor				指定当 Canvas 获得焦点的时候高亮边框的颜色
	highlightthickness			指定高亮边框的宽度
	relief						1. 指定 Canvas 的边框样式
								2. 默认值是 FLAT
								3. 其他可以选择的值是 SUNKEN，RAISED，GROOVE 和 RIDGE
	scrollregion				1. 指定 Canvas 可以被滚动的范围
								2. 该选项的值是一个 4 元组（x1, y1, x2, y2）表示的矩形
	selectbackground			指定当画布对象被选中时的背景色
	selectborderwidth			指定当画布对象被选中时的边框宽度（选中边框）
	selectforeground			指定当画布对象被选中时的前景色
	state						1. 设置 Canvas 的状态：NORMAL 或 DISABLED
								2. 默认值是 NORMAL
								3. 注意：该值不会影响画布对象的状态
	takefocus					1. 指定使用 Tab 键可以将焦点移动到输入框中
								2. 默认是开启的，可以将该选项设置为 False 避免焦点在此输入框中
	width						1. 指定 Canvas 的宽度
								2. 单位是像素
	xscrollcommand				1. 与 scrollbar（滚动条）组件相关联（水平方向）
								2. 使用方法可以参考：Scrollbar 组件
	xscrollincrement			1. 该选项指定 Canvas 水平滚动的“步长”
								2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
								3. 默认值是 0，表示可以水平滚动到任意位置
	yscrollcommand				1. 与 scrollbar（滚动条）组件相关联（垂直方向）
								2. 使用方法可以参考：Scrollbar 组件
	yscrollincrement			1. 该选项指定 Canvas 垂直滚动的“步长”
								2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
								3. 默认值是 0，表示可以水平滚动到任意位置
方法：

	addtag(tag, method, *args)
	-- 添加一个 Tag 到一系列画布对象中
	-- 指定添加 Tag 的位置，可以是："above"，"all"，"below"，"closest"，"enclosed"，"overlapping" 或 "withtag"
	-- args 是附加参数，请参考下方等同的方法
	
	addtag_above(tag, item)
	-- 为显示列表中 item 上方的画布对象添加 Tag
	-- 该方法相当于 addtag(tag, "above", item)
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	addtag_all(tag)
	-- 为 Canvas 组件中所有的画布对象添加 Tag
	-- 该方法相当于 addtag(tag, "all")
	
	addtag_below(tag, item)
	-- 为显示列表中 item 下方的画布对象添加 Tag
	-- 该方法相当于 addtag(tag, "below", item)
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	addtag_closest(tag, x, y, halo=None, start=None)
	-- 将 Tag 添加到与给定坐标（x, y）相临近的画布对象
	-- 可选参数 halo 指定一个距离，表示以（x, y）为中心，该距离内的所有画布对象均添加 Tag
	-- 可选参数 start 指定一个画布对象，该方法将为低于但最接近该对象的画布对象添加 Tag
	-- 该方法相当于 addtag(tag, "closet", x, y, halo=None, start=None)
	-- 注1：使用的是画布坐标系
	-- 注2：如果同时由几个画布对象与给定坐标（x, y）的距离相同，则为位于显示列表上方的那个画布对象添加 Tag
	
	addtag_enclosed(tag, x1, y1, x2, y2)
	-- 为所有坐标在矩形（x1, y1, x2, y2）中的画布对象添加 Tag
	-- 该方法相当于 addtag(tag, "enclosed", x1, y1, x2, y2)
	
	addtag_overlapped(tag, x1, y1, x2, y2)
	-- 跟 addtag_enclosed() 方法相似，不过该方法范围更广（即使画布对象只有一部分在矩形中也算）
	-- 该方法相当于 addtag(tag, "overlapping", x1, y1, x2, y2)
	
	addtag_withtag(tag, item)
	-- 为 item 参数指定的画布对象添加 Tag
	-- item 参数如果指定一个 Tag，则为所有拥有此 Tag 的画布对象添加新的 Tag
	-- item 参数如果指定一个画布对象，那么只为其添加 Tag
	-- 该方法相当于 addtag(tag, "withtag", item)
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	bbox(*args)
	-- 返回一个四元组（x1, y1, x2, y2）用于描述 args 指定的画布对象所在的矩形范围
	-- 如果 args 参数忽略，返回所有的画布对象所在的矩形范围
	
	canvasx(screenx, gridspacing=None)
	-- 将窗口坐标系的 X 坐标（screenx）转化为画布坐标系
	-- 如果提供 gridspacing 参数，则转换结果将为该参数的整数倍
	
	canvasy(screeny, gridspacing=None)
	-- 将窗口坐标系的 Y 坐标（screenx）转化为画布坐标系
	-- 如果提供 gridspacing 参数，则转换结果将为该参数的整数倍
	
	coords(*args)
	-- 如果仅提供一个参数（画布对象），返回该画布对象的坐标 (x1, y1, x2, y2)
	-- 你可以通过 coords(item, x1, y1, x2, y2) 来移动画布对象
	
	create_arc(bbox, **options)
	
	-- 根据 bbox (x1, y1, x2, y2) 创建一个扇形（PIESLICE）、弓形（CHORD）或弧形（ARC）
	-- 新创建的画布对象位于显示列表的顶端
	-- 创建成功后返回该画布对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
		选项							含义
	activedash					当画布对象状态为 ACTIVE 的时候，绘制虚线
	activefill					当画布对象状态为 ACTIVE 的时候，填充颜色
	activeoutline				当画布对象状态为 ACTIVE 的时候，绘制轮廓线
	activeoutlinestipple		当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图
	activestipple				当画布对象状态为 ACTIVE 的时候，指定填充的位图
	activewidth					当画布对象状态为 ACTIVE 的时候，指定边框的宽度
	dash						1. 指定绘制虚线轮廓
								2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔
								3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
	dashoffset					1. 指定虚线轮廓开始的偏移位置
								2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
	disableddash				当画布对象状态为 DISABLE 的时候，绘制虚线
	disabledfill				当画布对象状态为 DISABLE 的时候，填充颜色
	disabledoutline				当画布对象状态为 DISABLE 的时候，绘制轮廓线
	disabledoutlinestipple		当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图
	disabledstipple				当画布对象状态为 DISABLE 的时候，指定填充的位图
	disabledwidth				当画布对象状态为 DISABLE 的时候，指定边框的宽度
	extent						1. 指定跨度（从 start 选项指定的位置开始到结束位置的角度）
								2. 默认值是 90.0
	fill						1. 指定填充的颜色
								2. 空字符串表示透明
	offset						1. 指定当点画模式时填充位图的偏移
								2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outline						指定轮廓的颜色
	outlineoffset				1. 指定当点画模式绘制轮廓时位图的偏移
								2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outlinestipple				1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框
								2. 默认值是空字符串，表示黑色
	start						指定起始位置的偏移角度
	state						1. 指定该画布对象的状态
								2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
								3. 默认值是 NORMAL
	stipple						1. 指定一个位图用于填充
								2. 默认值是空字符串，表示实心
	style						1. 指定该方法创建的是扇形（PIESLICE）、弓形（CHORD）还是弧形（ARC）
								2. 默认创建的是扇形
	tags						为创建的画布对象添加标签
	width						指定边框的宽度

	create_bitmap(position, **options)
	
	-- 在 position 指定的位置（x, y）创建一个位图对象
	-- 创建成功后返回该位图对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
		选项						含义
	activebackground		指定当位图对象状态为 ACTIVE 时候的背景颜色
	activebitmap			指定当位图对象状态为 ACTIVE 时候填充的位图
	activeforeground		指定当位图对象状态为 ACTIVE 时候的前景颜色
	anchor					1. 指定位图在 position 参数的相对位置
							2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
							3. 默认值是 CENTER
	background				1. 指定背景颜色
							2. 即在位图中值为 0 的点的颜色
							2. 空字符串表示透明
	bitmap					指定显示的位图
	disabledbackground		指定当位图对象状态为 DISABLED 时候的背景颜色
	disabledbitmap			指定当位图对象状态为 DISABLED 时候填充的位图
	disabledforeground		指定当位图对象状态为 DISABLED 时候的前景颜色
	foreground				1. 指定前景颜色
							2. 即在位图中值为 1 的点的颜色
	state					1. 指定该画布对象的状态
							2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
							3. 默认值是 NORMAL
	tags					为创建的位图对象添加标签
	
	
	create_image(position, **options)
	
	-- 在 position 指定的位置（x, y）创建一个图片对象
	-- 创建成功后返回该图片对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
		选项					含义
	activeimage			指定当图片对象状态为 ACTIVE 时候显示的图片
	anchor				1. 指定位图在 position 参数的相对位置
						2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
						3. 默认值是 CENTER
	image				指定要显示的图片
	disabledimage		指定当图片对象状态为 DISABLED 时候显示的图片
	state				1. 指定该图片对象的状态
						2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
						3. 默认值是 NORMAL
	tags				为创建的图片对象添加标签
	
	
	create_line(coords, **options)
	
	-- 根据 coords 给定的坐标创建一条或多条线段
	-- 如果给定的坐标多余两个点，则会首尾相连变成一条折线
	-- 创建成功后返回该画布对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
		选项					含义
	activedash		当画布对象状态为 ACTIVE 的时候，绘制虚线
	activefill		当画布对象状态为 ACTIVE 的时候，填充颜色
	activestipple	当画布对象状态为 ACTIVE 的时候，指定填充的位图
	activewidth		当画布对象状态为 ACTIVE 的时候，指定边框的宽度
	arrow			1. 默认线段是不带箭头的
					2. 你可以通过设置该选项添加箭头到线段中
					3. FIRST 表示添加箭头到线段开始的位置
					4. LAST 表示添加箭头到线段结束的位置
					5. BOTH 表示两端均添加箭头
	arrowshape		1. 用一个三元组 (a, b, c) 来指定箭头的形状
					2. a, b, c 分别代表箭头的三条边的长
					3. 默认值是 (8, 10, 3)
	capstyle		1. 指定线段两端的样式
					2. 该选项的值可以是：
					-- BUTT（线段的两段平切于起点和终点）
					-- PROJECTING（线段的两段在起点和终点的位置分别延长一半 width 选项设置的长度）
					-- ROUND（线段的两段在起点和终点的位置分别延长一半 width 选项设置的长度并以圆角绘制）
					3. 默认值是 BUTT
					4. 如果还不理解请看小甲鱼下方图解你就秒懂了~
	dash			1. 绘制虚线
					2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔
					3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
	dashoffset		1. 指定虚线开始的偏移位置
	2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
	disableddash	当画布对象状态为 DISABLE 的时候，绘制虚线
	disabledfill	当画布对象状态为 DISABLE 的时候，填充颜色
	disabledstipple	当画布对象状态为 DISABLE 的时候，指定填充的位图
	disabledwidth	当画布对象状态为 DISABLE 的时候，指定边框的宽度
	fill			1. 指定填充的颜色
					2. 空字符串表示透明
	joinstyle		1. 指定当绘制两个相邻线段之间接口的样式
					2. 该选项的值可以是：
					-- ROUND（以连接点为圆心，1/2 width 选项设置的长度为半径绘制圆角）
					-- BEVEL（在连接点处对两线段的夹角平切）
					-- MITER（沿着两线段的夹角延伸至一个点）
					3. 默认值是 ROUND
					4. 如果还不理解请看上方 create_line() 函数 joinstyle 选项的图解你就秒懂了~
	offset			1. 指定当点画模式时填充位图的偏移
					2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	smooth			1. 该选项的值为 True 时，将绘制贝塞尔样条曲线代替线段（资料：戳我）
					2. 默认值为 False
	splinesteps		1. 当绘制贝塞尔样条曲线的时候，该选项指定由多少条折线来构成曲线
					2. 默认值是 12
					3. 只有当 smooth 选项为 True 时该选项才能生效
	state			1. 指定该画布对象的状态
					2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
					3. 默认值是 NORMAL
	stipple			1. 指定一个位图用于填充
					2. 默认值是空字符串，表示实心
	tags			为创建的画布对象添加标签
	width			指定边框的宽度
	create_oval(bbox, **options)
	
	-- 根据限定矩形 bbox 绘制一个椭圆
	-- 新创建的画布对象位于显示列表的顶端
	-- 创建成功后返回该画布对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	activedash	当画布对象状态为 ACTIVE 的时候，绘制虚线
	activefill	当画布对象状态为 ACTIVE 的时候，填充颜色
	activeoutline	当画布对象状态为 ACTIVE 的时候，绘制轮廓线
	activeoutlinestipple	当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图
	activestipple	当画布对象状态为 ACTIVE 的时候，指定填充的位图
	activewidth	当画布对象状态为 ACTIVE 的时候，指定边框的宽度
	dash	1. 指定绘制虚线轮廓
	2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔
	3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
	dashoffset	1. 指定虚线轮廓开始的偏移位置
	2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
	disableddash	当画布对象状态为 DISABLE 的时候，绘制虚线
	disabledfill	当画布对象状态为 DISABLE 的时候，填充颜色
	disabledoutline	当画布对象状态为 DISABLE 的时候，绘制轮廓线
	disabledoutlinestipple	当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图
	disabledstipple	当画布对象状态为 DISABLE 的时候，指定填充的位图
	disabledwidth	当画布对象状态为 DISABLE 的时候，指定边框的宽度
	fill	1. 指定填充的颜色
	2. 空字符串表示透明
	offset	1. 指定当点画模式时填充位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outline	指定轮廓的颜色
	outlineoffset	1. 指定当点画模式绘制轮廓时位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outlinestipple	1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框
	2. 默认值是空字符串，表示黑色
	state	1. 指定该画布对象的状态
	2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
	3. 默认值是 NORMAL
	stipple	1. 指定一个位图用于填充
	2. 默认值是空字符串，表示实心
	tags	为创建的画布对象添加标签
	width	指定边框的宽度
	
	
	create_polygon(coords, **options)
	
	-- 根据 coords 给定的坐标绘制一个多边形
	-- 新创建的画布对象位于显示列表的顶端
	-- 创建成功后返回该画布对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	activedash	当画布对象状态为 ACTIVE 的时候，绘制虚线
	activefill	当画布对象状态为 ACTIVE 的时候，填充颜色
	activeoutline	当画布对象状态为 ACTIVE 的时候，绘制轮廓线
	activeoutlinestipple	当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图
	activestipple	当画布对象状态为 ACTIVE 的时候，指定填充的位图
	activewidth	当画布对象状态为 ACTIVE 的时候，指定边框的宽度
	dash	1. 指定绘制虚线轮廓
	2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔
	3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
	dashoffset	1. 指定虚线轮廓开始的偏移位置
	2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
	disableddash	当画布对象状态为 DISABLE 的时候，绘制虚线
	disabledfill	当画布对象状态为 DISABLE 的时候，填充颜色
	disabledoutline	当画布对象状态为 DISABLE 的时候，绘制轮廓线
	disabledoutlinestipple	当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图
	disabledstipple	当画布对象状态为 DISABLE 的时候，指定填充的位图
	disabledwidth	当画布对象状态为 DISABLE 的时候，指定边框的宽度
	fill	1. 指定填充的颜色
	2. 空字符串表示透明
	joinstyle	1. 指定当绘制两个相邻线段之间接口的样式
	2. 该选项的值可以是：
	-- ROUND（以连接点为圆心，1/2 width 选项设置的长度为半径绘制圆角）
	-- BEVEL（在连接点处对两线段的夹角平切）
	-- MITER（沿着两线段的夹角延伸至一个点）
	3. 默认值是 ROUND
	4. 如果还不理解请看小甲鱼下方图解你就秒懂了~
	offset	1. 指定当点画模式时填充位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outline	指定轮廓的颜色
	outlineoffset	1. 指定当点画模式绘制轮廓时位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outlinestipple	1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框
	2. 默认值是空字符串，表示黑色
	smooth	1. 该选项的值为 True 时，将绘制贝塞尔样条曲线代替线段（资料：戳我）
	2. 默认值为 False
	splinesteps	1. 当绘制贝塞尔样条曲线的时候，该选项指定由多少条折线来构成曲线
	2. 默认值是 12
	3. 只有当 smooth 选项为 True 时该选项才能生效
	state	1. 指定该画布对象的状态
	2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
	3. 默认值是 NORMAL
	stipple	1. 指定一个位图用于填充
	2. 默认值是空字符串，表示实心
	tags	为创建的画布对象添加标签
	width	指定边框的宽度
	
	
	create_rectangle(bbox, **options)
	
	-- 根据限定矩形 bbox 绘制一个矩形
	-- 新创建的画布对象位于显示列表的顶端
	-- 创建成功后返回该画布对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	activedash	当画布对象状态为 ACTIVE 的时候，绘制虚线
	activefill	当画布对象状态为 ACTIVE 的时候，填充颜色
	activeoutline	当画布对象状态为 ACTIVE 的时候，绘制轮廓线
	activeoutlinestipple	当画布对象状态为 ACTIVE 的时候，指定填充轮廓的位图
	activestipple	当画布对象状态为 ACTIVE 的时候，指定填充的位图
	activewidth	当画布对象状态为 ACTIVE 的时候，指定边框的宽度
	dash	1. 指定绘制虚线轮廓
	2. 该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔
	3. 例如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔
	dashoffset	1. 指定虚线轮廓开始的偏移位置
	2. 例如当 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线
	disableddash	当画布对象状态为 DISABLE 的时候，绘制虚线
	disabledfill	当画布对象状态为 DISABLE 的时候，填充颜色
	disabledoutline	当画布对象状态为 DISABLE 的时候，绘制轮廓线
	disabledoutlinestipple	当画布对象状态为 DISABLE 的时候，指定填充轮廓的位图
	disabledstipple	当画布对象状态为 DISABLE 的时候，指定填充的位图
	disabledwidth	当画布对象状态为 DISABLE 的时候，指定边框的宽度
	fill	1. 指定填充的颜色
	2. 空字符串表示透明
	offset	1. 指定当点画模式时填充位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outline	指定轮廓的颜色
	outlineoffset	1. 指定当点画模式绘制轮廓时位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	outlinestipple	1. 当 outline 选项被设置时，该选项用于指定一个位图来填充边框
	2. 默认值是空字符串，表示黑色
	state	1. 指定该画布对象的状态
	2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
	3. 默认值是 NORMAL
	stipple	1. 指定一个位图用于填充
	2. 默认值是空字符串，表示实心
	tags	为创建的画布对象添加标签
	width	指定边框的宽度
	
	
	create_text(position, **options)
	
	-- 在 position 指定的位置（x, y）创建一个文本对象
	-- 创建成功后返回该文本对象的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	activefill	指定当文本对象状态为 ACTIVE 时候文本的颜色
	activestipple	指定当文本对象状态为 ACTIVE 时候文本填充的位图
	anchor	1. 指定文本在 position 参数的相对位置
	2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
	3. 默认值是 CENTER
	disabledfill	指定当文本对象状态为 DISABLED 时候文本的颜色
	disabledstipple	指定当文本对象状态为 ACTIVE 时候文本填充的位图
	fill	指定文本的颜色
	font	指定文本的字体、尺寸等信息
	justify	1. 指定对于多行文本的对齐方式
	2. 该选项可以使用的值有：LEFT（默认）、CENTER 和 RIGHT
	offset	1. 指定当点画模式时填充位图的偏移
	2. 该选项的值可以是："x,y", "#x,y", N, NE, E, SE, S, SW, W, NW, CENTER
	state	1. 指定该画布对象的状态
	2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
	3. 默认值是 NORMAL
	stipple	1. 指定一个位图用于填充
	2. 默认值是空字符串，表示实心
	tags	为创建的位图对象添加标签
	text	指定该文本对象将要显示的文本内容
	width	1. 如果指定该选项，则文本会在该宽度处自动断行
	2. 如果不指定该选项，文本对象的宽度等于文本最长行的长度
	
	
	create_window(position, **options)
	
	-- 在 position 指定的位置（x, y）创建一个窗口组件
	-- 创建成功后返回该窗口组件的 ID
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	anchor	1. 指定位图在 position 参数的相对位置
	2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
	3. 默认值是 CENTER
	height	指定窗口组件的高度
	state	1. 指定该图片的状态
	2. 可以是 NORMAL，DISABLED（不可用，不响应事件）和 HIDDEN（隐藏）
	3. 默认值是 NORMAL
	tags	为创建的图片对象添加标签
	width	指定窗口组件的宽度
	window	指定一个窗口组件
	
	
	dchars(item, from, to=None)
	-- 删除 item 中从 from 到 to（包含）参数中的字符串
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	delete(item)
	-- 删除 item 参数指定的画布对象
	-- 如果不存在 item 指定的画布对象，并不会产生错误
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	dtag(item, tag=None)
	-- 在 item 参数指定的画布对象中删除指定的 tag
	-- 如果 tag 参数被忽略，则删除指定画布对象所有的 tags
	-- 如果不存在 item 指定的画布对象，并不会产生错误
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	find_above(item)
	-- 返回在 item 参数指定的画布对象之上的 ID
	-- 如果有多个画布对象符合要求，那么返回最顶端的那个
	-- 如果 item 参数指定的是最顶层的画布对象，那么返回一个空元组
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	find_all()
	-- 返回 Canvas 组件上所有的画布对象
	-- 返回格式是一个元组，包含所有画布对象的 ID
	-- 按照显示列表的顺序返回
	-- 该方法相当于 find_withtag(ALL)
	
	find_below(item)
	-- 返回在 item 参数指定的画布对象之下的 ID
	-- 如果有多个画布对象符合要求，那么返回最底端的那个
	-- 如果 item 参数指定的是最底层的画布对象，那么返回一个空元组
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	find_closest(x, y, halo=None, start=None)
	-- 返回一个元组，包含所有靠近点（x, y）的画布对象的 ID
	-- 如果没有符合的画布对象，则返回一个空元组
	-- 可选参数 halo 用于增加点（x, y）的辐射范围
	-- 可选参数 start 指定一个画布对象，该方法仅返回在显示列表中低于但最接近的一个 ID
	-- 注意，点（x, y）的坐标是采用画布坐标系来表示
	
	find_enclosed(x1, y1, x2, y2)
	-- 返回完全包含在限定矩形内所有画布对象的 ID
	
	find_overlapping(x1, y1, x2, y2)
	-- 返回所有与限定矩形有重叠的画布对象的 ID（让然也包含在限定矩形内的画布对象）
	
	find_withtag(item)
	-- 返回 item 指定的所有画布对象的 ID
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	focus(item=None)
	-- 将焦点移动到指定的 item
	-- 如果有多个画布对象匹配，则将焦点移动到显示列表中第一个可以接受光标输入的画布对象
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	gettags(item)
	-- 返回与 item 相关联的所有 Tags
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	icursor(item, index)
	-- 将光标移动到 item 指定的画布对象
	-- 这里要求 item 指定的画布对象支持文本输入和转移焦点
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	index(item, index)
	-- 返回 index 在指定 item 中的位置（沿用 Python 的惯例：0 表示第一）
	-- index 参数可以是：INSERT（当前光标的位置），END（最后一个字符的位置），SEL_FIRST（当前选中文本的起始位置），SEL_LAST（当前选中文本的结束位置），还可以使用格式为 "@x, y"（x 和 y 是画布坐标系）来获得与此坐标最接近的位置
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	insert(item, index, text)
	-- 在允许进行文本编辑的画布对象的指定位置插入文本
	-- index 参数可以是：INSERT（当前光标的位置），END（最后一个字符的位置），SEL_FIRST（当前选中文本的起始位置），SEL_LAST（当前选中文本的结束位置），还可以使用格式为 "@x, y"（x 和 y 是画布坐标系）来获得与此坐标最接近的位置
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	itemcget(item, option)
	-- 获得指定 item 的选项的当前值
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	itemconfig(item, **options)
	-- 修改指定 item 的选项的当前值
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	itemconfigure(item, **options)
	-- 跟 itemconfig() 一样
	
	lift(item, **options)
	-- 将指定画布对象移动到显示列表的顶部
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 跟 tag_raise 一样
	
	lower(item, **options)
	-- 将指定画布对象移动到显示列表的底部
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 跟 tag_lower 一样
	
	move(item, dx, dy)
	-- 将 item 移动到新位置（x, y）
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	postscript(**options)
	-- 将 Canvas 的当前内容封装成 PostScript 格式（什么是 PostScript）表示
	-- 下方表格列举了各个 options 选项的具体含义：
	
	选项	含义
	colormode	该选项的值可以是：'color'（颜色输出），'gray'（灰阶输出）和 'mono'（黑白输出）
	file	1. 该选项指定一个文件，将 PostScript 写入该文件中
	2. 如果忽略该选项，PostScript 将以字符串的形式返回
	height	1. 指定要打印的 Canvas 组件的高度
	2. 默认值是 Canvas 组件的整体高度
	rotate	1. 如果该选项的值为 False，该页面将以纵向呈现
	2. 如果该选项的值为 True，该页面将以横向呈现
	x	开始打印的最左边位置，以画布坐标系表示
	y	开始打印的最顶端位置，以画布坐标系表示
	width	1. 指定要打印的 Canvas 组件的宽度
	2. 默认值是 Canvas 组件的整体宽度
	
	
	scale(item, xOrigin, yOrigin, xScale, yScale)
	-- 缩放 item 指定的画布对象
	-- xOrigin 和 yOrigin 决定要缩放的位置
	-- xScale 和 yScale 决定缩放的比例
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 注意：该方法无法缩放 Text 画布对象
	
	scan_dragto(x, y)
	-- 见下方 scan_mark(x, y)
	
	scan_mark(x, y)
	-- 使用这种方式来实现 Canvas 内容的滚动
	-- 需要将鼠标按钮事件及当前鼠标位置绑定到 scan_mark(x, y) 方法，然后再将 <motion> 事件及当前鼠标位置绑定到 scan_dragto(x, y) 方法，就可以实现 Canvas 在当前位置和 sacn_mack(x, y) 指定的位置 (x, y) 之间滚动
	
	select_adjust(item, index)
	-- 调整选中范围，使得给定的 index 参数指定的位置在范围内
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	select_clear()
	-- 取消 Canvas 组件中所有选中的范围
	
	select_from(item, index)
	-- 调整选中范围的起始位置为 index 参数指定的位置
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	select_item()
	-- 范围在 Canvas 组件中当前文本的选中范围
	-- 如果没有则返回 None
	
	select_to(item, index)
	-- 调整选中范围的结束位置为 index 参数指定的位置
	
	tag_bind(item, event=None, callback, add=None)
	-- 为 Canvas 组件上的画布对象绑定方法
	-- event 参数是绑定的事件名称，callback 是与之关联的方法
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 注意：与绑定事件关联的是画布对象，而不是 Tag
	
	tag_lower(item)
	-- 将一个或多个画布对象移至底部
	-- 如果是多个画布对象，将它们都移至底部并保留原有顺序
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 注意：该方法对窗口组件无效，请使用 lower 代替
	
	tag_raise(item)
	-- 将一个或多个画布对象移至顶部
	-- 如果是多个画布对象，将它们都移至顶部并保留原有顺序
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 注意：该方法对窗口组件无效，请使用 lift 代替
	
	tag_unbind(item, event, callback=None)
	-- 解除与 item 绑定的事件
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	
	tkraise(item, **options)
	-- 将指定画布对象移动到显示列表的顶部
	-- item 可以是单个画布对象的 ID，也可以是某个 Tag
	-- 跟 tag_raise 一样
	
	type(item)
	-- 返回指定画布对象的类型
	-- 返回值可以是："arc", "bitmap", "image", "line", "oval", "polygon", "rectangle", "text", 或 "window"
	
	xview(*args)
	-- 该方法用于在水平方向上滚动 Canvas 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
	-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端
	-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：xview(SCROLL, 3, UNITS) 表示向右滚动三行
	
	xview_moveto(fraction)
	-- 跟 xview(MOVETO, fraction) 一样
	
	xview_scroll(number, what)
	-- 跟 xview(SCROLL, number, what) 一样
	
	yview(*args)
	-- 该方法用于在垂直方向上滚动 Canvas 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现（具体操作参考：Scrollbar）
	-- 如果第一个参数是 MOVETO，则第二个参数表示滚动到指定的位置：0.0 表示最顶端，1.0 表示最底端
	-- 如果第一个参数是 SCROLL，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 UNITS 或 PAGES），例如：yview(SCROLL, 3, PAGES) 表示向下滚动三页
	
	yview_moveto(fraction)
	-- 跟 yview(MOVETO, fraction) 一样
	
	yview_scroll(number, what)
	-- 跟 yview(SCROLL, number, what) 一样
##2.Menu
Menu（菜单）组件用于实现顶级菜单、下拉菜单和弹出菜单。
- 用法

		from tkinter import *
		root = Tk()		
		def callback():
		    print("~被调用了~")		
		# 创建一个顶级菜单
		menubar = Menu(root)
		menubar.add_command(label="Hello", command=callback)
		menubar.add_command(label="Quit", command=root.quit)		
		# 显示菜单
		root.config(menu=menubar)		
		mainloop()
- 创建一个下拉菜单（或者其他子菜单），方法也是大同小异，最主要的区别是它们最后需要添加到主菜单上（而不是窗口上）：

		from tkinter import *
		root = Tk()		
		def callback():
		    print("~被调用了~")		
		# 创建一个顶级菜单
		menubar = Menu(root)	
		# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
		filemenu = Menu(menubar, tearoff=False)				//tearoff为TRUE表示下拉菜单选项可弹出
		filemenu.add_command(label="打开", command=callback)
		filemenu.add_command(label="保存", command=callback)
		filemenu.add_separator()			//加入一条分割线
		filemenu.add_command(label="退出", command=root.quit)
		menubar.add_cascade(label="文件", menu=filemenu)		//添加一个父菜单
		# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
		editmenu = Menu(menubar, tearoff=False)
		editmenu.add_command(label="剪切", command=callback)
		editmenu.add_command(label="拷贝", command=callback)
		editmenu.add_command(label="粘贴", command=callback)
		menubar.add_cascade(label="编辑", menu=editmenu)	
		# 显示菜单
		root.config(menu=menubar)		
		mainloop()
- 创建一个弹出菜单方法也是一致的，不过需要使用 post() 方法明确的将其显示出来：

		from tkinter import *
		root = Tk()		
		def callback():
		    print("~被调用了~")	
		# 创建一个弹出菜单
		menu = Menu(root, tearoff=False)
		menu.add_command(label="撤销", command=callback)
		menu.add_command(label="重做", command=callback)	
		frame = Frame(root, width=512, height=512)
		frame.pack()	
		def popup(event):
		    menu.post(event.x_root, event.y_root)	//在鼠标指定的位置弹出菜单
		# 绑定鼠标右键
		frame.bind("<Button-3>", popup)	
		mainloop()
##2.1参数和方法
- 参数

		Menu(master=None, **options) (class)
		master -- 父组件
		**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

			选项							含义
		activebackground	设置当 Menu 处于活动状态（通过 state 选项设置状态）的背景色
		activeborderwidth	设置当 Menu 处于活动状态（通过 state 选项设置状态）的边框宽度
		activeforeground	设置当 Menu 处于活动状态（通过 state 选项设置状态）的前景色
		background	设置背景颜色
		bg	跟 background 一样
		borderwidth	指定边框宽度
		bd	跟 borderwidth 一样
		cursor	指定当鼠标在 Menu 上飘过的时候的鼠标样式
		disabledforeground	指定当 Menu 处于 DISABLED 状态的时候的前景色
		font	指定 Menu 中文本的字体
		foreground	设置 Menu 的前景色
		fg	跟 foreground 一样
		postcommand	将此选项与一个方法相关联，当菜单被打开的时候该方法将自动被调用
		relief	1. 指定边框样式
				2. 默认值是 FLAT
				3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
		selectcolor	指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色
		tearoff	1. 默认情况下菜单可以被“撕下”（点击 IDLE 菜单上边的 --------- 试试）
				2. 将该选项设置为 Flase 关闭这一特性
		tearoffcommand	如果你希望当用户“撕下”你的菜单时通知你的程序，那么你可以将该选项与一个方法相关联，那么当用户“撕下”你的菜单时，Tkinter 会带着两个参数去调用你的方法（一个参数是当前窗口的 ID，另一个参数是承载被“撕下”的菜单的窗口 ID）
		title	默认情况下，被“撕下”的菜单标题是其主菜单的名字，不过你也可以通过修改此项的值来修改标题
- 方法

		add(type, **options)
		-- type 参数指定添加的菜单类型，可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"
		-- 还可以通过 options 选项设置菜单的属性，下表列举了 options 可以使用的选项和具体含义：

			选项				含义
		accelerator		1. 显示该菜单项的加速键（快捷键）
						2. 例如 accelerator = "Ctrl+N"
						3. 该选项仅显示，并没有实现加速键的功能（通过按键绑定实现）
		activebackground	设置当该菜单项处于活动状态（通过 state 选项设置状态）的背景色
		activeforeground	设置当该菜单项处于活动状态（通过 state 选项设置状态）的前景色
		background	设置该菜单项的背景颜色
		bitmap	指定显示到该菜单项上的位图
		columnbreak	从该菜单项开始另起一列显示
		command	将该选项与一个方法相关联，当用户点击该菜单项时将自动调用此方法
		compound	1. 控制菜单项中文本和图像的混合模式
					2. 如果该选项设置为 CENTER，文本显示在图像上（文本重叠图像）
					3. 如果该选项设置为 BOTTOM，LEFT，RIGHT 或 TOP，那么图像显示在文本的旁边（如 BOTTOM，则图像在文本的下方
		font	指定文本的字体
		foreground	设置前景色
		hidemargin	是否显示菜单项旁边的空白
		image	1. 指定菜单项显示的图片
				2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
		label	指定菜单项显示的文本
		menu	1. 该选项仅在 cascade 类型的菜单中使用
				2. 用于指定它的下级菜单
		offvalue	1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0
					2. 设置 offvalue 的值可以自定义未选中状态的值
		onvalue	1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0
					2. 设置 onvalue 的值可以自定义选中状态的值
		selectcolor	指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色
		selectimage	如果你在单选按钮或多选按钮菜单中使用图片代替文本，那么设置该选项指定被菜单项被选中时显示的图片
		state	1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键）
		underline	1. 用于指定在该菜单项的某一个字符处画下划线
					2. 例如设置为 1，则说明在该菜单项的第 2 个字符处画下划线
		value	1. 当菜单项为单选按钮时，用于标志该按钮的值
				2. 在同一组中的所有按钮应该拥有各不相同的值
				3. 通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮
				4. 如在使用上有不懂具体可以参照 Radiobutton 组件的说明
		variable	1. 当菜单项是单选按钮或多选按钮时，与之关联的变量
				2. 如在使用上有不懂具体可以参照：Checkbutton 和 Radiobutton 组件的说明
		
		
		add_cascade(**options)
		-- 添加一个父菜单
		-- 相当于 add("cascade", **options)
		add_checkbutton(**options)
		-- 添加一个多选按钮的菜单项
		-- 相当于 add("checkbutton", **options)
		add_command(**options)
		-- 添加一个普通的命令菜单项
		-- 相当于 add("command", **options)
		add_radiobutton(**options)
		-- 添加一个单选按钮的菜单项
		-- 相当于 add("radiobutton", **options)
		add_separator(**options)
		-- 添加一条分割线
		-- 相当于 add("separator", **options)
		delete(index1, index2=None)
		-- 删除 index1 ~ index2（包含）的所有菜单项
		-- 如果忽略 index2 参数，则删除 index1 指向的菜单项
		-- 注意：对于一个被“撕下”的菜单，你无法使用该方法
		entrycget(index, option)
		-- 获得指定菜单项的某选项的值
		entryconfig(index, **options)
		-- 设置指定菜单项的选项
		-- 选项的参数及具体含义请参考上方 add() 方法
		entryconfigure(index, **options)
		-- 跟 entryconfig() 一样
		index(index)
		-- 返回与 index 参数相应的选项的序号（例如 e.index(END)）
		insert(index, itemType, **options)
		-- 插入指定类型的菜单项到 index 参数指定的位置
		-- itemType 参数指定添加的菜单类型，可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"
		-- 选项的参数及具体含义请参考上方 add() 方法
		insert_cascade(index, **options)
		-- 在 index 参数指定的位置添加一个父菜单
		-- 相当于 insert("cascade", **options)
		insert_checkbutton(index, **options)
		-- 在 index 参数指定的位置添加一个多选按钮
		-- 相当于 insert("checkbutton", **options)
		insert_command(index, **options)
		-- 在 index 参数指定的位置添加一个普通的命令菜单项
		-- 相当于 insert("command", **options)
		insert_radiobutton(index, **options)
		-- 在 index 参数指定的位置添加一个单选按钮
		-- 相当于 insert("radiobutton", **options)
		insert_separator(index, **options)
		-- 在 index 参数指定的位置添加一条分割线
		-- 相当于 insert("separator", **options)
		invoke(index)
		-- 调用 index 指定的菜单项相关联的方法
		-- 如果是单选按钮，设置该菜单项为选中状态
		-- 如果是多选按钮，切换该菜单项的选中状态
		post(x, y)
		-- 在指定的位置显示弹出菜单
		-- 参考上方【用法】中的创建弹窗菜单的例子
		type(index)
		-- 获得 index 参数指定菜单项的类型
		-- 返回值可以是："command"，"cascade"，"checkbutton"，"radiobutton" 或 "separator"
		unpost()
		-- 移除弹出菜单
		yposition(index)
		-- 返回 index 参数指定的菜单项的垂直偏移位置
		-- 该方法的目的是为了让你精确放置相对于当前鼠标的位置弹出菜单
##3.Menubutton
Menubutton 组件是一个与 Menu 组件相关联的按钮，它可以放在窗口中的任意位置，并且在被按下时弹出下拉菜单。在 Tkinter 的早期版本，Menubutton 组件主要是用于实现顶级菜单，但现在我们直接用 Menu 组件就可以实现了。因此，现在该组件适用于你希望菜单按钮出现在其他位置的时候。

	from tkinter import *
	root = Tk()
	def callback():
	    print("~被调用了~")
	mb = Menubutton(root, text="点我", relief=RAISED)
	mb.pack()
	filemenu = Menu(mb, tearoff=False)
	filemenu.add_checkbutton(label="打开", command=callback, selectcolor="yellow")
	filemenu.add_command(label="保存", command=callback)
	filemenu.add_separator()
	filemenu.add_command(label="退出", command=root.quit)
	mb.config(menu = filemenu)
	mainloop()

参数

	Menubutton(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法

		选项						含义
	activebackground	设置当 Menubutton 处于活动状态（通过 state 选项设置状态）的背景色
	activeforeground	设置当 Menubutton 处于活动状态（通过 state 选项设置状态）的前景色
	anchor	1. 控制文本（或图像）在 Menubutton 中显示的位置
			2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
			3. 默认值是 CENTER
	background	设置背景颜色
	bg	跟 background 一样
	bitmap	指定显示到 Menubutton 上的位图
	borderwidth	指定 Menubutton 的边框宽度
	bd	跟 borderwidth 一样
	compound	1. 控制 Menubutton 中文本和图像的混合模式
				2. 如果该选项设置为 CENTER，文本显示在图像上（文本重叠图像）
				3. 如果该选项设置为 BOTTOM，LEFT，RIGHT 或 TOP，那么图像显示在文本的旁边（如 BOTTOM，则图像在文本的下方）
				4. 默认值是 NONE
	cursor	指定当鼠标在 Menubutton 上飘过的时候的鼠标样式
	direction	1. 默认情况下菜单是显示在按钮的下方，你可以通过修改此选项来改变这一特征
				2. 你可以将该选项设置为 "left"（按钮的左边），"right"（按钮的右边），"above"（按钮的上方）
	disabledforeground	指定当 Menubutton 不可用的时候前景色的颜色
	font	指定 Menubutton 中文本的字体
	foreground	设置 Menubutton 的文本和位图的颜色
	fg	跟 foreground 一样
	height	1. 设置 Menubutton 的高度
			2. 如果 Menubutton 显示的是文本，那么单位是文本单元
			3. 如果 Menubutton 显示的是图像，那么单位是像素（或屏幕单元）
			4. 如果设置为 0 或者干脆不设置，那么会自动根据 Menubutton 的内容计算出高度
	highlightbackground	指定当 Menubutton 没有获得焦点的时候高亮边框的颜色
	highlightcolor	指定当 Menubutton 获得焦点的时候高亮边框的颜色
	highlightthickness	指定高亮边框的宽度
	image	1. 指定 Menubutton 显示的图片
			2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
	justify	1. 定义如何对齐多行文本
			2. 使用 LEFT，RIGHT 或 CENTER
			3. 注意，文本的位置取决于 anchor 选项
			4. 默认值是 CENTER
	menu	1. 指定与 Menubutton 相关联的 Menu 组件
			2. Menu 组件的第一个参数必须是 Menubutton 的实例（参考上边例子）
	padx	指定 Menubutton 水平方向上的额外间距（内容和边框间）
	pady	指定 Menubutton 垂直方向上的额外间距（内容和边框间）
	relief	1. 指定边框样式
			2. 默认值是 FLAT
			3. 可以设置为 SUNKEN，RAISED，GROOVE，RIDGE
	state	1. 指定 Menubutton 的状态
			2. 默认值是 NORMAL
			3. 另外你还可以设置 ACTIVE 或 DISABLED
	takefocus	指定使用 Tab 键可以将焦点移到该 Button 组件上（这样按下空格键也相当于触发按钮事件）
	text	1. 指定 Menubutton 显示的文本
			2. 文本可以包含换行符
	textvariable	1. Menubutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
					2. 如果变量被修改，Menubutton 的文本会自动更新
	underline	1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键） 
				2. 默认值是 -1
				3. 例如设置为 1，则说明在 Menubutton 的第 2 个字符处画下划线
	width	1. 设置 Menubutton 的宽度
			2. 如果 Menubutton 显示的是文本，那么单位是文本单元
			3. 如果 Menubutton 显示的是图像，那么单位是像素（或屏幕单元）
			4. 如果设置为 0 或者干脆不设置，那么会自动根据 Menubutton 的内容计算出宽度
	wraplength	1. 决定 Menubutton 的文本应该被分成多少行
			2. 该选项指定每行的长度，单位是屏幕单元
			3. 默认值是 0
##4.OptionMenu（选择菜单）
OptionMenu（选择菜单）事实上是下拉菜单的改版，它的发明弥补了 Listbox 组件无法实现下拉列表框的遗憾。

	from tkinter import *
	root = Tk()
	variable = StringVar()
	variable.set("one")
	w = OptionMenu(root, variable, "one", "two", "three")
	w.pack()
	mainloop()
获得用户选择的内容，使用 Tkinter 变量的 get() 方法即可：

	def callback():
    print(variable.get())
	Button(root, text="点我", command=callback).pack()
下边例子演示如何将很多选项添加到选择菜单中：

	from tkinter import *
	OPTIONS = [
	    "California",
	    "458",
	    "FF",
	    "ENZO",
	    "LaFerrari"
	    ]
	root = Tk()
	variable = StringVar()
	variable.set(OPTIONS[0])
	w = OptionMenu(root, variable, *OPTIONS)
	w.pack()	
	def callback():
	    print(variable.get())	
	Button(root, text="点我", command=callback).pack()	
	mainloop()
注意：星号（*）作为形参的时候是起到“打包”的作用，相反，作为实参的时候是起到“解包”的作用。
##5. 星号（*）
1. 星号（*）作为形参，表示调用可变参数函数：通过在形参前加一个星号（*）或两个星号（**）来指定函数可以接收任意数量的实参。

		def fun1(*args):       
        print(type(args)) 
        print(args) 
		fun1(1, 2, 3, 4, 5)
		# 输出：
		# <class 'tuple'>
		# (1, 2, 3, 4, 5)

		def fun2(**args):
        print(type(args))
        print(args)
		fun2(a=1, b=2, c=3, d=4, e=5)
		# 输出：
		# <class 'dict'>
		# {'e': 5, 'a': 1, 'c': 3, 'd': 4, 'b': 2}
		从两个示例的输出可以看出：当参数形如 *args 时，传递给函数的任意个实参会按位置打包成一个元组（tuple）；
		当参数形如 **args 时，传递给函数的任意个 key = value 实参会被包装进一个字典（dict）。
2. 星号（*）作为实参时，表示通过解包参数调用函数
有打包就有解包，通过在实参前加一个星号（*）或两个星号（**）来对列表（list）、元组（tuple）或字典（dict）进行解包：

		
		>>> a = [1, 2, 3, 4, 5]
		>>> b = (1, 2, 3, 4, 5)
		(1, 2, 3, 4, 5)
		>>> fun1(*b)
		(1, 2, 3, 4, 5)
		>>> c = {'one':1, 'two':2, 'three':3}
		>>> fun2(**c)
		{'two': 2, 'one': 1, 'three': 3}
		>>> 
##6.事件绑定
一个 Tkinter 应用程序大部分时间花费在事件循环中（通过 mainloop() 方法进入）。事件可以有各种来源：包括用户触发的鼠标和键盘操作和窗口管理器触发的重绘事件（在多数情况下是由用户间接引起的）。Tkinter 提供一个强大的机制可以让你自由地处理事件，对于每个组件来说，你可以通过 bind() 方法将函数或方法绑定到具体的事件上。
	
	widget.bind(event, handler)
当被触发的事件满足该组件绑定的事件时，Tkinter 就会带着事件对象（Event）去调用 handler() 方法。

	# 捕获点击鼠标的位置
	from tkinter import *
	root = Tk()
	def callback(event):
	    print("点击位置：", event.x, event.y)
	frame = Frame(root, width=200, height=200)
	frame.bind("<Button-1>", callback)		//使用 Frame 组件的 bind() 方法将鼠标点击事件（<Button-1>）和我们自定义的 callback() 方法绑定起来
	frame.pack()
	mainloop()
只有当组件获得焦点的时候才能接收 键盘事件（Key），下边例子中我们用 focus_set() 获得焦点，当你你可以设置 Frame 的 takefocus 选项为 True，然后使用 Tab 将焦点转移上来。

	# 捕获键盘事件
	from tkinter import *
	root = Tk()
	def callback(event):		//event代表按下的按键
	    print("敲击位置：", repr(event.char))
	frame = Frame(root, width=200, height=200,takefocus=True)
	frame.bind("<Key>", callback)
	frame.focus_set()		//获取焦点
	frame.pack()
	mainloop()
捕获鼠标在组件上的运动轨迹，这里需要关注的是 <Motion> 事件

	from tkinter import *
	root = Tk()	
	def callback(event):
	    print("当前位置：", event.x, event.y)	
	frame = Frame(root, width=200, height=200)
	frame.bind("<Motion>", callback)
	frame.pack()	
	mainloop()
###6.1 事件序列
Tkinter 使用一种称为事件序列的机制来允许用户定义事件，用户需使用 bind() 方法将具体的事件序列与自定义的方法相绑定。事件序列是以字符串的形式表示的，可以表示一个或多个相关联的事件（如果是多个事件，那么对应的方法只有在满足所有事件的前提下才会被调用）。事件序列使用以下语法描述

	<modifier-type-detail>
	事件序列是包含在尖括号（<...>）中
	type 部分的内容是最重要的，它通常用于描述普通的事件类型，例如鼠标点击或键盘按键点击（详见下方）。
	modifier 部分的内容是可选的，它通常用于描述组合键，例如 Ctrl + c，Shift + 鼠标左键点击（详见下方）。
	detail 部分的内容是可选的，它通常用于描述具体的按键，例如 Button-1 表示鼠标左键。
示例
	事件序列	含义
	<Button-1>	用户点击鼠标左键
	<KeyPress-H>	用户点击 H 按键
	<Control-Shift-KeyPress-H>	用户同时点击 Ctrl + Shift + H
- type

			type	含义
		Activate	当组件的状态从“未激活”变为“激活”的时候触发该事件
		Button	1. 当用户点击鼠标按键的时候触发该事件
				2. detail 部分指定具体哪个按键：<Button-1>鼠标左键，<Button-2>鼠标中键，<Button-3>鼠标右键，<Button-4>滚轮上滚（Linux），<Button-5>滚轮下滚（Linux）
		ButtonRelease	1. 当用户释放鼠标按键的时候触发该事
						2. 在大多数情况下，比 Button 要更好用，因为如果当用户不小心按下鼠标，用户可以将鼠标移出组件再释放鼠标，从而避免不小心触发事件
		Configure	当组件的尺寸发生改变的时候触发该事件
		Deactivate	当组件的状态从“激活”变为“未激活”的时候触发该事件
		Destroy	当组件被销毁的时候触发该事件
		Enter	1. 当鼠标指针进入组件的时候触发该事件
				2. 注意：不是指用户按下回车键
		Expose	当窗口或组件的某部分不再被覆盖的时候触发该事件
		FocusIn	1. 当组件获得焦点的时候触发该事件
				2. 用户可以用 Tab 键将焦点转移到该组件上（需要该组件的 takefocus 选项为 True）
				3. 你也可以调用 focus_set() 方法使该组件获得焦点（见上方例子）
		FocusOut	当组件失去焦点的时候触发该事件
		KeyPress	1. 当用户按下键盘按键的时候触发该事件
					2. detail 可以指定具体的按键，例如 <KeyPress-H>表示当大写字母 H 被按下的时候触发该事件
					3. KeyPress 可以简写为 Key
		KeyRelease	当用户释放键盘按键的时候触发该事件
		Leave	当鼠标指针离开组件的时候触发该事件
		Map	1. 当组件被映射的时候触发该事件
			2. 意思是在应用程序中显示该组件的时候，例如调用 grid() 方法
		Motion	当鼠标在组件内移动的整个过程均触发该事件
		MouseWheel	1. 当鼠标滚轮滚动的时候触发该事件
					2. 目前该事件仅支持 Windows 和 Mac 系统，Linux 系统请参考 Button
		Unmap	1. 当组件被取消映射的时候触发该事件
				2. 意思是在应用程序中不再显示该组件的时候，例如调用 grid_remove() 方法
		Visibility	当应用程序至少有一部分在屏幕中是可见的时候触发该事件
- modifier

		在事件序列中，modifier 部分的内容可以是以下这些：

		modifier	含义
		Alt	当按下 Alt 按键的时候
		Any		1. 表示任何类型的按键被按下的时候
				2. 例如 <Any-KeyPress> 表示当用户按下任何按键时触发事件
		Control	当按下 Ctrl 按键的时候
		Double	1. 当后续两个事件被连续触发的时候
				2. 例如 <Double-Button-1> 表示当用户双击鼠标左键时触发事件
		Lock	当打开大写字母锁定键（CapsLock）的时候
		Shift	当按下 Shift 按键的时候
		Triple	跟 Double 类似，当后续三个事件被连续触发的时候
- Event 对象

		当 Tkinter 去回调你定义的函数的时候，都会带着 Event 对象（作为参数）去调用，Event 对象以下这些属性你可以使用：

			属性		含义
		widget	产生该事件的组件
		x, y	当前的鼠标位置坐标（相对于窗口左上角，像素为单位）
		x_root, y_root	当前的鼠标位置坐标（相对于屏幕左上角，像素为单位）
		char	按键对应的字符（键盘事件专属）
		keysym	按键名，见下方 Key names（键盘事件专属）
		keycode	按键码，见下方 Key names（键盘事件专属）
		num	按钮数字（鼠标事件专属）
		width, height	组件的新尺寸（Configure 事件专属）
		type	该事件类型
- Key names

	当事件为 <Key>，<KeyPress>，<KeyRelease> 的时候，detail 可以通过设定具体的按键名（keysym）来筛选。例如 <Key-H> 表示按下键盘上的大写字母 H 时候触发事件，<Key-Tab> 表示按下键盘上的 Tab 按键的时候触发事件。

	下表列举了键盘所有特殊按键的 keysym 和 keycode：
	（下边按键码是对应美国标准 101 键盘的“Latin-1”字符集，键盘标准不同对应的按键码不同，但按键名是一样的）

		按键名（keysym）	按键码（keycode）	代表的按键
		Alt_L				64			左边的 Alt 按键
		Alt_R				113			右边的 Alt 按键
		BackSpace			22			Backspace（退格）按键
		Cancel				110			break 按键
		Caps_Lock			66			CapsLock（大写字母锁定）按键
		Control_L			37			左边的 Ctrl 按键
		Control_R			109			右边的 Ctrl 按键
		Delete				107			Delete 按键
		Down				104			↓ 按键
		End					103			End 按键
		Escape				9			Esc 按键
		Execute				111			SysReq 按键
		F1					67			F1 按键
		F2					68			F2 按键
		F3					69			F3 按键
		F4					70			F4 按键
		F5					71			F5 按键
		F6					72			F6 按键
		F7					73			F7 按键
		F8					74			F8 按键
		F9					75			F9 按键
		F10					76			F10 按键
		F11					77			F11 按键
		F12					96			F12 按键
		Home				97			Home 按键
		Insert				106			Insert 按键
		Left				100			← 按键
		Linefeed			54			Linefeed（Ctrl + J）
		KP_0				90			小键盘数字 0
		KP_1				87			小键盘数字 1
		KP_2				88			小键盘数字 2
		KP_3				89			小键盘数字 3
		KP_4				83			小键盘数字 4
		KP_5				84			小键盘数字 5
		KP_6				85			小键盘数字 6
		KP_7				79			小键盘数字 7
		KP_8				80			小键盘数字 8
		KP_9				81			小键盘数字 9
		KP_Add				86			小键盘的 + 按键
		KP_Begin			84			小键盘的中间按键（5）
		KP_Decimal			91			小键盘的点按键（.）
		KP_Delete			91			小键盘的删除键
		KP_Divide			112			小键盘的 / 按键
		KP_Down				88			小键盘的 ↓ 按键
		KP_End				87			小键盘的 End 按键
		KP_Enter			108			小键盘的 Enter 按键
		KP_Home				79			小键盘的 Home 按键
		KP_Insert			90			小键盘的 Insert 按键
		KP_Left				83			小键盘的 ← 按键
		KP_Multiply			63			小键盘的 * 按键
		KP_Next				89			小键盘的 PageDown 按键
		KP_Prior			81			小键盘的 PageUp 按键
		KP_Right			85			小键盘的 → 按键
		KP_Subtract			82			小键盘的 - 按键
		KP_Up				80			小键盘的 ↑ 按键
		Next				105			PageDown 按键
		Num_Lock			77			NumLock（数字锁定）按键
		Pause				110			Pause（暂停）按键
		Print				111			PrintScrn（打印屏幕）按键
		Prior				99			PageUp 按键
		Return				36			Enter（回车）按键
		Right				102			→ 按键
		Scroll_Lock			78			ScrollLock 按键
		Shift_L				50			左边的 Shift 按键
		Shift_R				62			右边的 Shift 按键
		Tab					23			Tab（制表）按键
		Up					98			↑ 按键

##7.Message
Message（消息）组件是 Label 组件的变体，用于显示多行文本消息。Message 组件能够自动换行，并调整文本的尺寸使其适应给定的尺寸。通常你可以使用 Label 来代替。如果你希望使用多种字体来显示文本，那么应该使用 Text 组件。

	from tkinter import *
	root = Tk()	
	w1 = Message(root, text="这是一则消息", width=100)
	w1.pack()	
	w2 = Message(root, text="这是一则骇人听闻的长长长长长消息！", width=100)
	w2.pack()
	mainloop()
参数

	Message(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

	选项	含义
	anchor	1. 控制文本消息的显示位置
			2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN 代表东西南北，上北下南左西右东）
			3. 默认值是 CENTER
	aspect	1. 设置高宽比，即宽度/高度的百分比的值
			2. 默认值是 150（宽度比高度大 50%）
			3. 注意：如果设置了 width 选项的值，该选项将被忽略
	background	1. 设置背景颜色
				2. 默认值由系统指定
	bg	跟 background 一样
	borderwidth	1. 指定边框宽度
				2. 默认值由系统指定，通常是 1 或 2 像素
	bd	跟 borderwidth 一样
	cursor	1. 指定当鼠标在 Message 上飘过的时候的鼠标样式
			2. 默认值由系统指定
	font	1. 指定 Message 中文本的字体
			2. 只能指定一种字体
			3. 默认值由系统指定
	foreground	1. 设置 Message 的文本的颜色
				2. 默认值由系统指定
	fg	跟 foreground 一样
	highlightbackground	1. 指定当 Message 没有获得焦点的时候高亮边框的颜色
						2. 默认值由系统指定，通常是标准背景颜色
	highlightcolor	1. 指定当 Message 获得焦点的时候高亮边框的颜色
					2. 默认值由系统指定
	highlightthickness	1. 指定高亮边框的宽度
						2. 默认值是 0（不带高亮边框）
	justify	1. 定义如何对齐多行文本
			2. 使用 LEFT，RIGHT 或 CENTER
			3. 注意，文本的位置取决于 anchor 选项
			4. 默认值是 CENTER
	padx	1. 指定水平方向上的额外间距（内容和边框间）
			2. 单位是像素
	pady	1. 指定垂直方向上的额外间距（内容和边框间）
			2. 单位是像素
	relief	1. 指定边框样式
			2. 默认值是 FLAT
			3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
	takefocus	1. 如果是 True，该组件接受输入焦点
				2. 默认值是 False
	text	1. 指定 Label 显示的文本
			2. 为了达到指定的高宽比（aspect 选项指定），文本内容将自动进行换行
	textvariable	1. Message 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
					2. 如果变量被修改，Message 的文本会自动更新
	width	1. 设置 Message 的宽度
			2. 单位是文本单元
			3. 如果忽略该选项，将根据 aspect 选项设置的高宽比来设置合适的宽度
##7.Spinbox
Spinbox 组件（Tk8.4 新增）是 Entry 组件的变体，用于从一些固定的值中选取一个。通常用于在限定数字中选取的情况下代替普通的 Entry 组件。

	from tkinter import *
	root = Tk()	
	w = Spinbox(root, from_=0, to=10)
	w.pack()	
	mainloop()
还可以通过元组指定允许输入的值：

	from tkinter import *
	root = Tk()	
	w = Spinbox(root, values= ("小甲鱼", "~风介~", "wei_Y", "戴宇轩"))
	w.pack()	
	mainloop()
- 参数

	Spinbox(master=None, **options) (class)	
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

		选项	含义
		activebackground	设置当 Spinbox 处于 ACTIVE 状态下的背景颜色
		background	1. 设置背景颜色
					2. 默认值由系统指定
		bg	跟 background 一样
		borderwidth	1. 设置边框宽度
					2. 默认值是 1 或 2 像素
		buttonbackground	设置调节箭头的背景颜色
		buttoncursor	指定当鼠标在调节箭头上方的鼠标样式
		buttondownrelief	1. 指定向下调节箭头的样式
							2. 默认值是 RAISED
							3. 还可以设置为 FLAT，SUNKEN，GROOVE 和 RIDGE
		buttonup	1. 指定向上调节箭头的样式 
					2. 默认值是 RAISED
					3. 还可以设置为 FLAT，SUNKEN，GROOVE 和 RIDGE
		command	1. 指定一个函数，当用户点击调节箭头的时候将自动调用该函数
				2. 注意：当用户直接在输入框中输入数据时并不会触发该函数
		cursor	1. 指定当鼠标在 Spinbox 上飘过的时候的鼠标样式
				2. 默认值由系统指定
		disabledbackground	设置当 Spinbox 处于 DISABLED 状态下的背景颜色
		disabledforeground	设置当 Spinbox 处于 DISABLED 状态下的前景颜色
		exportselection	1. 指定选中的文本是否可以被复制到剪贴板
						2. 默认值是 True
						3. 可以修改为 False 表示不允许复制文本
		font	1. 指定 Spinbox 中文本的字体
				2. 默认值由系统指定
		foreground	1. 设置前景（文本）颜色
					2. 默认值由系统指定
		fg	跟 foreground 一样
		format	1. 使用该选项设置选择数值的样式（from_ 和 to 指定范围，用户自行输入的不算）
				2. 例如 format='%10.4f' 表示显示的数值占 10 位，小数点后保留 4 位
		from_	1. 该选项和 to 选项共同指定一个范围的数值
				2. increment 选项设置每次点击调节箭头递增（递减）的精度
		highlightbackground	1. 指定当 Spinbox 没有获得焦点的时候高亮边框的颜色
							2. 默认值由系统指定
		highlightcolor	1. 指定当 Spinbox 获得焦点的时候高亮边框的颜色
						2. 默认值由系统指定
		highlightthickness	指定高亮边框的宽度
		increment	1. 该选项指定当用户每次点击调节箭头的时候递增（递减）的精度
					2. 例如 from_=1, to=10, increment=0.5，那么每次用户点击调节箭头的时候，输入框中的数字递增（递减）0.5
		insertbackground	指定输入光标的颜色
		insertborderwidth	1. 指定输入光标的边框宽度
							2. 如果被设置为非 0 值，光标样式会被设置为 RAISED
							3. 小甲鱼温馨提示：将 insertwidth 设置大一点才能看到效果哦
		insertofftime	1. 该选项控制光标的闪烁频率（灭）
						2. 单位是毫秒
		insertontime	1. 该选项控制光标的闪烁频率（亮）
						2. 单位是毫秒
		insertwidth	1. 指定光标的宽度
					2. 默认值是 1 或 2 像素
		invalidcommand	1. 指定当输入框输入的内容“非法”时调用的函数
						2. 也就是指定当 validateCommand 选项指定的函数返回 False 时的函数
						3. 详见 Entry 组件最下方小甲鱼关于验证详解
		invcmd	跟 invalidcommand 一样
		justify	1. 定义如何对齐输入框中的文本
				2. 使用 LEFT，RIGHT 或 CENTER
				3. 默认值是 LEFT
		readonlybackground	设置当 Spinbox 处于 "readonly" 状态下的背景颜色
		relief	1. 指定边框样式
				2. 默认值是 SUNKEN
				3. 其他可以选择的值是 FLAT，RAISED，GROOVE 和 RIDGE
		repeatdelay	1. 该选项指定鼠标左键点击滚动条凹槽的响应时间
					2. 默认值是 400（毫秒）
		repeatinterval	1. 该选项指定鼠标左键紧按滚动条凹槽时的响应间隔
						2. 默认值是 100（毫秒）
		selectbackground	1. 指定输入框的文本被选中时的背景颜色
							2. 默认值由系统指定
		selectborderwidth	1. 指定输入框的文本被选中时的边框宽度（选中边框）
							2. 默认值由系统指定
		selectforeground	1. 指定输入框的文本被选中时的字体颜色
							2. 默认值由系统指定
		state	1. Spinbox 组件可以设置的状态：NORMAL，DISABLED 或 "readonly"（注意，这个是字符串。它跟 DISABLED 相似，但它		支持选中和拷贝，只是不能修改，而 DISABLED 是完全禁止）
				2. 默认值是 NORMAL
				3. 注意，如果此选项设置为 DISABLED 或 "readonly"，那么调用 insert() 和 delete() 方法都会被忽略
		takefocus	1. 指定使用 Tab 键可以将焦点移动到输入框中
					2. 默认是开启的，可以将该选项设置为 False 避免焦点在此输入框中
		textvariable	1. 指定一个与输入框的内容相关联的 Tkinter 变量（通常是 StringVar）
						2. 当输入框的内容发生改变时，该变量的值也会相应发生改变
		to	1. 该选项和 from_ 选项共同指定一个范围的数值
			2. increment 选项设置每次点击调节箭头递增（递减）的精度
		validate	1. 该选项设置是否启用内容验证 
					2. 详见 Entry 组件最下方小甲鱼关于验证详解
		validatecommand	1. 该选项指定一个验证函数，用于验证输入框内容是否合法
						2. 验证函数需要返回 True 或 False 表示验证结果
						3. 注意，该选项只有当 validate 的值非 "none" 时才有效
						3. 详见本内容最下方小甲鱼关于验证详解
		vcmd	跟 validatecommand 一样
		values	1. 提供两个方法限定用户输入的内容，一种是通过 from_ 和 to 选项设置范围，另一种则是将可选值以元组的形式赋值给 values 选项
				2. 例如 values= ("小甲鱼", "~风介~", "wei_Y", "戴宇轩") 则允许用户在这 4 个字符串中选择
		width	1. 设置输入框的宽度，以字符为单位
				2. 默认值是 20
				3. 对于变宽字体来说，组件的实际宽度等于字体的平均宽度乘以 width 选项的值
		wrap	1. 默认情况下（Flase），当输入框中的值是第一个（最后一个）的时候，再点击向上（向下）调节箭头，内容不会改变
				2. 当该选项的值设置为 True，则当达到第一个（最后一个）值的时候，再点击向上（向下）调节箭头，内容将回到最后一个（第一个）
				3. 小甲鱼注：其实就是开启循环的意^_^
		xscrollcommand	1. 与 scrollbar（滚动条）组件相关联
						2. 如果你觉得用户输入的内容会超过该组件的输入框宽度，那么可以考虑设置该选项
						3. 使用方法可以参考：Scrollbar 组件
##8.PanedWindow
PanedWindow 组件（Tk8.4 新增）是一个空间管理组件。跟 Frame 组件类似，都是为组件提供一个框架，不过 PanedWindow 允许让用户调整应用程序的空间划分。PanedWindow 组件会为每一个子组件生成一个独立地窗格，用户可以自由调整窗格的大小。

	from tkinter import *
	m = PanedWindow(orient=VERTICAL)		//orient指定窗格的分布方式
	m.pack(fill=BOTH, expand=1)	
	top = Label(m, text="top pane")
	m.add(top)
	bottom = Label(m, text="bottom pane")
	m.add(bottom)
	mainloop()
创建一个 3 窗格的 PanedWindow 组件则需要一点小技巧：

	from tkinter import *
	m1 = PanedWindow()
	m1.pack(fill=BOTH, expand=1)
	left = Label(m1, text="left pane")
	m1.add(left)
	m2 = PanedWindow(orient=VERTICAL)
	m1.add(m2)
	top = Label(m2, text="top pane")
	m2.add(top)
	bottom = Label(m2, text="bottom pane")
	m2.add(bottom)
	mainloop()
这里不同窗格事实上是有一条“分割线”（sash）隔开，虽然你看不到，但你却可以感受到它的存在。不信？不妨把鼠标缓慢移动到大概的位置，当鼠标指针改变的时候后拖拽鼠标.....但我们也可以把“分割线”给显式地显示出来，并且可以为它附上一个“手柄”（handle）：

	from tkinter import *
	m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN)
	m1.pack(fill=BOTH, expand=1)
	left = Label(m1, text="left pane")
	m1.add(left)
	m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
	m1.add(m2)
	top = Label(m2, text="top pane")
	m2.add(top)
	bottom = Label(m2, text="bottom pane")
	m2.add(bottom)
	mainloop()
参数

	PanedWindow(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：
	
	选项	含义
	background	设置背景颜色
	bg	跟 background 一样
	borderwidth	设置边框宽度
	bd	跟 borderwidth 一样
	cursor	1. 指定当鼠标在 PanedWindow 上飘过的时候的鼠标样式
	2. 默认值由系统指定
	handlepad	1. 调节“手柄”的位置
	2. 例如 orient=VERTICAL，则 handlepad 选项表示“分割线”上的手柄与左端的距离
	3. 默认值是 8 像素
	handlesize	1. 设置“手柄”的尺寸（由于“手柄”必须是一个正方形，所以是设置正方形的边长）
	2. 默认值是 8 像素
	height	1. 设置 PanedWindow 的高度
	2. 如果忽略该选项，则高度由子组件的尺寸决定
	opaqueresize	1. 该选项定义了用户调整窗格尺寸的操作
	2. 如果该选项的值为 True（默认），窗格的尺寸随用户鼠标的拖拽而改变
	3. 如果该选项的值为 False，窗格的尺寸在用户释放鼠标的时候才更新到新的位置
	orient	1. 指定窗格的分布方式
	2. 可以是 HORIZONTAL（横向分布）和 VERTICAL（纵向分布）
	relief	1. 指定边框样式
	2. 默认值是 FLAT
	3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
	sashpad	设置每一条分割线到窗格间的间距
	sashrelief	1. 设置分割线的样式
	2. 默认值是：FLAT
	3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
	sashwidth	设置分割线的宽度
	showhandle	1. 设置是否显示调节窗格的手柄
	2. 默认值为 False
	width	1. 设置 PanedWindow 的宽度
	2. 如果忽略该选项，则高度由子组件的尺寸决定


方法

	add(child, **options)
	-- 添加一个新的子组件到窗格中
	-- 下方表格列举了各个 options 选项具体含义：
	
	选项	含义
	after	添加新的子组件到指定子组件后边
	before	添加新的子组件到指定子组件前边
	height	指定子组件的高度
	minsize	1. 该选项控制窗格不得低于的值
	2. 如果 orient=HORIZONTAL，表示窗格的宽度不得低于该选项的值
	3. 如果 orient=VERTICAL，表示窗格的高度不得低于该选项的值
	padx	指定子组件的水平间距
	pady	指定子组件的垂直间距
	sticky	1. 当窗格的尺寸大于子组件时，该选项指定子组件位于窗格的位置
	2. 可选的值有：E、S、W、N（分别代表东南西北四个方位）以及它们的组合值
	3. 例如 NE 表示子组件显示在右上角的位置
	width	指定子组件的宽度
	
	
	forget(child)
	-- 删除一个子组件
	
	identify(x, y)
	-- 给定一个坐标（x, y），返回该坐标所在的元素名称
	-- 如果该坐标位于子组件上，返回空字符串
	-- 如果该坐标位于分割线上，返回一个二元组（n, 'sash'），n 为 0 表示第一个分割线
	-- 如果该坐标位于手柄上，返回一个二元组（n, 'handle'），n 为 0 表示第一个手柄
	
	panecget(child, option)
	-- 获得子组件指定选项的值
	
	paneconfig(child, **options)
	-- 设置子组件的各种选项
	-- 下方表格列举了各个 options 选项具体含义：
	
	选项	含义
	after	添加新的子组件到指定子组件后边
	before	添加新的子组件到指定子组件前边
	height	指定子组件的高度
	minsize	1. 该选项控制窗格不得低于的值
	2. 如果 orient=HORIZONTAL，表示窗格的宽度不得低于该选项的值
	3. 如果 orient=VERTICAL，表示窗格的高度不得低于该选项的值
	padx	指定子组件的水平间距
	pady	指定子组件的垂直间距
	sticky	1. 当窗格的尺寸大于子组件时，该选项指定子组件位于窗格的位置
	2. 可选的值有：E、S、W、N（分别代表东南西北四个方位）以及它们的组合值
	3. 例如 NE 表示子组件显示在右上角的位置
	width	指定子组件的宽度
	
	
	paneconfigure(child, **options)
	-- 跟 paneconfig() 一样
	
	panes()
	-- 将子组件以列表的形式返回
	
	remove(child)
	-- 跟 forget() 一样
	
	sash_coord(index)
	-- 返回一个二元组表示指定分割线的起点坐标
	
	sash_dragto(index, x, y)
	-- 实现将指定的分割线拖拽到一个新的位置
	-- 与 sash_mark() 一起实现
	
	sash_mark(index, x, y)
	-- 注册当前的鼠标位置
	
	sash_place(index, x, y)
	-- 将指定分割线移动到一个新的位置
##9Toplevel
Toplevel（顶级窗口）组件类似于 Frame 组件，但 Toplevel 组件是一个独立的顶级窗口，这种窗口通常拥有标题栏、边框等部件。通常用在显示额外的窗口、对话框和其他弹出窗口上。下边例子中，我们在 root 窗口添加一个按钮用于创建一个顶级窗口，点一下来一个：

	from tkinter import *
	root = Tk()
	def create():
	    top = Toplevel()
	    top.title("FishC Demo")
	    msg = Message(top, text="I love FishC.com!")
	    msg.pack()
	Button(root, text="创建顶级窗口", command=create).pack()
	mainloop()
参数

	Toplevel(master=None, **options) (class)
	master -- 父组件
	**options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：
	
	选项	含义
	background	1. 设置背景颜色
	2. 默认值由系统指定
	3. 为了防止更新，可以将颜色值设置为空字符串
	bg	跟 background 一样
	borderwidth	设置边框宽度
	bd	跟 borderwidth 一样
	class_	默认值是 Toplevel
	colormap	1. 有些显示器只支持 256 色（有些可能更少），这种显示器通常提供一个颜色映射来指定要使用要使用的 256 种颜色
				2. 该选项允许你指定用于该组件以及其子组件的颜色映射
				3. 默认情况下，Toplevel 使用与其父组件相同的颜色映射
				4. 使用此选项，你可以使用其他窗口的颜色映射代替（两窗口必须位于同个屏幕并且具有相同的视觉特性）
				5. 你也可以直接使用 "new" 为 Toplevel 组件分配一个新的颜色映射
				6. 一旦创建 Toplevel 组件实例，你就无法修改这个选项的值
	container	1. 该选项如果为 True，意味着该窗口将被用作容器，一些其它应用程序将被嵌入 
				2. 默认值是 False
	cursor	1. 指定当鼠标在 Toplevel 上飘过的时候的鼠标样式
			2. 默认值由系统指定
	height	设置高度
	highlightbackground	指定当 Toplevel 没有获得焦点的时候高亮边框的颜色
	highlightcolor	指定当 Toplevel 获得焦点的时候高亮边框的颜色
	highlightthickness	指定高亮边框的宽度
	menu	设置该选项为 Toplevel 窗口提供菜单栏
	padx	水平方向上的边距
	pady	垂直方向上的边距
	relief	1. 指定边框样式
			2. 默认值是 FLAT
			3. 另外你还可以设置 SUNKEN，RAISED，GROOVE 或 RIDGE
			4. 注意，如果你要设置边框样式，记得设置 borderwidth 或 bd 选项不为 0，才能看到边框
	takefocus	1. 指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来）
				2. 默认值是 False
	width	设置宽度
##10Tk && Toplevel
下边这一系列方法用于与窗口管理器进行交互。他们可以被 Tk（根窗口）进行调用，同样也适用于 Toplevel（顶级窗口）。注：并非所有操作系统均完全支持下方所有方法的实现。
	aspect(minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
	-- 控制该窗口的宽高比（width:height）
	-- 宽高比限制在：minNumer / minDenom ~ maxNumer / maxDenom
	-- 如果忽略参数，则返回一个 4 元组表示当前的限制（如果有的话）
	
	attributes(*args)
	-- 设置和获取窗口属性
	-- 如果你只给出选项名，将返回当前窗口该选项的值
	-- 注意：以下选项不支持关键字参数，你需要在选项前添加横杠（-）并用字符串的方式表示，用逗号（,）隔开选项和值。
	-- 例如你希望设置窗口的透明度为 50%，你应该使用 attribute("-alpha", 0.5) 代替 attribute(alpha=0.5)
	-- 下方表格列举了 args 可以使用各个选项的具体含义及用法：
	
		选项	含义
		alpha	1.（Windows，Mac）控制窗口的透明度
				2. 1.0 表示不透明，0.0 表示完全透明
				3. 该选项并不支持所有的系统，对于不支持的系统，Tkinter 绘制一个不透明（1.0）的窗口
		disabled	（Windows）禁用整个窗口（这时候你只能从任务管理器中关闭它）
		fullscreen	（Windows，Mac）如果设置为 True，则全屏显示窗口
		modified	（Mac）如果设置为 True，该窗口被标记为改动过
		titlepath	（Mac）设置窗口代理图标的路径
		toolwindow	（Windows）如果设置为 True，该窗口采用工具窗口的样式
		topmost	（Windows，Mac）如果设置为 True，该窗口将永远置于顶层	
		示例
			from tkinter import *
			root = Tk()
			def create():
			    top = Toplevel()
			    top.attributes("-alpha",0.5)
			    top.title("FishC Demo")		
			    msg = Message(top, text="I love FishC.com!")
			    msg.pack()	
			Button(root, text="创建顶级窗口", command=create).pack()	
			mainloop()
	client(name=None)
	-- 设置和获取 WM_CLIENT_MACHINE 属性
	-- 如果要删除 WM_CLIENT_MACHINE 属性，赋值为空字符串即可
	-- 该属性仅支持 X 窗口系统的窗口管理器，其他系统均忽略
	colormapwindows(*wlist)
	-- 设置和获取 WM_COLORMAP_WINDOWS 属性
	-- 该属性仅支持 X 窗口系统的窗口管理器，其他系统均忽略
	command(value=None)
	-- 设置和获取 WM_COMMAND 属性
	-- 该属性仅支持 X 窗口系统的窗口管理器，其他系统均忽略
	deiconify()
	-- 显示窗口
	-- 默认情况下新创建的窗口都会显示在屏幕上，但使用 iconify() 或 withdraw() 方法可以在屏幕上移除窗口
	focusmodel(model=None)
	-- 设置和获取焦点模式
	frame()
	-- 返回一个字符串表示当前系统特征
	-- 对于类 Unix 系统，返回值是 X 窗口标识符
	-- 对于 Windows 系统，返回值是 HWND 强制转换为长整形的结果
	geometry(geometry=None)
	-- 设置和获取窗口的尺寸
	-- geometry 参数的格式为："%dx%d%+d%+d" % (width, height, xoffset, yoffset)
	grid(baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
	-- 通知窗口管理器该窗口将以网格的形式重新调整尺寸
	-- baseWidth 和 baseHeight 指定 Tk_GeometryRequest 要求的网格单元数
	-- widthInc 和 heightInc 指定网格单元的宽度和高度（像素）
	group(window=None)
	-- 将窗口添加到窗口群中
	-- window 参数指定控制窗口群的主窗口
	-- 如果忽略该参数，将返回当前窗口群的主窗口
	iconbitmap(bitmap=None, default=None)
	-- 设置和获取窗口的图标
	-- 例如 root.iconbitmap(bitmap="FishC.ico")
	-- default 参数可以用于指定由该窗口创建的子窗口的默认图标
	iconify()
	-- 将窗口图标化（最小化）
	-- 需要重新显示窗口，使用 deiconify() 方法
	-- 该方法会使得 state() 返回 "iconic"
	iconmask(bitmap=None)
	-- 设置和获取位图掩码
	iconname(newName=None)
	-- 设置和获取当窗口图标化（最小化）时的图标名字
	iconposition(x=None, y=None)
	-- 设置和获取当窗口图标化（最小化）时的图标位置
	iconwindow(pathName=None)
	-- 设置和获取当窗口图标化（最小化）时的组件窗口
	-- 该方法会使得 state() 返回 "icon"
	maxsize(width=None, height=None)
	-- 设置和获取该窗口的最大尺寸
	minsize(width=None, height=None)
	-- 设置和获取该窗口的最小尺寸
	overrideredirect(boolean=None)
	-- 如果参数为 True，该窗口忽略所有的小部件（也就是说该窗口将没有传统的标题栏、边框等部件）
	positionfrom(who=None)
	-- 指定窗口位置由“谁”决定
	-- 如果 who 参数是 "user"，窗口位置由用户决定
	-- 如果 who 参数是 "program"，窗口位置由系统决定
	protocol(name=None, func=None)
	-- 将回调函数 func 与相应的规则 name 绑定
	-- name 参数可以是 "WM_DELETE_WINDOW"：窗口被关闭的时候
	-- name 参数可以是 "WM_SAVE_YOURSELF"：窗口被保存的时候
	- name 参数可以是 "WM_TAKE_FOCUS"：窗口获得焦点的时候
	resizable(width=None, height=None)
	-- 指定是否可以改变该窗口的尺寸
	-- width 为 True 说明允许调整窗口的水平尺寸
	-- height 为 True 说明允许调整窗口的垂直尺寸
	sizefrom(who=None)
	-- 指定窗口尺寸由“谁”决定
	-- 如果 who 参数是 "user"，窗口位置由用户决定
	-- 如果 who 参数是 "program"，窗口位置由系统决定
	state(newstate=None)
	-- 设置和获得当前窗口的状态
	-- newstate 的值可以是 "normal"，"iconic"（见 iconify），"withdrawn"（见 withdraw），"icon"（见 iconwindow）和 "zoomed"（放大，Windows 特有）
	title(string=None)
	-- 设置窗口的标题
	transient(master=None)
	-- 指定为 master 的临时窗口
	withdraw()
	-- 将窗口从屏幕上移除（并没有销毁）
	-- 需要重新显示窗口，使用 deiconify() 方法
	-- 该方法会使得 state() 返回 "withdrawn"
	wm_aspect(minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
	-- 见上方 aspect()
	wm_attributes(*args)
	-- 见上方 attributes()
	wm_client(name=None)
	-- 见上方 client()
	wm_colormapwindows(*wlist)
	-- 见上方 colormapwindows()
	wm_command(value=None)
	-- 见上方 command()
	wm_deiconify()
	-- 见上方 deiconify()
	wm_focusmodel(model=None)
	-- 见上方 focusmodel()
	wm_frame()
	-- 见上方 frame()
	wm_geometry(geometry=None)
	-- 见上方 geometry()
	wm_grid(baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
	-- 见上方 grid()
	wm_group(window=None)
	-- 见上方 group()
	wm_iconbitmap(bitmap=None, default=None)
	-- 见上方 iconbitmap()
	wm_iconify()
	-- 见上方 iconify()
	wm_iconmask(bitmap=None)
	-- 见上方 iconmask()
	wm_iconname(newName=None)
	-- 见上方 iconname()
	wm_iconposition(x=None, y=None)
	-- 见上方 iconposition()
	wm_iconwindow(pathName=None)
	-- 见上方 iconwindow()
	wm_maxsize(width=None, height=None)
	-- 见上方 maxsize()
	wm_minsize(width=None, height=None)
	-- 见上方 minsize()
	wm_overrideredirect(boolean=None)
	-- 见上方 overrideredirect()
	wm_positionfrom(who=None)
	-- 见上方 positionfrom()
	wm_protocol(name=None, func=None)
	-- 见上方 protocol()
	wm_resizable(width=None, height=None)
	-- 见上方 resizable()
	wm_sizefrom(who=None)
	-- 见上方 sizefrom()
	wm_state(newstate=None)
	-- 见上方 state()
	wm_title(string=None)
	-- 见上方 title()
	wm_transient(master=None)
	-- 见上方 transient()
	wm_withdraw()
	-- 见上方 withdraw()

#7.4
tips:


##1. Pack布局管理器
pack、grid 和 place 均用于管理同在一个父组件下的所有组件的布局，其中：

	pack 是按添加顺序排列组件
	grid 是按行/列形式排列组件
	place 则允许程序员指定组件的大小和位置
对比 grid 管理器，pack 更适用于少量组件的排列，但它在使用上更加简单（就像我们前边所有的例子中，展示一个组件我们一般都直接使用 .pack()，多简单~）。如果你需要创建相对复杂的布局结构，那么建议是使用多个框架（Frame）结构构成，或者使用 grid 管理器实现。

	注意：不要在同一个父组件中混合使用 pack 和 grid，因为 Tkinter 会很认真地在那儿计算到底先使用那个布局管理器......以至于你等了半个小时，Tkinter 还在那儿纠结不出结果！
我们常常会遇到的一个情况是将一个组件放到一个容器组件中，并填充整个父组件。这儿给大家举个例子，我们生成一个 Listbox 组件并将它填充到 root 窗口中：

	from tkinter import *
	root = Tk()
	listbox = Listbox(root)
	listbox.pack(fill=BOTH, expand=True)		//将listbox水平垂直填充，并填充父控件的额外空间
	for i in range(10):
	    listbox.insert(END, str(i))	
	mainloop()
其中，fill 选项是告诉窗口管理器该组件将填充整个分配给它的空间，BOTH 表示同时横向和纵向扩展，X 表示横向，Y 表示纵向；expand 选项是告诉窗口管理器将父组件的额外空间也填满。默认下，pack 是将添加的组件依次纵向排列

	from tkinter import *
	root = Tk()	
	Label(root, text="Red", bg="red", fg="white").pack(fill=X)
	Label(root, text="Green", bg="green", fg="black").pack(fill=X)
	Label(root, text="Blue", bg="blue", fg="white").pack(fill=X)	
	mainloop()
如果想要组件横向挨个儿排放，你可以使用 side 选项：

	from tkinter import *
	root = Tk()	
	Label(root, text="Red", bg="red", fg="white").pack(side=LEFT)
	Label(root, text="Green", bg="green", fg="black").pack(side=LEFT)
	Label(root, text="Blue", bg="blue", fg="white").pack(side=LEFT)
	mainloop()
方法，注：下边所有方法适用于所有组件

	pack(**options)
	-- 下方表格详细列举了各个选项的具体含义和用法：

	选项	含义
	anchor	1. 控制组件在 pack 分配的空间中的位置
			2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
			3. 默认值是 CENTER
	expand	1. 指定是否填充父组件的额外空间
			2. 默认值是 False
	fill	1. 指定填充 pack 分配的空间
			2. 默认值是 NONE，表示保持子组件的原始尺寸
			3. 还可以使用的值有：X（水平填充），Y（垂直填充）和 BOTH（水平和垂直填充）
	in_		1. 将该组件放到该选项指定的组件中
			2. 指定的组件必须是该组件的父组件
	ipadx	指定水平方向上的内边距
	ipady	指定垂直方向上的内边距
	padx	指定水平方向上的外边距
	pady	指定垂直方向上的外边距
	side	1. 指定组件的放置位置
			2. 默认值是 TOP
			3. 还可以设置的值有：LEFT，BOTTOM，RIGHT
		
	pack_configure(**options)
	-- 跟 pack() 一样	
	pack_forget()
	-- 将组件从屏幕中“删除”
	-- 并没有销毁该组件，只是看不到了
	-- 可以通过 pack 或其他布局管理器显示已“删除”的组件
	pack_info()
	-- 以字典的形式返回当前 pack 的选项
	pack_propagate(flag)
	-- 如果开启，父组件会自动调节尺寸以容纳所有子组件
	-- 默认值是开启（flag = True）
	-- 该方法仅适用于父组件
	pack_slaves()
	-- 以列表的形式返回该组件的所有子组件
	-- 该方法仅适用于父组件
##2.Grid布局管理器
grid 管理器可以说是 Tkinter 这三个布局管理器中最灵活多变的。如果你只希望学习使用一个布局管理器，那么 grid 绝对是首选。当你在设计对话框的时候，使用 gird 尤其便捷。如果你此前一直在用 pack 构造窗口布局，那么学习完 grid 你会悔恨当初为啥不早学它。使用一个 grid 就可以简单的实现你用很多个框架和 pack 搭建起来的效果。注意：不要在同一个父组件中混合使用 pack 和 grid，因为 Tkinter 会很认真地在那儿计算到底先使用那个布局管理器......以至于你等了半个小时，Tkinter 还在那儿纠结不出结果！<br/>

使用 grid 排列组件，只需告诉它你想要将组件放置的位置（行/列，row 选项指定行，cloumn 选项指定列）。此外，你并不用提前指出网格（grid 分布给组件的位置称为网格）的尺寸，因为管理器会自动计算。

	from tkinter import *	
	root = Tk()	
	# column 默认值是 0
	Label(root, text="用户名").grid(row=0)
	Label(root, text="密码").grid(row=1)	
	Entry(root).grid(row=0, column=1)
	Entry(root, show="*").grid(row=1, column=1)	
	mainloop()
默认情况下组件会居中显示在对应的网格里，你可以使用 sticky 选项来修改这一特性。该选项可以使用的值有 E，W，S，N（EWSN分别表示东西南北，即上北下南左西右东）以及它们的组合。因此，我们可以通过 sticky = W 使得 Label 左对齐：

	Label(root, text="用户名").grid(row=0, sticky=W)
	Label(root, text="密码").grid(row=1, sticky=W)
只需要指定 rowspan 和 columnspan 就可以实现跨行和跨列的功能：

	from tkinter import *
	root = Tk()
	Label(root, text="用户名").grid(row=0, sticky=W)		//第一行第一列左对齐
	Label(root, text="密码").grid(row=1, sticky=W)		//第二行第一例左对齐
	Entry(root).grid(row=0, column=1)
	Entry(root, show="*").grid(row=1, column=1)
	photo = PhotoImage(file="logo.gif")
	Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx=5, pady=5)	//rowspan表示跨几列	
	Button(text="提交", width=10).grid(row=2, columnspan=3, pady=5)
	mainloop()
方法

	grid(**options)
	-- 下方表格详细列举了各个选项的具体含义和用法：
	
			选项			含义
		column		1. 指定组件插入的列（0 表示第 1 列）
					2. 默认值是 0
		columnspan	指定用多少列（跨列）显示该组件
		in_			1. 将该组件放到该选项指定的组件中
					2. 指定的组件必须是该组件的父组件
		ipadx		指定水平方向上的内边距
		ipady		指定垂直方向上的内边距
		padx		指定水平方向上的外边距
		pady		指定垂直方向上的外边距
		row			指定组件插入的行（0 表示第 1 行）
		rowspan		指定用多少行（跨行）显示该组件
		sticky		1. 控制组件在 grid 分配的空间中的位置
					2. 可以使用 N, E, S, W 以及它们的组合来定位（EWSN代表东西南北，上北下南左西右东）
					3. 使用加号（+）表示拉长填充，例如 N + S 表示将组件垂直拉长填充网格，N + S + W + E 表示填充整个网格
					4. 不指定该值则居中显示
	
	grid_bbox(column=None, row=None, col2=None, row2=None)
	-- 返回一个 4 元组描述该组件所在的限定矩形-- 如果指定 column 和 cow 参数，则返回该位置（column, cow）的组件的限定矩形描述
	-- 如果指定 4 个参数，则返回从（column, cow）到（col2, row2）所有组件的限定矩形描述
	-- 例如 grid_bbox(0, 0, 1, 1) 返回的是 4 个组件所在的限定矩形	
	grid_columnconfigure(index, **options)
	-- 设置列的属性
	-- 注意：设置的是该组件所拥有的 grid 的列
	-- 可以设置的选项及含义如下：
	
		选项	含义
		minsize	指定该列的最小宽度
		pad	指定该列中最大网格的水平边距
		weight	1. 指定列与列之间的相对距离
				2. 默认值是 0
				3. 这个你比较难理解，小甲鱼还是详细解说下：初创建窗口的时候，grid 会自动根据组件的尺寸分配窗口的尺寸，当你拉伸窗口的尺寸时就会有空白显示出来。这个选项正是指定列与列之间是否填充空白，默认是不填充的。另外，该选项的值是指定填充空白的倍数，例如 weight = 2 的列会比 weight = 1 的列填充多一倍的空白。所以需要平均填充的话，只需要所有的列都设置 weight = 1 即可。
		
	grid_configure(**options)
	-- 跟 grid() 一样
	grid_forget()
	-- 将组件从屏幕中“删除”
	-- 并没有销毁该组件，只是看不到了
	-- 可以通过 grid 或其他布局管理器显示已“删除”的组件，但该组件所在网格的选项设置不会恢复	
	grid_info()
	-- 以字典的形式返回当前 grid 的选项	
	grid_location(x, y)
	-- 返回位于（或接近）给定坐标（x, y）的网格位置
	-- 返回值是一个 2 元组表示网格对应的（列，行）
	grid_propagate(flag)
	-- 如果开启，父组件会自动调节尺寸以容纳所有子组件
	-- 默认值是开启（flag = True）
	-- 该方法仅适用于父组件	
	grid_remove()
	-- 跟 grid_forget() 一样，但恢复的时候会记住该组件所在网格的选项设置	
	grid_rowconfigure(index, **options)
	-- 设置行的属性
	-- 注意：设置的是该组件所拥有的 grid 的行
	-- 可以设置的选项及含义如下：
	
		选项	含义
		minsize	指定该行的最小高度
		pad	指定该列中最大网格的垂直边距
		weight	1. 指定行与行之间的相对距离
				2. 默认值是 0
				3. 这个你比较难理解，不懂可以参考上边 grid_columnconfigure() 的详细解释
		
	grid_size()
	-- 返回该组件所拥有的 grid 的尺寸
	-- 返回值是一个 2 元组，表示（列, 行）分别的网格数
	grid_slaves(row=None, column=None)
	-- 以列表的形式返回该组件的所有子组件
	-- 该方法仅适用于父组件
##3.Place布局管理器
通常情况下不建议使用 place 布局管理器，因为对比起 pack 和 grid，place 要做更多的工作。不过纯在即合理，place 在一些特殊的情况下可以发挥妙用。请看下边例子。
- 将子组件显示在父组件的正中间：

		from tkinter import *
		root = Tk()		
		def callback():
		    print("正中靶心")		
		Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)		
		mainloop()
- 在某种情况下，或许你希望一个组件可以覆盖另一个组件，那么 place 又可以派上用场了。下边例子我们演示用 Button 覆盖 Label 组件：

		photo = PhotoImage(file="logo_big.gif")
		Label(root, image=photo).pack()
		Button(root, text="点我", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)
- relx 和 rely 选项指定的是相对于父组件的位置，范围是 00 ~ 1.0，因此 0.5 表示位于正中间。那么 relwidth 和 relheight 选项则是指定相对于父组件的尺寸：

		Label(root, bg="red").place(relx=0.5, rely=0.5, relheight=0.75, relwidth=0.75, anchor=CENTER)
		Label(root, bg="yellow").place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5, anchor=CENTER)
		Label(root, bg="green").place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25, anchor=CENTER)
x 和 y 选项用于设置偏移（像素），如果同时设置 relx（rely）和 x（y），那 place 将优先计算 relx 和 rely，然后再实现 x 和 y 指定的偏移值。

- 方法

		place(**options)
		-- 下方表格详细列举了各个选项的具体含义和用法：

			选项			含义
		anchor	1. 控制组件在 place 分配的空间中的位置
				2. N, NE, E, SE, S, SW, W, NW, 或 CENTER 来定位（EWSN代表东西南北，上北下南左西右东）
				3. 默认值是 NW
		bordermode	1. 指定边框模式（INSIDE 或 OUTSIDE）
					2. 默认值是 INSIDE
		height	指定该组件的高度（像素）
		in_		1. 将该组件放到该选项指定的组件中
				2. 指定的组件必须是该组件的父组件
		relheight	1. 指定该组件相对于父组件的高度
					2. 取值范围 0.0 ~ 1.0
		relwidth	1. 指定该组件相对于父组件的宽度
					2. 取值范围 0.0 ~ 1.0
		relx	1. 指定该组件相对于父组件的水平位置
				2. 取值范围 0.0 ~ 1.0
		rely	1. 指定该组件相对于父组件的垂直位置
				2. 取值范围 0.0 ~ 1.0
		width	指定该组件的宽度（像素）
		x		1. 指定该组件的水平偏移位置（像素）
				2. 如同时指定了 relx 选项，优先实现 relx 选项
		y		1. 指定该组件的垂直偏移位置（像素）
				2. 如同时指定了 rely 选项，优先实现 rely 选项
		
		place_configure(**options)
		-- 跟 place() 一样	
		place_forget()
		-- 将组件从屏幕中“删除”
		-- 并没有销毁该组件，只是看不到了
		-- 可以通过 place 或其他布局管理器显示已“删除”的组件	
		place_info()
		-- 以字典的形式返回当前 place 的选项	
		place_slaves()
		-- 以列表的形式返回该组件的所有子组件
		-- 该方法仅适用于父组件	
		slaves()
		-- 跟 place_slaves() 一样
##4.标准对话框
Tkinter 为了提供了三种标准对话框模块，它们分别是：

	messagebox
	filedialog
	colorchooser

注：这三个模块原来是独立的，分别是 tkMessageBox、tkFileDialog 和 tkColorChooser，需要导入才能使用。在 Python3 之后，这些模块全部被收归到 tkinter 模块的麾下。下边的所有演示都是在 Python3 下实现，如果你用的是 Python2.x，请在文件头 import tkMessageBox，然后将 messagebox 替换为 tkMessageBox 即可。

1. messagebox（消息对话框）

	下表为你列出了使用 messagebox 可以创建的所有标准对话框样式：

		askokcancel(title, message, options)	
		askquestion(title, message, options)	
		askretrycancel(title, message, options)			 
		askyesno(title, message, options)			 
		showerror(title, message, options)	
		showinfo(title, message, options)			 
		showwarning(title, message, options)	
	- 所有的这些函数都有相同的参数：
 
		title 参数毋庸置疑是设置标题栏的文本
		message 参数是设置对话框的主要文本内容，你可以用 '\n' 来实现换行
		options 参数可以设置的选项和含义如下表所示

		选项	含义
		default	1. 设置默认的按钮（也就是按下回车响应的那个按钮）
				2. 默认是第一个按钮（像“确定”，“是”或“重试”）
				3. 可以设置的值根据对话框函数的不同可以选择：CANCEL，IGNORE，OK，NO，RETRY 或 YES
		icon	1. 指定对话框显示的图标
				2. 可以指定的值有：ERROR，INFO，QUESTION 或 WARNING
				3. 注意：不能指定自己的图标
		parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
				2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w

	- 返回值

		askokcancel()，askretrycancel() 和 askyesno() 返回布尔类型的值：
			返回 True 表示用户点击了“确定”或“是”按钮
			返回 False 表示用户点击了“取消”或“否”按钮
		askquestion() 返回“yes”或“no”字符串表示用户点击了“是”或“否”按钮	
		showerror()，showinfo() 和 showwarning() 返回“ok”表示用户按下了“是”按钮

	示例

		from tkinter import *
		from tkinter import messagebox		//估计是由于messagebox模块隐藏不会自动导入，需手动导入
		print(messagebox.askokcancel("lcscim","大家好我是老长"))
		mainloop()
- filedialog（文件对话框）

	当你的应用程序需要使用打开文件或保存文件的功能时，文件对话框显得尤为重要。

		from tkinter import *
		root = Tk()		
		def callback():
		    fileName = filedialog.askopenfilename()
		    print(fileName)		
		Button(root, text="打开文件", command=callback).pack()		
		mainloop()

	filedialog 模块提供了两个函数：askopenfilename(**option) 和 asksaveasfilename(**option)，分别用于打开文件和保存文件。两个函数可供设置的选项是一样的，下边列举了可用的选项及含义：
		
		选项	含义
		defaultextension	1. 指定文件的后缀
							2. 例如：defaultextension=".jpg"，那么当用户输入一个文件名 "FishC" 的时候，文件名会自动添加后缀为 "FishC.jpg"
							3. 注意：如果用户输入文件名包含后缀，那么该选项不生效
		filetypes	1. 指定筛选文件类型的下拉菜单选项
					2. 该选项的值是由 2 元祖构成的列表
					3. 每个 2 元祖由（类型名，后缀）构成，例如：filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("GIF", ".gif")]
		initialdir	1. 指定打开/保存文件的默认路径
					2. 默认路径是当前文件夹
		parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
				2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w
		title	指定文件对话框的标题栏文本

	返回值

		1. 如果用户选择了一个文件，那么返回值是该文件的完整路径
		2. 如果用户点击了取消按钮，那么返回值是空字符串

3. colorchooser（颜色选择对话框）

		from tkinter import *
		from tkinter import colorchooser
		root = Tk()		
		def callback():
		    fileName = colorchooser.askcolor()
		    print(fileName)		
		Button(root, text="选择颜色", command=callback).pack()		
		mainloop()

	参数

		askcolor(color, **option) 函数的 color 参数用于指定初始化的颜色，默认是浅灰色；
		option 参数可以指定的选项及含义如下：

			选项	含义
		title	指定颜色对话框的标题栏文本
		parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
				2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w
			
	返回值
		
		1. 如果用户选择一个颜色并按下“确定”按钮后，返回值是一个 2 元祖，第 1 个元素是选择的 RGB 颜色值，第 2 个元素是对应的 16 进制颜色值
		2. 如果用户按下“取消”按钮，那么返回值是 (None, None)