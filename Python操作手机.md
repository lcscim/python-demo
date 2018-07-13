#0713
tips:



##1.连接手机
1. 下载adb
2. 配置环境变量

	右键我的电脑- 属性-高级系统设置-高级-环境变量，将Path中添加adb.exe的路径	
3. 通过adb devices命令判断是否连接成功，成功显示如下内容

		List of devices attached
		2369b073 	device
- 获取屏幕分辨率代码

		import os		//导入操作系统模块，文档http://www.runoob.com/python3/python3-os-file-methods.html
		import re		//导入正则表达式模块，文档http://www.runoob.com/python/python-reg-expressions.html
		size_str = os.popen('adb shell wm size').read()		//os.popen() 方法用于从一个命令打开一个管道，并用read方法从文件读取指定的字节数
		if not size_str:
		    print('请安装 ADB 及驱动并配置环境变量')
		    sys.exit()
		m = re.search(r'(\d+)x(\d+)', size_str)		//re.search 扫描整个字符串并返回第一个成功的匹配。第一个参数正则表达式，第二个是要匹配的字符串
		if m:
		    print(m)
##2.adb文档
adb全名Andorid Debug Bridge. 顾名思义, 这是一个Debug工具。官方文档：https://github.com/mzlogin/awesome-adb/blob/master/README.en.md#reference-links

- adb详细文档目录，中文https://blog.csdn.net/u010375364/article/details/52344120/

		基本用法
			命令语法
			为命令指定目标设备
			启动/停止
			查看 adb 版本
			以 root 权限运行 adbd
			指定 adb server 的网络端口
		设备连接管理
			查询已连接设备/模拟器
			USB 连接
			无线连接
		应用管理
			查看应用列表
				所有应用
				系统应用
				第三方应用
				包名包含某字符串的应用
			安装 APK
			卸载应用
			清除应用数据与缓存
			查看前台 Activity
		与应用交互
			调起 Activity
			调起 Service
			发送广播
			强制停止应用
		文件管理
			复制设备里的文件到电脑
			复制电脑里的文件到设备
		模拟按键/输入
			电源键
			菜单键
			HOME 键
			返回键
			音量控制
			媒体控制
			点亮/熄灭屏幕
			滑动解锁
			输入文本
		查看日志
			Android 日志
				按级别过滤日志
				按 tag 和级别过滤日志
				日志格式
				清空日志
			内核日志
		查看设备信息
			型号
			电池状况
			屏幕分辨率
			屏幕密度
			显示屏参数
			android_id
			IMEI
			Android 系统版本
			Mac 地址
			CPU 信息
			更多硬件与系统属性
		实用功能
			屏幕截图
			录制屏幕
			重新挂载 system 分区为可写
			查看连接过的 WiFi 密码
			设置系统日期和时间
			重启手机
			检测设备是否已 root
			使用 Monkey 进行压力测试
		刷机相关命令
			重启到 Recovery 模式
			从 Recovery 重启到 Android
			重启到 Fastboot 模式
			通过 sideload 更新系统
		更多 adb shell 命令
			查看进程
			查看实时资源占用情况
			其它
