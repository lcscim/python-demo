#7.23
线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
##1.多进程（multiprocessing）
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：

	from multiprocessing import Process
	import os
	
	# 子进程要执行的代码
	def run_proc(name):
	    print('Run child process %s (%s)...' % (name, os.getpid()))	
		# getpid()获取当前进程的ID
	if __name__=='__main__':
	    print('Parent process %s.' % os.getpid())
	    p = Process(target=run_proc, args=('test',))# 创建一个进程
	    print('Child process will start.')
	    p.start()	# 启动子进程
	    p.join()	# 等待子进程结束后再继续往下运行，通常用于进程间的同步。
	    print('Child process end.')
执行结果如下：

	Parent process 928.
	Process will start.
	Run child process test (929)...
	Process end.
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

- Pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

		from multiprocessing import Pool
		import os, time, random
		
		def long_time_task(name):
		    print('Run task %s (%s)...' % (name, os.getpid()))
		    start = time.time()
		    time.sleep(random.random() * 3)
		    end = time.time()
		    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
		
		if __name__=='__main__':
		    print('Parent process %s.' % os.getpid())
		    p = Pool(4)
		    for i in range(5):
		        p.apply_async(long_time_task, args=(i,))
		    print('Waiting for all subprocesses done...')
		    p.close()
		    p.join()
		    print('All subprocesses done.')
	对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

	请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
- 子进程 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

	subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

	下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

		import subprocess
		print('$ nslookup www.python.org')
		r = subprocess.call(['nslookup', 'www.python.org'])
		print('Exit code:', r)
	如果子进程还需要输入，则可以通过communicate()方法输入：
	
		import subprocess
		print('$ nslookup')
		p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
		print(output.decode('utf-8'))
		print('Exit code:', p.returncode)
	上面的代码相当于在命令行执行命令nslookup，然后手动输入：
- 进程间通信 Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

	我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

		from multiprocessing import Process, Queue
		import os, time, random
		
		# 写数据进程执行的代码:
		def write(q):
		    print('Process to write: %s' % os.getpid())
		    for value in ['A', 'B', 'C']:
		        print('Put %s to queue...' % value)
		        q.put(value)
		        time.sleep(random.random())
		
		# 读数据进程执行的代码:
		def read(q):
		    print('Process to read: %s' % os.getpid())
		    while True:
		        value = q.get(True)
		        print('Get %s from queue.' % value)
		
		if __name__=='__main__':
		    # 父进程创建Queue，并传给各个子进程：
		    q = Queue()
		    pw = Process(target=write, args=(q,))
		    pr = Process(target=read, args=(q,))
		    # 启动子进程pw，写入:
		    pw.start()
		    # 启动子进程pr，读取:
		    pr.start()
		    # 等待pw结束:
		    pw.join()
		    # pr进程里是死循环，无法等待其结束，只能强行终止:
		    pr.terminate()
- 小结

	在Unix/Linux下，可以使用fork()调用实现多进程。
	
	要实现跨平台的多进程，可以使用multiprocessing模块。
	
	进程间通信是通过Queue、Pipes等实现的。

##2.多线程
多任务可以由多进程完成，也可以由一个进程内的多线程完成。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

	import time, threading
	# 新线程执行的代码:
	def loop():
	    print('thread %s is running...' % threading.current_thread().name)
	    n = 0
	    while n < 5:
	        n = n + 1
	        print('thread %s >>> %s' % (threading.current_thread().name, n))
	        time.sleep(1)
	    print('thread %s ended.' % threading.current_thread().name)
	
	print('thread %s is running...' % threading.current_thread().name)
	t = threading.Thread(target=loop, name='LoopThread')
	t.start()
	t.join()
	print('thread %s ended.' % threading.current_thread().name)
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

- Lock 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

	如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：

		balance = 0
		lock = threading.Lock()
		def run_thread(n):
		    for i in range(100000):
		        # 先要获取锁:
		        lock.acquire()
		        try:
		            # 放心地改吧:
		            change_it(n)
		        finally:
		            # 改完了一定要释放锁:
		            lock.release()
小结
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。


#7.25

##1.python并发编程之多进程
##1.1multiprocessing模块介绍
python中的多线程无法利用多核优势，如果想要充分地使用多核CPU的资源（os.cpu_count()查看），在python中大部分情况需要使用多进程。Python提供了非常好用的多进程包multiprocessing。

multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。

multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。

##1.2 Process类的介绍
- 创建进程的类

	Process([group [, target [, name [, args [, kwargs]]]]])，由该类实例化得到的对象，表示一个子进程中的任务（尚未启动）
	
		强调：
		1. 需要使用关键字的方式来指定参数
		2. args指定的为传给target函数的位置参数，是一个元组形式，必须有逗号

- 参数介绍

	group参数未使用，值始终为None

	target表示调用对象，即子进程要执行的任务
	
	args表示调用对象的位置参数元组，args=(1,2,'hexin',)
	
	kwargs表示调用对象的字典,kwargs={'name':'hexin','age':18}
	
	name为子进程的名称
- 方法介绍

	p.start()：启动进程，并调用该子进程中的p.run() 
	p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法  
	
	p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
	p.is_alive():如果p仍然运行，返回True
	
	p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程
- 属性介绍

	p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置

	p.name:进程的名称
	
	p.pid：进程的pid
	
	p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
	
	p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）
1. 例1，创建并开启子进程的方式一

		import time
		import random
		from multiprocessing import Process
		def piao(name):
		    print('%s piao' %name)
		    time.sleep(random.randrange(1,5))
		    print('%s piao end' %name)
		p1=Process(target=piao,args=('e',)) #必须加,号
		p2=Process(target=piao,args=('a',))	#新建四个进程任务
		p3=Process(target=piao,args=('w',))
		p4=Process(target=piao,args=('y',))
		p1.start()
		p2.start()
		p3.start()
		p4.start()		# 开启四个进程
		print('主线程')
2. 例2，创建并开启子进程的方式二

		import time
		import random
		from multiprocessing import Process
		class Piao(Process):	//创建Piao类继承Process
		    def __init__(self,name):
		        super().__init__()
		        self.name=name
		    def run(self):	#重写父类run方法
		        print('%s piaoing' %self.name)
		
		        time.sleep(random.randrange(1,5))
		        print('%s piao end' %self.name)
		p1=Piao('e')
		p2=Piao('a')
		p3=Piao('w')
		p4=Piao('y')
		p1.start() #start会自动调用run
		p2.start()
		p3.start()
		p4.start()
		print('主线程')

	注意：在windows中Process()必须放到# if __name__ == '__main__':下
3. Process对象的其他方法或属性1

		#进程对象的其他方法一:terminate,is_alive
		from multiprocessing import Process
		import time
		import random
		class Piao(Process):
		    def __init__(self,name):
		        self.name=name
		        super().__init__()
		    def run(self):
		        print('%s is piaoing' %self.name)
		        time.sleep(random.randrange(1,5))
		        print('%s is piao end' %self.name)
		
		p1=Piao('e1')
		p1.start()
		p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
		print(p1.is_alive()) #结果为True
		print('开始')
		print(p1.is_alive()) #结果为False


		#进程对象的其他方法二:p.daemon=True,p.join
		from multiprocessing import Process
		import time
		import random
		class Piao(Process):
		    def __init__(self,name):
		        self.name=name
		        super().__init__()
		    def run(self):
		        print('%s is piaoing' %self.name)
		        time.sleep(random.randrange(1,3))
		        print('%s is piao end' %self.name)
		p=Piao('e')
		p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程死,p跟着一起死
		p.start()
		p.join(0.0001) #等待p停止,等0.0001秒就不再等了
		print('开始')

	注意：p.join(),是父进程在等p的结束，是父进程阻塞在原地，而p仍然在后台运行
4. 进程对象的其他属性:name,pid

		from multiprocessing import Process
		import time
		import random
		class Piao(Process):
		    def __init__(self,name):
		        # self.name=name
		        # super().__init__() #Process的__init__方法会执行self.name=Piao-1,
		        #                    #所以加到这里,会覆盖我们的self.name=name
		        #为我们开启的进程设置名字的做法
		        super().__init__()
		        self.name=name
		    def run(self):
		        print('%s is piaoing' %self.name)
		        time.sleep(random.randrange(1,3))
		        print('%s is piao end' %self.name)
		p=Piao('e')
		p.start()
		print('开始')
		print(p.pid) #查看pid
- 进程同步（锁）

	进程之间数据不共享,但是共享同一套文件系统,所以访问同一个文件,或同一个打印终端,是没有问题的。共享同一打印终端，发现会有多行内容打印到一行的现象（多个进程共享并抢占同一个打印终端，乱了）既然可以用文件共享数据，那么进程间通信用文件作为数据传输介质就可以了啊，可以，但是有问题：1.效率 2.需要自己加锁处理。加锁的目的是为了保证多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，没错，速度是慢了，牺牲了速度而保证了数据安全。
	 
	文件当做数据库，模拟抢票（Lock互斥锁）

		#文件db的内容为：{"count":2}
		#注意一定要用双引号，不然json无法识别
		from multiprocessing import Process,Lock
		import json
		import time
		import random
		import os
		def work(filename,lock): #买票
		    # lock.acquire()
		    with lock:
		        with open(filename,encoding='utf-8') as f:
		            dic=json.loads(f.read())
		            # print('剩余票数: %s' % dic['count'])
		        if dic['count'] > 0:
		            dic['count']-=1
		            time.sleep(random.randint(1,3)) #模拟网络延迟
		            with open(filename,'w',encoding='utf-8') as f:
		                f.write(json.dumps(dic))
		            print('%s 购票成功' %os.getpid())
		        else:
		            print('%s 购票失败' %os.getpid())
		    # lock.release()
		if __name__ == '__main__':
		    lock=Lock()
		    p_l=[]
		    for i in range(10):
		        p=Process(target=work,args=('db',lock))
		        p_l.append(p)
		        p.start()
		    for p in p_l:
		        p.join()
		    print('主线程')

##1.3 进程间的通信
进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。
- 进程间通信（IPC）方式一：队列（推荐使用）

	队列先进先出，栈后进先出。创建队列的类（底层就是以管道和锁定的方式实现）：
	
		Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
			参数介绍：maxsize是队列中允许最大项数，省略则无大小限制。
	方法介绍：

		q.put方法用以插入数据到队列中
		put方法还有两个可选参数：blocked和timeout。
		如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
		如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
		q.get方法可以从队列读取并且删除一个元素。
		get方法有两个可选参数：blocked和timeout。
		如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。
		如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.
		q.get_nowait():同q.get(False)
		q.put_nowait():同q.put(False)
		q.empty():调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
		q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
		q.qsize():返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样


		'''
		multiprocessing模块支持进程间通信的两种主要形式:管道和队列
		都是基于消息传递实现的,但是队列接口
		'''
		from multiprocessing import Process,Queue
		import time
		q=Queue(3)
		#put ,get ,put_nowait,get_nowait,full,empty
		q.put(3)
		q.put(3)
		q.put(3)
		print(q.full()) #满了
		print(q.get())
		print(q.get())
		print(q.get())
		print(q.empty()) #空了

##1.4 进程池
开多进程的目的是为了并发，如果有多核，通常有几个核就开几个进程，进程开启过多，效率反而会下降（开启进程是需要占用系统资源的，而且开启多余核数目的进程也无法做到并行），但很明显需要并发执行的任务要远大于核数，这时我们就可以通过维护一个进程池来控制进程数目，比如httpd的进程模式，规定最小进程数和最大进程数...    

当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。而且对于远程过程调用的高级应用程序而言，应该使用进程池，Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，就重用进程池中的进程。

在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。

	创建进程池的类：
	Pool([numprocess  [,initializer [, initargs]]]):创建进程池
    参数介绍：
	numprocess:要创建的进程数，如果省略，将默认使用cpu_count()的值
	initializer：是每个工作进程启动时要执行的可调用对象，默认为None
	initargs：是要传给initializer的参数组

	方法介绍：
	p.apply(func [, args [, kwargs]]):在一个池工作进程中执行func(*args,**kwargs),然后返回结果。需要强调的是：此操作并不会在所有池工作进程中并执行func函数。如果要通过不同参数并发地执行func函数，必须从不同线程调用p.apply()函数或者使用p.apply_async()
	p.apply_async(func [, args [, kwargs]]):在一个池工作进程中执行func(*args,**kwargs),然后返回结果。此方法的结果是AsyncResult类的实例，callback是可调用对象，接收输入参数。当func的结果变为可用时，将理解传递给callback。callback禁止执行任何阻塞操作，否则将接收其他异步操作中的结果。
	   
	p.close():关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成5 P.jion():等待所有工作进程退出。此方法只能在close（）或teminate()之后调用
	方法apply_async()和map_async（）的返回值是AsyncResul的实例obj。实例具有以下方法
	obj.get():返回结果，如果有必要则等待结果到达。timeout是可选的。如果在指定时间内还没有到达，将引发一场。如果远程操作中引发了异常，它将在调用此方法时再次被引发。
	obj.ready():如果调用完成，返回True
	obj.successful():如果调用完成且没有引发异常，返回True，如果在结果就绪之前调用此方法，引发异常
	obj.wait([timeout]):等待结果变为可用。
	obj.terminate()：立即终止所有工作进程，同时不执行任何清理或结束任何挂起工作。如果p被垃圾回收，将自动调用此函数

https://www.cnblogs.com/smallmars/p/7093603.html