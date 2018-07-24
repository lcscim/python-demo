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
