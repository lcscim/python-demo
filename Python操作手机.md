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
#7.14

tips:
1. 自用三星desired_caps['deviceName'] = 'samsung-sm_a9100-2369b073'


##1.appium
appium 是一个自动化测试开源工具，支持 iOS 平台和 Android 平台上的原生应用，web应用和混合应用。是一个跨平台的工具：它允许测试人员在不同的平台（iOS，Android）使用同一套API来写自动化测试脚本，这样大大增加了iOS和Android测试套件间代码的复用性。

###1.1安装
1. 如果使用 Android 模拟器运行测试的话需要安装ANDROID SDK。教程地址：

	http://www.testclass.net/appium/appium-base-sdk/
2. 安装 appium Server，教程地址http://www.testclass.net/appium/appium-base-server/

	下载地址：https://bitbucket.org/appium/appium.app/downloads/
3. 对于Python，需安装python-client，安装与测试http://www.testclass.net/appium/appium-base-python/

	使用pip安装语句如下

		pip install Appium-Python-Client
	安装后使用以下内容测试：

		from appium import webdriver
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'samsung-sm_a9100-2369b073'
		desired_caps['appPackage'] = 'com.android.calculator2'
		desired_caps['appActivity'] = '.Calculator'
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		driver.find_element_by_name("1").click()		
		driver.find_element_by_name("5").click()		
		driver.find_element_by_name("9").click()		
		driver.find_element_by_name("delete").click()		
		driver.find_element_by_name("9").click()	
		driver.find_element_by_name("5").click()	
		driver.find_element_by_name("+").click()	
		driver.find_element_by_name("6").click()	
		driver.find_element_by_name("=").click()	
		driver.quit()
	注意：使用安卓虚拟机测试以安卓6.0版本测试，其他不保证正常运行，以下保证正常运行

		from appium import webdriver
		import time
		
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['appPackage'] = 'com.android.calculator2'
		desired_caps['appActivity'] = '.Calculator'
		
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'delete')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'plus')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'7')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@text,'6')]").click()
		driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'equals')]").click()
		time.sleep(5)
		
		driver.quit()
4. 由于appium server很久没更新， Appium-desktop出现为其续命，语法有些改变

	下载地址：https://github.com/appium/appium-desktop/releases

##1.2Desired Capabilities
Desired Capabilities 本质上是以 key value 字典的方式存放，客户端将这些键值对发给服务端，告诉服务端我们想要怎么测试。它告诉 appium Server这样一些事情：

	本次测试是启动浏览器还是启动移动设备。
	是启动Andorid还是启动iOS。
	启动Android时，app的package是什么。
	启动Android时，app的activity是什么。
示例：

	DesiredCapabilities capabilities = new DesiredCapabilities();
	capabilities.setCapability("deviceName", "Android Emulator");
	capabilities.setCapability("automationName", "Appium");
	capabilities.setCapability("platformName", "Android");
	capabilities.setCapability("platformVersion", "5.1");
	capabilities.setCapability("appPackage", "com.android.calculator2");
	capabilities.setCapability("appActivity", ".Calculator");
	
	WebDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

	deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator，iPad Simulator，iPhone Retina 4-inch，Android Emulator，Galaxy S4…
	automationName：使用哪种自动化引擎。appium（默认）还是Selendroid。
	platformName：使用哪种移动平台。iOS, Android, orFirefoxOS。
	platformVersion：指定平台的系统版本。例如指的Android平台，版本为5.1。
	appActivity：待测试的app的Activity名字。比如MainActivity、.Settings。注意，原生app的话要在activity前加个”.“。
	appPackage：待测试的app的Java package。比如com.example.android.myApp, com.android.settings。
更多配置参数见：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md

##1.3定位控件
appium 通过 uiautomatorviewer.bat 工具来查看控件的属性。该工具位于 Android SDK 的 /tools/bin/ 目录下。

- id 定位

	通过uiautomatorviewer.bat 工具可以查看对象的id属性。如果目标设备的API Level低于18则UIAutomatorViewer不能获得对应的Resource ID，只有等于大于18的时候才能使用。查看界面右下方node detail一栏，resource-id 就是我们理解的id属性了。使用方法：

		driver.findElement(By.id("com.android.calculator2:id/formula"))
- name定位

	与ID定位同理，text就是我们要查找的name，使用方法

		driver.findElement(By.name("9"))
- class name 定位

	与ID定位同理，界面上的的class属性是：android.widget.Button。使用方法

		WebElement button = driver.findElement(By.className("android.widget.Button"));
	使用 Class Name 一般获得的 view 都不止一个，所以应该需要遍历一遍得到的 views，然后缩小搜索条件来获得目标控件。
- XPath定位
	
	在 WebDriver 上 XPath 定位是功能强大的一种定位方式。我个人惯用于此方法来定位Web页面上的元素。下面看看在 Android 上 XPath 定位的用法。用class的属性来替代做标签的名字。使用方法

		driver.findElement(By.xpath("//android.view.ViewGroup/android.widget.Button"))
	当果如果出现class 相同的情况下可以用控件的属性值进行区分。

		driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click(); //7
		driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'times')]")).click(); //*
		driver.findElement(By.xpath("//android.widget.Button[contains(@text,'7')]")).click();  //7
		driver.findElement(By.xpath("//android.widget.Button[contains(@content-desc,'equals')]")).click(); //=
	即，格式如下：

		xpath("//class属性[contains(@text或content-desc,'对应值')]")
- Accessibility ID定位

	这个方法属于Appium扩展的定位方法。我们的核心是要找到元素的contentDescription属性。它就是元素的 content-desc 。使用方法：

		driver.findElementByAccessibilityId("plus").click();
- android uiautomator定位

	这个方法也属于 Appium（Android）扩展的定位方法。同样使用 UIAutomatorViewer.bat 工具直接查看。也就是说一个元素的任意属性都可以通过android uiautomator方法来进行定位，但要保证这种定位方式的唯一性。使用方法：

		driver.findElementByAndroidUIAutomator("new UiSelector().text(\"clr\")").click();
		driver.findElementByAndroidUIAutomator("new UiSelector().text(\"8\")").click();
		driver.findElementByAndroidUIAutomator("new UiSelector().description(\"plus\")").click();
		driver.findElementByAndroidUIAutomator("new UiSelector().text(\"5\")").click();
		driver.findElementByAndroidUIAutomator("new UiSelector().description(\"equals\")").click();
	需要注意的是 description() 方法用的是content-desc属性。
##1.4appium API 之应用操作
1. 安装应用

	方法：installApp()安装应用到设备中去。需要apk包的路径。

		driver.installApp("path/to/my.apk");
		driver.installApp("D:\\android\\apk\\ContactManager.apk");
2. 卸载应用

	方法：removeApp()从设备中删除一个应用。

		driver.removeApp("com.example.android.apis");
3. 关闭应用

	方法：closeApp()关闭打开的应用，默认关闭当前打开的应用，所以不需要入参。这个方法并非真正的关闭应用，相当于按home键将应用置于后台，可以通过launchApp()再次启动。

4. 启动应用

	方法：launchApp()启动应用。你一定很迷惑，不是在初始化的配置信息已经指定了应用，脚本运行的时候就需要启动应用，为什么还要有这个方法去启动应用呢？重新启动应用也是一个测试点，该方法需要配合closeApp()使用的。

		driver.closeApp();
		driver.launchApp();
5. 检查应用是否安装
	
	方法：isAppInstalled()检查应用是否已经安装。需要传参应用包的名字。返回结果为Ture或False。

		driver.isAppInstalled('com.example.android.apis');
6. 将应用置于后台

	方法：runAppInBackground()将当前活跃的应用程序发送到后台。这个方法需要入参，需要指定应用置于后台的时长。

		driver.runAppInBackground(2);
7. 应用重置

	方法：resetApp()重置当前被测程序到出始化状态。该方法不需要入参。

		driver.resetApp();
##1.5appium API 之上下文操作
1、获取当前上下文

	方法：getContext()获取当前所有的可用的上下文。该方法不需要入参。

		String ct = driver.getContext();
		System.out.println(ct);
		
		-----------计算器应用的打印结果-----------------------
		NATIVE_APP
2、当前所有上下文句柄

	方法：getContextHandles()获取当前所有可用的上下文。该方法不需要入参。

3、切换上下文

	context()切换到特定的上下文中。需要指定上下文的名称。

		driver.context('NATIVE_APP')
		driver.context('WEBVIEW_1')
##1.6appium API 之键盘操作
模拟键盘输入也是非常重要的操作。这一小节来介绍那些关于键盘的操作。

1、sendKeys()方法

	方法：sendKeys()用法：

		driver.findElements(By.name("Name")).sendKeys("jack");
2、pressKeyCode()方法除此之外，appium扩展提供了pressKeyCode()方法。该方法Android特有。方法：

	pressKeyCode()发送一个键码的操作。需要一个入参。

		driver.pressKeyCode(29); // 字母“a”
	如果想点击Android的HOME键应该怎么实现的呢？如下

		driver.pressKeyCode(AndroidKeyCode.HOME);
下面提供Android keycode参考表：

	电话键
	KEYCODE_CALL 拨号键 5
	KEYCODE_ENDCALL 挂机键 6
	KEYCODE_HOME 按键Home 3
	KEYCODE_MENU 菜单键 82
	KEYCODE_BACK 返回键 4
	KEYCODE_SEARCH 搜索键 84
	KEYCODE_CAMERA 拍照键 27
	KEYCODE_FOCUS 拍照对焦键 80
	KEYCODE_POWER 电源键 26
	KEYCODE_NOTIFICATION 通知键 83
	KEYCODE_MUTE 话筒静音键 91
	KEYCODE_VOLUME_MUTE 扬声器静音键 164
	KEYCODE_VOLUME_UP 音量增加键 24
	KEYCODE_VOLUME_DOWN 音量减小键 25
	控制键
	KEYCODE_ENTER 回车键 66
	KEYCODE_ESCAPE ESC键 111
	KEYCODE_DPAD_CENTER 导航键 确定键 23
	KEYCODE_DPAD_UP 导航键 向上 19
	KEYCODE_DPAD_DOWN 导航键 向下 20
	KEYCODE_DPAD_LEFT 导航键 向左 21
	KEYCODE_DPAD_RIGHT 导航键 向右 22
	KEYCODE_MOVE_HOME 光标移动到开始键 122
	KEYCODE_MOVE_END 光标移动到末尾键 123
	KEYCODE_PAGE_UP 向上翻页键 92
	KEYCODE_PAGE_DOWN 向下翻页键 93
	KEYCODE_DEL 退格键 67
	KEYCODE_FORWARD_DEL 删除键 112
	KEYCODE_INSERT 插入键 124
	KEYCODE_TAB Tab键 61
	KEYCODE_NUM_LOCK 小键盘锁 143
	KEYCODE_CAPS_LOCK 大写锁定键 115
	KEYCODE_BREAK Break/Pause键 121
	KEYCODE_SCROLL_LOCK 滚动锁定键 116
	KEYCODE_ZOOM_IN 放大键 168
	KEYCODE_ZOOM_OUT 缩小键 169
	组合键
	KEYCODE_ALT_LEFT Alt+Left
	KEYCODE_ALT_RIGHT Alt+Right
	KEYCODE_CTRL_LEFT Control+Left
	KEYCODE_CTRL_RIGHT Control+Right
	KEYCODE_SHIFT_LEFT Shift+Left
	KEYCODE_SHIFT_RIGHT Shift+Right
	基本
	KEYCODE_0 按键’0’ 7
	KEYCODE_1 按键’1’ 8
	KEYCODE_2 按键’2’ 9
	KEYCODE_3 按键’3’ 10
	KEYCODE_4 按键’4’ 11
	KEYCODE_5 按键’5’ 12
	KEYCODE_6 按键’6’ 13
	KEYCODE_7 按键’7’ 14
	KEYCODE_8 按键’8’ 15
	KEYCODE_9 按键’9’ 16
	KEYCODE_A 按键’A’ 29
	KEYCODE_B 按键’B’ 30
	KEYCODE_C 按键’C’ 31
	KEYCODE_D 按键’D’ 32
	KEYCODE_E 按键’E’ 33
	KEYCODE_F 按键’F’ 34
	KEYCODE_G 按键’G’ 35
	KEYCODE_H 按键’H’ 36
	KEYCODE_I 按键’I’ 37
	KEYCODE_J 按键’J’ 38
	KEYCODE_K 按键’K’ 39
	KEYCODE_L 按键’L’ 40
	KEYCODE_M 按键’M’ 41
	KEYCODE_N 按键’N’ 42
	KEYCODE_O 按键’O’ 43
	KEYCODE_P 按键’P’ 44
	KEYCODE_Q 按键’Q’ 45
	KEYCODE_R 按键’R’ 46
	KEYCODE_S 按键’S’ 47
	KEYCODE_T 按键’T’ 48
	KEYCODE_U 按键’U’ 49
	KEYCODE_V 按键’V’ 50
	KEYCODE_W 按键’W’ 51
	KEYCODE_X 按键’X’ 52
	KEYCODE_Y 按键’Y’ 53
	KEYCODE_Z 按键’Z’ 54
##1.7 appium API 之 TouchAction 操作
Appium的辅助类，主要针对手势操作，比如滑动、长按、拖动等。

1、按压控件

	方法：press()开始按压一个元素或坐标点（x,y）。通过手指按压手机屏幕的某个位置。

		press(WebElement el, int x, int y)
		press也可以接收屏幕的坐标（x,y）。
	例：

		TouchAction(driver).press(x=0,y=308).release().perform()
	除了press()方法之外，本例中还用到了别外两个新方法。

		release() 结束的行动取消屏幕上的指针。
		Perform() 执行的操作发送到服务器的命令操作。
2、长按控件

	方法：longPress()开始按压一个元素或坐标点（x,y）。 相比press()方法，longPress()多了一个入参，既然长按，得有按的时间吧。duration以毫秒为单位。1000表示按一秒钟。其用法与press()方法相同。

		longPress(WebElement el, int x, int y, Duration duration)

	例：

		TouchAction action = new TouchAction(driver);
		action.longPress(names.get(1),1000).perform().release();
		action.longPress(1 ,302,1000).perform().release();
3、点击控件

	方法：tap()对一个元素或控件执行点击操作。用法参考press()。

		tap(WebElement el, int x, int y)

	例：

		TouchAction action = new TouchAction(driver);
		action.tap(names.get(1)).perform().release();
		action.tap(1 ,302).perform().release();
4、移动

	方法：moveTo()将指针（光标）从过去指向指定的元素或点。

		movTo(WebElement el, int x, int y)

	其用法参考press()方法。

	例：

		TouchAction action = new TouchAction(driver);
		action.moveTo(names.get(1)).perform().release();
		action.moveTo(1 ,302).perform().release();
5、暂停

	方法：wait()暂停脚本的执行，单位为毫秒。

		action.wait(1000);
##1.8 appium API 之其他操作
其它操作针对移动设备上特有的一些操作。

1、熄屏

	方法： * lockDevice()点击电源键熄灭屏幕。在iOS设备可以设置熄屏一段时间。Android上面不带参数，所以熄屏之后就不会再点亮屏幕了。

		driver.lockDevice(1000);  // iOS
		driver.lockDriice();   //Android  
2、当前Activity（Android only）

	方法：currentActivity()得到当前应用的activity。只适用于Android。 例（通讯录）：

		String ca = driver.currentActivity();
		System.out.print(ca);
		-------------输出结果为-------------
		.activities.PeopleActivity
3、收起键盘

	方法：hideKeyboard()收起键盘，这个方法很有用，当我们对一个输入框输入完成后，需要将键盘收起，再切换到一下输入框进行输入。

		driver.hideKeyboard();  //收起键盘
4、滑动

	方法：swipe()模拟用户滑动。将控件或元素从一个位置（x,y）拖动到另一个位置（x,y）。swipe(int startx, int starty, int endx, int endy, int duration) * start_x：开始滑动的x坐标。 * start_y：开始滑动的y坐标。 * end_x：结束滑动的x坐标。 * end_y：结束滑动的y坐标。 * duration：持续时间。例：

		driver.swipe(75, 500, 75, 0, 800);
5、拉出文件

	方法：pullFile()从设备中拉出文件。例：

		driver.pullFile('Library/AddressBook/AddressBook.sqlitedb')
6、推送文件

	方法：pushFile()推送文件到设备中去。

		pushFile(String remotePath, byte[] base64Data)

	例：

		String content = "some data for the file";
		byte[] data = Base64.encodeBase64(content.getBytes());
		driver.pushFile("sdcard/test.txt", data);
##1.9 获取android app的Activity
方法一

	如有你有待测项目的源码，那么直接查看源码就好。如果没有，那么请联系有源码的同学，这是推荐方法。

方法二

	如果你没有代码，那么可以反编译该app。
	这里将用到2个工具，分别是dex2jar和jd-gui。你可以在这里下载目前为止的最新版本以及示例apk。
	我们以工具包里的ContactManager.apk为例，简单介绍一下反编译的流程。
	1，重命名ContactManager.apk为ContactManager.zip并解压得到文件classes.dex；
	2，解压dex2jar-0.0.9.15.zip，并从命令行进入该文件夹；
	3，运行命令
		d2j-dex2jar.bat path_to\classes.dex
		在当前文件夹下得到classes-dex2jar.jar；
	4，解压jd-gui-0.3.6.windows.zip得到文件jd-gui.exe；
	5，使用jd-gui.exe打开classes-dex2jar.jar；
方法三

	使用log查看大法(嗯，windows上没grep不幸福，好在有powershell的Select-String，可以拿来勉强一用)，直接搬砖。

		a、启动待测apk
		b、开启日志输出：adb logcat>D:/log.txt
		c、关闭日志输出：ctrl+c
		d、查看日志
	找寻：

	Displayed com.mm.android.hsy/.ui.LoginActivity: +3s859ms
	appPackage = com.mm.android.hsy
	appActivity = .ui.LoginActivity