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
1. k近邻法(k-nearest neighbor, k-NN)是1967年由Cover T和Hart P提出的一种基本分类与回归方法。它的工作原理是：存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，即我们知道样本集中每一个数据与所属分类的对应关系。输入没有标签的新数据后，将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类。

    举个简单的例子，我们可以使用k-近邻算法分类一个电影是爱情片还是动作片。

		电影名称	 打斗镜头  接吻镜头 电影类型
		电影1		1		101		爱情片
		电影2		5		89		爱情片
		电影3		108		5		动作片
		电影4		115		8		动作片

表1.1 就是我们已有的数据集合，也就是训练样本集。这个数据集有两个特征，即打斗镜头数和接吻镜头数。除此之外，我们也知道每个电影的所属类型，即分类标签。用肉眼粗略地观察，接吻镜头多的，是爱情片。打斗镜头多的，是动作片。以我们多年的看片经验，这个分类还算合理。如果现在给我一部电影，你告诉我这个电影打斗镜头数和接吻镜头数。不告诉我这个电影类型，我可以根据你给我的信息进行判断，这个电影是属于爱情片还是动作片。而k-近邻算法也可以像我们人一样做到这一点，不同的地方在于，我们的经验更"牛逼"，而k-近邻算法是靠已有的数据。比如，你告诉我这个电影打斗镜头数为2，接吻镜头数为102，我的经验会告诉你这个是爱情片，k-近邻算法也会告诉你这个是爱情片。你又告诉我另一个电影打斗镜头数为49，接吻镜头数为51，我"邪恶"的经验可能会告诉你，这有可能是个"爱情动作片"，画面太美，我不敢想象。 (如果说，你不知道"爱情动作片"是什么？请评论留言与我联系，我需要你这样像我一样纯洁的朋友。) 但是k-近邻算法不会告诉你这些，因为在它的眼里，电影类型只有爱情片和动作片，它会提取样本集中特征最相似数据(最邻近)的分类标签，得到的结果可能是爱情片，也可能是动作片，但绝不会是"爱情动作片"。当然，这些取决于数据集的大小以及最近邻的判断标准等因素。

2. 距离度量

	我们已经知道k-近邻算法根据特征比较，然后提取样本集中特征最相似数据(最邻近)的分类标签。那么，如何进行比较呢？比如，我们还是以表1.1为例，怎么判断红色圆点标记的电影所属的类别呢？ 如下图所示。

![打斗镜头](http://cuijiahua.com/wp-content/uploads/2017/11/ml_1_10-1.jpg)
我们可以从散点图大致推断，这个红色圆点标记的电影可能属于动作片，因为距离已知的那两个动作片的圆点更近。k-近邻算法用什么方法进行判断呢？没错，就是距离度量。这个电影分类的例子有2个特征，也就是在2维实数向量空间，可以使用我们高中学过的两点距离公式计算距离，如图1.2所示。

![](http://cuijiahua.com/wp-content/uploads/2017/11/ml_1_3.jpg)

通过计算，我们可以得到如下结果：

		(101,20)->动作片(108,5)的距离约为16.55
		(101,20)->动作片(115,8)的距离约为18.44
		(101,20)->爱情片(5,89)的距离约为118.22
		(101,20)->爱情片(1,101)的距离约为128.69
	通过计算可知，红色圆点标记的电影到动作片 (108,5)的距离最近，为16.55。如果算法直接根据这个结果，判断该红色圆点标记的电影为动作片，这个算法就是最近邻算法，而非k-近邻算法。那么k-近邻算法是什么呢？k-近邻算法步骤如下：

	计算已知类别数据集中的点与当前点之间的距离；
		按照距离递增次序排序；
		选取与当前点距离最小的k个点；
		确定前k个点所在类别的出现频率；
		返回前k个点所出现频率最高的类别作为当前点的预测分类。
	比如，现在我这个k值取3，那么在电影例子中，按距离依次排序的三个点分别是动作片(108,5)、动作片(115,8)、爱情片(5,89)。在这三个点中，动作片出现的频率为三分之二，爱情片出现的频率为三分之一，所以该红色圆点标记的电影为动作片。这个判别过程就是k-近邻算法。
3. Python3代码实现

	我们已经知道了k-近邻算法的原理，那么接下来就是使用Python3实现该算法，依然以电影分类为例。
	(1)准备数据集对于表1.1中的数据，我们可以使用numpy直接创建，代码如下：

		import numpy as np
		 
		"""
		函数说明:创建数据集
		 
		Parameters:
		    无
		Returns:
		    group - 数据集
		    labels - 分类标签
		Modify:
		    2017-07-13
		"""
		def createDataSet():
		    #四组二维特征
		    group = np.array([[1,101],[5,89],[108,5],[115,8]])
		    #四组特征的标签
		    labels = ['爱情片','爱情片','动作片','动作片']
		    return group, labels
		if __name__ == '__main__':
		    #创建数据集
		    group, labels = createDataSet()
		    #打印数据集
		    print(group)
		    print(labels)
	(2)k-近邻算法，根据两点距离公式，计算距离，选择距离最小的前k个点，并返回分类结果。
	
		import numpy as np
		import operator
		 
		"""
		函数说明:创建数据集
		 
		Parameters:
		    无
		Returns:
		    group - 数据集
		    labels - 分类标签
		Modify:
		    2017-07-13
		"""
		def createDataSet():
		    #四组二维特征
		    group = np.array([[1,101],[5,89],[108,5],[115,8]])
		    #四组特征的标签
		    labels = ['爱情片','爱情片','动作片','动作片']
		    return group, labels
		 
		"""
		函数说明:kNN算法,分类器
		 
		Parameters:
		    inX - 用于分类的数据(测试集)
		    dataSet - 用于训练的数据(训练集)
		    labes - 分类标签
		    k - kNN算法参数,选择距离最小的k个点
		Returns:
		    sortedClassCount[0][0] - 分类结果
		 
		Modify:
		    2017-07-13
		"""
		def classify0(inX, dataSet, labels, k):
		    #numpy函数shape[0]返回dataSet的行数
		    dataSetSize = dataSet.shape[0]
		    #在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
		    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
		    #二维特征相减后平方
		    sqDiffMat = diffMat**2
		    #sum()所有元素相加，sum(0)列相加，sum(1)行相加
		    sqDistances = sqDiffMat.sum(axis=1)
		    #开方，计算出距离
		    distances = sqDistances**0.5
		    #返回distances中元素从小到大排序后的索引值
		    sortedDistIndices = distances.argsort()
		    #定一个记录类别次数的字典
		    classCount = {}
		    for i in range(k):
		        #取出前k个元素的类别
		        voteIlabel = labels[sortedDistIndices[i]]
		        #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
		        #计算类别次数
		        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		    #python3中用items()替换python2中的iteritems()
		    #key=operator.itemgetter(1)根据字典的值进行排序
		    #key=operator.itemgetter(0)根据字典的键进行排序
		    #reverse降序排序字典
		    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
		    #返回次数最多的类别,即所要分类的类别
		    return sortedClassCount[0][0]
		 
		if __name__ == '__main__':
		    #创建数据集
		    group, labels = createDataSet()
		    #测试集
		    test = [101,20]
		    #kNN分类
		    test_class = classify0(test, group, labels, 3)
		    #打印分类结果
		    print(test_class)
	到这里，也许有人早已经发现，电影例子中的特征是2维的，这样的距离度量可以用两 点距离公式计算，但是如果是更高维的呢？对，没错。我们可以用欧氏距离(也称欧几里德度量)，如图1.5所示。我们高中所学的两点距离公式就是欧氏距离在二维空间上的公式，也就是欧氏距离的n的值为2的情况。
	
	![](http://cuijiahua.com/wp-content/uploads/2017/11/ml_1_6.jpg)

	看到这里，有人可能会问：“分类器何种情况下会出错？”或者“答案是否总是正确的？”答案是否定的，分类器并不会得到百分百正确的结果，我们可以使用多种方法检测分类器的正确率。此外分类器的性能也会受到多种因素的影响，如分类器设置和数据集等。不同的算法在不同数据集上的表现可能完全不同。为了测试分类器的效果，我们可以使用已知答案的数据，当然答案不能告诉分类器，检验分类器给出的结果是否符合预期结果。通过大量的测试数据，我们可以得到分类器的错误率-分类器给出错误结果的次数除以测试执行的总数。错误率是常用的评估方法，主要用于评估分类器在某个数据集上的执行效果。完美分类器的错误率为0，最差分类器的错误率是1.0。同时，我们也不难发现，k-近邻算法没有进行数据的训练，直接使用未知的数据与已知的数据进行比较，得到结果。因此，可以说k-近邻算法不具有显式的学习过程。
##1.1 k-近邻算法实战之约会网站配对效果判定
k-近邻算法的一般流程：

	收集数据：可以使用爬虫进行数据的收集，也可以使用第三方提供的免费或收费的数据。一般来讲，数据放在txt文本文件中，按照一定的格式进行存储，便于解析及处理。
	准备数据：使用Python解析、预处理数据。
	分析数据：可以使用很多方法对数据进行分析，例如使用Matplotlib将数据可视化。
	测试算法：计算错误率。
	使用算法：错误率在可接受范围内，就可以运行k-近邻算法进行分类。
- 实战背景

	海伦女士一直使用在线约会网站寻找适合自己的约会对象。尽管约会网站会推荐不同的任选，但她并不是喜欢每一个人。经过一番总结，她发现自己交往过的人可以进行如下分类：

		不喜欢的人
		魅力一般的人
		极具魅力的人
	海伦收集约会数据已经有了一段时间，她把这些数据存放在文本文件datingTestSet.txt中，每个样本数据占据一行，总共有1000行。
		海伦收集的样本数据主要包含以下3种特征：

		每年获得的飞行常客里程数
		玩视频游戏所消耗时间百分比
		每周消费的冰淇淋公升数
- 准备数据：解析数据

	
