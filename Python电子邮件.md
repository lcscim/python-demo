#8.20

#1.电子邮件
假设我们自己的电子邮件地址是me@163.com，对方的电子邮件地址是friend@sina.com（注意地址都是虚构的哈），现在我们用Outlook或者Foxmail之类的软件写好邮件，填上对方的Email地址，点“发送”，电子邮件就发出去了。这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。

Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等。由于我们自己的电子邮件是163.com，所以，Email首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。

Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。Email到达MDA后，就静静地躺在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。

一封电子邮件的旅程就是：

	发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

- 发邮件时：MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
- 收邮件时：MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等。

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是你要发到哪个MTA上。假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，因为它只服务新浪的用户，所以，你得填163提供的SMTP服务器地址：smtp.163.com，为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，这样，MUA才能正常地把Email通过SMTP协议发送到MTA。

类似的，从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。

在使用Python收发邮件前，请先准备好至少两个电子邮件，如xxx@163.com，xxx@sina.com，xxx@qq.com等，注意两个邮箱不要用同一家邮件服务商。

最后特别注意，目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录
##1.1SMTP发送邮件
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
- 构造一个最简单的纯文本邮件

		from email.mime.text import MIMEText
		msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
		#构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
- 通过SMTP发出去：

		# 输入Email地址和口令:
		from_addr = input('From: ')
		password = input('Password: ')
		# 输入收件人地址:
		to_addr = input('To: ')
		# 输入SMTP服务器地址:
		smtp_server = input('SMTP server: ')
		import smtplib
		server = smtplib.SMTP(smtp_server, 25) 
		# SMTP协议默认端口是25
		server.set_debuglevel(1)
		# set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
		server.login(from_addr, password)
		# login()方法用来登录SMTP服务器
		server.sendmail(from_addr, [to_addr], msg.as_string())
		# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
		server.quit()

完整示例：

	from email import encoders
	from email.header import Header
	from email.mime.text import MIMEText
	from email.utils import parseaddr, formataddr
	
	import smtplib
	
	def _format_addr(s):
	    name, addr = parseaddr(s)
	    return formataddr((Header(name, 'utf-8').encode(), addr))
	# 函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
	from_addr = input('From: ')
	password = input('Password: ')
	# 使用163邮箱时，密码为开启smtp的授权码
	to_addr = input('To: ')
	smtp_server = input('SMTP server: ')
	
	msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
	msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
	msg['To'] = _format_addr('管理员 <%s>' % to_addr)
	msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
	
	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()

- 发送HTML邮件

	如果我们要发送HTML邮件，而不是普通的纯文本文件怎么办？方法很简单，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：

		msg = MIMEText('<html><body><h1>Hello</h1>' +
    			'<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8') 
- 发送附件

	带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：

		# 邮件对象:
		msg = MIMEMultipart()
		msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
		msg['To'] = _format_addr('管理员 <%s>' % to_addr)
		msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
		
		# 邮件正文是MIMEText:
		msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
		
		# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
		with open('/Users/michael/Downloads/test.png', 'rb') as f:
		    # 设置附件的MIME和文件名，这里是png类型:
		    mime = MIMEBase('image', 'png', filename='test.png')
		    # 加上必要的头信息:
		    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
		    mime.add_header('Content-ID', '<0>')
		    mime.add_header('X-Attachment-Id', '0')
		    # 把附件的内容读进来:
		    mime.set_payload(f.read())
		    # 用Base64编码:
		    encoders.encode_base64(mime)
		    # 添加到MIMEMultipart:
		    msg.attach(mime)
- 发送图片

	大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。
	要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。

	把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：

		msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
		    '<p><img src="cid:0"></p>' +'</body></html>', 'html', 'utf-8'))

- 同时支持HTML和Plain格式

	办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。

	利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：

		msg = MIMEMultipart('alternative')
		msg['From'] = ...
		msg['To'] = ...
		msg['Subject'] = ...
		
		msg.attach(MIMEText('hello', 'plain', 'utf-8'))
		msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
		# 正常发送msg对象...
- 加密SMTP

	使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

	Gmail，提供的SMTP服务必须要加密传输。必须知道，Gmail的SMTP端口是587

		smtp_server = 'smtp.gmail.com'
		smtp_port = 587
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		# 剩下的代码和前面的一模一样:
		server.set_debuglevel(1)
		...
		# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样。
- 小结

	构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：

		Message
		+- MIMEBase
		   +- MIMEMultipart
		   +- MIMENonMultipart
		      +- MIMEMessage
		      +- MIMEText
		      +- MIMEImage

##1.2 POP3收取邮件
收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。

Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

- 所以，收取邮件分两步：

	第一步：用poplib把邮件的原始文本下载到本地；
	第二步：用email解析原始文本，还原为邮件对象。
###1.2.1 通过POP3下载邮件

	import poplib
	# 输入邮件地址, 口令和POP3服务器地址:
	email = input('Email: ')
	password = input('Password: ')
	pop3_server = input('POP3 server: ')
	# 连接到POP3服务器:
	server = poplib.POP3(pop3_server)
	# 可以打开或关闭调试信息:
	server.set_debuglevel(1)
	# 可选:打印POP3服务器的欢迎文字:
	print(server.getwelcome().decode('utf-8'))
	# 身份认证:
	server.user(email)
	server.pass_(password)
	
	# stat()返回邮件数量和占用空间:
	print('Messages: %s. Size: %s' % server.stat())
	# list()返回所有邮件的编号:
	resp, mails, octets = server.list()
	# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
	print(mails)
	
	# 获取最新一封邮件, 注意索引号从1开始:
	index = len(mails)
	resp, lines, octets = server.retr(index)
	
	# lines存储了邮件的原始文本的每一行,
	# 可以获得整个邮件的原始文本:
	msg_content = b'\r\n'.join(lines).decode('utf-8')
	# 稍后解析出邮件:
	msg = Parser().parsestr(msg_content)
	
	# 可以根据邮件索引号直接从服务器删除邮件:
	# server.dele(index)
	# 关闭连接:
	server.quit()
###1.2.2 解析邮件
	# 先导入必要的模块：
	from email.parser import Parser
	from email.header import decode_header
	from email.utils import parseaddr
	import poplib
	# 把邮件内容解析为Message对象：
	msg = Parser().parsestr(msg_content)
	# 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。所以我们要递归地打印出Message对象的层次结构：
	# indent用于缩进显示:
	def print_info(msg, indent=0):
	    if indent == 0:
	        for header in ['From', 'To', 'Subject']:
	            value = msg.get(header, '')
	            if value:
	                if header=='Subject':
	                    value = decode_str(value)
	                else:
	                    hdr, addr = parseaddr(value)
	                    name = decode_str(hdr)
	                    value = u'%s <%s>' % (name, addr)
	            print('%s%s: %s' % ('  ' * indent, header, value))
	    if (msg.is_multipart()):
	        parts = msg.get_payload()
	        for n, part in enumerate(parts):
	            print('%spart %s' % ('  ' * indent, n))
	            print('%s--------------------' % ('  ' * indent))
	            print_info(part, indent + 1)
	    else:
	        content_type = msg.get_content_type()
	        if content_type=='text/plain' or content_type=='text/html':
	            content = msg.get_payload(decode=True)
	            charset = guess_charset(msg)
	            if charset:
	                content = content.decode(charset)
	            print('%sText: %s' % ('  ' * indent, content + '...'))
	        else:
	            print('%sAttachment: %s' % ('  ' * indent, content_type))
	# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode：
	def decode_str(s):
	    value, charset = decode_header(s)[0]
	    if charset:
	        value = value.decode(charset)
	    return value
	# decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
	# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
	def guess_charset(msg):
	    charset = msg.get_charset()
	    if charset is None:
	        content_type = msg.get('Content-Type', '').lower()
	        pos = content_type.find('charset=')
	        if pos >= 0:
	            charset = content_type[pos + 8:].strip()
	    return charset
- 小结 

	用Python的poplib模块收取邮件分两步：第一步是用POP3协议把邮件获取到本地，第二步是用email模块把原始邮件解析为Message对象，然后，用适当的形式把邮件内容展示给用户即可。

接受总代码：

	from email.parser import Parser
	from email.header import decode_header
	from email.utils import parseaddr
	
	import poplib
	
	# 输入邮件地址, 口令和POP3服务器地址:
	email = input('Email: ')
	password = input('Password: ')
	pop3_server = input('POP3 server: ')
	
	def guess_charset(msg):
	    charset = msg.get_charset()
	    if charset is None:
	        content_type = msg.get('Content-Type', '').lower()
	        pos = content_type.find('charset=')
	        if pos >= 0:
	            charset = content_type[pos + 8:].strip()
	    return charset
	
	def decode_str(s):
	    value, charset = decode_header(s)[0]
	    if charset:
	        value = value.decode(charset)
	    return value
	
	def print_info(msg, indent=0):
	    if indent == 0:
	        for header in ['From', 'To', 'Subject']:
	            value = msg.get(header, '')
	            if value:
	                if header=='Subject':
	                    value = decode_str(value)
	                else:
	                    hdr, addr = parseaddr(value)
	                    name = decode_str(hdr)
	                    value = u'%s <%s>' % (name, addr)
	            print('%s%s: %s' % ('  ' * indent, header, value))
	    if (msg.is_multipart()):
	        parts = msg.get_payload()
	        for n, part in enumerate(parts):
	            print('%spart %s' % ('  ' * indent, n))
	            print('%s--------------------' % ('  ' * indent))
	            print_info(part, indent + 1)
	    else:
	        content_type = msg.get_content_type()
	        if content_type=='text/plain' or content_type=='text/html':
	            content = msg.get_payload(decode=True)
	            charset = guess_charset(msg)
	            if charset:
	                content = content.decode(charset)
	            print('%sText: %s' % ('  ' * indent, content + '...'))
	        else:
	            print('%sAttachment: %s' % ('  ' * indent, content_type))
	
	# 连接到POP3服务器:
	server = poplib.POP3(pop3_server)
	# 可以打开或关闭调试信息:
	server.set_debuglevel(1)
	# 可选:打印POP3服务器的欢迎文字:
	print(server.getwelcome().decode('utf-8'))
	# 身份认证:
	server.user(email)
	server.pass_(password)
	# stat()返回邮件数量和占用空间:
	print('Messages: %s. Size: %s' % server.stat())
	# list()返回所有邮件的编号:
	resp, mails, octets = server.list()
	# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
	print(mails)
	# 获取最新一封邮件, 注意索引号从1开始:
	index = len(mails)
	resp, lines, octets = server.retr(index)
	# lines存储了邮件的原始文本的每一行,
	# 可以获得整个邮件的原始文本:
	msg_content = b'\r\n'.join(lines).decode('utf-8')
	# 稍后解析出邮件:
	msg = Parser().parsestr(msg_content)
	print_info(msg)
	# 可以根据邮件索引号直接从服务器删除邮件:
	# server.dele(index)
	# 关闭连接:
	server.quit()
