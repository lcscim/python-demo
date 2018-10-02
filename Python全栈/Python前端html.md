#10.1
http://www.cnblogs.com/yuanchenqi/articles/5976755.html
##1.HTML
- 制作服务端

		import socket
		def main():
		    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    sock.bind(('localhost',8089))
		    sock.listen(5)
		
		    while True:
		        connection, address = sock.accept()
		        buf = connection.recv(1024)
		        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
		        connection.sendall(bytes("<h1>Hello,World</h1>","utf8"))
		        connection.close()
		if __name__ == '__main__':
		    main()
	此时在浏览器上访问：localhost：8089即可获得
- HTML 是什么？

	htyper text markup language  即超文本标记语言
	超文本: 就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。
	标记语言: 标记（标签）构成的语言.
	网页==HTML文档，由浏览器解析，用来展示的
	
	静态网页：静态的资源，如xxx.html
	动态网页：html代码是由某种开发语言根据用户请求动态生成的
	
	html文档树形结构图：![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161025132859984-662031019.png)
- 什么是标签

	- 是由一对尖括号包裹的单词构成 例如: <html> *所有标签中的单词不可能以数字开头.
	- 标签不区分大小写.<html> 和 <HTML>. 推荐使用小写.
	- 标签分为两部分: 开始标签<a> 和 结束标签</a>. 两个标签之间的部分 我们叫做标签体.
	- 有些标签功能比较简单.使用一个标签即可.这种标签叫做自闭和标签.例如: <br/> <hr/> <input /> <img />
	- 标签可以嵌套.但是不能交叉嵌套. <a><b></a></b>
- 标签的属性

	- 通常是以键值对形式出现的. 例如 name="alex"
	- 属性只能出现在开始标签 或 自闭和标签中.
	- 属性名字全部小写. *属性值必须使用双引号或单引号包裹 例如 name="alex"
	- 如果属性值和属性名完全一样.直接写属性名即可. 例如 readonly
- <!DOCTYPE html>标签

	由于历史的原因，各个浏览器在对页面的渲染上存在差异，甚至同一浏览器在不同版本中，对页面的渲染也不同。在
	W3C标准出台以前，浏览器在对页面的渲染上没有统一规范，产生了差异(Quirks mode或者称为Compatibility 
	Mode)；由于W3C标准的推出，浏览器渲染页面有了统一的标准(CSScompat或称为Strict mode也有叫做Standars
	mode)，这就是二者最简单的区别。
	      W3C标准推出以后，浏览器都开始采纳新标准，但存在一个问题就是如何保证旧的网页还能继续浏览，在标准出来以前，
	很多页面都是根据旧的渲染方法编写的，如果用的标准来渲染，将导致页面显示异常。为保持浏览器渲染的兼容性，使以
	前的页面能够正常浏览，浏览器都保留了旧的渲染方法（如：微软的IE）。这样浏览器渲染上就产生了Quircks mode
	和Standars mode，两种渲染方法共存在一个浏览器上。
	
	window.top.document.compatMode：
	//BackCompat：怪异模式，浏览器使用自己的怪异模式解析渲染页面。 
	//CSS1Compat：标准模式，浏览器使用W3C的标准解析渲染页面。
	       这个属性会被浏览器识别并使用，但是如果你的页面没有DOCTYPE的声明，那么compatMode默认就是BackCompat,
	
	这也就是恶魔的开始 -- 浏览器按照自己的方式解析渲染页面，那么，在不同的浏览器就会显示不同的样式。
	
	    如果你的页面添加了<!DOCTYPE html>那么，那么就等同于开启了标准模式，那么浏览器就得老老实实的按照W3C的
	
	标准解析渲染页面，这样一来，你的页面在所有的浏览器里显示的就都是一个样子了。
	
	这就是<!DOCTYPE html>的作用。
- <meta>

     meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。

    1: name属性主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。     
		#用于搜索引擎发现网站关键词
		<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">	
		#用于在搜索界面显示当前网站的简要信息
		<meta name="description" content="老男孩培训机构是由一个老的男孩创建的">
    2: http-equiv顾名思义，相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确和精确地显示网页内容，与之对应的属性值为content，              content中的内容其实就是各个参数的变量值。   
		#如果未指定URL表明2秒后刷新当前页面，指定表明2秒后跳转到该页面
		<meta http-equiv="Refresh" content="2;URL=https://www.baidu.com"> //(注意后面的引号，分别在秒数的前面和网址的后面)

		<meta http-equiv="content-Type" charset=UTF8">

		<meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" />
	#注意：X-UA-Compatible 针对IE浏览器
	3.非meta标签
		#指定网站的标题即浏览器的标签页标题文字
	    <title>oldboy</title>
		#指定在浏览器标签页显示的图标
	    <link rel="icon" href="http://www.jd.com/favicon.ico">
		#链接外部的CSS样式
	    <link rel="stylesheet" href="css.css">
		#关联外部的js代码
	    <script src="hello.js"></script>　 
##1.1body标签
一 基本标签（块级标签和内联标签）

	<hn>: n的取值范围是1~6; 从大到小. 用来表示标题.
	<p>: 段落标签. 包裹的内容被换行.并且也上下内容之间有一行空白.
	<b> <strong>: 加粗标签.
	<strike>: 为文字加上一条中线.
	<em>: 文字变成斜体.
	<sup>和<sub>: 上角标 和 下角表.
	<br>:换行.
	<hr>:水平线
	<div><span>

	- 块级标签：<p><h1><table><ol><ul><form><div>
	
	- 内联标签：<a><input><img><sub><sup><textarea><span>
	
	block（块）元素的特点
		
		 总是在新行上开始；
		 宽度缺省是它的容器的100%，除非设定一个宽度。
		 它可以容纳内联元素和其他块元素
		
	inline元素的特点
		
		和其他元素都在一行上；
		宽度就是它的文字或图片的宽度，不可改变
		内联元素只能容纳文本或者其他内联元素
		
	特殊字符具体特殊字符可以搜索
		
	     &lt; &gt；&quot；&copy;&reg;
		<,>
二 图形标签: <img> 

	src: 要显示图片的路径.
	alt: 图片没有加载成功时的提示.
	title: 鼠标悬浮时的提示信息.
	width: 图片的宽
	height:图片的高 (宽高两个属性只用一个会自动等比缩放.)

三 超链接标签(锚标签)<a>

	href:要连接的资源路径 格式如下: href="http://www.baidu.com" 
	target: _blank : 在新的窗口打开超链接. 框架名称: 在指定框架中打开连接内容.
	name: 定义一个页面的书签.
	用于跳转 href : #id.（锚）
 
四 列表标签：

	<ul>: 无序列表
	<ol>: 有序列表
	     <li>:列表中的每一项.
	<dl>  定义列表
	     <dt> 列表标题
	     <dd> 列表项

五 表格标签: <table>

	border: 表格边框.
	cellpadding: 内边距
	cellspacing: 外边距.
	width: 像素 百分比.（最好通过css来设置长宽）
	<tr>: table row  每行
	     <th>: table head cell	标题列，效果是加粗
	     <td>: table data cell	数值列
	rowspan:  单元格竖跨多少行
	colspan:  单元格横跨多少列（即合并单元格）
	<th>: table header <tbody>(不常用): 为表格进行分区.

六 表单标签<form>
	表单用于向服务器传输数据。
	
	表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。
	
	表单还可以包含textarea、select、fieldset和 label 元素。

	1.表单属性

　　		HTML 表单用于接收不同类型的用户输入，用户提交表单时向服务器传输数据，从而实现用户与Web服务器的交互。表单标签, 要提交的所有内容都应该在该标签中.

            action: 表单提交到哪. 一般指向服务器端一个程序,程序接收到表单提交过来的数据（即表单元素值）作相应处理，比如https://www.sogou.com/web

            method: 表单的提交方式 post/get 默认取值 就是 get（信封）

                  get: 1.提交的键值对.放在地址栏中url后面. 2.安全性相对较差. 3.对提交内容的长度有限制.
                  post:1.提交的键值对 不在地址栏. 2.安全性相对较高. 3.对提交内容的长度理论上无限制.
                  get/post是常见的两种请求方式.

	2.表单元素

    <input>  标签的属性和对应值              

	type:    text 文本输入框
	
             password 密码输入框

             radio 单选框，属性name的值必须相同才能实现

             checkbox 多选框  

             submit 提交按钮            

             button 按钮(需要配合js使用.) button和submit的区别？
			 #button需要配合js代码使用用来触发某种效果，submit是用来提交数据

             file 提交文件：form表单需要加上属性enctype="multipart/form-data"   
	
	name:    表单提交项的键.注意和id属性的区别：name属性是和服务器通信时使用的名称；而id属性是浏览器端使用的名称，该属性主要是为了方便客户端编程，而在css和javascript中使用的
	value:   表单提交项的值.对于不同的输入类型，value 属性的用法也不同：
	
		type="button", "reset", "submit" - 定义按钮上的显示的文本
		type="text", "password", "hidden" - 定义输入字段的初始值
		type="checkbox", "radio", "image" - 定义与输入相关联的值　　
		checked:  radio 和 checkbox 默认被选中
		readonly: 只读. text 和 password
		disabled: 对所用input都好使.
	
	上传文件注意两点：
	
	 1 请求方式必须是post
	 2 enctype="multipart/form-data"
	 上传文件                 
	          <select> 下拉选标签属性
	
	
	          name:表单提交项的键.
	
	          size：选项个数
	
	          multiple：multiple 
	
	                 <option> 下拉选中的每一项 属性：
	
	                       value:表单提交项的值.   selected: selected下拉选默认被选中
	
	                 <optgroup>为每一项加上分组
	
	<textarea> 文本域              
	
		name:    表单提交项的键.
		cols:    文本域默认有多少列
		rows:    文本域默认有多少行
	<label>  实现点击姓名就可达到点击输入框的效果  
	
		<label for="www">姓名</label>
		<input id="www" type="text">

	<fieldset>	组合表单中的相关元素，标签将表单内容的一部分打包，生成一组相关表单的字段。
	当一组表单元素放到 <fieldset> 标签内时，浏览器会以特殊方式来显示它们，它们可能有特殊的边界、3D 效果，或者甚至可创建一个子表单来处理这些元素。

		<fieldset>
		    <legend>登录吧</legend>  该标签为 fieldset 元素定义标题。
		    <input type="text">
		</fieldset>

#10.2
https://www.cnblogs.com/yuanchenqi/articles/6000358.html
##1.HTTP协议
###1.1 HTTP概述

HTTP（hypertext transport protocol），即超文本传输协议。这个协议详细规定了浏览器和万维网服务器之间互相通信的规则。

HTTP就是一个通信规则，通信规则规定了客户端发送给服务器的内容格式，也规定了服务器发送给客户端的内容格式。其实我们要学习的就是这个两个格式！客户端发送给服务器的格式叫“请求协议”；服务器发送给客户端的格式叫“响应协议”。

特点：

	HTTP叫超文本传输协议，基于请求/响应模式的！
	HTTP是无状态协议。
URL：统一资源定位符，就是一个网址：协议名://域名:端口/路径，例如：http://www.oldboy.cn:80/index.html
###1.2 请求协议
请求协议的格式如下：

请求首行；  // 请求方式 请求路径 协议和版本，例如：GET /index.html HTTP/1.1
请求头信息；// 请求头名称:请求头内容，即为key:value格式，例如：Host:localhost
空行；     // 用来与请求体分隔开
请求体。   // GET没有请求体，只有POST有请求体。
浏览器发送给服务器的内容就这个格式的，如果不是这个格式服务器将无法解读！在HTTP协议中，请求有很多请求方法，其中最为常用的就是GET和POST。不同的请求方法之间的区别，后面会一点一点的介绍。

1. GET请求

	HTTP默认的请求方法就是GET
	     * 没有请求体
	     * 数据必须在1K之内！
	     * GET请求数据会暴露在浏览器的地址栏中
	
	GET请求常用的操作：
	       1. 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
	       2. 点击页面上的超链接也一定是GET请求
	       3. 提交表单时，表单默认使用GET请求，但可以设置为POST
		#告诉服务器支持那种方式
		Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
		#指定数据压缩方式
		Accept-Encoding:gzip, deflate, sdch
		#接受语言
		Accept-Language:zh-CN,zh;q=0.8
		#设置缓存
		Cache-Control:no-cache
		Connection:keep-alive
		Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
		#发送目标位置
		Host:127.0.0.1:8090
		Pragma:no-cache
		Upgrade-Insecure-Requests:1
		#当前浏览器信息
		User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36
		Name
		login/
		1 requests ❘ 737 B transferred ❘ Finish: 5 ms ❘ DOMContentLoaded: 14 ms ❘ Load: 14 ms

	- GET 127.0.0.1:8090/login  HTTP/1.1：GET请求，请求服务器路径为  127.0.0.1:8090/login ，协议为1.1；
	- Host:localhost：请求的主机名为localhost；
	- *User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0：与浏览器和OS相关的信息。有些网站会显示用户的系统版本和浏览器版本信息，这都是通过获取User-Agent头信息而来的；
	- Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8：告诉服务器，当前客户端可以接收的文档类型，其实这里包含了*/*，就表示什么都可以接收；
	- Accept-Language: zh-cn,zh;q=0.5：当前客户端支持的语言，可以在浏览器的工具选项中找到语言相关信息；
	- Accept-Encoding: gzip, deflate：支持的压缩格式。数据在网络上传递时，可能服务器会把数据压缩后再发送；
	- Accept-Charset: GB2312,utf-8;q=0.7,*;q=0.7：客户端支持的编码；
	- Connection: keep-alive：客户端支持的链接方式，保持一段时间链接，默认为3000ms；
	- Cookie: JSESSIONID=369766FDF6220F7803433C0B2DE36D98：因为不是第一次访问这个地址，所以会在请求中把上一次服务器响应中发送过来的Cookie在请求中一并发送去过；这个Cookie的名字为JSESSIONID。

	#注意
	HTTP无状态：无状态是指协议对于事务处理没有记忆能力，服务器不知道客户端是什么状态。从另一方面讲，打开一个服务器上的网页
	和你之前打开这个服务器上的网页之间没有任何联系
	如果你要实现一个购物车，需要借助于Cookie或Session或服务器端API（如NSAPI and ISAPI）记录这些信息，请求服务器结算页面时同时将这些信息提交到服务器
	当你登录到一个网站时，你的登录状态也是由Cookie或Session来“记忆”的，因为服务器并不知道你是否登录
	优点：服务器不用为每个客户端连接分配内存来记忆大量状态，也不用在客户端失去连接时去清理内存，以更高效地去处理WEB业务
	缺点：客户端的每次请求都需要携带相应参数，服务器需要处理这些参数
	
	容易犯的误区：
	1、HTTP是一个无状态的面向连接的协议，无状态不代表HTTP不能保持TCP连接，更不能代表HTTP使用的是UDP协议（无连接）
	2、从HTTP/1.1起，默认都开启了Keep-Alive，保持连接特性，简单地说，当一个网页打开完成后，客户端和服务器之间用于传输
	HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
	3、Keep-Alive不会永久保持连接，它有一个保持时间，可以在不同的服务器软件（如Apache）中设定这个时间
2. POST请求

	(1). 数据不会出现在地址栏中
	(2). 数据的大小没有上限
	(3). 有请求体
	(4). 请求体中如果存在中文，会使用URL编码！

		username=%E5%BC%A0%E4%B8%89&password=123

	我们都知道Http协议中参数的传输是"key=value"这种简直对形式的，如果要传多个参数就需要用“&”符号对键值对进行分割。如"?name1=value1&name2=value2"，这样在服务端在收到这种字符串的时候，会用“&”分割出每一个参数，然后再用“=”来分割出参数值。

 

	针对“name1=value1&name2=value2”我们来说一下客户端到服务端的概念上解析过程: 
  	上述字符串在计算机中用ASCII吗表示为： 
	  6E616D6531 3D 76616C756531 26 6E616D6532 3D 76616C756532。 
	   6E616D6531：name1 
	   3D：= 
	   76616C756531：value1 
	   26：&
	   6E616D6532：name2 
	   3D：= 
	   76616C756532：value2 
	   服务端在接收到该数据后就可以遍历该字节流，首先一个字节一个字节的吃，当吃到3D这字节后，服务端就知道前面吃得字节表示一个key，再想后吃，如果遇到26，说明从刚才吃的3D到26子节之间的是上一个key的value，以此类推就可以解析出客户端传过来的参数。

	   现在有这样一个问题，如果我的参数值中就包含=或&这种特殊字符的时候该怎么办。 
	比如说“name1=value1”,其中value1的值是“va&lu=e1”字符串，那么实际在传输过程中就会变成这样“name1=va&lu=e1”。我们的本意是就只有一个键值对，但是服务端会解析成两个键值对，这样就产生了奇异。

	如何解决上述问题带来的歧义呢？解决的办法就是对参数进行URL编码 
	   URL编码只是简单的在特殊字符的各个字节前加上%，例如，我们对上述会产生奇异的字符进行URL编码后结果：“name1=va%26lu%3D”，这样服务端会把紧跟在“%”后的字节当成普通的字节，就是不会把它当成各个参数或键值对的分隔符。

	使用表单可以发POST请求，但表单默认是GET
	
		<form action="" method="post">
		  关键字：<input type="text" name="keyword"/>
		  <input type="submit" value="提交"/>
		</form>
	输入yuan后点击提交，查看请求内容如下：

		Request Headers
		Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
		Accept-Encoding:gzip, deflate
		Accept-Language:zh-CN,zh;q=0.8
		Cache-Control:no-cache
		Connection:keep-alive
		Content-Length:13
		Content-Type:application/x-www-form-urlencoded
		Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
		Host:127.0.0.1:8090
		Origin:http://127.0.0.1:8090
		Pragma:no-cache
		Referer:http://127.0.0.1:8090/login/
		Upgrade-Insecure-Requests:1
		User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) 
		           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36

		Form Data
		username:yuan

	POST请求是可以有体的，而GET请求不能有请求体。

	- Referer: http://localhost:8080/hello/index.jsp：请求来自哪个页面，例如你在百度上点击链接到了这里，那么Referer:http://www.baidu.com；如果你是在浏览器的地址栏中直接输入的地址，那么就没有Referer这个请求头了；
	- Content-Type: application/x-www-form-urlencoded：表单的数据类型，说明会使用url格式编码数据；url编码的数据都是以“%”为前缀，后面跟随两位的16进制。
	- Content-Length:13：请求体的长度，这里表示13个字节。
	- keyword=hello：请求体内容！hello是在表单中输入的数据，keyword是表单字段的名字。

	Referer请求头是比较有用的一个请求头，它可以用来做统计工作，也可以用来做防盗链。
	统计工作：我公司网站在百度上做了广告，但不知道在百度上做广告对我们网站的访问量是否有影响，那么可以对每个请求中的Referer进行分析，如果Referer为百度的很多，那么说明用户都是通过百度找到我们公司网站的。
	防盗链：我公司网站上有一个下载链接，而其他网站盗链了这个地址，例如在我网站上的index.html页面中有一个链接，点击即可下载JDK7.0，但有某个人的微博中盗链了这个资源，它也有一个链接指向我们网站的JDK7.0，也就是说登录它的微博，点击链接就可以从我网站上下载JDK7.0，这导致我们网站的广告没有看，但下载的却是我网站的资源。这时可以使用Referer进行防盗链，在资源被下载之前，我们对Referer进行判断，如果请求来自本网站，那么允许下载，如果非本网站，先跳转到本网站看广告，然后再允许下载。
###1.3响应内容
响应协议的格式如下：

	响应首行；
	响应头信息；
	空行；
	响应体。
响应内容是由服务器发送给浏览器的内容，浏览器会根据响应内容来显示。遇到<img src=''>会开一个新的线程加载，所以有时图片多的话，内容会先显示出来，然后图片才一张张加载出来。

	Request URL:http://127.0.0.1:8090/login/
	Request Method:GET
	Status Code:200 OK
	Remote Address:127.0.0.1:8090
	Response Headers
	view source
	Content-Type:text/html; charset=utf-8
	Date:Wed, 26 Oct 2016 06:48:50 GMT
	Server:WSGIServer/0.2 CPython/3.5.2
	X-Frame-Options:SAMEORIGIN
	
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	<form action="/login/" method="post">
	  用户名：<input type="text" name="username"/>
	  <input type="submit" value="提交"/>
	</form>    
	</body>
	</html>

- HTTP/1.1 200 OK：响应协议为HTTP1.1，状态码为200，表示请求成功，OK是对状态码的解释；
- Server:WSGIServer/0.2 CPython/3.5.2：服务器的版本信息；
- Content-Type: text/html;charset=UTF-8：响应体使用的编码为UTF-8；
- Content-Length: 724：响应体为724字节；
- Set-Cookie: JSESSIONID=C97E2B4C55553EAB46079A4F263435A4; Path=/hello：响应给客户端的Cookie；
- Date: Wed, 25 Sep 2012 04:15:03 GMT：响应的时间，这可能会有8小时的时区差；
3.2　状态码
响应头对浏览器来说很重要，它说明了响应的真正含义。例如200表示响应成功了，302表示重定向，这说明浏览器需要再发一个新的请求。

- 200：请求成功，浏览器会把响应体内容（通常是html）显示在浏览器中；
- 404：请求的资源没有找到，说明客户端错误的请求了不存在的资源；
- 500：请求资源找到了，但服务器内部出现了错误；
- 302：重定向，当响应码为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，它指定了新请求的URL地址；
- 304：

	当用户第一次请求index.html时，服务器会添加一个名为Last-Modified响应头，这个头说明了
	index.html的最后修改时间，浏览器会把index.html内容，以及最后响应时间缓存下来。当用户第
	二次请求index.html时，在请求中包含一个名为If-Modified-Since请求头，它的值就是第一次请
	求时服务器通过Last-Modified响应头发送给浏览器的值，即index.html最后的修改时间，
	If-Modified-Since请求头就是在告诉服务器，我这里浏览器缓存的index.html最后修改时间是这个,
	您看看现在的index.html最后修改时间是不是这个，如果还是，那么您就不用再响应这个index.html
	内容了，我会把缓存的内容直接显示出来。而服务器端会获取If-Modified-Since值，与index.html
	的当前最后修改时间比对，如果相同，服务器会发响应码304，表示index.html与浏览器上次缓存的相
	同，无需再次发送，浏览器可以显示自己的缓存页面，如果比对不同，那么说明index.html已经做了修
	改，服务器会响应200。

	![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161026162455218-1166783413.png)	
         
3.3　其他响应头

告诉浏览器不要缓存的响应头：

- Expires: -1；
- Cache-Control: no-cache；
- Pragma: no-cache；
自动刷新响应头，浏览器会在3秒之后请求http://www.baidu.com：

- Refresh: 3;url=http://www.baidu.com 
3.4　HTML中指定响应头

在HTMl页面中可以使用<meta http-equiv="" content="">来指定响应头，例如在index.html页面中给出<meta http-equiv="Refresh" content="3;url=http://www.baidu.com">，表示浏览器只会显示index.html页面3秒，然后自动跳转到http://www.baidu.com.

##2.CSS协议
https://www.cnblogs.com/yuanchenqi/articles/5977825.html

CSS是Cascading Style Sheets的简称，中文称为层叠样式表，用来控制网页数据的表现，可以使网页的表现与数据内容分离。
##2.1css的四种引入方式
1. 行内式
	
	行内式是在标记的style属性中设定CSS样式。这种方式没有体现出CSS的优势，不推荐使用。
	<p style="background-color: rebeccapurple">hello yuan</p>
2. 嵌入式

	嵌入式是将CSS样式集中写在网页的<head></head>标签对的<style></style>标签对中。格式如下：

		<head>
		    <meta charset="UTF-8">
		    <title>Title</title>
		    <style>
		        p{
		            background-color: #2b99ff;
		        }
		    </style>
		</head>
3. 链接式
	
	将一个.css文件引入到HTML文件中

	<link href="mystyle.css" rel="stylesheet" type="text/css"/>
4. 导入式
	
	将一个独立的.css文件引入HTML文件中，导入式使用CSS规则引入外部CSS文件，<style>标记也是写在<head>标记中，使用的语法如下：    

		<style type="text/css">
	          @import"mystyle.css"; 此处要注意.css文件的路径
		</style>　
	注意：

		导入式会在整个网页装载完后再装载CSS文件，因此这就导致了一个问题，如果网页比较大则会儿出现先显示无样式的页面，闪烁一下之后，再出现网页的样式。这是导入式固有的一个缺陷。使用链接式时与导入式不同的是它会以网页文件主体装载前装载CSS文件，因此显示出来的网页从一开始就是带样式的效果的，它不会象导入式那样先显示无样式的网页，然后再显示有样式的网页，这是链接式的优点。
		尽量不要使用
##2.2 css的选择器（Selector）
“选择器”指明了{}中的“样式”的作用对象，也就是“样式”作用于网页中的哪些元素

1. 基础选择器

	- ＊ ：           通用元素选择器，匹配任何元素                    * { margin:0; padding:0; }
	
	- E  ：          标签选择器，匹配所有使用E标签的元素               p { color:green; }
	
	- .info和E.info: class选择器，匹配所有class属性中包含info的元素   .info { background:#ff0; }    p.info { background:blue; }
	
	- #info和E#info  id选择器，匹配所有id属性等于footer的元素         #info { background:#ff0; }   p#info { background:#ff0; }

2. 组合选择器

	- E,F         多元素选择器，同时匹配所有E元素或F元素，E和F之间用逗号分隔         div,p { color:#f00; }
	
	- E F         后代元素选择器，匹配所有属于E元素后代的F元素，E和F之间用空格分隔    li a { font-weight:bold;
	
	- E > F       子元素选择器，匹配所有E元素的子元素F                            div > p { color:#f00; }
	
	- E + F       毗邻元素选择器，匹配所有紧随E元素之后的同级元素F                  div + p { color:#f00; }  

		<!DOCTYPE html>
		<html lang="en">
		<head>
		    <meta charset="UTF-8">
		    <title>Title</title>
		    <style>
		
		        .div1>p{
		            background-color: aqua;
		            color: deeppink;
		        }
		
		        .main2>div{
		            background-color: blueviolet;
		            color: chartreuse;
		        }
		    </style>
		</head>
		<body>
		
		      <div class="div1">hello1
		          <div class="div2">hello2
		              <div>hello4</div>
		              <p>hello5</p>
		          </div>
		          <p>hello3</p>
		      </div>
		      <p>hello6</p>
		
		<hr>
		
		     <div class="main2">1
		       <div>2
		           <div>
		           </div>
		       </div>
		       <div>
		           </div>
		     </div>
		</body>
		</html>
	#注意嵌套规则：

	1. 块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。
	2. 有几个特殊的块级元素只能包含内联元素，不能包含块级元素。如h1,h2,h3,h4,h5,h6,p,dt
	3. li内可以包含div
	4. 块级元素与块级元素并列、内联元素与内联元素并列。

3. 属性选择器

	- E[att]         匹配所有具有att属性的E元素，不考虑它的值。（注意：E在此处可以省略，比如“[cheacked]”。以下同。）   p[title] { color:#f00; }
	
	- E[att=val]     匹配所有att属性等于“val”的E元素                                 div[class=”error”] { color:#f00; }
	
	- E[att~=val]    匹配所有att属性具有多个空格分隔的值、其中一个值等于“val”的E元素      td[class~=”name”] { color:#f00; }
	
	- E[attr^=val]    匹配属性值以指定值开头的每个元素                     div[class^="test"]{background:#ffff00;}
	
	- E[attr$=val]    匹配属性值以指定值结尾的每个元素                     div[class$="test"]{background:#ffff00;}
	
	- E[attr*=val]    匹配属性值中包含指定值的每个元素                     div[class*="test"]{background:#ffff00;}

4. 伪类(Pseudo-classes)

	CSS伪类是用来给选择器添加一些特殊效果。

	anchor伪类：专用于控制链接的显示效果

	- a:link（没有接触过的链接）,用于定义了链接的常规状态。
	- a:hover（鼠标放在链接上的状态）,用于产生视觉效果。
	- a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。
	- a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。
	- 伪类选择器 : 伪类指的是标签的不同状态:
	      a ==> 点过状态 没有点过的状态 鼠标悬浮状态 激活状态
		  a:link {color: #FF0000} /* 未访问的链接 */
		  a:visited {color: #00FF00} /* 已访问的链接 */
		  a:hover {color: #FF00FF} /* 鼠标移动到链接上 */
		  a:active {color: #0000FF} /* 选定的链接 */ 格式: 标签:伪类名称{ css代码; }
	before after伪类 ：

	- :before    p:before       在每个<p>元素之前插入内容
	- :after     p:after        在每个<p>元素之后插入内容
	
	- p:before        在每个 <p> 元素的内容之前插入内容                    p:before{content:"hello";color:red}
	- p:after         在每个 <p> 元素的内容之前插入内容                    p:after{ content:"hello"；color:red}


