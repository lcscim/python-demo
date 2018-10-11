#10.11
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