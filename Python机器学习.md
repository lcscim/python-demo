#机器学习
##1.认识机器学习
利用计算机从历史数据中找出规律，并把这些规律用到对未来不确定场景的决策
##2.机器学习的典型应用
- 典型应用-购物车纸尿裤和啤酒
- 典型应用-聚类即用户细分精准营销
- 典型应用-垃圾邮件处理和信用卡欺诈
- 典型应用-ctr预估和协同过滤
- 典型应用自然语言处理和图像识别
##3.数据分析和机器学习的区别
##4.常见的算法和分类
##5.解决问题
##6.图片识别demo演示
- 需安装一下模块

		pip install scipy
		pip install opencv-python
示例如下：

	import cv2	//OpenCV是一个C++库，用于实时处理计算机视觉方面的问题，涵盖了很多计算机视觉领域的模块。 
	import numpy as np
	import os
	from scipy.cluster.vq import *	//Scipy是一个高级的科学计算库，它和Numpy联系很密切，Scipy一般都是操控Numpy数组来进行科学计算，所以可以说是基于Numpy之上了。Scipy有很多子模块可以应对不同的应用，例如插值运算，优化算法、图像处理、数学统计等。
	import shutil	//高级的 文件、文件夹、压缩包 处理模块
	import colorsys	//颜色转换
	
	class imageKmeans(object):
	    #初始化
	    def __init__(self, k):
	        self.basedir = os.path.dirname(os.path.abspath(__file__))  //os.path.dirname()返回脚本的绝对路径路径
	        self.imagedir = os.path.join(self.basedir, 'flowers')  //获取当前目录并和后面组成新目录
	        self.k = k  #簇的个数
	        for i in range(self.k):  # 创建k个文件夹用于存放分类后的图片
	            clusterDir = os.path.join(self.basedir, 'cluster-{}'.format(i))
	            if not os.path.isdir(clusterDir):
	                os.mkdir(clusterDir)
	
	    # 返回图片一维数组
	    def _loadImages(self):
	        images = os.listdir(self.imagedir)
	        imagesfiles = [os.path.join(self.imagedir, image) for image in images]
	        return imagesfiles
	
	    # 将h,s,v合并
	    def _hsvToL(self, h, s, v):
	        OH = 0
	        if (h <= 20 or h > 315):
	            OH = 0
	        if (h > 20 and h <= 40):
	            OH = 1
	        if (h > 40 and h <= 75):
	            OH = 2
	        if (h > 75 and h <= 155):
	            OH = 3
	        if (h > 155 and h <= 190):
	            OH = 4
	        if (h > 190 and h <= 271):
	            OH = 5
	        if (h > 271 and h <= 295):
	            OH = 6
	        if (h > 295 and h <= 315):
	            OH = 7
	
	        OS = 0
	        if (s >= 0 and s <= 0.2):
	            OS = 0
	        if (s > 0.2 and s < 0.7):
	            OS = 1
	        if (s > 0.7 and s <= 1.0):
	            OS = 2
	
	        OV = 0
	        if (v >= 0 and v <= 0.2):
	            OV = 0
	        if (v > 0.2 and v <= 0.7):
	            OV = 1
	        if (v > 0.7 and v <= 1.0):
	            OV = 2
	
	        L = 9 * OH + 3 * OS + OV
	        assert L >= 0 and L <= 71		//程序为假抛出AssertionError异常，该方法停止，确保条件一定成立才运行
	        return L
	
	    # 提取图片特征
	    def _getColor(self,oneImage):
	        image = cv2.imread(oneImage)	//使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
	        image = cv2.resize(image, (600, 600))	//调整图像大小。
	        Row = image.shape[0]  # 行600
	        Col = image.shape[1]  # 列600		//查看数组的维数
	        vector = [0]*12
	        for row in range(Row):
	            for col in range(Col):
	                b, g, r = image[row][col]	//获取每个像素的bgr值
	                h, s, v = colorsys.rgb_to_hsv(r / 255., g / 255., b / 255.)		//将颜色从RGB坐标转换为HSV坐标。
	                h *= 360
	                L = self._hsvToL(h,s,v)
	                vector[L//6] += L   #L//6范围 0~11
	        Lsum = sum(vector)
	        result = [v*1.0/Lsum for v in vector]
	        return result
	
	    #调用Kmeans
	    def getCluster(self):
	        images = self._loadImages() #图片一维数组(绝对地址)
	        Avector = []
	        for oneImage in images:
	            Vector = self._getColor(oneImage)
	            print(Vector)
	            Avector.append(Vector)
	        image_list = np.reshape(Avector,(len(images),-1))
	        cu, fangcha = kmeans(image_list, self.k)
	        fenlei, juli = vq(image_list, cu)
	        print(fenlei)
	        for i in range(len(images)):
	            for j in range(self.k):
	                if ( fenlei[i] == j ):
	                    shutil.copyfile(images[i], os.path.join(os.path.join(self.basedir,'cluster-{}'.format(j)), os.path.basename(images[i])))
	
	#主函数
	if __name__ == '__main__':
	    imagekmeans = imageKmeans(3)
	    imagekmeans.getCluster()

##7.OpenCV API 开发文档
OpenCV是一个基于BSD许可（开源）发行的跨平台计算机视觉库，可以运行在Linux、Windows、Android和Mac OS操作系统上。它轻量级而且高效——由一系列 C 函数和少量 C++ 类构成，同时提供了Python、Ruby、MATLAB等语言的接口，实现了图像处理和计算机视觉方面的很多通用算法。<br/>
OpenCV用C++语言编写，它的主要接口也是C++语言，但是依然保留了大量的C语言接口。该库也有大量的Python、Java and MATLAB/OCTAVE（版本2.5）的接口。这些语言的API接口函数可以通过在线文档获得。如今也提供对于C#、Ch、Ruby,GO的支持。<br/>

文档地址：https://docs.opencv.org/2.4/modules/refman.html

###7.1
- cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) 调整图像大小

	src - 输入图像。
	dst - 输出图像; 它具有尺寸dsize（当它是不为零）或大小从计算src.size()，fx和fy; 的类型dst是相同的src。
	dsize - 输出图像尺寸; 如果它等于零，则计算如下：
		dsize = Size（round（fx * src.cols），round（fy * src.rows））
		无论是 dsize 或两者 fx 并 fy 必须为非零。
	fx -沿水平轴的比例因子; 当它等于0时，计算为
		（double）dsize.width / src.cols}
	fy -沿垂直轴的比例因子; 当它等于0时，计算为
		（double）dsize.height / src.rows}

	插值 -插值方法：

		INTER_NEAREST - 最近邻插值
		INTER_LINEAR - 双线性插值（默认使用）
		INTER_AREA - 使用像素区域关系重新采样。它可能是图像抽取的首选方法，因为它可以提供无莫尔条纹的结果。但是当图像被缩放时，它与INTER_NEAREST 方法类似 。
		INTER_CUBIC - 4x4像素邻域上的双三次插值
		INTER_LANCZOS4 - 8x8像素邻域的Lanczos插值
- cv2.imread(filename[, flags]) → 从文件加载图片，

	filename - 要加载的文件的名称。
	flag - 指定加载图像的颜色类型的标志：

	
##8.numpy
NumPy系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。

一个用python实现的科学计算包。包括：1、一个强大的N维数组对象Array；2、比较成熟的（广播）函数库；3、用于整合C/C++和Fortran代码的工具包；4、实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。

NumPy（Numeric Python）提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如：Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。

文档地址：https://docs.scipy.org/doc/numpy/index.html
###8.1
- shape()shape函数是numpy.core.fromnumeric中的函数，它的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度。shape的输入参数可以是一个整数（表示维度），也可以是一个矩阵。

##9.shutil
shutil模块对文件和文件集合提供了许多高级操作。特别是，提供了支持文件复制和删除的功能。

文档地址：https://docs.python.org/2/library/shutil.html
##10.colorsys- 颜色系统之间的转换
colorsys模块定义了在计算机监视器中使用的RGB（红绿蓝）颜色空间和三个其他坐标系统中表示的颜色之间的颜色值的双向转换：YIQ，HLS（色调亮度饱和度）和HSV（色调饱和度值）。所有这些颜色空间中的坐标都是浮点值。在YIQ空间中，Y坐标介于0和1之间，但I和Q坐标可以是正数或负数。在所有其他空间中，坐标都在0和1之间。

文档地址：https://docs.python.org/2/library/colorsys.html

该colorsys模块定义了以下功能：

	colorsys.rgb_to_yiq（r，g，b ）将颜色从RGB坐标转换为YIQ坐标。
	colorsys.yiq_to_rgb（y，i，q ）将颜色从YIQ坐标转换为RGB坐标。
	colorsys.rgb_to_hls（r，g，b ）将颜色从RGB坐标转换为HLS坐标。
	colorsys.hls_to_rgb（h，l，s ）将颜色从HLS坐标转换为RGB坐标。
	colorsys.rgb_to_hsv（r，g，b ）将颜色从RGB坐标转换为HSV坐标。
	colorsys.hsv_to_rgb（h，s，v ）将颜色从HSV坐标转换为RGB坐标。

##11.scipy
是数学，科学和工程的开源软件。

文档地址：https://docs.scipy.org/doc/scipy/reference/


#7.17
tips：


##1. 学习笔记（一）：k-近邻算法
k近邻法(k-nearest neighbor, k-NN)是1967年由Cover T和Hart P提出的一种基本分类与回归方法。它的工作原理是：存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一个数据与所属分类的对应关系。输入没有标签的新数据后，将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。

    举个简单的例子，我们可以使用k-近邻算法分类一个电影是爱情片还是动作片。

		电影名称	 打斗镜头  接吻镜头 电影类型
		电影1		1		101		爱情片
		电影2		5		89		爱情片
		电影3		108		5		动作片
		电影4		115		8		动作片