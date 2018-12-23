#8.18

##1.itchat
itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。

- 安装

	pip install itchat
代码：

	import itchat
	itchat.login()
	#爬取自己好友相关信息， 返回一个json文件
	friends = itchat.get_friends(update=True)[0:]
	#初始化计数器
	male = female = other = 0
	#friends[0]是自己的信息，所以要从friends[1]开始
	for i in friends[1:]:
	    sex = i["Sex"]
	    if sex == 1:
	        male += 1
	    elif sex == 2:
	        female += 1
	    else:
	        other +=1
	#计算朋友总数
	total = len(friends[1:])
	#打印出自己的好友性别比例
	print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
	"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
	"不明性别好友： %.2f%%" % (float(other) / total * 100))
	#定义一个函数，用来爬取各个变量
	def get_var(var):
	    variable = []
	    for i in friends:
	        value = i[var]
	        variable.append(value)
	    return variable
	#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
	NickName = get_var("NickName")
	Sex = get_var('Sex')
	Province = get_var('Province')
	City = get_var('City')
	Signature = get_var('Signature')
	from pandas import DataFrame
	data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
	        'City': City, 'Signature': Signature}
	frame = DataFrame(data)
	frame.to_csv('data.csv', index=True,encoding = "GB18030")
##2.Wordcloud
Python中的一个小词云生成器
- 安装

		pip install wordcloud
	安装失败，在https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud下载对应版本并在该文件所在目录使用 
		pip install+下载的文件名
##3.Selenium + PhantomJS
- Selenium: web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装： pip install selenium==2.48.0
    - 官网： http://selenium-python.readthedocs.io/index.html
- PhantomJS(幽灵)
    - 基于Webkit 的无界面的浏览器 
    - 官网： http://phantomjs.org/download.html
- Selenium 库有有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例 v36
- chrome + chromedriver
    - 下载安装chrome： 下载+安装
    - 下载安装chromedriver：
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例37