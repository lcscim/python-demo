#0710（已弃用）
tips：

1. https://www.cnblogs.com/wzben/p/5930538.html教程
2. 需要将tesseract路径设置到环境变量PATH和path中
3. https://blog.csdn.net/u013421629/article/details/76854778
4. jtessboxeditor 中文乱码，将jtessboxeditor的setting里改字体为宋体，regular就可以了。
##1.安装
- 安装其他编译器pycharm

	http://www.jetbrains.com/pycharm/download/#section=windows在该网站下载，并根据实际系统版本安装
	
	激活使用http://idea.uri.ci（新版本使用），详细信息去http://idea.liyang.io/
	打开时有可能需要安装R语言
- 安装pytesseract和PIL

	PIL全称：Python Imaging Library，python图像处理库，这个库支持多种文件格式，并提供了强大的图像处理和图形处理能力。由于PIL仅支持到Python 2.7，所以在PIL的基础上创建了Pillow库，支持最新Python 3.x。
	pytesseract图片识别工具

	安装方法：1.pip命令安装

		pip install pytesseract 
		pip install Pillow		//安装第一个后一般会自动安装该模块
	2.使用pycharm编辑器安装，直接搜索安装

- 安装识别引擎tesseract-ocr

	1. 下载Tesseract-OCR引擎，注意要3.0以上才支持中文哦，按照提示安装就行。

		https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.0.0-beta.1.20180608.exe
	2. 下载chi_sim.traindata字库。要有这个才能识别中文。下好后，放到Tesseract-OCR项目的tessdata文件夹里面。
	
		https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/chi_sim.traineddata
	3. 下载jTessBoxEditor，这个是用来训练字库的。	

		https://jaist.dl.sourceforge.net/project/vietocr/jTessBoxEditor/jTessBoxEditor-2.0.zip
	测试语句

		1、进入cmd，进入到要识别的图片的路径下。
		2、输入命令
			tesseract 图片名称 生成的结果文件的名称 字库
		例如我的图片识别就是：
			tesseract test.png result -l chi_sim
	4. 训练jTessBoxEditor
	
		1、将图片转换成tif格式，用于后面生成box文件。可以通过画图，然后另存为tif即可。
	
			更改图片名字，这个是有要求的=。=
			tif文面命名格式[lang].[fontname].exp[num].tif
			lang是语言 fontname是字体 
			比如我们要训练自定义字库 mjorcen字体名normal
			那么我们把图片文件重命名 mjorcen.normal.exp0.jpg在转tif。
		2、生成box文件
	
			tesseract mjorcen.normal.exp0.png mjorcen.normal.exp0 -l chi_sim batch.nochop makebox
		3、打开jTessBoxEditor矫正错误并训练
	
			打开train.bat找到tif图，打开，并校正。
	5. 训练

		只要在命令行输入命令即可。

			tesseract  mjorcen.normal.exp0.png mjorcen.normal.exp0  nobatch box.train
			unicharset_extractor mjorcen.normal.exp0.box
		
		新建一个font_properties文件里面内容写入 normal 0 0 0 0 0 表示默认普通字体,没有后缀

		继续敲命令

			shapeclustering -F font_properties -U unicharset mjorcen.normal.exp0.tr
			mftraining -F font_properties -U unicharset -O unicharset mjorcen.normal.exp0.tr
			cntraining mjorcen.normal.exp0.tr
		最后会生成五个文件，把目录下的unicharset、inttemp、pffmtable、shapetable、normproto这五个文件前面都加上"normal."

		合并五个文件

			combine_tessdata normal.
	6. 测试

		1、把 normal.traineddata 复制到Tesseract-OCR 安装目录下的tessdata文件夹中
		2、识别命令：
		
			tesseract mjorcen.normal.exp0.png mjorcen.normal.exp0 -l normal

##2.在python中代码实现

	from PIL import Image
	import pytesseract
	text=pytesseract.image_to_string(Image.open('test.png'),lang='chi_sim')
	print(text)

#7.11
tips:
1. 管理面板http://console.bce.baidu.com/ai/#/ai/ocr/app/list
2. 开发文档https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html


##1.使用百度OCR
安装百度ocr

	执行pip install baidu-aip
示例语句：

	from aip import AipOcr

	#你的 APPID AK SK
	APP_ID = '你的 App ID'		
	API_KEY = '你的 Api Key'
	SECRET_KEY = '你的 Secret Key'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

	#读取图片
	def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()
	image = get_file_content('example.jpg')
	
	#调用通用文字识别, 图片参数为本地图片
	client.basicGeneral(image);
	
	#如果有可选参数
	options = {}
	options["language_type"] = "CHN_ENG"
	options["detect_direction"] = "true"
	options["detect_language"] = "true"
	options["probability"] = "true"
	
	#带参数调用通用文字识别, 图片参数为本地图片
	client.basicGeneral(image, options)
	
	#调用通用文字识别, 图片参数为远程url图片
	url = "https//www.x.com/sample.jpg"
	client.basicGeneralUrl(url);
	
	#如果有可选参数
	options = {}
	options["language_type"] = "CHN_ENG"
	options["detect_direction"] = "true"
	options["detect_language"] = "true"
	options["probability"] = "true"
	
	#带参数调用通用文字识别, 图片参数为远程url图片
	client.basicGeneralUrl(url, options)
通用文字识别 请求参数详情：

	参数名称	 是否必选	类型	  可选值范围	  默认值	   说明
	image	  是	  	   string			         图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
	url		  是	       string			        图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大	4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
	language_type	否	string	CHN_ENG  CHN_ENG  识别语言类型，默认为CHN_ENG。可选值包括：
								ENG					- CHN_ENG：中英文混合；
								POR					- ENG：英文；
								FRE					- POR：葡萄牙语；
								GER					- FRE：法语；
								ITA					- GER：德语；
								SPA					- ITA：意大利语；
								RUS					- SPA：西班牙语；
								JAP					- RUS：俄语；
								KOR					- JAP：日语；
													- KOR：韩语；
								
	detect_direction 否	string	true 	false	是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:
										false				- true：检测朝向；
															- false：不检测朝向。
	detect_language	否	string	true	false	是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）							
								false			
	probability		否	string	true 				是否返回识别结果中每一行的置信
								false

示例：

	from aip import AipOcr
	# 定义常量  
	APP_ID = '11521768'
	API_KEY = 'HU6vkBZNSzBNCjc03wmKURKA'
	SECRET_KEY = 'RwtseKzRBdqPQDt8y5i8Nu6zYBXVOjR2'
	# 初始化文字识别分类器
	aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)
	# 读取图片  
	filePath = "test.png"
	def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()
	# 定义参数变量
	options = {
	    'detect_direction': 'true',
	    'language_type': 'CHN_ENG',
	}
	# 网络图片文字文字识别接口
	result = aipOcr.webImage(get_file_content(filePath),options)
	# 如果图片是url 调用示例如下
	# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')
	print(result)
示例输出结果：

	{'log_id': 3630035229987430278, 'direction': 0, 'words_result_num': 1, 'words_result': [{'words': '庆幸还年轻,还可以做一个无拘无束的浪子。有肉吃肉,无肉喝水'}]}

将输出文字保存：

	from aip import AipOcr
	# 定义常量  
	APP_ID = '11521768'
	API_KEY = 'HU6vkBZNSzBNCjc03wmKURKA'
	SECRET_KEY = 'RwtseKzRBdqPQDt8y5i8Nu6zYBXVOjR2'
	# 初始化文字识别分类器
	aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)
	# 读取图片  
	filePath = "ry.jpg"
	def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()
	# 定义参数变量
	options = {
	    'detect_direction': 'true',
	    'language_type': 'CHN_ENG',
	}
	# 新建文件来存储
	file_name = open('text-a.txt','w')
	# 网络图片文字文字识别接口
	result = aipOcr.webImage(get_file_content(filePath),options)
	# 如果图片是url 调用示例如下
	# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')
	f = result.get('words_result')
	for i in f:
	    file_name.write(i.get('words'))
	file_name.close()
#7.12


##1.百度OCR识别表格

	from aip import AipOcr
	import urllib.request
	import time
	
	# 定义常量  
	APP_ID = '11521768'
	API_KEY = 'HU6vkBZNSzBNCjc03wmKURKA'
	SECRET_KEY = 'RwtseKzRBdqPQDt8y5i8Nu6zYBXVOjR2'
	
	# 初始化文字识别分类器
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
	
	# 读取图片  
	def get_file_content(filePath):
	    with open(filePath, 'rb') as fp:
	        return fp.read()
	
	image = get_file_content('ry.jpg')
	
	wzsb = client.tableRecognitionAsync(image)		//获得请求数据，返回示例如下行红字
	
	# {'result': [{'request_id': '11521768_379174'}], 'log_id': 153140371183330}
	
	requestId = wzsb.get('result')[0].get('request_id')		//获取下载request_id
	time.sleep(20)		//由于识别需要时间，所以需要先将程序睡眠20秒左右
	
	""" 调用表格识别结果 """
	# client.getTableRecognitionResult(requestId);
	
	""" 如果有可选参数 """
	# options = {}
	# options['request_type'] = 'excel'
	
	""" 带参数调用表格识别结果 """
	# client.getTableRecognitionResult(requestId,options);

	result = client.getTableRecognitionResult(requestId)	//表格识别结果 返回数据参数详情如下行红字
	# { result: { result_data: 'url',ret_msg: '未开始', request_id: '10829160_178511',percent: 0,ret_code: 1 },log_id: 151852085326438 }
	url = result.get('result').get('result_data')	//获取返回值得URL
	response = urllib.request.urlopen(url)		//剩余几句将程序下载到本地
	exc = response.read()
	with open('test.xls', 'wb') as f:
	    f.write(exc)
		
