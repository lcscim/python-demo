#8.18

#1.网络编程
计算机网络就是把各个计算机连接到一起，让网络中的计算机可以互相通信。网络编程就是如何在程序中实现两台计算机的通信。
##1.1TCP/IP简介
把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。最重要的两个协议是TCP和IP协议。大家把互联网的协议简称TCP/IP协议。

通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。互联网上每个计算机的唯一标识就是IP地址，类似123.123.123.123。如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。

- IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。

	IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。

	IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于2001:0db8:85a3:0042:1000:8a2e:0370:7334。
- TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

	一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
	
	在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

	一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。
##1.2TCP编程
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
##1.2.1客户端
大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。

举个例子，当我们在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。如果一切顺利，新浪的服务器接受了我们的连接，一个TCP连接就建立起来的，后面的通信就是发送网页内容了。所以，我们要创建一个基于TCP连接的Socket，可以这样做：

	# 导入socket库:
	import socket
	# 创建一个socket:AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此百度提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 建立连接:客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。参数是一个tuple，包含地址和端口号。
	s.connect(('www.baidu.com', 80))
	# 发送数据:发送的文本格式必须符合HTTP标准
	s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
	# 接收数据:while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
	buffer = []
	while True:
	    # 每次最多接收1k字节:调用recv(max)方法，一次最多接收指定的字节数
	    d = s.recv(1024)
	    if d:
	        buffer.append(d)
	    else:
	        break
	data = b''.join(buffer)
	# 关闭连接:当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了
	s.close()
	header, html = data.split(b'\r\n\r\n', 1)
	print(header.decode('utf-8'))
	# 把接收的数据写入文件:接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
	with open('baidu.html', 'wb') as f:
	    f.write(html)
注意：

- 其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
- TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

###1.2.2服务器
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

示例：
- 服务端

		import socket
		import threading
		import time
		# 创建一个基于IPv4和TCP协议的Socket：
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 监听端口:127.0.0.1是一个特殊的IP地址，表示本机地址。这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
		s.bind(('127.0.0.1', 9999))
		# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
		s.listen(5)
		print('Waiting for connection...')
		# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
		def tcplink(sock, addr):
		    print('Accept new connection from %s:%s...' % addr)
		    sock.send(b'Welcome!')
		    while True:
		        data = sock.recv(1024)
		        time.sleep(1)
		        if not data or data.decode('utf-8') == 'exit':
		            break
		        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
		    sock.close()
		    print('Connection from %s:%s closed.' % addr)
		# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
		while True:
		    # 接受一个新连接:
		    sock, addr = s.accept()
		    # 创建新线程来处理TCP连接:
		    t = threading.Thread(target=tcplink, args=(sock, addr))
		    t.start()
- 客户端

		import socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 建立连接:
		s.connect(('127.0.0.1', 9999))
		# 接收欢迎消息:
		print(s.recv(1024).decode('utf-8'))
		for data in [b'Michael', b'Tracy', b'Sarah']:
		    # 发送数据:
		    s.send(data)
		    print(s.recv(1024).decode('utf-8'))
		s.send(b'exit')
		s.close()
##1.3UDP编程
TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

	优点：和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
	缺点：UDP传输数据不可靠
和TCP类似，使用UDP的通信双方也分为客户端和服务器。
###1.3.1服务器

	import socket
	import threading
	import time
	# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 绑定端口:
	s.bind(('127.0.0.1', 9999))
	print('Bind UDP on 9999...')
	def tcplink(data,addr):
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)
	while True:
		# recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
	    data, addr = s.recvfrom(1024)
	    t = threading.Thread(target=tcplink, args=(data, addr))
	    t.start()
###1.3.2客户端

	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	for data in [b'Michael', b'Tracy', b'Sarah']:
	    # 发送数据:
	    s.sendto(data, ('127.0.0.1', 9999))
	    # 接收数据:
	    print(s.recv(1024).decode('utf-8'))
	s.close()



#9.16

##1.网络通信要素
- IP地址

	1. 用来标识网络上一台独立的主机
	2. IP地址 = 网络地址+主机地址（网络地址：用于识别主机所在的网络/网段；主机地址：用来标识该网络上的主机）
	3. 特殊的IP地址：127.0.0.1（本地回环地址，保留地址，点分十进制，可用于测试网卡是否故障，表示本机）
- 端口号

	1. 用于表示进程的逻辑地址，不同的进程有不同的端口标识
	2. 端口：要将数据发送到对方指定的应用程序上，为了表示这些应用程序，所应对这些网络应用程序都用数据进行了表示。为了方便称呼这些数字，则将这些数字称为端口，是逻辑端口
- 传输协议：通讯的规则。如：TCP，UDP

	- IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
	- TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。
	- TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
##2.TCP
访问百度

	# 导入socket库:
	import socket
	# 创建一个socket:AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此百度提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 建立连接:客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号。参数是一个tuple，包含地址和端口号。
	s.connect(('www.baidu.com', 80))
	# 发送数据:发送的文本格式必须符合HTTP标准
	s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
	# 接收数据:while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
	buffer = []
	while True:
	    # 每次最多接收1k字节:调用recv(max)方法，一次最多接收指定的字节数
	    d = s.recv(1024)
	    if d:
	        buffer.append(d)
	    else:
	        break
	data = b''.join(buffer)
	# 关闭连接:当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了
	s.close()
	header, html = data.split(b'\r\n\r\n', 1)
	print(header.decode('utf-8'))
	# 把接收的数据写入文件:接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
	with open('baidu.html', 'wb') as f:
	    f.write(html)
- 服务端

		import socket
		import threading
		import time
		# 创建一个基于IPv4和TCP协议的Socket：
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 监听端口:127.0.0.1是一个特殊的IP地址，表示本机地址。这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
		s.bind(('127.0.0.1', 9999))
		# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
		s.listen(5)
		print('Waiting for connection...')
		# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
		def tcplink(sock, addr):
		    print('Accept new connection from %s:%s...' % addr)
		    sock.send(b'Welcome!')
		    while True:
		        data = sock.recv(1024)
		        time.sleep(1)
		        if not data or data.decode('utf-8') == 'exit':
		            break
		        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
		    sock.close()
		    print('Connection from %s:%s closed.' % addr)
		# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
		while True:
		    # 接受一个新连接:
		    sock, addr = s.accept()
		    # 创建新线程来处理TCP连接:
		    t = threading.Thread(target=tcplink, args=(sock, addr))
		    t.start()
- 客户端

		import socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 建立连接:
		s.connect(('127.0.0.1', 9999))
		# 接收欢迎消息:
		print(s.recv(1024).decode('utf-8'))
		for data in [b'Michael', b'Tracy', b'Sarah']:
		    # 发送数据:
		    s.send(data)
		    print(s.recv(1024).decode('utf-8'))
		s.send(b'exit')
		s.close()
具体流程如下
![](https://i.imgur.com/E1mZvrn.jpg)


#9.19

##1.socket，可聊天应用
服务端

	import socket
	
	s = socket.socket()
	address = ('127.0.0.1',8888)
	s.bind(address)
	s.listen(3)
	while 1:
	    conn,addr = s.accept()
	    print(addr)
	    while 1:
	        try:
	            data = conn.recv(1024)
	        except Exception:
	            break
	        print('.......',str(data,'utf8'))
	        inp = input('>>>')
	        conn.send(bytes(inp,'utf8'))
	s.close()
客户端

	import socket
	
	s = socket.socket()
	print(s)
	address = ('127.0.0.1',8888)
	s.connect(address)
	while True:
	
	    inp = input('>>>')
	    if inp == 'exit':
	        break
	    s.send(bytes(inp,'utf8'))
	    data = s.recv(1024)
	    print(str(data,'utf8'))
	s.close()
##2.远程执行命令

	#------------------------------------------------server
	#------------------------------------------------
	import socket
	import subprocess
	ip_port = ('127.0.0.1',8879)
	sk = socket.socket()
	sk.bind(ip_port)
	sk.listen(5)
	print ("服务端启动...")
	while True:
	    conn,address = sk.accept()
	    while True:
	        try:
	
	            client_data=conn.recv(1024)
	        except Exception:
	            break
	        print (str(client_data,"utf8"))
	        print ("waiting...")
	        # server_response=input(">>>")
	        # conn.sendall(bytes(server_response,"utf8"))
	        cmd=str(client_data,"utf8").strip()		//删除命令行左和右的空格
	        cmd_call=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
				//传入cmd参数，把shell设置成True，指定的命令会在shell里解释执行。 ，subprocess.PIPE表示创建一个通道
	        cmd_result=cmd_call.stdout.read()	//对cmd返回的对象进行读取
	        if len(cmd_result)==0:
	            cmd_result=b"no output!"
	        conn.sendall(cmd_result)	//将返回的数据发送回客户端
	        print('send data size',len(cmd_result))
	        print('******************')
	        print('******************')
	        print('******************')
	
	    conn.close()
	    
	#------------------------------------------------client 
	#------------------------------------------------
	import socket
	ip_port = ('127.0.0.1',8879)
	sk = socket.socket()
	sk.connect(ip_port)
	print ("客户端启动：")
	while True:
	    inp = input('cdm:>>>').strip( )
	    if len(inp)==0:
	        continue
	    if inp=="q":
	        break
	    sk.sendall(bytes(inp,"utf8"))
	    server_response=sk.recv(1024)
	    print (str(server_response,"gbk"))
	    print('receive data size',len(server_response))
	    if inp == 'exit':
	        break
	sk.close()

- subprocess.Popen

	subprocess模块定义了一个类： Popen
		class subprocess.Popen( args, 
		      bufsize=0, 
		      executable=None,
		      stdin=None,
		      stdout=None, 
		      stderr=None, 
		      preexec_fn=None, 
		      close_fds=False, 
		      shell=False, 
		      cwd=None, 
		      env=None, 
		      universal_newlines=False, 
		      startupinfo=None, 
		      creationflags=0)
	![](http://img1.51cto.com/attachment/201203/120613646.jpg)


#9.20

##1.粘包现象
连续两次或多次发送信息，有可能出现错误，这种现象叫做粘包现象

解决办法：在两次发送间隔断一下如：

	...
	conn.sendall(cmd_result)
	conn.recv(1024)
	conn.sendall(cmd)
	...
##2.编码
- Python3中只有两种数据类型 str byte
- 由str>>>bytes:  编码（encode方法）
- 由bytes>>>str:  解码（decode方法）

##3.文件上传

	import socket,os
	ip_port=("127.0.0.1",8898)
	sk=socket.socket()
	sk.bind(ip_port)
	sk.listen(5)
	BASE_DIR=os.path.dirname(os.path.abspath(__file__))
	#获取文件的路径
	while True:
	    print("waiting connect")
	    conn,addr=sk.accept()
	    flag = True
	    while flag:
	
	            client_bytes=conn.recv(1024)
	            client_str=str(client_bytes,"utf8")
	            func,file_byte_size,filename=client_str.split("|",2)
	
	            path=os.path.join(BASE_DIR,'yuan',filename)
	            has_received=0
	            file_byte_size=int(file_byte_size)
	
	            f=open(path,"wb")
	            while has_received<file_byte_size:
	                data=conn.recv(1024)
	                f.write(data)
	                has_received+=len(data)
	            print("ending")
	            f.close()
	
	#----------------------------------------------client
	#----------------------------------------------
	import socket
	import re,os,sys
	ip_port=("127.0.0.1",8898)
	sk=socket.socket()
	sk.connect(ip_port)
	BASE_DIR=os.path.dirname(os.path.abspath(__file__))
	print("客户端启动....")
	
	while True:
	    inp=input("please input:")
	
	    if inp.startswith("post"):
	        method,local_path=inp.split("|",1)
	        local_path=os.path.join(BASE_DIR,local_path)
	        file_byte_size=os.stat(local_path).st_size
	        file_name=os.path.basename(local_path)
	        post_info="post|%s|%s"%(file_byte_size,file_name)
	        sk.sendall(bytes(post_info,"utf8"))
	        has_sent=0
	        file_obj=open(local_path,"rb")
	        while has_sent<file_byte_size:
	            data=file_obj.read(1024)
	            sk.sendall(data)
	            has_sent+=len(data)
	        file_obj.close()
	        print("上传成功")