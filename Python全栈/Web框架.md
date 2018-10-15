#10.11
- {{}}中是变量
- （%%}中是语句
https://www.cnblogs.com/yuanchenqi/articles/6083427.html
##1. Django的流程
1. 安装

	 #安装： pip3 install django
          添加环境变量
    #1  创建project
       django-admin startproject mysite
       ---mysite
          ---settings.py
          ---url.py
          ---wsgi.py
       ---- manage.py(启动文件)  
    #2  创建APP       
       python mannage.py startapp  app01
    #3  settings配置
       TEMPLATES
       STATICFILES_DIRS=(
            os.path.join(BASE_DIR,"statics"),
        )
       STATIC_URL = '/static/' 
       #  我们只能用 STATIC_URL，但STATIC_URL会按着你的STATICFILES_DIRS去找#4  根据需求设计代码
           url.py
           view.py
    #5  使用模版
       render(req,"index.html")   
    #6  启动项目
       python manage.py runserver  127.0.0.1:8090
    #7  连接数据库，操作数据
       model.py
2. django的命令行工具

	#在命令行中如此操作，pycharm除外
	<1> 创建一个django工程 : django-admin.py startproject 工程名
	<2>在mysite目录下创建blog应用: python manage.py startapp 应用名
	#在pycharm中
	<3>启动django项目：python manage.py runserver 8080
	<4>生成同步数据库的脚本：python manage.py makemigrations 工程名 
               同步数据库:  python manage.py migrate 工程名
	<5>当我们访问http://127.0.0.1:8080/admin/时就会显示

	注：在urls文件中

		from django.contrib import admin
		from django.urls import path
		from mysite import views	导入包
		
		urlpatterns = [
		    path('admin/', admin.site.urls),
			#网站目录，和启用方法
		    path('index/', views.userInfor),
		]

#10.12

##1. Django URL (路由系统)
- 无名分组
	
	urlpatterns = [
	    url(正则表达式, views视图函数，参数，别名),
	]
	参数说明：
	
		一个正则表达式字符串
		一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
		可选的要传递给视图函数的默认参数（字典形式）
		一个可选的name参数
		
		#正则表达式
		- ^s表示必须以s开头
		- s$表示必须以s结尾
	示例
	
		from django.conf.urls import url
		from django.contrib import admin
		from app01 import views
		urlpatterns = [
			#匹配路径名必须是articles/2003/。
		    url(r'^articles/2003/$', views.special_case_2003),
			# [0-9]{4} =》  0-9任意一个重复四次，加一个小括号表示这个数字可以用变量接受  year_archive方法必须接受两个参数一个req另一个就是括号内
		    url(r'^articles/([0-9]{4})/$', views.year_archive),  #no_named group
			#如果两个参数表示再添加两个参数
		    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
			#此时经过分组并且命名，方法内的形参名必须是该分组名
		    url(r'^articles/(?p<year>[0-9]{4})/(?p<month>[0-9]{2})/(?p<day>[0-9]+)/$', views.article_detail),
		
		]
- 有名分组
	
	(?P<id>\d{3})表示分组组名叫id
	
		import re
		#(?P<id>\d{3})/(?P<name>\w{3}) 表示分组
		ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
		print(ret.group())			//123/ooo
		print(ret.group('id'))		//123
		print(ret.group('name'))	//ooo

- 如果传入的参数与分组的参数名相同，后面的覆盖前面的

	url(r'^articles/(?P<name>[0-9]{4})/$', views.year_archive，{"name","alex"}),

##2.Django Views（视图函数）
http请求中产生两个核心对象：

        http请求：HttpRequest对象
        http响应：HttpResponse对象

所在位置：django.http

之前我们用到的参数req就是HttpRequest    检测方法：isinstance(request,HttpRequest)

1. HttpRequest对象的属性和方法：

	# path：       请求页面的全路径，不包括域名
	# method：     请求中使用的HTTP方法的字符串表示。全大写表示。例如
	#                    if  req.method=="GET":
	#                              do_something()
	#                    elseif req.method=="POST":
	#                              do_something_else()
	# GET:         包含所有HTTP GET参数的类字典对象
	# POST：       包含所有HTTP POST参数的类字典对象
	#              服务器收到空的POST请求的情况也是可能发生的，也就是说，表单form通过
	#              HTTP POST方法提交请求，但是表单中可能没有数据，因此不能使用
	#              if req.POST来判断是否使用了HTTP POST 方法；应该使用  if req.method=="POST"
	# COOKIES:     包含所有cookies的标准Python字典对象；keys和values都是字符串。
	# FILES：      包含所有上传文件的类字典对象；FILES中的每一个Key都是<input type="file" name="" />标签中                     name属性的值，FILES中的每一个value同时也是一个标准的python字典对象，包含下面三个Keys：
	#             filename：      上传文件名，用字符串表示
	#             content_type:   上传文件的Content Type
	#             content：       上传文件的原始内容
	# user：       是一个django.contrib.auth.models.User对象，代表当前登陆的用户。如果访问用户当前
	#              没有登陆，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。你
	#              可以通过user的is_authenticated()方法来辨别用户是否登陆：
	#              if req.user.is_authenticated();只有激活Django中的AuthenticationMiddleware
	#              时该属性才可用
	# session：    唯一可读写的属性，代表当前会话的字典对象；自己有激活Django中的session支持时该属性才可用。
	
	#方法
	get_full_path(),   比如：http://127.0.0.1:8000/index33/?name=123 ,req.get_full_path()得到的结果就是/index33/?name=123
	req.path:/index33
2. HttpResponse对象：
  
	对于HttpRequest对象来说，是由django自动创建的，但是，HttpResponse对象就必须我们自己创建。每个view请求处理方法必须返回一个HttpResponse对象。

  	HttpResponse类在django.http.HttpResponse

  	在HttpResponse对象上扩展的常用方法：

	页面渲染：         	render()（推荐）<br>                		
						render_to_response(),
	页面跳转：         	redirect("路径")
	
	locals()：    可以直接将函数中所有的变量传给模板
	- render(req,"login.html")
	- render_to_response("login.html",{"name":"alex"})	,可向login.html中的{{name}}变量进行修改
	- render_to_response("login.html",locals())		这样可以直接在login.html中使用方法中的变量{{ 函数中的变量名 }}



#10.14

##1.tips

- form表单提交数据会刷新页面，此时就需要使用jQuery的ajax 
- 在前端也有json  

	- json.parse(字符串)		把字符串变为json对象
	- json.stringify(对象)	把对象变为字符串

- 在前端location.reload()表示刷新当前页面
- 在前端location.href(路径)表示跳转到目标路径