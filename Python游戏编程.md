#7.4
tips:

##1.Pygame
使用python开发游戏需要用到pygame
###1.1安装pygame
1. 官网https://www.pygame.org
2. 获取下载语句在本地cmd中安装

		py -m pip install -U pygame --user
		
	该句可以查看示例游戏

		py -m pygame.examples.aliens
3. 使用以下语句可查看安装的版本

		import pygame
		pygame.ver	
###1.2分析示例

	import pygame
	import sys
	pygame.init()			//初始化Pygame
	size = width, height = 600, 400
	speed = [-2, 1]
	bg = (255, 255, 255) # RGB
	screen = pygame.display.set_mode(size)			// 创建指定大小的窗口  返回Surface对象
	pygame.display.set_caption("初次见面，请大家多多关照！")		//设置标题
	turtle = pygame.image.load("turtle.png")			//加载图片，可使用较多的图片格式如png，jpg
	
	position = turtle.get_rect()		//获得图像的位置矩形
	while True:
	    for event in pygame.event.get():	//设置退出方法
	        if event.type == pygame.QUIT:
	            sys.exit()
	    
	    position = position.move(speed)		// 移动图像
	    if position.left < 0 or position.right > width:
	        
	        turtle = pygame.transform.flip(turtle, True, False)		// 翻转图像三个参数第一个表示哪个图片，第二个是否水平翻转，第三个表示是否垂直翻转
	        
	        speed[0] = -speed[0]  // 反方向移动
	    if position.top < 0 or position.bottom > height:
	        speed[1] = -speed[1]
	    
	    screen.fill(bg)# 填充背景
	    
	    screen.blit(turtle, position)		//更新图像
	   
	    pygame.display.flip() 		//更新界面
	    
	    pygame.time.delay(10)		//延迟10毫秒

- surface对象就是pygame中的图像的对象

##2.事件
1. 该实例创建一个文件并记录下在窗口中的操作

	import pygame
	import sys
	# 初始化Pygame
	pygame.init()
	size = width, height = 600, 400
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("初次见面，请大家多多关照！")
	f = open("read.txt",'w')
	while True:
	    for event in pygame.event.get():
	        f.write(str(event)+'\n')
	
	        if event.type == pygame.QUIT:
	            f.close()
	            sys.exit()
2. 实例2在页面上进行刷新显示

		import pygame
		import sys
		pygame.init()
		size = width, height = 600, 400
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")
		bg = (0,0,0)
		font = pygame.font.Font(None,20)
		line_height = font.get_linesize()
		position = 0
		screen.fill(bg)
		while True:
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            sys.exit()
		        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
		        position += line_height
		        if position>height:
		            position=0
		            screen.fill(bg)
		    pygame.display.flip()
3. 键盘对surface对象进行控制

		import pygame
		import sys
		from pygame.locals import *		//导入该模块这个模块包含了 Pygame 定义的各种常量。它的内容会被自动放入到 Pygame 模块的名字空间中
		# 初始化Pygame
		pygame.init()
		size = width, height = 600, 400
		speed = [-2, 1]
		bg = (255, 255, 255) # RGB
		# 创建指定大小的窗口 Surface
		screen = pygame.display.set_mode(size)
		# 设置窗口标题
		pygame.display.set_caption("初次见面，请大家多多关照！")
		# 加在图片
		turtle = pygame.image.load("turtle.png")
		# 获得图像的位置矩形
		position = turtle.get_rect()	//返回渲染文本的大小和偏移量
		l_head = turtle
		r_head = pygame.transform.flip(turtle, True, False)	//水平翻转图片
		d_head = pygame.transform.flip(turtle, false, True)	//垂直翻转
		while True:
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            sys.exit()
		        if event.type == KEYDOWN:
		            if event.key == K_LEFT:
		                turtle = l_head
		                speed = [-1, 0]
		            if event.key == K_RIGHT:
		                turtle = r_head
		                speed = [1, 0]
		            if event.key == K_UP:
						turtle = d_head
		                speed = [0, -1]
		            if event.key == K_DOWN:
						turtle = d_head
		                speed = [0, 1]
		    # 移动图像
		    position = position.move(speed)
		    if position.left < 0 or position.right > width:
		        # 翻转图像
		        turtle = pygame.transform.flip(turtle, True, False)
		        # 反方向移动
		        speed[0] = -speed[0]
		    if position.top < 0 or position.bottom > height:
		        speed[1] = -speed[1]
		    # 填充背景
		    screen.fill(bg)
		    # 更新图像
		    screen.blit(turtle, position)
		    # 更新界面
		    pygame.display.flip()
		    # 延迟10毫秒
		    pygame.time.delay(10)

#7.5

##1.提高游戏颜值display 
Pygame 中用于控制窗口和屏幕显示的模块。函数：

	pygame.display.init()  —  初始化 display 模块
	pygame.display.quit()  —  结束 display 模块
	pygame.display.get_init()  —  如果 display 模块已经初始化，返回 True
	pygame.display.set_mode()  —  初始化一个准备显示的窗口或屏幕
	pygame.display.get_surface()  —  获取当前显示的 Surface 对象
	pygame.display.flip()  —  更新整个待显示的 Surface 对象到屏幕上
	pygame.display.update()  —  更新部分软件界面显示
	pygame.display.get_driver()  —  获取 Pygame 显示后端的名字
	pygame.display.Info()  —  创建有关显示界面的信息对象
	pygame.display.get_wm_info()  —  获取关于当前窗口系统的信息
	pygame.display.list_modes()  —  获取全屏模式下可使用的分辨率
	pygame.display.mode_ok()  —  为显示模式选择最合适的颜色深度
	pygame.display.gl_get_attribute()  —  获取当前显示界面 OpenGL 的属性值
	pygame.display.gl_set_attribute()  —  设置当前显示模式的 OpenGL 属性值
	pygame.display.get_active()  —  当前显示界面显示在屏幕上时返回 True
	pygame.display.iconify()  —  最小化显示的 Surface 对象
	pygame.display.toggle_fullscreen()  —  切换全屏模式和窗口模式
	pygame.display.set_gamma()  —  修改硬件显示的 gama 坡道
	pygame.display.set_gamma_ramp()  —  自定义修改硬件显示的 gama 坡道
	pygame.display.set_icon()  —  修改显示窗口的图标
	pygame.display.set_caption()  —  Set the current window caption
	pygame.display.get_caption()  —  Get the current window caption
	pygame.display.set_palette()  —  Set the display color palette for indexed displays
函数详解：

	pygame.display.init()
	初始化 display 模块。
	init() -> None
	初始化 Pygame 的 display 模块。在初始化之前，display 模块无法做任何事情。但当你调用更高级别的 pygame.init()，变会自动调用 pygame.display.init() 进行初始化。
	初始化后，Pygame 将自动从几个内部的显示后端中选择一个。显示模式由平台和当前用户权限决定。在 display 模块被初始化之前，可以通过环境变量 SDL_VIDEODRIVER 设置哪一个显示后端将被使用。具有多种显示后端的系统如下：
		Windows : windib, directx
		Unix : x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib
	在一些平台上，可以将 Pygame 的 display 嵌入到已经存在的窗口中。如果这么做，环境变量 SDL_WINDOWID 必须被设置为一个包含窗口 ID 或句柄的字符串。当 Pygame 的 display 被初始化的时候，将检测环境变量。注意，在一个运行的窗口嵌入 display 会产生许多奇怪的副作用。
	多次调用该函数并没有任何问题，但也不会有什么效果。
	
	pygame.display.quit()
	结束 display 模块。
	quit() -> None
	这个函数会关闭整个 display 模块。这将意味着任何一个活跃的显示界面都将被关闭。当主程序退出时，该函数也会被自动调用。
	多次调用该函数并没有任何问题，但也不会有什么效果。
	
	pygame.display.get_init()
	如果 display 模块已经初始化，返回 True。

	get_init() -> bool
	如果 display 模块已经初始化，返回 True。
	
	pygame.display.set_mode()
	初始化一个准备显示的窗口或屏幕。
	set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
	这个函数将创建一个 Surface 对象的显示界面。传入的参数用于指定显示类型。最终创建出来的显示界面将是最大可能地匹配当前操作系统。
	resolution 参数是一个二元组，表示宽和高。flags 参数是附件选项的集合。depth 参数表示使用的颜色深度。
	返回的 Surface 对象可以像常规的 Surface 对象那样去绘制，但发生的改变最终会显示到屏幕上。
	如果没有传入 resolution 参数，或者使用默认设置 (0, 0)，且 Pygame 使用 SDL1.2.10 以上版本，那么创建出来的 Surface 对象将与当前屏幕用户一样的分辨率。如果只有宽或高其中一项被设置为 0，那么 Surface 对象将使用屏幕分辨率的宽或高代替它。如果 SDL 版本低于 1.2.10，那么将抛出异常。
	通常来说，最好的做法是不要传递 depth 参数。因为默认 Pygame 会根据当前操作系统选择最好和最快的颜色深度。如果你的游戏确实需要一个特殊的颜色格式，那么你可以通过控制 depth 参数来实现。Pygame 将为模拟一个非现成的颜色深度而耗费更多的时间。
	当使用全屏显示模式的时候，有时候无法完全匹配到需要的分辨率。在这种情况下，Pygame 将自动选择最匹配的分辨率使用，而返回的 Surface 对象将保持与需求的分辨率一致。
	flags 参数指定你想要的显示类型。提供几个选择给你，你可以通过位操作同时使用多个类型（管道操作符 "|"）。如果你传入 0 或没有传入 flags 参数，默认会使用软件驱动窗口。这儿是 flags 参数提供的几个可选项：
	
		选项		含义
		pygame.FULLSCREEN	创建一个全屏显示
		pygame.DOUBLEBUF	1. 双缓冲模式 
		2. 推荐和 HWSURFACE 或 OPENGL 一起使用
		pygame.HWSURFACE	硬件加速，只有在 FULLSCREEN 下可以使用
		pygame.OPENGL	创建一个 OPENGL 渲染的显示
		pygame.RESIZABLE	创建一个可调整尺寸的窗口
		pygame.NOFRAME	创建一个没有边框和控制按钮的窗口
	
		举个栗子：
		# 在屏幕中创建一个 700 * 400 的窗口
		screen_width=700
		screen_height=400
		screen=pygame.display.set_mode([screen_width, screen_height])

	pygame.display.get_surface()
	获取当前显示的 Surface 对象。
	
	get_surface() -> Surface
	返回当前显示的 Surface 对象。如果没有设置任何显示模式，那么返回 None。
	
	pygame.display.flip()
	更新整个待显示的 Surface 对象到屏幕上。
	
	flip() -> None
	这个函数将更新整个显示界面的内容。如果你的显示模式使用了 pygame.HWSURFACE（硬件加速）和 pygame.DOUBLEBUF（双缓冲）标志，那么将等待垂直会扫并切换显示界面。如果你使用不同类型的显示模式，那么它将简单的更新整个显示界面的内容。
	当使用 pygame.OPENGL（使用 OPENGL 渲染）显示模式时，将创建一个 gl 缓冲切换区。
	小甲鱼温馨提示：垂直回扫是与视频显示相关的时间测量，它代表了一个帧的结束和下一帧的开始时间之间的时间间隔。
	
	pygame.display.update()
	更新部分软件界面显示。
	
	update(rectangle=None) -> None
	
	update(rectangle_list) -> None
	这个函数可以看作是 pygame.display.flip() 函数在软件界面显示的优化版。它允许更新屏幕的部分内容，而不必完全更新。如果没有传入任何参数，那么该函数就像 pygame.display.flip() 那样更新整个界面。
	你可以传递一个或多个矩形区域给该函数。一次性传递多个矩形区域比多次传递更有效率。如果传入的是一个空列表或者 None，那么将忽略参数。
	该函数不能在 pygame.OPENGL 显示模式下调用，否则会抛出异常。
	
	pygame.display.get_driver()
	获取 Pygame 显示后端的名字。
	
	get_driver() -> name
	初始化的时候，Pygame 会从多个可用的显示后端中选择一个。这个函数返回显示后端内部使用的名字。可以用来提供有关显示性能加速的一些信息。可以参考 pygame.display.set_mode() 的 SDL_VIDEODRIVER 环境变量。	
	
	pygame.display.Info()
	创建有关显示界面的信息对象。
	
	Info() -> VideoInfo
	创建一个对象，包含对当前图形环境一些属性的描述。在一些平台上，如果这个函数在 pygame.display.set_mode() 前被调用，可以提供一些关于默认显示模式的信息。也可以在设置完显示模式后调用该函数，以确认显示选项是否如愿以偿。
	返回的 VideoInfo 对象包含以下这些属性：
		属性			含义
		hw	如果是 True，则表示启用硬件加速
		wm	如果是 True，则表示显示窗口模式
		video_mem	表示显存是多少兆字节（mb），0 表示不清楚
		bitsize	表示每个像素存放多少位
		bytesize	表示每个像素存放多少字节
		masks	4 个值用于打包像素的 RGBA 值
		shifts	4 个值用于打包像素的 RGBA 值
		losses	4 个值用于打包像素的 RGBA 值
		blit_hw	如果是 True，则表示加速硬件驱动的 Surface 对象绘制
		blit_hw_CC	如果是 True，则表示加速硬件驱动的 Surface 对象 colorkey 绘制
		blit_hw_A	如果是 True，则表示加速硬件驱动的 Surface 对象 pixel alpha 绘制
		blit_sw	如果是 True，则表示加速软件驱动的 Surface 对象绘制
		blit_sw_CC	如果是 True，则表示加速软件驱动的 Surface 对象 colorkey 绘制
		blit_sw_A	如果是 True，则表示加速软件驱动的 Surface 对象 pixel alpha 绘制
		current_w, current_h	1. 表示当前显示模式的宽和高（如果在 display.set_mode() 前被调用，则表示当前桌面的宽和高）
								2. current_w, current_h 在 Pygame 1.8.0 以后，SDL 1.2.10 以后才支持
								3. -1 表示错误，或者 SDL 版本太旧
	
	pygame.display.get_wm_info()
	获取关于当前窗口系统的信息。
	
	get_wm_info() -> dict
	创建一个由操作系统填充数据的字典。一些操作系统可能不会往里边填充信息，则返回一个空字典。大多数平台将返回一个 "window" 键，对应的值是当前显示界面的系统 ID。
	Pygame 1.7.1 新增加的。
	
	pygame.display.list_modes()
	获取全屏模式下可使用的分辨率。
	
	list_modes(depth=0, flags=pygame.FULLSCREEN) -> list
	这个函数返回一个列表，包含指定颜色深度所支持的所有分辨率。如果显示模式非全屏，则返回一个空列表。如果返回 -1 表示支持任何分辨率（类似于窗口模式）。返回的列表由大到小排列。
	如果颜色深度是 0，SDL 将选择当前/最合适的颜色深度显示。flags 参数默认值是 pygame.FULLSCREEN，但你可能需要添加额外的全屏模式标志。

	pygame.display.mode_ok()
	为显示模式选择最合适的颜色深度。
	
	mode_ok(size, flags=0, depth=0) -> depth
	这个函数使用与 pygame.display.set_mode() 函数一样的参数。一般用于判断一个显示模式是否可用。如果显示模式无法设置，则返回 0。正常情况下将会返回显示需求的像素深度。
	通常不用理会 depth 参数，除非一些支持多个显示深度的平台，它会提示哪个颜色深度是更合适的。
	最有用的 flags 参数是 pygame.HWSURFACE，pygame.DOUBLEBUF 和 pygame.FULLSCREEN。如果这些标志不支持，那么该函数会返回 0。
	
	pygame.display.gl_get_attribute()
	获取当前显示界面 OpenGL 的属性值。
	
	gl_get_attribute(flag) -> value
	在调用设置了 pygame.OPENGL 标志的 pygame.display.set_mode() 函数之后，检查 OpenGL 的属性值不失为一个好的习惯。参考 pygame.display.gl_set_attribute() 关于合法标志的列表。
	
	pygame.display.gl_set_attribute()
	设置当前显示模式的 OpenGL 属性值。
	
	gl_set_attribute(flag, value) -> None
	当调用设置了 pygame.OPENGL 标志的 pygame.display.set_mode() 函数时，Pygame 会自动设置 OpenGL 的一些属性值，例如颜色和双缓冲区。OpenGL 其实还提供了其他一些属性值供你控制。在 flag 参数中传入属性名，并将其值设置在 value 参数中。这个函数必须在 pygame.display.set_mode() 前设置。
	这些 OPENGL 标志是：
		GL_ALPHA_SIZE, GL_DEPTH_SIZE, GL_STENCIL_SIZE, GL_ACCUM_RED_SIZE,
		GL_ACCUM_GREEN_SIZE,  GL_ACCUM_BLUE_SIZE, GL_ACCUM_ALPHA_SIZE,
		GL_MULTISAMPLEBUFFERS, GL_MULTISAMPLESAMPLES, GL_STEREO
		
	pygame.display.get_active()	
	当前显示界面显示在屏幕上时返回 True。
	
	get_active() -> bool	
	pygame.display.set_mode() 函数被调用之后，Surface 对象将被显示在屏幕上。大多数窗口都支持隐藏，如果显示的 Surface 对象被隐藏和最小化，那么该函数将返回 False。
		
	pygame.display.iconify()	
	最小化显示的 Surface 对象。
	
	iconify() -> bool	
	将显示的 Surface 对象最小化或隐藏。并不是所有的操作系统都支持最小化显示界面。如果该函数调用成功，返回 True。	
	当显示界面最小化时，pygame.display.get_active() 返回 False。事件队列将接收到 ACTIVEEVENT 事件。
		
	pygame.display.toggle_fullscreen()	
	切换全屏模式和窗口模式。
	
	toggle_fullscreen() -> bool	
	切换全屏模式和窗口模式。这个函数只在 unix x11 显示驱动下工作。在大多数情况下，建议调用 pygame.display.set_mode() 创建一个新的显示模式进行切换。
		
	pygame.display.set_gamma()	
	修改硬件显示的 gama 坡道。
	
	set_gamma(red, green=None, blue=None) -> bool
	设置硬件驱动显示的红色、绿色和蓝色伽马值。如果没有传递 green 和 blue 参数，它们将与 red 值相等。不是所有的操作系统和硬件都支持伽马坡道。如果函数修改成功，则返回 True。
	伽马值为 1.0 创建一个线性颜色表，较低的值会使屏幕变暗，较高的值会使屏幕变量。
	
	pygame.display.set_gamma_ramp()
	自定义修改硬件显示的 gama 坡道
	
	set_gamma_ramp(red, green, blue) -> bool
	使用自定义表设置硬件驱动显示的红色、绿色和蓝色伽马坡道。每个参数必须是 256 位整数的列表。每位整数应该在 0 和 0xffff 之间。不是所有的操作系统和硬件都支持伽马坡道。如果函数修改成功，则返回 True。
	
	pygame.display.set_icon()
	修改显示窗口的图标。
	
	set_icon(Surface) -> None
	设置显示窗口执行时的图标。所有的操作系统默认都是以简单的 Pygame LOGO 作为图标。
	你可以传入任何 Surface 对象作为图标，但大多数操作系统要求图标的大小是 32 * 32。图标可以设置 colorkey 透明度。
	一些操作系统不允许修改显示中的窗口图标。对于这类操作系统，该函数需要再调用 pygame.display.set_mode() 前先创建并设置图标。
		
	pygame.display.set_caption()	
	设置当前窗口的标题栏。
	
	set_caption(title, icontitle=None) -> None	
	如果显示窗口拥有一个标题栏，这个函数将修改窗口标题栏的文本。一些操作系统支持最小化窗口时切换标题栏，通过设置 icontitle 参数实现。
	
	pygame.display.get_caption()	
	获取当前窗口的标题栏。
	
	get_caption() -> (title, icontitle)	
	返回当前窗口的标题栏和最小化标题栏，通常这两个值是一样的。	
	
	pygame.display.set_palette()	
	设置显示界面的调色板。
	
	set_palette(palette=None) -> None
	这个函数将修改显示界面的 8 位调色板。这不会改变 Surface 对象实际的调色板，仅用于 Surface 对象的显示。如果没有传入参数，将恢复系统默认调色板。调色板是一组 RGB 三元组序列。
- 使用display模块的set_mode()控制界面大小，返回surface对象

            # 按下F11全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1024, 768), FULLSCREEN | HWSURFACE)	//全屏显示和硬件加速
                else:
                    screen = pygame.display.set_mode(size)

- 查看当前屏幕分辨率

	在IDLE中，输入以下内容就可以看到自己显示器的分辨率

		>>> import pygame
		>>> pygame.init()            //使用pygame模块必须使用该句
		(6, 0)
		>>> pygame.display.list_modes()

- 用户调整窗口尺寸

		 if event.type == VIDEORESIZE:	
	            size = event.size
	            width, height = size
	            print(size)
	            screen = pygame.display.set_mode(size, RESIZABLE)		//创建一个可调整尺寸的窗口

- 将表面平滑地缩放到任意大小

	pygame.transform.smoothscale（Surface，（width，height），DestSurface = None） - > Surface

		# 设置放大缩小的比率
		ratio = 1.0
		....
			# 放大、缩小小乌龟（=、-），空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                # 最大只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle, \
                                             (int(oturtle_rect.width * ratio), \
                                             int(oturtle_rect.height * ratio)))
                l_head = turtle
                r_head = pygame.transform.flip(turtle, True, False)
- 旋转图像

	pygame.transform.rotate(Surface, angle)		//第一个参数是图像，第二个是旋转角度逆时针旋转如：90，180.270...

	示例：

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()# 初始化Pygame
		size = width, height = 600, 400
		bg = (255, 255, 255) # RGB
		fullscreen = False
		screen = pygame.display.set_mode(size)# 创建指定大小的窗口 Surface
		pygame.display.set_caption("初次见面，请大家多多关照！")# 设置窗口标题
		turtle = pygame.image.load("turtle.png")# 加在图片
		position = turtle.get_rect()# 获得图像的位置矩形
		speed = [5, 0]
		turtle_right = pygame.transform.rotate(turtle, 90)			//旋转图像
		turtle_top = pygame.transform.rotate(turtle, 180)
		turtle_left = pygame.transform.rotate(turtle, 270)
		turtle_bottom = turtle
		turtle = turtle_top
		l_head = turtle
		r_head = pygame.transform.flip(turtle, True, False)
		while True:
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            sys.exit()
		        if event.type == KEYDOWN:		            
		            if event.key == K_F11:# 全屏（F11）
		                fullscreen = not fullscreen
		                if fullscreen:
		                    screen = pygame.display.set_mode((1024, 768), FULLSCREEN | HWSURFACE)
		                else:
		                    screen = pygame.display.set_mode(size)
		    position = position.move(speed)# 移动图像
		    if position.right > width:
		        turtle = turtle_right
		        position = turtle_rect = turtle.get_rect()
		        position.left = width - turtle_rect.width
		        speed = [0, 5]
		    if position.bottom > height:
		        turtle = turtle_bottom
		        position = turtle_rect = turtle.get_rect()
		        position.left = width - turtle_rect.width
		        position.top = height - turtle_rect.height
		        speed = [-5, 0]
		    if position.left < 0:
		        turtle = turtle_left
		        position = turtle_rect = turtle.get_rect()
		        position.top = height - turtle_rect.height
		        speed = [0, -5]
		    if position.top < 0:
		        turtle = turtle_top
		        position = turtle_rect = turtle.get_rect()
		        speed = [5, 0]  
		    screen.fill(bg)# 填充背景
		    screen.blit(turtle, position)# 更新图像    
		    pygame.display.flip()# 更新界面
		    pygame.time.delay(10)# 延迟10毫秒
- 裁剪图片pygame.draw.rect（）

	rect（Surface，color，Rect，width = 0） - > Rect
		在Surface上绘制一个矩形形状。给定的Rect是矩形的区域。width参数是绘制外边缘的粗细。如果width为零，则填充矩形。Rect，表示包含实际绘制图形的矩形区域。
	capture = screen.subsurface(select_rect).copy()
		创建一个引用其父级的新表面并复制出来赋值给capture

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()		
		size = width, height = 800, 600
		bg = (255, 255, 255)	
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")	
		turtle = pygame.image.load("turtle.png")	
		# 0 -> 未选择，1 -> 选择中，2 -> 完成选择
		select = 0
		select_rect = pygame.Rect(0, 0, 0, 0)		
		# 0 -> 未拖拽，1 -> 拖拽中，2 -> 完成拖拽
		drag = 0	
		position = turtle.get_rect()
		position.center = width // 2, height // 2
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		        elif event.type == MOUSEBUTTONDOWN:
		            if event.button == 1:
		                # 第一次点击，选择范围
		                if select == 0 and drag == 0:
		                    pos_start = event.pos
		                    select = 1
		                # 第二次点击，推拽图像
		                elif select == 2 and drag == 0:
		                    capture = screen.subsurface(select_rect).copy()
		                    cap_rect = capture.get_rect()
		                    drag = 1
		                # 第三次点击，初始化
		                elif select == 2 and drag == 2:
		                    select = 0
		                    drag = 0
		        elif event.type == MOUSEBUTTONUP:
		            if event.button == 1:
		                # 第一次释放，结束选择
		                if select == 1 and drag == 0:
		                    pos_stop = event.pos
		                    select = 2
		                # 第二次释放，结束拖拽
		                if select == 2 and drag == 1:
		                    drag = 2      
		    screen.fill(bg)
		    screen.blit(turtle, position)
		    # 实时绘制选择框
		    if select:
		        mouse_pos = pygame.mouse.get_pos()
		        if select == 1:
		            pos_stop = mouse_pos
		
		        select_rect.left, select_rect.top = pos_start
		        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
		        pygame.draw.rect(screen, (0, 0, 0), select_rect,1)
		    # 拖拽裁剪的图像
		    if drag:
		        if drag == 1:
		            cap_rect.center = mouse_pos
		        screen.blit(capture, cap_rect)   
		    pygame.display.flip()
		    clock.tick(30)
- 图像相关

	更改图像的像素格式

		bg = pygame.image.load("bg.jpg").convert()	//更改图像的像素格式为Surface对象的像素格式RGB颜色
		turtle = pygame.image.load("turtle.png").convert_alpha()	//对于包含RGBA颜色中的A（透明）改变像素格式需用此方法

	示例1：

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()
		size = width, height = 640, 480
		bg = (0, 0, 0)
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")
		turtle = pygame.image.load("turtle.jpg").convert()		//转换像素对象格式
		background = pygame.image.load("background.jpg").convert()
		position = turtle.get_rect()
		position.center = width // 2, height // 2
		turtle.set_colorkey((255, 255, 255))	//设置当前颜色键
		turtle.set_alpha(200)		//设置透明度
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		    screen.blit(background, (0, 0))
		    screen.blit(turtle, position)
		    pygame.display.flip()
		    clock.tick(30)
	示例2：

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()	
		size = width, height = 640, 480
		bg = (0, 0, 0)	
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")
		turtle = pygame.image.load("turtle.png").convert_alpha()	//带有透明度的ＲＧＢＡ像素
		background  = pygame.image.load("background.jpg").convert()
		position = turtle.get_rect()
		position.center = width // 2, height // 2
		for i in range(position.width):		//遍历所有图像的像素
		    for j in range(position.height):
		        temp = turtle.get_at((i, j))		//get_at()获取单个像素的颜色值传入参数为像素位置
		        if temp[3] != 0:			//获取RGBA颜色，第四个为透明度
		            temp[3] = 200
		        turtle.set_at((i, j), temp)		//设置RGBA颜色
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		    screen.blit(background, (0, 0))
		    screen.blit(turtle, position)
		    pygame.display.flip()
		    clock.tick(30)
	示例3

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()		
		size = width, height = 640, 480
		bg = (0, 0, 0)		
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")		
		turtle = pygame.image.load("turtle.png").convert_alpha()
		background  = pygame.image.load("background.jpg").convert()
		position = turtle.get_rect()
		position.center = width // 2, height // 2		
		def blit_alpha(target, source, location, opacity):
		    x = location[0]
		    y = location[1]
		    temp = pygame.Surface((source.get_width(), source.get_height())).convert()	//创建不带Alpah的对象
		    temp.blit(target, (-x, -y ))
		    temp.blit(source, (0, 0))
		    temp.set_alpha(opacity)        
		    target.blit(temp, location)		
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()		
		    screen.blit(background, (0, 0))
		    blit_alpha(screen, turtle, position, 200)	    
		    pygame.display.flip()	    
		    clock.tick(30)

#7.6

##1.基本图形绘制
pygame.draw用于绘制形状的pygame模块

	pygame.draw.rect	-	画一个矩形的形状
	pygame.draw.polygon	-	画出任意数量的形状
	pygame.draw.circle	-	围绕一个点画一个圆圈
	pygame.draw.ellipse	-	在矩形内绘制圆形
	pygame.draw.arc		-	绘制椭圆的局部剖面
	pygame.draw.line	-	绘制一条直线段
	pygame.draw.lines	-	绘制多个连续的线段
	pygame.draw.aaline	-	绘制精细的抗锯齿线
	pygame.draw.aalines	-	绘制连接的抗锯齿线序列

- pygame.draw.rect（）画一个矩形的形状

		rect（Surface，color，Rect，width = 0） - > Rect
		surface表示绘制在哪个对象上，color指定对象的颜色，rect指定矩形的范围，width是绘制外边缘的粗细如果width为零则填充矩形

		import pygame
		import sys
		from pygame.locals import *		
		pygame.init()		
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)	
		size = width, height = 640, 200
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")	
		clock = pygame.time.Clock()	
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		    screen.fill(WHITE)	    
		    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)	//对象Rect四个参数(left, top, width, height)
		    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
		    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)
		    pygame.display.flip()		//将完整显示Surface从内存更新到屏幕
		    clock.tick(10)			//设置每秒钟绘制10次，将函数延迟使游戏运行速度低于每秒给定的帧数
- pygame.draw.polygon（）画多边形

		polygon（Surface，color，pointlist，width = 0） - > Rect		//第三个参数是多边形各个顶点的坐标，是一个列表

		import pygame
		import sys
		from pygame.locals import *
		pygame.init()
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)
		points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]
		size = width, height = 640, 200
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")
		clock = pygame.time.Clock()
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		    screen.fill(WHITE)  
		    pygame.draw.polygon(screen, GREEN, points, 0)
		    pygame.display.flip()
		    clock.tick(10)
- pygame.draw.circle（）围绕一个点画一个圆圈

		circle（Surface，color，pos，radius，width = 0） - > Rect
		pos参数是圆的中心，radius是大小

		import pygame
		import sys
		from pygame.locals import *	
		pygame.init()		
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		BLUE = (0, 0, 255)		
		size = width, height = 640, 480
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")		
		position = size[0]//2, size[1]//2
		moving = False		
		clock = pygame.time.Clock()		
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()	
		        if event.type == MOUSEBUTTONDOWN:
		            if event.button == 1:
		                moving = True	
		        if event.type == MOUSEBUTTONUP:
		            if event.button == 1:
		                moving = False
		    if moving:
		        position = pygame.mouse.get_pos()		//获得鼠标光标的位置并将其指定为圆心
		    screen.fill(WHITE)   
		    pygame.draw.circle(screen, RED, position, 25, 1)
		    pygame.draw.circle(screen, GREEN, position, 75, 1)
		    pygame.draw.circle(screen, BLUE, position, 125, 1)
		    pygame.display.flip()
		    clock.tick(120)
- pygame.draw.ellipse（）在矩形内绘制椭圆

		ellipse（Surface，color，Rect，width = 0） - > Rect
		在指定的矩形内绘制椭圆

		import pygame
		import sys
		from pygame.locals import *	
		pygame.init()	
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		BLUE = (0, 0, 255)
		size = width, height = 640, 300
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")	
		clock = pygame.time.Clock()	
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()	
		    screen.fill(WHITE)	    
		    pygame.draw.ellipse(screen, BLACK, (100, 100, 440, 100), 1)
		    pygame.draw.ellipse(screen, BLACK, (220, 50, 200, 200), 1)	
		    pygame.display.flip()	
		    clock.tick(120)
- pygame.draw.arc（）绘制弧线

		arc（Surface，color，Rect，start_angle，stop_angle，width = 1） - > Rect

		
		import pygame
		import sys
		import math
		from pygame.locals import *	
		pygame.init()
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		BLUE = (0, 0, 255)
		size = width, height = 640, 300
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")
		clock = pygame.time.Clock()
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()
		    screen.fill(WHITE)
		    pygame.draw.arc(screen, BLACK, (100, 100, 440, 100), 0, math.pi, 1)		//起始角度0终止角度180
		    pygame.draw.arc(screen, BLACK, (220, 50, 200, 200), math.pi, math.pi * 2, 1)		
		    pygame.display.flip()		
		    clock.tick(120)
- 绘制线段pygame.draw.line（）,pygame.draw.lines（）,pygame.draw.aaline（）,pygame.draw.aalines（）

		line（Surface，color，start_pos，end_pos，width = 1） - > Rect		//绘制一条线段
		lines(Surface, color, closed, pointlist, width=1) -> Rect		//绘制一系列线条,pointlist参数是一系列由一条线连接的点如果closed参数为true，则在第一个和最后一个点之间绘制一个额外的线段。
		aaline（Surface，color，startpos，endpos，blend = 1） - > Rect		//在曲面上绘制抗锯齿线。这将遵循剪裁矩形。受影响区域的边界框作为矩形返回。如果blend为true或1，则阴影将与现有像素阴影混合而不是覆盖它们。此函数接受端点的浮点值。
		aalines（Surface，color，closed，pointlist，blend = 1） - > Rect		//在表面上绘制序列。您必须在点序列中至少传递两个点。closed参数是一个简单的布尔值，如果为true，则在第一个和最后一个点之间绘制一条线。布尔混合参数设置为true会将阴影与现有阴影混合而不是覆盖它们。此函数接受端点的浮点值

		import pygame
		import sys
		from pygame.locals import *		
		pygame.init()		
		WHITE = (255, 255, 255)
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)		
		points = [(200, 75), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]	
		size = width, height = 640, 480
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("FishC Demo")	
		clock = pygame.time.Clock()	
		while True:
		    for event in pygame.event.get():
		        if event.type == QUIT:
		            sys.exit()	
		    screen.fill(WHITE)	    
		    pygame.draw.lines(screen, GREEN, 1, points, 1)		//第三个参数设置为1或True相同，0和false相同
		    pygame.draw.line(screen, BLACK, (100, 200), (540, 250), 1)
		    pygame.draw.aaline(screen, BLACK, (100, 250), (540, 300), 1)
		    pygame.draw.aaline(screen, BLACK, (100, 300), (540, 350), 0)	
		    pygame.display.flip()	
		    clock.tick(10)
##2.动画精灵
要使用动画精灵需要先继承pygame.sprite.Sprite，是基类

	import pygame
	import sys
	from pygame.locals import *
	from random import *
	class Ball(pygame.sprite.Sprite):
	    def __init__(self, image, position, speed, bg_size):
	        pygame.sprite.Sprite.__init__(self)		//初始化动画精灵，并调用__init__方法
	        self.image = pygame.image.load(image).convert_alpha()		//加载图片
	        self.rect = self.image.get_rect()		//获取尺寸
	        self.rect.left, self.rect.top = position
	        self.speed = speed
	        self.width, self.height = bg_size[0], bg_size[1]
	    def move(self):
	        self.rect = self.rect.move(self.speed)
	        if self.rect.right < 0:
	            self.rect.left = self.width
	        elif self.rect.left > self.width:
	            self.rect.right = 0
	        elif self.rect.bottom < 0:
	            self.rect.top = self.height
	        elif self.rect.top > self.height:
	            self.rect.bottom = 0
	def main():
	    pygame.init()
	    ball_image = "gray_ball.png"
	    bg_image = "background.png"
	    running = True
	    bg_size = width, height = 1024, 681
	    screen = pygame.display.set_mode(bg_size)	//初始化窗口
	    pygame.display.set_caption("Play the ball - FishC Demo")	//设置当前窗口标题
	    background = pygame.image.load(bg_image).convert_alpha()	//加载背景图片
	    balls = []
	    for i in range(5):
	        position = randint(0, width-100), randint(0, height-100)	//设置范围，以免出背景范围
	        speed = [randint(-10, 10), randint(-10, 10)]		
	        ball = Ball(ball_image, position, speed, bg_size)
	        balls.append(ball)
	    clock = pygame.time.Clock()		//刷新页面
	    while running:
	        for event in pygame.event.get():
	            if event.type == QUIT:
	                sys.exit()
	        screen.blit(background, (0, 0))	//将背景图加载到页面上
	        for each in balls:			//将每个球加载到页面上
	            each.move()
	            screen.blit(each.image, each.rect)
	        pygame.display.flip()		//刷新页面
	        clock.tick(30)		//设置每秒30帧
	if __name__ == "__main__":
	    main()

##3.碰撞体积
- 仅适用于圆与圆之间的碰撞检测

		import pygame
		import sys
		import math
		from pygame.locals import *
		from random import *
		# 球类继承自Spirte类
		class Ball(pygame.sprite.Sprite):
		    def __init__(self, image, position, speed, bg_size):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)
		        self.image = pygame.image.load(image).convert_alpha()
		        self.rect = self.image.get_rect()
		        # 将小球放在指定位置
		        self.rect.left, self.rect.top = position
		        self.speed = speed
		        self.width, self.height = bg_size[0], bg_size[1]
		    def move(self):
		        self.rect = self.rect.move(self.speed)
		        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界 这样便实现了从左边进入，右边出来的效果
		        if self.rect.right < 0:
		            self.rect.left = self.width
		        elif self.rect.left > self.width:
		            self.rect.right = 0
		        elif self.rect.bottom < 0:
		            self.rect.top = self.height
		        elif self.rect.top > self.height:
		            self.rect.bottom = 0
		def collide_check(item, target):		//该方法计算碰撞体积
		    col_balls = []
		    for each in target:
		        distance = math.sqrt(\			math.sqrt开平方，pow是几次幂，第一个参数是底数第二个是指数
		            math.pow((item.rect.center[0] - each.rect.center[0]), 2) + \
		            math.pow((item.rect.center[1] - each.rect.center[1]), 2))		//计算两物体中心点间距
		        if distance <= (item.rect.width + each.rect.width) / 2:			
		            col_balls.append(each)				//如果两中心点的间距小于等于两物体的平均半径则将该物体添加到列表中 
		    return col_balls
		def main():
		    pygame.init()
		    ball_image = "gray_ball.png"
		    bg_image = "background.png"
		    running = True
		    # 根据背景图片指定游戏界面尺寸
		    bg_size = width, height = 1024, 681
		    screen = pygame.display.set_mode(bg_size)
		    pygame.display.set_caption("Play the ball - FishC Demo")
		    background = pygame.image.load(bg_image).convert_alpha()
		    # 用来存放小球对象的列表
		    balls = []
		    # 创建五个小球
		    BALL_NUM = 5
		    for i in range(BALL_NUM):
		        # 位置随机，速度随机
		        position = randint(0, width-100), randint(0, height-100)		//随机生成一个位置
		        speed = [randint(-10, 10), randint(-10, 10)]		//随机生成一个速度
		        ball = Ball(ball_image, position, speed, bg_size)
		        while collide_check(ball, balls):		//如果一开始两球就碰撞了
		            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)		//重新分配位置
		        balls.append(ball)
		    clock = pygame.time.Clock()
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                sys.exit()        
		        screen.blit(background, (0, 0))
		        for each in balls:
		            each.move()
		            screen.blit(each.image, each.rect)
		        for i in range(BALL_NUM):
		            item = balls.pop(i)
		            if collide_check(item, balls):
		                item.speed[0] = -item.speed[0]
		                item.speed[1] = -item.speed[1]
		            balls.insert(i, item)
		        pygame.display.flip()
- 同样适用碰撞检测函数pygame.sprite.spritecollide（）也是需要继承pygame.sprite.Sprite

	spritecollide（sprite，group，dokill，collided = None） - > Sprite_list
	第一个参数指定被检测精灵，第二个是指定一个组（需要用sprite。Group（）生成的组），第三个参数是否从组中删除被监测的精灵，第四个回调函数指定额外的检测方法，如果为none检测精灵间的right属性
	collide_circle(left, right) -> bool		//检测两圆之间是否碰撞

		import pygame
		import sys
		from pygame.locals import *
		from random import *
		# 球类继承自Spirte类
		class Ball(pygame.sprite.Sprite):
		    def __init__(self, image, position, speed, bg_size):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)	
		        self.image = pygame.image.load(image).convert_alpha()
		        self.rect = self.image.get_rect()
		        # 将小球放在指定位置
		        self.rect.left, self.rect.top = position
		        self.speed = speed
		        self.width, self.height = bg_size[0], bg_size[1]
		        self.radius = self.rect.width / 2					//添加半径的精灵属性
		    def move(self):
		        self.rect = self.rect.move(self.speed)
		        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
		        # 这样便实现了从左边进入，右边出来的效果
		        if self.rect.right < 0:
		            self.rect.left = self.width
		        elif self.rect.left > self.width:
		            self.rect.right = 0
		        elif self.rect.bottom < 0:
		            self.rect.top = self.height
		        elif self.rect.top > self.height:
		            self.rect.bottom = 0 
		def main():
		    pygame.init()		
		    ball_image = "gray_ball.png"
		    bg_image = "background.png"	
		    running = True	
		    # 根据背景图片指定游戏界面尺寸
		    bg_size = width, height = 1024, 681
		    screen = pygame.display.set_mode(bg_size)
		    pygame.display.set_caption("Play the ball - FishC Demo")
		    background = pygame.image.load(bg_image).convert_alpha()
		    # 用来存放小球对象的列表
		    balls = []
		    group = pygame.sprite.Group()
		    # 创建五个小球
		    for i in range(5):
		        # 位置随机，速度随机
		        position = randint(0, width-100), randint(0, height-100)
		        speed = [randint(-10, 10), randint(-10, 10)]
		        ball = Ball(ball_image, position, speed, bg_size)
		        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):	//调用该方法检测是否碰撞
		            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
		        balls.append(ball)
		        group.add(ball)
		    clock = pygame.time.Clock()	
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                sys.exit()	            
		        screen.blit(background, (0, 0))	
		        for each in balls:
		            each.move()
		            screen.blit(each.image, each.rect)
		        for each in group:
		            group.remove(each)
		            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
		                each.speed[0] = -each.speed[0]
		                each.speed[1] = -each.speed[1]
		            group.add(each
		        pygame.display.flip()
		        clock.tick(30)
		if __name__ == "__main__":
		    main()
		
- 播放声音和音效

	- 播放音效支持wav格式，其他格式需转成改格式

			pygame.mixer.Sound()
				play()				-	开始播放声音
				stop()				-	停止声音播放
				fadeout()			-	淡出后停止声音播放
				set_volume()		-	设置此声音的播放音量
				get_volume()		-	获取播放音量
				get_num_channels()	-	计算此声音播放的次数
				get_length()		-	得到声音的长度
				get_raw()			-	将该音效以二进制格式的字符串返回
	- 播放背景音乐支持ogg格式

			pygame.mixer.music
				pygame.mixer.music.load()  ——  载入一个音乐文件用于播放
				pygame.mixer.music.play()  ——  开始播放音乐流
				pygame.mixer.music.rewind()  ——  重新开始播放音乐
				pygame.mixer.music.stop()  ——  结束音乐播放
				pygame.mixer.music.pause()  ——  暂停音乐播放
				pygame.mixer.music.unpause()  ——  恢复音乐播放
				pygame.mixer.music.fadeout()  ——  淡出的效果结束音乐播放
				pygame.mixer.music.set_volume()  ——  设置音量
				pygame.mixer.music.get_volume()  ——  获取音量
				pygame.mixer.music.get_busy()  ——  检查是否正在播放音乐
				pygame.mixer.music.set_pos()  ——  设置播放的位置
				pygame.mixer.music.get_pos()  ——  获取播放的位置
				pygame.mixer.music.queue()  ——  将一个音乐文件放入队列中，并排在当前播放的音乐之后
				pygame.mixer.music.set_endevent()  ——  当播放结束时发出一个事件
				pygame.mixer.music.get_endevent()  ——  获取播放结束时发送的事件
	- 示例1

			import pygame
			import sys
			from pygame.locals import *
			pygame.init()	
			pygame.mixer.init()		//初始化模块
			pygame.mixer.music.load("bg_music.ogg")		//加载背景音乐
			pygame.mixer.music.set_volume(0.2)			//设置音量
			pygame.mixer.music.play()			//开始播放
			cat_sound = pygame.mixer.Sound("cat.wav")		//加载猫的音效
			cat_sound.set_volume(0.2)		//设置音量
			dog_sound = pygame.mixer.Sound("dog.wav")
			dog_sound.set_volume(0.2)
			bg_size = width, height = 300, 200		//设置窗口
			screen = pygame.display.set_mode(bg_size)		//设置界面
			pygame.display.set_caption("Music - FishC Demo")		//设置标题
			pause = False		//表示是否暂停
			pause_image = pygame.image.load("pause.png").convert_alpha()
			unpause_image = pygame.image.load("unpause.png").convert_alpha()		//加载两张图片
			pause_rect = pause_image.get_rect()
			pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2
			clock = pygame.time.Clock()
			while True:
			    for event in pygame.event.get():
			        if event.type == QUIT:
			            sys.exit()
			        if event.type == MOUSEBUTTONDOWN:	
			            if event.button == 1:		//点击鼠标左键播放猫叫
			                cat_sound.play()
			            if event.button == 3:
			                dog_sound.play()		//点击右键播放狗叫
			        if event.type == KEYDOWN:
			            if event.key == K_SPACE:			//按下空格将pause取反
			                pause = not pause
			    screen.fill((255, 255, 255))
			    if pause:		//如果暂停，绘制暂停按钮并暂停播放音乐
			        screen.blit(pause_image, pause_rect)
			        pygame.mixer.music.pause()
			    else:
			        screen.blit(unpause_image, pause_rect)
			        pygame.mixer.music.unpause()
			    pygame.display.flip()	//刷新页面
			    clock.tick(30)		//没秒30帧

		- 示例2

				import pygame
				import sys
				from pygame.locals import *
				from random import *
				# 球类继承自Spirte类
				class Ball(pygame.sprite.Sprite):
				    def __init__(self, image, position, speed, bg_size):
				        # 初始化动画精灵
				        pygame.sprite.Sprite.__init__(self)
				
				        self.image = pygame.image.load(image).convert_alpha()
				        self.rect = self.image.get_rect()
				        # 将小球放在指定位置
				        self.rect.left, self.rect.top = position
				        self.speed = speed
				        self.width, self.height = bg_size[0], bg_size[1]
				        self.radius = self.rect.width / 2
				    def move(self):
				        self.rect = self.rect.move(self.speed)
				        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
				        # 这样便实现了从左边进入，右边出来的效果
				        if self.rect.right < 0:
				            self.rect.left = self.width
				        elif self.rect.left > self.width:
				            self.rect.right = 0
				        elif self.rect.bottom < 0:
				            self.rect.top = self.height
				        elif self.rect.top > self.height:
				            self.rect.bottom = 0
				def main():
				    pygame.init()
				    ball_image = "gray_ball.png"
				    bg_image = "background.png"
				    running = True
				    # 添加魔性的背景音乐
				    pygame.mixer.music.load("bg_music.ogg")
				    pygame.mixer.music.play()
				    # 添加音效
				    loser_sound = pygame.mixer.Sound("loser.wav")
				    laugh_sound = pygame.mixer.Sound("laugh.wav")
				    winner_sound = pygame.mixer.Sound("winner.wav")
				    hole_sound = pygame.mixer.Sound("hole.wav")
				    # 音乐播放完时游戏结束
				    GAMEOVER = USEREVENT
				    pygame.mixer.music.set_endevent(GAMEOVER)
				    # 根据背景图片指定游戏界面尺寸
				    bg_size = width, height = 1024, 681
				    screen = pygame.display.set_mode(bg_size)
				    pygame.display.set_caption("Play the ball - FishC Demo")
				    background = pygame.image.load(bg_image).convert_alpha()
				    # 用来存放小球对象的列表
				    balls = []
				    group = pygame.sprite.Group()
				    # 创建五个小球
				    for i in range(5):
				        # 位置随机，速度随机
				        position = randint(0, width-100), randint(0, height-100)
				        speed = [randint(-10, 10), randint(-10, 10)]
				        ball = Ball(ball_image, position, speed, bg_size)
				        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
				            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
				        balls.append(ball)
				        group.add(ball)
				    clock = pygame.time.Clock()
				    while running:
				        for event in pygame.event.get():
				            if event.type == QUIT:
				                sys.exit()
				            elif event.type == GAMEOVER:
				                loser_sound.play()		//游戏结束播放失败音乐
				                pygame.time.delay(2000)	//暂停两秒
				                laugh_sound.play()		//播放嘲笑音乐
				                running = False		//跳出循环
				        screen.blit(background, (0, 0))
				        for each in balls:
				            each.move()
				            screen.blit(each.image, each.rect)
				        for each in group:
				            group.remove(each)
				            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
				                each.speed[0] = -each.speed[0]
				                each.speed[1] = -each.speed[1]
				            group.add(each)
				        pygame.display.flip()
				        clock.tick(30)
				if __name__ == "__main__":
				    main()

- 显示玻璃面板

		import pygame
		import sys
		from pygame.locals import *
		from random import *
		# 球类继承自Spirte类
		class Ball(pygame.sprite.Sprite):
		    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)
		        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
		        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
		        self.rect = self.grayball_image.get_rect()
		        # 将小球放在指定位置
		        self.rect.left, self.rect.top = position
		        self.speed = speed
		        self.target = target
		        self.control = False
		        self.width, self.height = bg_size[0], bg_size[1]
		        self.radius = self.rect.width / 2
		    def move(self):
		        self.rect = self.rect.move(self.speed)
		        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
		        # 这样便实现了从左边进入，右边出来的效果
		        if self.rect.right < 0:
		            self.rect.left = self.width
		        elif self.rect.left > self.width:
		            self.rect.right = 0
		        elif self.rect.bottom < 0:
		            self.rect.top = self.height
		        elif self.rect.top > self.height:
		            self.rect.bottom = 0
		    def check(self, motion):		//判断鼠标在1秒钟时间内产生的事件数量匹配是否此目标
		        if self.target < motion < self.target + 5:
		            return True
		        else:
		            return False
		class Glass(pygame.sprite.Sprite):
		    def __init__(self, glass_image, mouse_image, bg_size):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)
		        self.glass_image = pygame.image.load(glass_image).convert_alpha()		//加载玻璃图片
		        self.glass_rect = self.glass_image.get_rect()		//获取图片矩形位置
		        self.glass_rect.left, self.glass_rect.top =(bg_size[0] - self.glass_rect.width) // 2,bg_size[1] - self.glass_rect.height		//设置图片矩形位置
		        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()	//设置鼠标图片
		        self.mouse_rect = self.mouse_image.get_rect()
		        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top	//设置鼠标位置
		        pygame.mouse.set_visible(False)		//将原鼠标设置为不可见
		def main():
		    pygame.init()
		    grayball_image = "gray_ball.png"
		    greenball_image = "green_ball.png"
		    glass_image = "glass.png"
		    mouse_image = "hand.png"
		    bg_image = "background.png"
		    running = True
		    # 添加魔性的背景音乐
		    pygame.mixer.music.load("bg_music.ogg")
		    pygame.mixer.music.play()
		    # 添加音效
		    loser_sound = pygame.mixer.Sound("loser.wav")
		    laugh_sound = pygame.mixer.Sound("laugh.wav")
		    winner_sound = pygame.mixer.Sound("winner.wav")
		    hole_sound = pygame.mixer.Sound("hole.wav")
		    # 音乐播放完时游戏结束
		    GAMEOVER = USEREVENT
		    pygame.mixer.music.set_endevent(GAMEOVER)
		    # 根据背景图片指定游戏界面尺寸
		    bg_size = width, height = 1024, 681
		    screen = pygame.display.set_mode(bg_size)
		    pygame.display.set_caption("Play the ball - FishC Demo")
		    background = pygame.image.load(bg_image).convert_alpha()
		    # 用来存放小球对象的列表
		    balls = []
		    group = pygame.sprite.Group()
		    # 创建五个小球
		    for i in range(5):
		        # 位置随机，速度随机
		        position = randint(0, width-100), randint(0, height-100)
		        speed = [randint(-10, 10), randint(-10, 10)]
		        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i+1))
		        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
		            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
		        balls.append(ball)
		        group.add(ball)
		    glass = Glass(glass_image, mouse_image, bg_size)	//创建玻璃面板实例
		    motion = 0		//记录鼠标每一秒钟产生的事件数量
		    MYTIMER = USEREVENT + 1
		    pygame.time.set_timer(MYTIMER, 1000)
		    clock = pygame.time.Clock()
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                sys.exit()
		            elif event.type == GAMEOVER:
		                loser_sound.play()
		                pygame.time.delay(2000)
		                laugh_sound.play()
		                running = False
		            elif event.type == MYTIMER:
		                if motion:
		                    for each in group:
		                        if each.check(motion):
		                            each.speed = [0, 0]
		                            each.control = True
		                    motion = 0
		            elif event.type == MOUSEMOTION:
		                motion += 1
		        screen.blit(background, (0, 0))
		        screen.blit(glass.glass_image, glass.glass_rect)	//加载玻璃面板设置到screen上
		        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()	//获取鼠标位置并设置给图标位置
		        if glass.mouse_rect.left < glass.glass_rect.left:	//限制鼠标位置在玻璃面板内
		            glass.mouse_rect.left = glass.glass_rect.left
		        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
		            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
		        if glass.mouse_rect.top < glass.glass_rect.top:
		            glass.mouse_rect.top = glass.glass_rect.top
		        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
		            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height
		        screen.blit(glass.mouse_image, glass.mouse_rect)	//将鼠标设置到页面上
		        for each in balls:
		            each.move()
		            if each.control:
		                screen.blit(each.greenball_image, each.rect)
		            else:
		                screen.blit(each.grayball_image, each.rect)
		        for each in group:
		            group.remove(each)
		            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
		                each.speed[0] = -each.speed[0]
		                each.speed[1] = -each.speed[1]
		            group.add(each)
		        pygame.display.flip()
		        clock.tick(30)
		if __name__ == "__main__":
		    main()

- 响应相关事件

		import pygame
		import sys
		import traceback
		from pygame.locals import *
		from random import *
		# 球类继承自Spirte类
		class Ball(pygame.sprite.Sprite):
		    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)
		        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
		        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
		        self.rect = self.grayball_image.get_rect()
		        # 将小球放在指定位置
		        self.rect.left, self.rect.top = position
		        self.side = [choice([-1, 1]), choice([-1, 1])]
		        self.speed = speed
		        self.collide = False
		        self.target = target
		        self.control = False
		        self.width, self.height = bg_size[0], bg_size[1]
		        self.radius = self.rect.width / 2
		    def move(self):
		        if self.control:
		            self.rect = self.rect.move(self.speed)
		        else:
		            self.rect = self.rect.move((self.side[0] * self.speed[0], \
		                                        self.side[1] * self.speed[1]))
		
		        # 如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
		        # 这样便实现了从左边进入，右边出来的效果
		        if self.rect.right <= 0:
		            self.rect.left = self.width
		        elif self.rect.left >= self.width:
		            self.rect.right = 0
		        elif self.rect.bottom <= 0:
		            self.rect.top = self.height
		        elif self.rect.top >= self.height:
		            self.rect.bottom = 0
		    def check(self, motion):
		        if self.target < motion < self.target + 5:
		            return True
		        else:
		            return False
		class Glass(pygame.sprite.Sprite):
		    def __init__(self, glass_image, mouse_image, bg_size):
		        # 初始化动画精灵
		        pygame.sprite.Sprite.__init__(self)
		        self.glass_image = pygame.image.load(glass_image).convert_alpha()
		        self.glass_rect = self.glass_image.get_rect()
		        self.glass_rect.left, self.glass_rect.top = \
		                             (bg_size[0] - self.glass_rect.width) // 2, \
		                             bg_size[1] - self.glass_rect.height
		        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
		        self.mouse_rect = self.mouse_image.get_rect()
		        self.mouse_rect.left, self.mouse_rect.top = \
		                              self.glass_rect.left, self.glass_rect.top
		        pygame.mouse.set_visible(False)
		def main():
		    pygame.init()
		    grayball_image = "gray_ball.png"
		    greenball_image = "green_ball.png"
		    glass_image = "glass.png"
		    mouse_image = "hand.png"
		    bg_image = "background.png"
		    running = True
		    # 添加魔性的背景音乐
		    pygame.mixer.music.load("bg_music.ogg")
		    pygame.mixer.music.play()
		    # 添加音效
		    loser_sound = pygame.mixer.Sound("loser.wav")
		    laugh_sound = pygame.mixer.Sound("laugh.wav")
		    winner_sound = pygame.mixer.Sound("winner.wav")
		    hole_sound = pygame.mixer.Sound("hole.wav")
		    # 音乐播放完时游戏结束
		    GAMEOVER = USEREVENT
		    pygame.mixer.music.set_endevent(GAMEOVER)
		    # 根据背景图片指定游戏界面尺寸
		    bg_size = width, height = 1024, 681
		    screen = pygame.display.set_mode(bg_size)
		    pygame.display.set_caption("Play the ball - FishC Demo")
		    background = pygame.image.load(bg_image).convert_alpha()
		    # 5 个坑的范围，因为 100% 命中太难，所以只要在范围内即可
		    # 每个元素：(x1, x2, y1, y2)
		    hole = [(117, 119, 199, 201), (225, 227, 390, 392), \
		            (503, 505, 320, 322), (698, 700, 192, 194), \
		            (906, 908, 419, 421)]
		    # 存放要打印的消息
		    msgs = []
		    # 用来存放小球对象的列表
		    balls = []
		    group = pygame.sprite.Group()
		    # 创建 5 个小球
		    for i in range(5):
		        # 位置随机，速度随机
		        position = randint(0, width-100), randint(0, height-100)
		        speed = [randint(1, 10), randint(1, 10)]
		        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i+1))
		        # 检测新诞生的球是否会卡住其他球
		        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
		            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
		        balls.append(ball)
		        group.add(ball)
		    # 生成摩擦摩擦的玻璃面板
		    glass = Glass(glass_image, mouse_image, bg_size)
		    # motion 记录鼠标在玻璃面板产生的事件数量
		    motion = 0
		    # 1 秒检查 1 次鼠标摩擦摩擦产生的事件数量
		    MYTIMER = USEREVENT + 1
		    pygame.time.set_timer(MYTIMER, 1000)
		    # 设置持续按下键盘的重复响应
		    pygame.key.set_repeat(100, 100)
		    clock = pygame.time.Clock()
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                pygame.quit()
		                sys.exit()
		            # 游戏失败
		            elif event.type == GAMEOVER:
		                loser_sound.play()
		                pygame.time.delay(2000)
		                laugh_sound.play()
		                running = False
		            # 1 秒检查 1 次鼠标摩擦摩擦产生的事件数量
		            elif event.type == MYTIMER:
		                if motion:
		                    for each in group:
		                        if each.check(motion):
		                            each.speed = [0, 0]
		                            each.control = True
		                    motion = 0
		            elif event.type == MOUSEMOTION:
		                motion += 1
		            # 当小球的 control 属性为 True 时
		            # 可是使用按键 w、s、a、d 分别上、下、左、右移动小球
		            # 带加速度的哦^_^
		            elif event.type == KEYDOWN:
		                if event.key == K_w:
		                    for each in group:
		                        if each.control:
		                            each.speed[1] -= 1
		                if event.key == K_s:
		                    for each in group:
		                        if each.control:
		                            each.speed[1] += 1
		                if event.key == K_a:
		                    for each in group:
		                        if each.control:
		                            each.speed[0] -= 1
		                if event.key == K_d:
		                    for each in group:
		                        if each.control:
		                            each.speed[0] += 1
		                if event.key == K_SPACE:
		                    # 判断小球是否在坑内
		                    for each in group:
		                        if each.control:
		                            for i in hole:
		                                if i[0] <= each.rect.left <= i[1] and \
		                                   i[2] <= each.rect.top <= i[3]:
		                                    # 播放音效
		                                    hole_sound.play()
		                                    each.speed = [0, 0]
		                                    # 从 group 中移出，这样其他球就会忽视它
		                                    group.remove(each)
		                                    # 放到 balls 列表中的最前，也就是第一个绘制的球
		                                    # 这样当球在坑里时，其它球会从它上边过去，而不是下边
		                                    temp = balls.pop(balls.index(each))
		                                    balls.insert(0, temp)
		                                    # 一个坑一个球
		                                    hole.remove(i)
		                            # 坑都补完了，游戏结束
		                            if not hole:
		                                pygame.mixer.music.stop()
		                                winner_sound.play()
		                                pygame.time.delay(3000)
		                                # 打印“然并卵”
		                                msg = pygame.image.load("win.png").convert_alpha()
		                                msg_pos = (width - msg.get_width()) // 2, \
		                                          (height - msg.get_height()) // 2
		                                msgs.append((msg, msg_pos))
		                                laugh_sound.play()
		        screen.blit(background, (0, 0))
		        screen.blit(glass.glass_image, glass.glass_rect)
		        # 限制鼠标只能在玻璃内摩擦摩擦
		        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
		        if glass.mouse_rect.left < glass.glass_rect.left:
		            glass.mouse_rect.left = glass.glass_rect.left
		        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
		            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
		        if glass.mouse_rect.top < glass.glass_rect.top:
		            glass.mouse_rect.top = glass.glass_rect.top
		        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
		            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height
		        screen.blit(glass.mouse_image, glass.mouse_rect)
		        for each in balls:
		            each.move()
		            if each.collide:
		                each.speed = [randint(1, 10), randint(1, 10)]
		                each.collide = False
		            if each.control:
		                screen.blit(each.greenball_image, each.rect)
		            else:
		                screen.blit(each.grayball_image, each.rect)
		        for each in group:
		            # 先从组中移出当前球
		            group.remove(each)
		            # 判断当前球与其他球是否相撞
		            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
		                each.side[0] = -each.side[0]
		                each.side[1] = -each.side[1]
		                each.collide = True
		                if each.control:
		                    each.side[0] = -1
		                    each.side[1] = -1
		                    each.control = False
		            # 将当前球添加回组中
		            group.add(each)
		        for msg in msgs:
		            screen.blit(msg[0], msg[1])
		        pygame.display.flip()
		        clock.tick(30)
		if __name__ == "__main__":
		    # 这样做的好处是双击打开时如果出现异常可以报告异常，而不是一闪而过！
		    try:
		        main()
		    except SystemExit:
		        pass
		    except:
		        traceback.print_exc()
		        pygame.quit()
		        input()

#7.8

##1.实战，飞机大战
###1.1加载声音等资源

	# main.py
	import pygame		//导入游戏模块
	import sys			//访问系统特定的参数和功能
	import traceback	//处理异常栈
	import myplane		
	import bullet
	import enemy
	import supply
	from pygame.locals import *		//该模块包含pygame使用的各种常量
	from random import *	//随机数模块
	pygame.init()	//初始化pygame模块
	pygame.mixer.init()		//初始化mixer模块
	bg_size = width, height = 480, 700		//设置背景尺寸
	screen = pygame.display.set_mode(bg_size)		//初始化窗口或屏幕以进行显示
	pygame.display.set_caption("飞机大战 -- FishC Demo")		//设置当前窗口标题
	background = pygame.image.load("images/background.png").convert()	//加载背景图片并更改像素格式
	# 载入游戏音乐
	pygame.mixer.music.load("sound/game_music.ogg")		//加载音乐设置音量
	pygame.mixer.music.set_volume(0.2)
	bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
	bullet_sound.set_volume(0.2)
	bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
	bomb_sound.set_volume(0.2)
	supply_sound = pygame.mixer.Sound("sound/supply.wav")
	supply_sound.set_volume(0.2)
	get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
	get_bomb_sound.set_volume(0.2)
	get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
	get_bullet_sound.set_volume(0.2)
	upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
	upgrade_sound.set_volume(0.2)
	enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
	enemy3_fly_sound.set_volume(0.2)
	enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
	enemy1_down_sound.set_volume(0.1)
	enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
	enemy2_down_sound.set_volume(0.2)
	enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
	enemy3_down_sound.set_volume(0.5)
	me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
	me_down_sound.set_volume(0.2)
	
	def main():
	    pygame.mixer.music.play(-1)		//传入-1设置音乐无限循环
	    clock = pygame.time.Clock()		//创建一个对象跟踪事件
	    running = True
	    while running:
	        for event in pygame.event.get():
	            if event.type == QUIT:
	                pygame.quit()
	                sys.exit()
	        screen.blit(background, (0, 0))	
	        pygame.display.flip()		//更新屏幕
	        clock.tick(60)		//设置帧数60
	        
	if __name__ == "__main__":
	    try:
	        main()
	    except SystemExit:
	        pass
	    except:
	        traceback.print_exc()
	        pygame.quit()
	        input()
##1.2设置我方飞机

	import pygame
	class MyPlane(pygame.sprite.Sprite):
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
	        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
	        self.rect = self.image1.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.rect.left, self.rect.top = \
	                        (self.width - self.rect.width) // 2, \
	                        self.height - self.rect.height - 60
	        self.speed = 10
	    def moveUp(self):
	        if self.rect.top > 0:
	            self.rect.top -= self.speed
	        else:
	            self.rect.top = 0
	    def moveDown(self):
	        if self.rect.bottom < self.height - 60:
	            self.rect.top += self.speed
	        else:
	            self.rect.bottom = self.height - 60
	    def moveLeft(self):
	        if self.rect.left > 0:
	            self.rect.left -= self.speed
	        else:
	            self.rect.left = 0
	    def moveRight(self):
	        if self.rect.right < self.width:
	            self.rect.left += self.speed
	        else:
	            self.rect.right = self.width
	
##1.3设置敌机

	import pygame
	from random import *
	class SmallEnemy(pygame.sprite.Sprite):	//设置小敌机
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)		//调用父类构造函数
	        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 2
	        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	    def reset(self):
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-5 * self.height, 0)
	class MidEnemy(pygame.sprite.Sprite):		//设置中型敌机
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	    def reset(self):
	        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),randint(-10 * self.height, -self.height)
	class BigEnemy(pygame.sprite.Sprite):		//设置大型敌机
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
	        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
	        self.rect = self.image1.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height, -5 * self.height)
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	    def reset(self):
	        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),randint(-15 * self.height, -5 * self.height)
##1.4在main方法中添加我方飞机和敌方飞机

	# main.py
	import pygame
	import sys
	import traceback
	import myplane
	import enemy
	
	from pygame.locals import *
	from random import *
	
	pygame.init()
	pygame.mixer.init()
	
	bg_size = width, height = 480, 700
	screen = pygame.display.set_mode(bg_size)
	pygame.display.set_caption("飞机大战 -- FishC Demo")
	
	background = pygame.image.load("images/background.png").convert()
	
	# 载入游戏音乐
	.....
	def add_small_enemies(group1, group2, num):
	    for i in range(num):
	        e1 = enemy.SmallEnemy(bg_size)
	        group1.add(e1)
	        group2.add(e1)
	
	def add_mid_enemies(group1, group2, num):
	    for i in range(num):
	        e2 = enemy.MidEnemy(bg_size)
	        group1.add(e2)
	        group2.add(e2)
	
	def add_big_enemies(group1, group2, num):
	    for i in range(num):
	        e3 = enemy.BigEnemy(bg_size)
	        group1.add(e3)
	        group2.add(e3)
	        	
	def main():
	    pygame.mixer.music.play(-1)
	    # 生成我方飞机
	    me = myplane.MyPlane(bg_size)
	    enemies = pygame.sprite.Group()
	    # 生成敌方小型飞机
	    small_enemies = pygame.sprite.Group()
	    add_small_enemies(small_enemies, enemies, 15)
	    # 生成敌方中型飞机
	    mid_enemies = pygame.sprite.Group()
	    add_mid_enemies(mid_enemies, enemies, 4)
	    # 生成敌方大型飞机
	    big_enemies = pygame.sprite.Group()
	    add_big_enemies(big_enemies, enemies, 2)
	    clock = pygame.time.Clock()
	    # 用于切换图片
	    switch_image = True
	    # 用于延迟
	    delay = 100
	    running = True
	    while running:
	        for event in pygame.event.get():
	            if event.type == QUIT:
	                pygame.quit()
	                sys.exit()
	        # 检测用户的键盘操作
	        key_pressed = pygame.key.get_pressed()
	        if key_pressed[K_w] or key_pressed[K_UP]:
	            me.moveUp()     
	        if key_pressed[K_s] or key_pressed[K_DOWN]:
	            me.moveDown()
	        if key_pressed[K_a] or key_pressed[K_LEFT]:
	            me.moveLeft()
	        if key_pressed[K_d] or key_pressed[K_RIGHT]:
	            me.moveRight()
	        screen.blit(background, (0, 0))
	        # 绘制大型敌机
	        for each in big_enemies:
	            each.move()
	            if switch_image:
	                screen.blit(each.image1, each.rect)
	            else:
	                screen.blit(each.image2, each.rect)
	            # 即将出现在画面中，播放音效
	            if each.rect.bottom > -50:
	                enemy3_fly_sound.play()
	        # 绘制中型敌机：
	        for each in mid_enemies:
	            each.move()
	            screen.blit(each.image, each.rect)
	        # 绘制小型敌机：
	        for each in small_enemies:
	            each.move()
	            screen.blit(each.image, each.rect)
	        # 绘制我方飞机
	        if switch_image:
	            screen.blit(me.image1, me.rect)
	        else:
	            screen.blit(me.image2, me.rect)
	        # 切换图片
	        if not(delay % 5):
	            switch_image = not switch_image
	        delay -= 1
	        if not delay:
	            delay = 100
	        pygame.display.flip()
	        clock.tick(60) 
	if __name__ == "__main__":
	    try:
	        main()
	    except SystemExit:
	        pass
	    except:
	        traceback.print_exc()
	        pygame.quit()
	        input()
##1.5设置碰撞爆炸样式

	import pygame
	from random import *
	class SmallEnemy(pygame.sprite.Sprite):
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        #设置加载小飞机损毁画面
	        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
	        self.destroy_images = []
	        self.destroy_images.extend([\
	            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down4.png").convert_alpha() \
	            ])
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 2
	        #设置存活参数为true，然后在碰撞事件中将其设置为false然后调用reset重新创建
	        self.active = True
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-5 * self.height, 0)
	        self.mask = pygame.mask.from_surface(self.image)
	
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	
	    def reset(self):
	        self.active = True
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-5 * self.height, 0)
	class MidEnemy(pygame.sprite.Sprite):
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        #设置中等飞机损毁画面
	        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
	        self.destroy_images = []
	        self.destroy_images.extend([\
	            pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down4.png").convert_alpha() \
	            ])
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.active = True
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-10 * self.height, -self.height)
	        self.mask = pygame.mask.from_surface(self.image)
	
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	
	    def reset(self):
	        self.active = True      
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-10 * self.height, -self.height)
	class BigEnemy(pygame.sprite.Sprite):
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        #设置大型敌机损毁画面
	        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
	        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
	        self.destroy_images = []
	        self.destroy_images.extend([\
	            pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down6.png").convert_alpha() \
	            ])
	        self.rect = self.image1.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.active = True
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-15 * self.height, -5 * self.height)
	        self.mask = pygame.mask.from_surface(self.image1)
	
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	
	    def reset(self):
	        self.active = True
	        self.rect.left, self.rect.top = \
	                        randint(0, self.width - self.rect.width), \
	                        randint(-15 * self.height, -5 * self.height)
- 在主函数中判断是否碰撞碰撞的话响应相关事件

		# main.py
		import pygame
		import sys
		import traceback
		import myplane
		import enemy
		from pygame.locals import *
		from random import *
		
		pygame.init()
		pygame.mixer.init()
		bg_size = width, height = 480, 700
		screen = pygame.display.set_mode(bg_size)
		pygame.display.set_caption("飞机大战 -- FishC Demo")
		background = pygame.image.load("images/background.png").convert()
		# 载入游戏音乐
		......
		
		def main():
		    pygame.mixer.music.play(-1)
		
		    # 生成我方飞机
		    me = myplane.MyPlane(bg_size)
		    enemies = pygame.sprite.Group()
		    # 生成敌方小型飞机
		    small_enemies = pygame.sprite.Group()
		    add_small_enemies(small_enemies, enemies, 15)
		    # 生成敌方中型飞机
		    mid_enemies = pygame.sprite.Group()
		    add_mid_enemies(mid_enemies, enemies, 4)
		    # 生成敌方大型飞机
		    big_enemies = pygame.sprite.Group()
		    add_big_enemies(big_enemies, enemies, 2)
		    clock = pygame.time.Clock()
		    # 中弹图片索引
		    e1_destroy_index = 0
		    e2_destroy_index = 0
		    e3_destroy_index = 0
		    me_destroy_index = 0
		    # 用于切换图片
		    switch_image = True
		    # 用于延迟
		    delay = 100
		    running = True
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                pygame.quit()
		                sys.exit()
		        # 检测用户的键盘操作
		        key_pressed = pygame.key.get_pressed()
		        if key_pressed[K_w] or key_pressed[K_UP]:
		            me.moveUp()
		        if key_pressed[K_s] or key_pressed[K_DOWN]:
		            me.moveDown()
		        if key_pressed[K_a] or key_pressed[K_LEFT]:
		            me.moveLeft()
		        if key_pressed[K_d] or key_pressed[K_RIGHT]:
		            me.moveRight()
		        screen.blit(background, (0, 0))
		        # 绘制大型敌机
		        for each in big_enemies:
		            if each.active:
		                each.move()
		                if switch_image:
		                    screen.blit(each.image1, each.rect)
		                else:
		                    screen.blit(each.image2, each.rect)
		                # 即将出现在画面中，播放音效
		                if each.rect.bottom == -50:
		                    enemy3_fly_sound.play(-1)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e3_destroy_index == 0:
		                        enemy3_down_sound.play()
		                    screen.blit(each.destroy_images[e3_destroy_index], each.rect)
		                    e3_destroy_index = (e3_destroy_index + 1) % 6
		                    if e3_destroy_index == 0:
		                        me_down_sound.stop()
		                        each.reset()
		        # 绘制中型敌机：
		        for each in mid_enemies:
		            if each.active:
		                each.move()
		                screen.blit(each.image, each.rect)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e2_destroy_index == 0:
		                        enemy2_down_sound.play()
		                    screen.blit(each.destroy_images[e2_destroy_index], each.rect)
		                    e2_destroy_index = (e2_destroy_index + 1) % 4
		                    if e2_destroy_index == 0:
		                        each.reset()
		        # 绘制小型敌机：
		        for each in small_enemies:
		            if each.active:
		                each.move()
		                screen.blit(each.image, each.rect)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e1_destroy_index == 0:
		                        enemy1_down_sound.play()
		                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
		                    e1_destroy_index = (e1_destroy_index + 1) % 4
		                    if e1_destroy_index == 0:
		                        each.reset()
		        # 检测我方飞机是否被撞
		        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
		        if enemies_down:
		            # me.active = False
		            for e in enemies_down:
		                e.active = False
		        # 绘制我方飞机
		        if me.active:
		            if switch_image:
		                screen.blit(me.image1, me.rect)
		            else:
		                screen.blit(me.image2, me.rect)
		        else:
		            # 毁灭
		            if not(delay % 3):
		                if me_destroy_index == 0:
		                    me_down_sound.play()
		                screen.blit(me.destroy_images[me_destroy_index], me.rect)
		                me_destroy_index = (me_destroy_index + 1) % 4
		                if me_destroy_index == 0:
		                    print("Game Over!")
		                    running = False
		        # 切换图片
		        if not(delay % 5):
		            switch_image = not switch_image
		        delay -= 1
		        if not delay:
		            delay = 100
		        pygame.display.flip()
		        clock.tick(60)
		if __name__ == "__main__":
		    try:
		        main()
		    except SystemExit:
		        pass
		    except:
		        traceback.print_exc()
		        pygame.quit()
		        input()
##1.6设置子弹
    
	import pygame
	class Bullet1(pygame.sprite.Sprite):	//设置普通子弹
	    def __init__(self, position):
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
	        self.rect = self.image.get_rect()
	        self.rect.left, self.rect.top = position
	        self.speed = 12
	        self.active = True
	        self.mask = pygame.mask.from_surface(self.image)	//设置子弹图片的非透明部分
	    def move(self):
	        self.rect.top -= self.speed
	        if self.rect.top < 0:
	            self.active = False
	    def reset(self, position):
	        self.rect.left, self.rect.top = position
	        self.active = True

- 添加大型敌机和中型的生命值，修改敌机函数

		import pygame
		from random import *
		
		class SmallEnemy(pygame.sprite.Sprite):
		   .....
		class MidEnemy(pygame.sprite.Sprite):
		    energy = 8
		    
		    def __init__(self, bg_size):
		        .....
		        self.energy = MidEnemy.energy
		        self.hit = False
		    ....
		class BigEnemy(pygame.sprite.Sprite):
		    energy = 20
		    
		    def __init__(self, bg_size):
		        pygame.sprite.Sprite.__init__(self)
		.....
		        self.energy = BigEnemy.energy
		        self.hit = False
		
		 ....
- 在主方法中生成子弹

		# main.py
		import pygame
		import sys
		import traceback
		import myplane
		import enemy
		import bullet
		
		from pygame.locals import *
		from random import *
		
		pygame.init()
		pygame.mixer.init()
		
		bg_size = width, height = 480, 700
		screen = pygame.display.set_mode(bg_size)
		pygame.display.set_caption("飞机大战 -- FishC Demo")
		
		background = pygame.image.load("images/background.png").convert()
		
		BLACK = (0, 0, 0)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		
		# 载入游戏音乐
 		.....
		
		def main():
		    pygame.mixer.music.play(-1)
		
		    # 生成我方飞机
		    me = myplane.MyPlane(bg_size)
		
		    enemies = pygame.sprite.Group()
		
		    # 生成敌方小型飞机
		    small_enemies = pygame.sprite.Group()
		    add_small_enemies(small_enemies, enemies, 15)
		
		    # 生成敌方中型飞机
		    mid_enemies = pygame.sprite.Group()
		    add_mid_enemies(mid_enemies, enemies, 4)
		
		    # 生成敌方大型飞机
		    big_enemies = pygame.sprite.Group()
		    add_big_enemies(big_enemies, enemies, 2)
		
		    # 生成普通子弹
		    bullet1 = []
		    bullet1_index = 0
		    BULLET1_NUM = 4
		    for i in range(BULLET1_NUM):
		        bullet1.append(bullet.Bullet1(me.rect.midtop))
		
		    clock = pygame.time.Clock()
		
		    # 中弹图片索引
		    e1_destroy_index = 0
		    e2_destroy_index = 0
		    e3_destroy_index = 0
		    me_destroy_index = 0
		
		    # 用于切换图片
		    switch_image = True
		
		    # 用于延迟
		    delay = 100
		
		    running = True
		
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                pygame.quit()
		                sys.exit()
		
		        # 检测用户的键盘操作
		        key_pressed = pygame.key.get_pressed()
		
		        if key_pressed[K_w] or key_pressed[K_UP]:
		            me.moveUp()
		        if key_pressed[K_s] or key_pressed[K_DOWN]:
		            me.moveDown()
		        if key_pressed[K_a] or key_pressed[K_LEFT]:
		            me.moveLeft()
		        if key_pressed[K_d] or key_pressed[K_RIGHT]:
		            me.moveRight()
		    
		        screen.blit(background, (0, 0))
		
		        # 发射子弹每10帧发射一枚子弹
		        if not(delay % 10):
		            bullet1[bullet1_index].reset(me.rect.midtop)
		            bullet1_index = (bullet1_index + 1) % BULLET1_NUM
		
		        # 检测子弹是否击中敌机
		        for b in bullet1:
		            if b.active:
		                b.move()
		                screen.blit(b.image, b.rect)
		                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
		                if enemy_hit:
		                    b.active = False
		                    for e in enemy_hit:
		                        if e in mid_enemies or e in big_enemies:
		                            e.hit = True
		                            e.energy -= 1
		                            if e.energy == 0:
		                                e.active = False
		                        else:
		                            e.active = False
		        
		        # 绘制大型敌机
		        for each in big_enemies:
		            if each.active:
		                each.move()
		                if each.hit:
		                    screen.blit(each.image_hit, each.rect)
		                    each.hit = False
		                else:
		                    if switch_image:
		                        screen.blit(each.image1, each.rect)
		                    else:
		                        screen.blit(each.image2, each.rect)
		
		                # 绘制血槽
		                pygame.draw.line(screen, BLACK, \
		                                 (each.rect.left, each.rect.top - 5), \
		                                 (each.rect.right, each.rect.top - 5), \
		                                 2)
		                # 当生命大于20%显示绿色，否则显示红色
		                energy_remain = each.energy / enemy.BigEnemy.energy
		                if energy_remain > 0.2:
		                    energy_color = GREEN
		                else:
		                    energy_color = RED
		                pygame.draw.line(screen, energy_color, \
		                                 (each.rect.left, each.rect.top - 5), \
		                                 (each.rect.left + each.rect.width * energy_remain, \
		                                  each.rect.top - 5), 2)
		                    
		                # 即将出现在画面中，播放音效
		                if each.rect.bottom == -50:
		                    enemy3_fly_sound.play(-1)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e3_destroy_index == 0:
		                        enemy3_down_sound.play()
		                    screen.blit(each.destroy_images[e3_destroy_index], each.rect)
		                    e3_destroy_index = (e3_destroy_index + 1) % 6
		                    if e3_destroy_index == 0:
		                        enemy3_fly_sound.stop()
		                        each.reset()
		
		        # 绘制中型敌机：
		        for each in mid_enemies:
		            if each.active:
		                each.move()
		
		                if each.hit:
		                    screen.blit(each.image_hit, each.rect)
		                    each.hit = False
		                else:
		                    screen.blit(each.image, each.rect)
		
		                # 绘制血槽
		                pygame.draw.line(screen, BLACK, \
		                                 (each.rect.left, each.rect.top - 5), \
		                                 (each.rect.right, each.rect.top - 5), \
		                                 2)
		                # 当生命大于20%显示绿色，否则显示红色
		                energy_remain = each.energy / enemy.MidEnemy.energy
		                if energy_remain > 0.2:
		                    energy_color = GREEN
		                else:
		                    energy_color = RED
		                pygame.draw.line(screen, energy_color, \
		                                 (each.rect.left, each.rect.top - 5), \
		                                 (each.rect.left + each.rect.width * energy_remain, \
		                                  each.rect.top - 5), 2)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e2_destroy_index == 0:
		                        enemy2_down_sound.play()
		                    screen.blit(each.destroy_images[e2_destroy_index], each.rect)
		                    e2_destroy_index = (e2_destroy_index + 1) % 4
		                    if e2_destroy_index == 0:
		                        each.reset()
		
		        # 绘制小型敌机：
		        for each in small_enemies:
		            if each.active:
		                each.move()
		                screen.blit(each.image, each.rect)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if e1_destroy_index == 0:
		                        enemy1_down_sound.play()
		                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
		                    e1_destroy_index = (e1_destroy_index + 1) % 4
		                    if e1_destroy_index == 0:
		                        each.reset()
		
		        # 检测我方飞机是否被撞
		        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
		        if enemies_down:
		            # me.active = False
		            for e in enemies_down:
		                e.active = False
		        
		        # 绘制我方飞机
		        if me.active:
		            if switch_image:
		                screen.blit(me.image1, me.rect)
		            else:
		                screen.blit(me.image2, me.rect)
		        else:
		            # 毁灭
		            if not(delay % 3):
		                if me_destroy_index == 0:
		                    me_down_sound.play()
		                screen.blit(me.destroy_images[me_destroy_index], me.rect)
		                me_destroy_index = (me_destroy_index + 1) % 4
		                if me_destroy_index == 0:
		                    print("Game Over!")
		                    running = False
		
		        # 切换图片
		        if not(delay % 5):
		            switch_image = not switch_image
		
		        delay -= 1
		        if not delay:
		            delay = 100
		
		        pygame.display.flip()
		        clock.tick(60)
		        
		if __name__ == "__main__":
		    try:
		        main()
		    except SystemExit:
		        pass
		    except:
		        traceback.print_exc()
		        pygame.quit()
		        input()
- 显示分数及界面控制

		# main.py
		import pygame
		import sys
		import traceback
		import myplane
		import enemy
		import bullet
		from pygame.locals import *
		from random import *
		
		pygame.init()
		pygame.mixer.init()
		bg_size = width, height = 480, 700
		screen = pygame.display.set_mode(bg_size)
		pygame.display.set_caption("飞机大战 -- FishC Demo")
		background = pygame.image.load("images/background.png").convert()
		BLACK = (0, 0, 0)
		WHITE = (255, 255, 255)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		# 载入游戏音乐
		.....
		
		def inc_speed(target, inc):
		    for each in target:
		        each.speed += inc
		
		def main():
		    pygame.mixer.music.play(-1)
		    # 生成我方飞机
		    me = myplane.MyPlane(bg_size)
		    enemies = pygame.sprite.Group()
		    # 生成敌方小型飞机
		    small_enemies = pygame.sprite.Group()
		    add_small_enemies(small_enemies, enemies, 15)
		    # 生成敌方中型飞机
		    mid_enemies = pygame.sprite.Group()
		    add_mid_enemies(mid_enemies, enemies, 4)
		    # 生成敌方大型飞机
		    big_enemies = pygame.sprite.Group()
		    add_big_enemies(big_enemies, enemies, 2)
		    # 生成普通子弹
		    bullet1 = []
		    bullet1_index = 0
		    BULLET1_NUM = 4
		    for i in range(BULLET1_NUM):
		        bullet1.append(bullet.Bullet1(me.rect.midtop))
		    clock = pygame.time.Clock()
		    # 中弹图片索引
		    e1_destroy_index = 0
		    e2_destroy_index = 0
		    e3_destroy_index = 0
		    me_destroy_index = 0
		    # 统计得分
		    score = 0
		    score_font = pygame.font.Font("font/font.ttf", 36)
		    # 标志是否暂停游戏
		    paused = False
		    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
		    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
		    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
		    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
		    paused_rect = pause_nor_image.get_rect()
		    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
		    paused_image = pause_nor_image
		    # 设置难度级别
		    level = 1
		    # 全屏炸弹
		    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
		    bomb_rect = bomb_image.get_rect()
		    bomb_font = pygame.font.Font("font/font.ttf", 48)
		    bomb_num = 3
		    # 用于切换图片
		    switch_image = True
		    # 用于延迟
		    delay = 100
		    running = True
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                pygame.quit()
		                sys.exit()
		            elif event.type == MOUSEBUTTONDOWN:
		                if event.button == 1 and paused_rect.collidepoint(event.pos):
		                    paused = not paused
		            elif event.type == MOUSEMOTION:
		                if paused_rect.collidepoint(event.pos):
		                    if paused:
		                        paused_image = resume_pressed_image
		                    else:
		                        paused_image = pause_pressed_image
		                else:
		                    if paused:
		                        paused_image = resume_nor_image
		                    else:
		                       paused_image = pause_nor_image
		            elif event.type == KEYDOWN:
		                if event.key == K_SPACE:
		                    if bomb_num:
		                        bomb_num -= 1
		                        bomb_sound.play()
		                        for each in enemies:
		                            if each.rect.bottom > 0:
		                                each.active = False
		        # 根据用户的得分增加难度
		        if level == 1 and score > 50000:
		            level = 2
		            upgrade_sound.play()
		            # 增加3架小型敌机、2架中型敌机和1架大型敌机
		            add_small_enemies(small_enemies, enemies, 3)
		            add_mid_enemies(mid_enemies, enemies, 2)
		            add_big_enemies(big_enemies, enemies, 1)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		        elif level == 2 and score > 300000:
		            level = 3
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		        elif level == 3 and score > 600000:
		            level = 4
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		        elif level == 4 and score > 1000000:
		            level = 5
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		        screen.blit(background, (0, 0))
		        if not paused:
		            # 检测用户的键盘操作
		            key_pressed = pygame.key.get_pressed()
		
		            if key_pressed[K_w] or key_pressed[K_UP]:
		                me.moveUp()
		            if key_pressed[K_s] or key_pressed[K_DOWN]:
		                me.moveDown()
		            if key_pressed[K_a] or key_pressed[K_LEFT]:
		                me.moveLeft()
		            if key_pressed[K_d] or key_pressed[K_RIGHT]:
		                me.moveRight()
		
		            # 发射子弹
		            if not(delay % 10):
		                bullet1[bullet1_index].reset(me.rect.midtop)
		                bullet1_index = (bullet1_index + 1) % BULLET1_NUM
		
		            # 检测子弹是否击中敌机
		            for b in bullet1:
		                if b.active:
		                    b.move()
		                    screen.blit(b.image, b.rect)
		                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
		                    if enemy_hit:
		                        b.active = False
		                        for e in enemy_hit:
		                            if e in mid_enemies or e in big_enemies:
		                                e.hit = True
		                                e.energy -= 1
		                                if e.energy == 0:
		                                    e.active = False
		                            else:
		                                e.active = False
		            
		            # 绘制大型敌机
		            for each in big_enemies:
		                if each.active:
		                    each.move()
		                    if each.hit:
		                        screen.blit(each.image_hit, each.rect)
		                        each.hit = False
		                    else:
		                        if switch_image:
		                            screen.blit(each.image1, each.rect)
		                        else:
		                            screen.blit(each.image2, each.rect)
		
		                    # 绘制血槽
		                    pygame.draw.line(screen, BLACK, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.right, each.rect.top - 5), \
		                                     2)
		                    # 当生命大于20%显示绿色，否则显示红色
		                    energy_remain = each.energy / enemy.BigEnemy.energy
		                    if energy_remain > 0.2:
		                        energy_color = GREEN
		                    else:
		                        energy_color = RED
		                    pygame.draw.line(screen, energy_color, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.left + each.rect.width * energy_remain, \
		                                      each.rect.top - 5), 2)
		                        
		                    # 即将出现在画面中，播放音效
		                    if each.rect.bottom == -50:
		                        enemy3_fly_sound.play(-1)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e3_destroy_index == 0:
		                            enemy3_down_sound.play()
		                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
		                        e3_destroy_index = (e3_destroy_index + 1) % 6
		                        if e3_destroy_index == 0:
		                            enemy3_fly_sound.stop()
		                            score += 10000
		                            each.reset()
		
		            # 绘制中型敌机：
		            for each in mid_enemies:
		                if each.active:
		                    each.move()
		
		                    if each.hit:
		                        screen.blit(each.image_hit, each.rect)
		                        each.hit = False
		                    else:
		                        screen.blit(each.image, each.rect)
		
		                    # 绘制血槽
		                    pygame.draw.line(screen, BLACK, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.right, each.rect.top - 5), \
		                                     2)
		                    # 当生命大于20%显示绿色，否则显示红色
		                    energy_remain = each.energy / enemy.MidEnemy.energy
		                    if energy_remain > 0.2:
		                        energy_color = GREEN
		                    else:
		                        energy_color = RED
		                    pygame.draw.line(screen, energy_color, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.left + each.rect.width * energy_remain, \
		                                      each.rect.top - 5), 2)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e2_destroy_index == 0:
		                            enemy2_down_sound.play()
		                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
		                        e2_destroy_index = (e2_destroy_index + 1) % 4
		                        if e2_destroy_index == 0:
		                            score += 6000
		                            each.reset()
		
		            # 绘制小型敌机：
		            for each in small_enemies:
		                if each.active:
		                    each.move()
		                    screen.blit(each.image, each.rect)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e1_destroy_index == 0:
		                            enemy1_down_sound.play()
		                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
		                        e1_destroy_index = (e1_destroy_index + 1) % 4
		                        if e1_destroy_index == 0:
		                            score += 1000
		                            each.reset()
		
		            # 检测我方飞机是否被撞
		            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
		            if enemies_down:
		                # me.active = False
		                for e in enemies_down:
		                    e.active = False
		            
		            # 绘制我方飞机
		            if me.active:
		                if switch_image:
		                    screen.blit(me.image1, me.rect)
		                else:
		                    screen.blit(me.image2, me.rect)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if me_destroy_index == 0:
		                        me_down_sound.play()
		                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
		                    me_destroy_index = (me_destroy_index + 1) % 4
		                    if me_destroy_index == 0:
		                        print("Game Over!")
		                        running = False
		
		            # 绘制全屏炸弹数量
		            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
		            text_rect = bomb_text.get_rect()
		            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
		            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))
		
		        # 绘制得分
		        score_text = score_font.render("Score : %s" % str(score), True, WHITE)
		        screen.blit(score_text, (10, 5))
		        # 绘制暂停按钮
		        screen.blit(paused_image, paused_rect)
		        # 切换图片
		        if not(delay % 5):
		            switch_image = not switch_image
		
		        delay -= 1
		        if not delay:
		            delay = 100
		
		        pygame.display.flip()
		        clock.tick(60)
		        
		if __name__ == "__main__":
		    try:
		        main()
		    except SystemExit:
		        pass
		    except:
		        traceback.print_exc()
		        pygame.quit()
		        input()
- 创建补给包函数

		import pygame
		from random import *
		class Bullet_Supply(pygame.sprite.Sprite):
		    def __init__(self, bg_size):
		        pygame.sprite.Sprite.__init__(self)
		        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()
		        self.rect = self.image.get_rect()
		        self.width, self.height = bg_size[0], bg_size[1]
		        self.rect.left, self.rect.bottom = \
		                        randint(0, self.width - self.rect.width), -100
		        self.speed = 5
		        self.active = False
		        self.mask = pygame.mask.from_surface(self.image)
		    def move(self):
		        if self.rect.top < self.height:
		            self.rect.top += self.speed
		        else:
		            self.active = False
		    def reset(self):
		        self.active = True
		        self.rect.left, self.rect.bottom =randint(0, self.width - self.rect.width), -100
		class Bomb_Supply(pygame.sprite.Sprite):
		    def __init__(self, bg_size):
		        pygame.sprite.Sprite.__init__(self)
		        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
		        self.rect = self.image.get_rect()
		        self.width, self.height = bg_size[0], bg_size[1]
		        self.rect.left, self.rect.bottom =randint(0, self.width - self.rect.width), -100
		        self.speed = 5
		        self.active = False
		        self.mask = pygame.mask.from_surface(self.image)
		    def move(self):
		        if self.rect.top < self.height:
		            self.rect.top += self.speed
		        else:
		            self.active = False
		    def reset(self):
		        self.active = True
		        self.rect.left, self.rect.bottom =randint(0, self.width - self.rect.width), -100   

- 关联并设置到主函数中

		# main.py
		import pygame
		import sys
		import traceback
		import myplane
		import enemy
		import bullet
		import supply
		from pygame.locals import *
		from random import *
		
		pygame.init()
		pygame.mixer.init()
		
		bg_size = width, height = 480, 700
		screen = pygame.display.set_mode(bg_size)
		pygame.display.set_caption("飞机大战 -- FishC Demo")
		
		background = pygame.image.load("images/background.png").convert()
		
		BLACK = (0, 0, 0)
		WHITE = (255, 255, 255)
		GREEN = (0, 255, 0)
		RED = (255, 0, 0)
		
		# 载入游戏音乐
			....
		
		def inc_speed(target, inc):
		    for each in target:
		        each.speed += inc
		
		def main():
		    pygame.mixer.music.play(-1)
		
		    # 生成我方飞机
		    me = myplane.MyPlane(bg_size)
		
		    enemies = pygame.sprite.Group()
		
		    # 生成敌方小型飞机
		    small_enemies = pygame.sprite.Group()
		    add_small_enemies(small_enemies, enemies, 15)
		
		    # 生成敌方中型飞机
		    mid_enemies = pygame.sprite.Group()
		    add_mid_enemies(mid_enemies, enemies, 4)
		
		    # 生成敌方大型飞机
		    big_enemies = pygame.sprite.Group()
		    add_big_enemies(big_enemies, enemies, 2)
		
		    # 生成普通子弹
		    bullet1 = []
		    bullet1_index = 0
		    BULLET1_NUM = 4
		    for i in range(BULLET1_NUM):
		        bullet1.append(bullet.Bullet1(me.rect.midtop))
		
		    # 生成超级子弹
		    bullet2 = []
		    bullet2_index = 0
		    BULLET2_NUM = 8
		    for i in range(BULLET2_NUM//2):
		        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))
		        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))
		
		    clock = pygame.time.Clock()
		
		    # 中弹图片索引
		    e1_destroy_index = 0
		    e2_destroy_index = 0
		    e3_destroy_index = 0
		    me_destroy_index = 0
		
		    # 统计得分
		    score = 0
		    score_font = pygame.font.Font("font/font.ttf", 36)
		
		    # 标志是否暂停游戏
		    paused = False
		    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
		    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
		    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
		    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
		    paused_rect = pause_nor_image.get_rect()
		    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
		    paused_image = pause_nor_image
		
		    # 设置难度级别
		    level = 1
		
		    # 全屏炸弹
		    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
		    bomb_rect = bomb_image.get_rect()
		    bomb_font = pygame.font.Font("font/font.ttf", 48)
		    bomb_num = 3
		
		    # 每30秒发放一个补给包
		    bullet_supply = supply.Bullet_Supply(bg_size)
		    bomb_supply = supply.Bomb_Supply(bg_size)
		    SUPPLY_TIME = USEREVENT
		    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
		
		    # 超级子弹定时器
		    DOUBLE_BULLET_TIME = USEREVENT + 1
		
		    # 标志是否使用超级子弹
		    is_double_bullet = False
		
		    # 用于切换图片
		    switch_image = True
		
		    # 用于延迟
		    delay = 100
		
		    running = True
		
		    while running:
		        for event in pygame.event.get():
		            if event.type == QUIT:
		                pygame.quit()
		                sys.exit()
		
		            elif event.type == MOUSEBUTTONDOWN:
		                if event.button == 1 and paused_rect.collidepoint(event.pos):
		                    paused = not paused
		                    if paused:
		                        pygame.time.set_timer(SUPPLY_TIME, 0)
		                        pygame.mixer.music.pause()
		                        pygame.mixer.pause()
		                    else:
		                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
		                        pygame.mixer.music.unpause()
		                        pygame.mixer.unpause()
		
		            elif event.type == MOUSEMOTION:
		                if paused_rect.collidepoint(event.pos):
		                    if paused:
		                        paused_image = resume_pressed_image
		                    else:
		                        paused_image = pause_pressed_image
		                else:
		                    if paused:
		                        paused_image = resume_nor_image
		                    else:
		                       paused_image = pause_nor_image
		
		            elif event.type == KEYDOWN:
		                if event.key == K_SPACE:
		                    if bomb_num:
		                        bomb_num -= 1
		                        bomb_sound.play()
		                        for each in enemies:
		                            if each.rect.bottom > 0:
		                                each.active = False
		
		            elif event.type == SUPPLY_TIME:
		                supply_sound.play()
		                if choice([True, False]):
		                    bomb_supply.reset()
		                else:
		                    bullet_supply.reset()
		
		            elif event.type == DOUBLE_BULLET_TIME:
		                is_double_bullet = False
		                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
		                         
		
		        # 根据用户的得分增加难度
		        if level == 1 and score > 50000:
		            level = 2
		            upgrade_sound.play()
		            # 增加3架小型敌机、2架中型敌机和1架大型敌机
		            add_small_enemies(small_enemies, enemies, 3)
		            add_mid_enemies(mid_enemies, enemies, 2)
		            add_big_enemies(big_enemies, enemies, 1)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		        elif level == 2 and score > 300000:
		            level = 3
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		        elif level == 3 and score > 600000:
		            level = 4
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		        elif level == 4 and score > 1000000:
		            level = 5
		            upgrade_sound.play()
		            # 增加5架小型敌机、3架中型敌机和2架大型敌机
		            add_small_enemies(small_enemies, enemies, 5)
		            add_mid_enemies(mid_enemies, enemies, 3)
		            add_big_enemies(big_enemies, enemies, 2)
		            # 提升小型敌机的速度
		            inc_speed(small_enemies, 1)
		            inc_speed(mid_enemies, 1)
		            
		
		        screen.blit(background, (0, 0))
		                
		        if not paused:
		            # 检测用户的键盘操作
		            key_pressed = pygame.key.get_pressed()
		
		            if key_pressed[K_w] or key_pressed[K_UP]:
		                me.moveUp()
		            if key_pressed[K_s] or key_pressed[K_DOWN]:
		                me.moveDown()
		            if key_pressed[K_a] or key_pressed[K_LEFT]:
		                me.moveLeft()
		            if key_pressed[K_d] or key_pressed[K_RIGHT]:
		                me.moveRight()
		
		            # 绘制全屏炸弹补给并检测是否获得
		            if bomb_supply.active:
		                bomb_supply.move()
		                screen.blit(bomb_supply.image, bomb_supply.rect)
		                if pygame.sprite.collide_mask(bomb_supply, me):
		                    get_bomb_sound.play()
		                    if bomb_num < 3:
		                        bomb_num += 1
		                    bomb_supply.active = False
		
		            # 绘制超级子弹补给并检测是否获得
		            if bullet_supply.active:
		                bullet_supply.move()
		                screen.blit(bullet_supply.image, bullet_supply.rect)
		                if pygame.sprite.collide_mask(bullet_supply, me):
		                    get_bullet_sound.play()
		                    is_double_bullet = True
		                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
		                    bullet_supply.active = False
		
		            # 发射子弹
		            if not(delay % 10):
		                bullet_sound.play()
		                if is_double_bullet:
		                    bullets = bullet2
		                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
		                    bullets[bullet2_index+1].reset((me.rect.centerx+30, me.rect.centery))
		                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
		                else:
		                    bullets = bullet1
		                    bullets[bullet1_index].reset(me.rect.midtop)
		                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
		
		                
		            # 检测子弹是否击中敌机
		            for b in bullets:
		                if b.active:
		                    b.move()
		                    screen.blit(b.image, b.rect)
		                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
		                    if enemy_hit:
		                        b.active = False
		                        for e in enemy_hit:
		                            if e in mid_enemies or e in big_enemies:
		                                e.hit = True
		                                e.energy -= 1
		                                if e.energy == 0:
		                                    e.active = False
		                            else:
		                                e.active = False
		            
		            # 绘制大型敌机
		            for each in big_enemies:
		                if each.active:
		                    each.move()
		                    if each.hit:
		                        screen.blit(each.image_hit, each.rect)
		                        each.hit = False
		                    else:
		                        if switch_image:
		                            screen.blit(each.image1, each.rect)
		                        else:
		                            screen.blit(each.image2, each.rect)
		
		                    # 绘制血槽
		                    pygame.draw.line(screen, BLACK, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.right, each.rect.top - 5), \
		                                     2)
		                    # 当生命大于20%显示绿色，否则显示红色
		                    energy_remain = each.energy / enemy.BigEnemy.energy
		                    if energy_remain > 0.2:
		                        energy_color = GREEN
		                    else:
		                        energy_color = RED
		                    pygame.draw.line(screen, energy_color, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.left + each.rect.width * energy_remain, \
		                                      each.rect.top - 5), 2)
		                        
		                    # 即将出现在画面中，播放音效
		                    if each.rect.bottom == -50:
		                        enemy3_fly_sound.play(-1)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e3_destroy_index == 0:
		                            enemy3_down_sound.play()
		                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
		                        e3_destroy_index = (e3_destroy_index + 1) % 6
		                        if e3_destroy_index == 0:
		                            enemy3_fly_sound.stop()
		                            score += 10000
		                            each.reset()
		
		            # 绘制中型敌机：
		            for each in mid_enemies:
		                if each.active:
		                    each.move()
		
		                    if each.hit:
		                        screen.blit(each.image_hit, each.rect)
		                        each.hit = False
		                    else:
		                        screen.blit(each.image, each.rect)
		
		                    # 绘制血槽
		                    pygame.draw.line(screen, BLACK, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.right, each.rect.top - 5), \
		                                     2)
		                    # 当生命大于20%显示绿色，否则显示红色
		                    energy_remain = each.energy / enemy.MidEnemy.energy
		                    if energy_remain > 0.2:
		                        energy_color = GREEN
		                    else:
		                        energy_color = RED
		                    pygame.draw.line(screen, energy_color, \
		                                     (each.rect.left, each.rect.top - 5), \
		                                     (each.rect.left + each.rect.width * energy_remain, \
		                                      each.rect.top - 5), 2)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e2_destroy_index == 0:
		                            enemy2_down_sound.play()
		                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
		                        e2_destroy_index = (e2_destroy_index + 1) % 4
		                        if e2_destroy_index == 0:
		                            score += 6000
		                            each.reset()
		
		            # 绘制小型敌机：
		            for each in small_enemies:
		                if each.active:
		                    each.move()
		                    screen.blit(each.image, each.rect)
		                else:
		                    # 毁灭
		                    if not(delay % 3):
		                        if e1_destroy_index == 0:
		                            enemy1_down_sound.play()
		                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
		                        e1_destroy_index = (e1_destroy_index + 1) % 4
		                        if e1_destroy_index == 0:
		                            score += 1000
		                            each.reset()
		
		            # 检测我方飞机是否被撞
		            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
		            if enemies_down:
		                # me.active = False
		                for e in enemies_down:
		                    e.active = False
		            
		            # 绘制我方飞机
		            if me.active:
		                if switch_image:
		                    screen.blit(me.image1, me.rect)
		                else:
		                    screen.blit(me.image2, me.rect)
		            else:
		                # 毁灭
		                if not(delay % 3):
		                    if me_destroy_index == 0:
		                        me_down_sound.play()
		                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
		                    me_destroy_index = (me_destroy_index + 1) % 4
		                    if me_destroy_index == 0:
		                        print("Game Over!")
		                        running = False
		
		            # 绘制全屏炸弹数量
		            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
		            text_rect = bomb_text.get_rect()
		            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
		            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))
		
		        # 绘制得分
		        score_text = score_font.render("Score : %s" % str(score), True, WHITE)
		        screen.blit(score_text, (10, 5))
		
		        # 绘制暂停按钮
		        screen.blit(paused_image, paused_rect)
		
		        # 切换图片
		        if not(delay % 5):
		            switch_image = not switch_image
		
		        delay -= 1
		        if not delay:
		            delay = 100
		
		        pygame.display.flip()
		        clock.tick(60)
		        
		if __name__ == "__main__":
		    try:
		        main()
		    except SystemExit:
		        pass
		    except:
		        traceback.print_exc()
		        pygame.quit()
		        input()

#7.9

##1.最终函数及详解
##1.1子弹模块bullet

	import pygame		//导入游戏模块
	class Bullet1(pygame.sprite.Sprite):		//子弹类型1，使用游戏精灵必须继承pygame.sprite.Sprite，他为基类
	    def __init__(self, position):
	        pygame.sprite.Sprite.__init__(self)			//调用父类构造方法
	        self.image = pygame.image.load("images/bullet1.png").convert_alpha()	//加载图像并改变像素格式
	        self.rect = self.image.get_rect()			//得到图片的矩形区域
	        self.rect.left, self.rect.top = position		//获取图片的坐标
	        self.speed = 12			//设置子弹速度
	        self.active = False			//设置子弹是否存在
	        self.mask = pygame.mask.from_surface(self.image)	//设置子弹图片的有效面积
	
	    def move(self):		//子弹移动
	        self.rect.top -= self.speed				//设置子弹的高度
	        if self.rect.top < 0:		
	            self.active = False		//如果子弹超出屏幕，将子弹状态设置为消失
	
	    def reset(self, position):		//刷新函数，重新设置子弹位置将其设置为存在
	        self.rect.left, self.rect.top = position
	        self.active = True
	
	class Bullet2(pygame.sprite.Sprite):		//子弹类型2，语句和子弹类型1相似
	    def __init__(self, position):
	        pygame.sprite.Sprite.__init__(self)
	
	        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
	        self.rect = self.image.get_rect()
	        self.rect.left, self.rect.top = position
	        self.speed = 14
	        self.active = False
	        self.mask = pygame.mask.from_surface(self.image)
	
	    def move(self):
	        self.rect.top -= self.speed
	
	        if self.rect.top < 0:
	            self.active = False
	
	    def reset(self, position):
	        self.rect.left, self.rect.top = position
        self.active = True
    
##1.2敌机enemy

	import pygame		//导入游戏模块
	from random import *		//导入生成随机数模块
	class SmallEnemy(pygame.sprite.Sprite):		//创建小敌机类，使用游戏精灵继承自pygame.sprite.Sprite基类
	    def __init__(self, bg_size):		//设置构造函数
	        pygame.sprite.Sprite.__init__(self)		//调用父类构造方法
	
	        self.image = pygame.image.load("images/enemy1.png").convert_alpha()		//加载图片并设置像素格式
	        self.destroy_images = []		//创建空列表存放加载销毁飞机图片语句
	        self.destroy_images.extend([\	
	            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy1_down4.png").convert_alpha() \
	            ])		//使用extend向列表中加载列表
	        self.rect = self.image.get_rect()		//获取图片矩形区域
	        self.width, self.height = bg_size[0], bg_size[1]	//设置宽度和高度为传入参数的宽度和高度
	        self.speed = 2		//设置速度
	        self.active = True		//设置存活参数
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-5 * self.height, 0)
			//设置位置为随机生成，高度位置为在距离界面顶端5个机身位开始刷新
	        self.mask = pygame.mask.from_surface(self.image)		//设置小敌机的有效碰撞体积
	
	    def move(self):		//设置移动函数，当飞机加载到页面中时，设置高度为原高度加自身速度，否则重置敌机位置
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	
	    def reset(self):		//设置重置函数，将活动参数设置为TRUE，重新设置飞机位置
	        self.active = True
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-5 * self.height, 0)
	class MidEnemy(pygame.sprite.Sprite):		//设置中型敌机，大部分作用同小敌机
	    energy = 8		//设置中型敌机生命值
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	
	        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
	        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
	        self.destroy_images = []
	        self.destroy_images.extend([\
	            pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy2_down4.png").convert_alpha() \
	            ])
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.active = True		//存活参数
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-10 * self.height, -self.height)
	        self.mask = pygame.mask.from_surface(self.image)
	        self.energy = MidEnemy.energy		//设置生命值
	        self.hit = False		//碰撞参数
	
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	    def reset(self):
	        self.active = True	
	        self.energy = MidEnemy.energy	//重新设置生命值
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-10 * self.height, -self.height)
	class BigEnemy(pygame.sprite.Sprite):		//设置大型敌机，与中型敌机基本相同
	    energy = 20
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
	        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
	        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
	        self.destroy_images = []
	        self.destroy_images.extend([\
	            pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
	            pygame.image.load("images/enemy3_down6.png").convert_alpha() \
	            ])
	        self.rect = self.image1.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.speed = 1
	        self.active = True
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-15 * self.height, -5 * self.height)
	        self.mask = pygame.mask.from_surface(self.image1)
	        self.energy = BigEnemy.energy
	        self.hit = False
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.reset()
	    def reset(self):
	        self.active = True
	        self.energy = BigEnemy.energy
	        self.rect.left, self.rect.top =randint(0, self.width - self.rect.width),randint(-15 * self.height, -5 * self.height)

##1.3己方飞机模块myplane

	import pygame		//导入游戏模块
	class MyPlane(pygame.sprite.Sprite):	//己方飞机，使用动画精灵需继承父类pygame.sprite.Sprite
	    def __init__(self, bg_size):	//设置构造函数,创建了该类的实例时就会调用该方法
	        pygame.sprite.Sprite.__init__(self)		//调用父类构造方法
	        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
	        self.image2 = pygame.image.load("images/me2.png").convert_alpha()//加载图像并改变像素格式用于切换生成动画
	        self.destroy_images = []	//创建空列表用于存放加载销毁图片的语句
	        self.destroy_images.extend([\
	            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
	            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
	            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
	            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
	            ])		//extend（）向空列表中添加列表
	        self.rect = self.image1.get_rect()		//得到图片的矩形区域
	        self.width, self.height = bg_size[0], bg_size[1]		//设置宽度和高度为传入参数的宽度和高度
	        self.rect.left,self.rect.top=(self.width - self.rect.width) // 2,self.height - self.rect.height - 60
			//设置飞机的默认位置为背景图片正中距离底部60的位置
	        self.speed = 10		//设置速度
	        self.active = True		//设置存活参数
	        self.invincible = False		//设置无敌
	        self.mask = pygame.mask.from_surface(self.image1)	//设置飞机图片有效面积
	    def moveUp(self):		//设置向上移动函数，如果图片位置高度大于0，则新高度就等于原高度减速度，否则一直等于0，其余移动函数同理
	        if self.rect.top > 0:
	            self.rect.top -= self.speed
	        else:
	            self.rect.top = 0
	    def moveDown(self):		//向下移动
	        if self.rect.bottom < self.height - 60:
	            self.rect.top += self.speed
	        else:
	            self.rect.bottom = self.height - 60
	    def moveLeft(self):		//向左移动
	        if self.rect.left > 0:
	            self.rect.left -= self.speed
	        else:
	            self.rect.left = 0
	    def moveRight(self):		//向右移动
	        if self.rect.right < self.width:
	            self.rect.left += self.speed
	        else:
	            self.rect.right = self.width
	    def reset(self):		//重置飞机，重新设置位置和存活以及无敌
	        self.rect.left,self.rect.top =(self.width - self.rect.width) // 2,self.height - self.rect.height - 60
	        self.active = True
	        self.invincible = True
##1.4补给模块supply

	import pygame	//导入游戏模块
	from random import *		//导入随机数模块
	class Bullet_Supply(pygame.sprite.Sprite):	//设置子弹补给，使用动画精灵，继承pygame.sprite.Sprite基类
	    def __init__(self, bg_size):	//设置构造方法
	        pygame.sprite.Sprite.__init__(self)		//重写父类构造方法
	        self.image = pygame.image.load("images/bullet_supply.png").convert_alpha()		//加载子弹补给图片并转换像素
	        self.rect = self.image.get_rect()		//获取图片位置
	        self.width, self.height = bg_size[0], bg_size[1]	//由传入参数设置宽和高
	        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100	//设置生成位置
	        self.speed = 5		//设置速度
	        self.active = False		//设置存活参数
	        self.mask = pygame.mask.from_surface(self.image)		//设置碰撞有效区域
	    def move(self):		//设置移动方法
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.active = False
	    def reset(self):		//设置刷新方法
	        self.active = True
	        self.rect.left, self.rect.bottom =randint(0, self.width - self.rect.width), -100
	class Bomb_Supply(pygame.sprite.Sprite):	//设置炸弹补给与子弹补给类似
	    def __init__(self, bg_size):
	        pygame.sprite.Sprite.__init__(self)
	        self.image = pygame.image.load("images/bomb_supply.png").convert_alpha()
	        self.rect = self.image.get_rect()
	        self.width, self.height = bg_size[0], bg_size[1]
	        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -100
	        self.speed = 5
	        self.active = False
	        self.mask = pygame.mask.from_surface(self.image)
	    def move(self):
	        if self.rect.top < self.height:
	            self.rect.top += self.speed
	        else:
	            self.active = False
	    def reset(self):
	        self.active = True
	        self.rect.left, self.rect.bottom =randint(0, self.width - self.rect.width), -100  

##1.5主函数main

	# main.py
	import pygame		//导入游戏模块
	import sys			//导入sys模块用于负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。
	import traceback	//导入traceback模块用于从程序运行的堆栈中提取，格式化或打印程序目前执行的上下文信息
	import myplane		//导入飞机模块
	import enemy		//导入敌机模块
	import bullet		//导入子弹模块
	import supply		//导入补给模块
	
	from pygame.locals import *		//该模块包含pygame的各种常量
	from random import *	//导入随机数模块
	
	pygame.init()		//初始化所有导入的pygame模块
	pygame.mixer.init()		//初始化混音器模块
	
	bg_size = width, height = 480, 700		//设置主程序大小为多少
	screen = pygame.display.set_mode(bg_size)	//对程序窗口进行设置
	pygame.display.set_caption("飞机大战 -- FishC Demo")		//设置窗口标题
	
	background = pygame.image.load("images/background.png").convert()	//设置窗口背景
	
	BLACK = (0, 0, 0)		//常用颜色色值
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	
	# 载入游戏音乐
	pygame.mixer.music.load("sound/game_music.ogg")		//加载游戏背景音
	pygame.mixer.music.set_volume(0.2)		//设置音量
	bullet_sound = pygame.mixer.Sound("sound/bullet.wav")	//加载游戏音效
	bullet_sound.set_volume(0.2)
	bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
	bomb_sound.set_volume(0.2)
	supply_sound = pygame.mixer.Sound("sound/supply.wav")
	supply_sound.set_volume(0.2)
	get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
	get_bomb_sound.set_volume(0.2)
	get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
	get_bullet_sound.set_volume(0.2)
	upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
	upgrade_sound.set_volume(0.2)
	enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
	enemy3_fly_sound.set_volume(0.2)
	enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
	enemy1_down_sound.set_volume(0.2)
	enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
	enemy2_down_sound.set_volume(0.2)
	enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
	enemy3_down_sound.set_volume(0.5)
	me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
	me_down_sound.set_volume(0.2)
	
	def add_small_enemies(group1, group2, num):		//添加小型敌机方法
	    for i in range(num):
	        e1 = enemy.SmallEnemy(bg_size)
	        group1.add(e1)
	        group2.add(e1)
	
	def add_mid_enemies(group1, group2, num):		//添加中型敌机方法
	    for i in range(num):
	        e2 = enemy.MidEnemy(bg_size)
	        group1.add(e2)
	        group2.add(e2)
	
	def add_big_enemies(group1, group2, num):		//添加大型敌机方法
	    for i in range(num):
	        e3 = enemy.BigEnemy(bg_size)
	        group1.add(e3)
	        group2.add(e3)
	
	def inc_speed(target, inc):
	    for each in target:
	        each.speed += inc
	
	def main():
	    pygame.mixer.music.play(-1)		//设置背景音乐循环播放
	
	    # 生成我方飞机
	    me = myplane.MyPlane(bg_size)		//实例化己方飞机对象
	    enemies = pygame.sprite.Group()		//创建用于保存和管理多个Sprite对象的容器类
	
	    # 生成敌方小型飞机
	    small_enemies = pygame.sprite.Group()	//创建用于保存和管理多个小敌机的容器类
	    add_small_enemies(small_enemies, enemies, 15)	//向该容器添加15个敌机向总容器添加15个敌机
	
	    # 生成敌方中型飞机
	    mid_enemies = pygame.sprite.Group()
	    add_mid_enemies(mid_enemies, enemies, 4)
	
	    # 生成敌方大型飞机
	    big_enemies = pygame.sprite.Group()
	    add_big_enemies(big_enemies, enemies, 2)
	
	    # 生成普通子弹
	    bullet1 = []
	    bullet1_index = 0
	    BULLET1_NUM = 4
	    for i in range(BULLET1_NUM):
	        bullet1.append(bullet.Bullet1(me.rect.midtop))
	
	    # 生成超级子弹
	    bullet2 = []
	    bullet2_index = 0
	    BULLET2_NUM = 8
	    for i in range(BULLET2_NUM//2):
	        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))	//添加子弹2并设置位置
	        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))
	
	    clock = pygame.time.Clock()		//创建一个时间对象来帮助跟踪时间
	
	    # 中弹图片索引
	    e1_destroy_index = 0
	    e2_destroy_index = 0
	    e3_destroy_index = 0
	    me_destroy_index = 0
	
	    # 统计得分
	    score = 0
	    score_font = pygame.font.Font("font/font.ttf", 36)	//从文件创造一个新的font对象，第一个字体文件，第二个大小
	
	    # 标志是否暂停游戏
	    paused = False		//设置游戏暂停参数
	    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()	//加载暂停图片
	    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()	//鼠标悬停时加载的图片
	    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()	//加载开始图片
	    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()//加载鼠标悬停开始图片
	    paused_rect = pause_nor_image.get_rect()	//获取暂停图片矩形区域
	    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10		//设置图片位置
	    paused_image = pause_nor_image
	
	    # 设置难度级别
	    level = 1
	
	    # 全屏炸弹
	    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
	    bomb_rect = bomb_image.get_rect()
	    bomb_font = pygame.font.Font("font/font.ttf", 48)
	    bomb_num = 3
	
	    # 每30秒发放一个补给包
	    bullet_supply = supply.Bullet_Supply(bg_size)
	    bomb_supply = supply.Bomb_Supply(bg_size)
	    SUPPLY_TIME = USEREVENT
	    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)	//创建重复时间每隔30秒
	
	    # 超级子弹定时器
	    DOUBLE_BULLET_TIME = USEREVENT + 1
	
	    # 标志是否使用超级子弹
	    is_double_bullet = False
	
	    # 解除我方无敌状态定时器
	    INVINCIBLE_TIME = USEREVENT + 2
	
	    # 生命数量
	    life_image = pygame.image.load("images/life.png").convert_alpha()	//加载生命值图片
	    life_rect = life_image.get_rect()
	    life_num = 3	//设置生命数量
	
	    # 用于阻止重复打开记录文件
	    recorded = False
	
	    # 游戏结束画面
	    gameover_font = pygame.font.Font("font/font.TTF", 48)
	    again_image = pygame.image.load("images/again.png").convert_alpha()
	    again_rect = again_image.get_rect()
	    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
	    gameover_rect = gameover_image.get_rect()
	
	    # 用于切换图片
	    switch_image = True
	
	    # 用于延迟
	    delay = 100
	
	    running = True
	
	    while running:
	        for event in pygame.event.get():	//从队列中获取事件
	            if event.type == QUIT:		//如果事件标识符是QUIT
	                pygame.quit()
	                sys.exit()
	
	            elif event.type == MOUSEBUTTONDOWN:
	                if event.button == 1 and paused_rect.collidepoint(event.pos):
	                    paused = not paused
	                    if paused:
	                        pygame.time.set_timer(SUPPLY_TIME, 0)
	                        pygame.mixer.music.pause()
	                        pygame.mixer.pause()
	                    else:
	                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
	                        pygame.mixer.music.unpause()
	                        pygame.mixer.unpause()
	
	            elif event.type == MOUSEMOTION:
	                if paused_rect.collidepoint(event.pos):
	                    if paused:
	                        paused_image = resume_pressed_image
	                    else:
	                        paused_image = pause_pressed_image
	                else:
	                    if paused:
	                        paused_image = resume_nor_image
	                    else:
	                       paused_image = pause_nor_image
	
	            elif event.type == KEYDOWN:
	                if event.key == K_SPACE:
	                    if bomb_num:
	                        bomb_num -= 1
	                        bomb_sound.play()
	                        for each in enemies:
	                            if each.rect.bottom > 0:
	                                each.active = False
	
	            elif event.type == SUPPLY_TIME:
	                supply_sound.play()
	                if choice([True, False]):
	                    bomb_supply.reset()
	                else:
	                    bullet_supply.reset()
	
	            elif event.type == DOUBLE_BULLET_TIME:
	                is_double_bullet = False
	                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
	
	            elif event.type == INVINCIBLE_TIME:
	                me.invincible = False
	                pygame.time.set_timer(INVINCIBLE_TIME, 0)
	                         
	
	        # 根据用户的得分增加难度
	        if level == 1 and score > 50000:
	            level = 2
	            upgrade_sound.play()
	            # 增加3架小型敌机、2架中型敌机和1架大型敌机
	            add_small_enemies(small_enemies, enemies, 3)
	            add_mid_enemies(mid_enemies, enemies, 2)
	            add_big_enemies(big_enemies, enemies, 1)
	            # 提升小型敌机的速度
	            inc_speed(small_enemies, 1)
	        elif level == 2 and score > 300000:
	            level = 3
	            upgrade_sound.play()
	            # 增加5架小型敌机、3架中型敌机和2架大型敌机
	            add_small_enemies(small_enemies, enemies, 5)
	            add_mid_enemies(mid_enemies, enemies, 3)
	            add_big_enemies(big_enemies, enemies, 2)
	            # 提升小型敌机的速度
	            inc_speed(small_enemies, 1)
	            inc_speed(mid_enemies, 1)
	        elif level == 3 and score > 600000:
	            level = 4
	            upgrade_sound.play()
	            # 增加5架小型敌机、3架中型敌机和2架大型敌机
	            add_small_enemies(small_enemies, enemies, 5)
	            add_mid_enemies(mid_enemies, enemies, 3)
	            add_big_enemies(big_enemies, enemies, 2)
	            # 提升小型敌机的速度
	            inc_speed(small_enemies, 1)
	            inc_speed(mid_enemies, 1)
	        elif level == 4 and score > 1000000:
	            level = 5
	            upgrade_sound.play()
	            # 增加5架小型敌机、3架中型敌机和2架大型敌机
	            add_small_enemies(small_enemies, enemies, 5)
	            add_mid_enemies(mid_enemies, enemies, 3)
	            add_big_enemies(big_enemies, enemies, 2)
	            # 提升小型敌机的速度
	            inc_speed(small_enemies, 1)
	            inc_speed(mid_enemies, 1)
	            
	
	        screen.blit(background, (0, 0))
	                
	        if life_num and not paused:
	            # 检测用户的键盘操作
	            key_pressed = pygame.key.get_pressed()
	
	            if key_pressed[K_w] or key_pressed[K_UP]:
	                me.moveUp()
	            if key_pressed[K_s] or key_pressed[K_DOWN]:
	                me.moveDown()
	            if key_pressed[K_a] or key_pressed[K_LEFT]:
	                me.moveLeft()
	            if key_pressed[K_d] or key_pressed[K_RIGHT]:
	                me.moveRight()
	
	            # 绘制全屏炸弹补给并检测是否获得
	            if bomb_supply.active:
	                bomb_supply.move()
	                screen.blit(bomb_supply.image, bomb_supply.rect)
	                if pygame.sprite.collide_mask(bomb_supply, me):
	                    get_bomb_sound.play()
	                    if bomb_num < 3:
	                        bomb_num += 1
	                    bomb_supply.active = False
	
	            # 绘制超级子弹补给并检测是否获得
	            if bullet_supply.active:
	                bullet_supply.move()
	                screen.blit(bullet_supply.image, bullet_supply.rect)
	                if pygame.sprite.collide_mask(bullet_supply, me):
	                    get_bullet_sound.play()
	                    is_double_bullet = True
	                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18 * 1000)
	                    bullet_supply.active = False
	
	            # 发射子弹
	            if not(delay % 10):
	                bullet_sound.play()
	                if is_double_bullet:
	                    bullets = bullet2
	                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
	                    bullets[bullet2_index+1].reset((me.rect.centerx+30, me.rect.centery))
	                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
	                else:
	                    bullets = bullet1
	                    bullets[bullet1_index].reset(me.rect.midtop)
	                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
	
	                
	            # 检测子弹是否击中敌机
	            for b in bullets:
	                if b.active:
	                    b.move()
	                    screen.blit(b.image, b.rect)
	                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
	                    if enemy_hit:
	                        b.active = False
	                        for e in enemy_hit:
	                            if e in mid_enemies or e in big_enemies:
	                                e.hit = True
	                                e.energy -= 1
	                                if e.energy == 0:
	                                    e.active = False
	                            else:
	                                e.active = False
	            
	            # 绘制大型敌机
	            for each in big_enemies:
	                if each.active:
	                    each.move()
	                    if each.hit:
	                        screen.blit(each.image_hit, each.rect)
	                        each.hit = False
	                    else:
	                        if switch_image:
	                            screen.blit(each.image1, each.rect)
	                        else:
	                            screen.blit(each.image2, each.rect)
	
	                    # 绘制血槽
	                    pygame.draw.line(screen, BLACK, \
	                                     (each.rect.left, each.rect.top - 5), \
	                                     (each.rect.right, each.rect.top - 5), \
	                                     2)
	                    # 当生命大于20%显示绿色，否则显示红色
	                    energy_remain = each.energy / enemy.BigEnemy.energy
	                    if energy_remain > 0.2:
	                        energy_color = GREEN
	                    else:
	                        energy_color = RED
	                    pygame.draw.line(screen, energy_color, \
	                                     (each.rect.left, each.rect.top - 5), \
	                                     (each.rect.left + each.rect.width * energy_remain, \
	                                      each.rect.top - 5), 2)
	                        
	                    # 即将出现在画面中，播放音效
	                    if each.rect.bottom == -50:
	                        enemy3_fly_sound.play(-1)
	                else:
	                    # 毁灭
	                    if not(delay % 3):
	                        if e3_destroy_index == 0:
	                            enemy3_down_sound.play()
	                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
	                        e3_destroy_index = (e3_destroy_index + 1) % 6
	                        if e3_destroy_index == 0:
	                            enemy3_fly_sound.stop()
	                            score += 10000
	                            each.reset()
	
	            # 绘制中型敌机：
	            for each in mid_enemies:
	                if each.active:
	                    each.move()
	
	                    if each.hit:
	                        screen.blit(each.image_hit, each.rect)
	                        each.hit = False
	                    else:
	                        screen.blit(each.image, each.rect)
	
	                    # 绘制血槽
	                    pygame.draw.line(screen, BLACK, \
	                                     (each.rect.left, each.rect.top - 5), \
	                                     (each.rect.right, each.rect.top - 5), \
	                                     2)
	                    # 当生命大于20%显示绿色，否则显示红色
	                    energy_remain = each.energy / enemy.MidEnemy.energy
	                    if energy_remain > 0.2:
	                        energy_color = GREEN
	                    else:
	                        energy_color = RED
	                    pygame.draw.line(screen, energy_color, \
	                                     (each.rect.left, each.rect.top - 5), \
	                                     (each.rect.left + each.rect.width * energy_remain, \
	                                      each.rect.top - 5), 2)
	                else:
	                    # 毁灭
	                    if not(delay % 3):
	                        if e2_destroy_index == 0:
	                            enemy2_down_sound.play()
	                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
	                        e2_destroy_index = (e2_destroy_index + 1) % 4
	                        if e2_destroy_index == 0:
	                            score += 6000
	                            each.reset()
	
	            # 绘制小型敌机：
	            for each in small_enemies:
	                if each.active:
	                    each.move()
	                    screen.blit(each.image, each.rect)
	                else:
	                    # 毁灭
	                    if not(delay % 3):
	                        if e1_destroy_index == 0:
	                            enemy1_down_sound.play()
	                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
	                        e1_destroy_index = (e1_destroy_index + 1) % 4
	                        if e1_destroy_index == 0:
	                            score += 1000
	                            each.reset()
	
	            # 检测我方飞机是否被撞
	            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
	            if enemies_down and not me.invincible:
	                me.active = False
	                for e in enemies_down:
	                    e.active = False
	            
	            # 绘制我方飞机
	            if me.active:
	                if switch_image:
	                    screen.blit(me.image1, me.rect)
	                else:
	                    screen.blit(me.image2, me.rect)
	            else:
	                # 毁灭
	                if not(delay % 3):
	                    if me_destroy_index == 0:
	                        me_down_sound.play()
	                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
	                    me_destroy_index = (me_destroy_index + 1) % 4
	                    if me_destroy_index == 0:
	                        life_num -= 1
	                        me.reset()
	                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)
	
	            # 绘制全屏炸弹数量
	            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
	            text_rect = bomb_text.get_rect()
	            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
	            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))
	
	            # 绘制剩余生命数量
	            if life_num:
	                for i in range(life_num):
	                    screen.blit(life_image, \
	                                (width-10-(i+1)*life_rect.width, \
	                                 height-10-life_rect.height))
	
	            # 绘制得分
	            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
	            screen.blit(score_text, (10, 5))
	
	        # 绘制游戏结束画面
	        elif life_num == 0:
	            # 背景音乐停止
	            pygame.mixer.music.stop()
	
	            # 停止全部音效
	            pygame.mixer.stop()
	
	            # 停止发放补给
	            pygame.time.set_timer(SUPPLY_TIME, 0)
	
	            if not recorded:
	                recorded = True
	                # 读取历史最高得分
	                with open("record.txt", "r") as f:
	                    record_score = int(f.read())
	
	                # 如果玩家得分高于历史最高得分，则存档
	                if score > record_score:
	                    with open("record.txt", "w") as f:
	                        f.write(str(score))
	
	            # 绘制结束画面
	            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
				//在新界面绘制文字，第一个参数文本，第二个参数是否开启抗锯齿，第三个是颜色
	            screen.blit(record_score_text, (50, 50))	//将文字添加到界面上
	            
	            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
	            gameover_text1_rect = gameover_text1.get_rect()
	            gameover_text1_rect.left, gameover_text1_rect.top = \
	                                 (width - gameover_text1_rect.width) // 2, height // 3
	            screen.blit(gameover_text1, gameover_text1_rect)
	            
	            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
	            gameover_text2_rect = gameover_text2.get_rect()
	            gameover_text2_rect.left, gameover_text2_rect.top = \
	                                 (width - gameover_text2_rect.width) // 2, \
	                                 gameover_text1_rect.bottom + 10
	            screen.blit(gameover_text2, gameover_text2_rect)
	
	            again_rect.left, again_rect.top = \
	                             (width - again_rect.width) // 2, \
	                             gameover_text2_rect.bottom + 50
	            screen.blit(again_image, again_rect)
	
	            gameover_rect.left, gameover_rect.top = \
	                                (width - again_rect.width) // 2, \
	                                again_rect.bottom + 10
	            screen.blit(gameover_image, gameover_rect)
	
	            # 检测用户的鼠标操作
	            # 如果用户按下鼠标左键
	            if pygame.mouse.get_pressed()[0]:
	                # 获取鼠标坐标
	                pos = pygame.mouse.get_pos()
	                # 如果用户点击“重新开始”
	                if again_rect.left < pos[0] < again_rect.right and \
	                   again_rect.top < pos[1] < again_rect.bottom:
	                    # 调用main函数，重新开始游戏
	                    main()
	                # 如果用户点击“结束游戏”            
	                elif gameover_rect.left < pos[0] < gameover_rect.right and \
	                     gameover_rect.top < pos[1] < gameover_rect.bottom:
	                    # 退出游戏
	                    pygame.quit()
	                    sys.exit()      
	
	        # 绘制暂停按钮
	        screen.blit(paused_image, paused_rect)
	
	        # 切换图片
	        if not(delay % 5):
	            switch_image = not switch_image
	
	        delay -= 1
	        if not delay:
	            delay = 100
	
	        pygame.display.flip()
	        clock.tick(60)
	        
	if __name__ == "__main__":
	    try:
	        main()
	    except SystemExit:
	        pass
	    except:
	        traceback.print_exc()
	        pygame.quit()
	        input()



	