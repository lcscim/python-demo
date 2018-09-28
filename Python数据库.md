#9.27
http://www.cnblogs.com/wupeiqi/articles/5713315.html
http://www.cnblogs.com/wupeiqi/articles/5713323.html
http://www.cnblogs.com/wupeiqi/articles/5729934.html
http://www.cnblogs.com/wupeiqi/articles/5716963.html

##1.数据管理系统DBMS 软件
##2.安装MySQL
MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下公司。MySQL 最流行的关系型数据库管理系统，在 WEB 应用方面MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。

想要使用MySQL来存储并操作数据，则需要做几件事情：
　　a. 安装MySQL服务端
　　b. 安装MySQL客户端
　　b. 【客户端】连接【服务端】
　　c. 【客户端】发送命令给【服务端MySQL】服务的接受命令并执行相应操作(增删改查等)

下载
        http://dev.mysql.com/downloads/mysql/

Window版本

1、下载

	MySQL Community Server 5.7.16
	http://dev.mysql.com/downloads/mysql/
2、解压

如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64

3、初始化

MySQL解压后的 bin 目录下有一大堆的可执行文件，执行如下命令初始化数据：

	cd c:\mysql-5.7.16-winx64\bin
	mysqld --initialize-insecure
4、启动MySQL服务

执行命令从而启动MySQL服务

	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	# 启动MySQL服务
	mysqld
5、启动MySQL客户端并连接MySQL服务

由于初始化时使用的【mysqld --initialize-insecure】命令，其默认未给root账户设置密码

	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	# 连接MySQL服务器
	mysql -u root -p
	# 提示请输入密码，直接回车

到此为止，MySQL服务端已经安装成功并且客户端已经可以连接上，以后再操作MySQL时，只需要重复上述4、5步骤即可。但是，在4、5步骤中重复的进入可执行文件目录比较繁琐，如想日后操作简便，可以做如下操作。

a. 添加环境变量

将MySQL可执行文件添加到环境变量中，从而执行执行命令即可

	
	【右键计算机】--》【属性】--》【高级系统设置】--》【高级】--》【环境变量】--》【在第二个内容框中找到 变量名为Path 的一行，双击】 --> 【将MySQL的bin目录路径追加到变值值中，用 ； 分割】
	
	# 启动MySQL服务，在终端输入
	mysqld
	# 连接MySQL服务，在终端输入：
	mysql -u root -p
b. 将MySQL服务制作成windows服务

上一步解决了一些问题，但不够彻底，因为在执行【mysqd】启动MySQL服务器时，当前终端会被hang住，那么做一下设置即可解决此问题：

	# 制作MySQL的Windows服务，在终端执行此命令：
	"c:\mysql-5.7.16-winx64\bin\mysqld" --install
	# 移除MySQL的Windows服务，在终端执行此命令：
	"c:\mysql-5.7.16-winx64\bin\mysqld" --remove
注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令：
	# 启动MySQL服务
	net start mysql
	# 关闭MySQL服务
	net stop mysql

##3.介绍
1. 概念

	数据库，相当于文件夹
	数据库表，相当于文件
	数据行，相当于文件中的一行数据
2. 命令

	1、显示数据库，查看当前MySQL有哪些数据根目录有哪些文件夹
	
		SHOW DATABASES;
		#默认数据库：
		　　mysql - 用户权限相关数据
		　　test - 用于用户测试数据
		　　information_schema - MySQL本身架构相关数据

	2、创建数据库
	
		create database 数据库名；
		
		# utf-8
		CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
		# gbk
		CREATE DATABASE 数据库名称 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
	3、使用数据库
	
		USE 数据库名; 	使用数据库
		SHOW TABLES;	显示当前使用的数据库中所有表：
		create table 表名(nid int,name varchar(20));    创建数据表并指定内容
		select * from 表名; 		查看表中所有数据
		insert into 表名(nid,name) values(1,'alex');		向表中插入数据
		desc 表名； 展示所有数据
3. 授权

	1、用户管理，只适用于MySQL用户表,密码要加引号

		创建用户
		    create user '用户名'@'IP地址' identified by '密码';
		删除用户
		    drop user '用户名'@'IP地址';
		修改用户
		    rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
		修改密码
		    set password for '用户名'@'IP地址' = Password('新密码')

		PS：用户权限相关数据保存在mysql数据库的user表中，所以也可以直接对其进行操作（不建议）
		#使用创建的用户登录
		C:\mysql5.7.21\bin\mysql -u 用户名 -h IP地址 -p
	2、授权管理
	
		show grants for '用户'@'IP地址'                  -- 查看权限
		grant  权限 on 数据库.表 to   '用户'@'IP地址'      -- 授权
		revoke 权限 on 数据库.表 from '用户'@'IP地址'      -- 取消权限
		#例如，给lcscim@127.0.0.1添加对于表test.tb1的选择权限
		grant select on test.tb1 to lcscim@127.0.0.1;

		#具体权限如下	
            all privileges  除grant外的所有权限
            select          仅查权限
            select,insert   查和插入权限
            ...
            usage                   无访问权限
            alter                   使用alter table
            alter routine           使用alter procedure和drop procedure
            create                  使用create table
            create routine          使用create procedure
            create temporary tables 使用create temporary tables
            create user             使用create user、drop user、rename user和revoke  all privileges
            create view             使用create view
            delete                  使用delete
            drop                    使用drop table
            execute                 使用call和存储过程
            file                    使用select into outfile 和 load data infile
            grant option            使用grant 和 revoke
            index                   使用index
            insert                  使用insert
            lock tables             使用lock table
            process                 使用show full processlist
            select                  使用select
            show databases          使用show databases
            show view               使用show view
            update                  使用update
            reload                  使用flush
            shutdown                使用mysqladmin shutdown(关闭MySQL)
            super                   􏱂􏰈使用change master、kill、logs、purge、master和set global。还允许mysqladmin􏵗􏵘􏲊􏲋调试登陆
            replication client      服务器位置的访问
            replication slave       由复制从属使用
	
       #对于目标数据库以及内部其他：
            数据库名.*           数据库中的所有
            数据库名.表          指定数据库中的某张表
            数据库名.存储过程     指定数据库中的存储过程
            *.*                所有数据库

            用户名@IP地址         用户只能在改IP下才能访问
            用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
            用户名@%             用户可以再任意IP下访问(默认IP地址为%)
			此时需要加引号

            grant all privileges on db1.tb1 TO '用户名'@'IP'

            grant select on db1.* TO '用户名'@'IP'

            grant select,insert on *.* TO '用户名'@'IP'

            revoke select on db1.tb1 from '用户名'@'IP'
		#特殊的：
	
			flush privileges，将数据读取到内存中，从而立即生效。
		
		# 启动免授权服务端
		mysqld --skip-grant-tables
		
		# 客户端
		mysql -u root -p
		
		# 修改用户名密码
		update mysql.user set authentication_string=password('666') where user='root';
		flush privileges;
4. sql语句

	数据库级别：

		show databases;		展示数据库
		create database 数据表名；	创建数据库
		CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
		
		use 数据库名；	打开数据库
		drop 数据库名；	删除数据库
	表级别

		show tables;		展示库里的数据表
		desc tbl;			展示表结构

		create table tb1(nid int not null auto_increment primary key,
							name varchar(16),age int default 19)
		engine=innodb default charset=utf8;
		#创建表名为tb1，nid不为空，自增为主键。。。engine=innodb指定数据库引擎