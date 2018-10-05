#10.5
https://www.cnblogs.com/yuanchenqi/articles/5980312.html

##1.JavaScript概述 
- JavaScript的历史

	- 1992年Nombas开发出C-minus-minus(C--)的嵌入式脚本语言(最初绑定在CEnvi软件中).后将其改名ScriptEase.(客户端执行的语言)
	- Netscape(网景)接收Nombas的理念,(Brendan Eich)在其Netscape Navigator 2.0产品中开发出一套livescript的脚本语言.Sun和Netscape共同完成.后改名叫Javascript
	- 微软随后模仿在其IE3.0的产品中搭载了一个JavaScript的克隆版叫Jscript.
	- 为了统一三家,ECMA(欧洲计算机制造协会)定义了ECMA-262规范.国际标准化组织及国际电工委员会（ISO/IEC）也采纳 ECMAScript 作为标准（ISO/IEC-16262）。从此，Web 浏览器就开始努力（虽然有着不同的程度的成功和失败）将 ECMAScript 作为 JavaScript 实现的基础。EcmaScript是规范.
- ECMAScript  
	
	尽管 ECMAScript 是一个重要的标准，但它并不是 JavaScript 唯一的部分，当然，也不是唯一被标准化的部分。实际上，一个完整的 JavaScript 实现是由以下 3 个不同部分组成的：
	
	- 核心（ECMAScript） 
	- 文档对象模型（DOM） Document object model (整合js，css，html)
	- 浏览器对象模型（BOM） Broswer object model（整合js和浏览器）
	- Javascript 在开发中绝大多数情况是基于对象的.也是面向对象的. 
	![](https://images2015.cnblogs.com/blog/877318/201610/877318-20161023211134529-32650400.png)
	简单地说，ECMAScript 描述了以下内容：
	
	- 语法 
	- 类型 
	- 语句 
	- 关键字 
	- 保留字 
	- 运算符 
	- 对象 (封装 继承 多态) 基于对象的语言.使用对象.
- JavaScript的引入方式

	{#1 直接编写#}
	    <script>
	        alert('hello yuan')
	    </script>
	{#2 导入文件#}
	    <script src="hello.js"></script>　　
##2. JavaScript的基础
