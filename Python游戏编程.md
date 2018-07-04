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
		position = turtle.get_rect()
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