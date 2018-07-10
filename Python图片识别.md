#0710
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
	
			tesseract mjorcen.normal.exp0.jpg mjorcen.normal.exp0 -l chi_sim batch.nochop makebox
		3、打开jTessBoxEditor矫正错误并训练
	
			打开train.bat找到tif图，打开，并校正。
	5. 训练

		只要在命令行输入命令即可。

			tesseract  mjorcen.normal.exp0.jpg mjorcen.normal.exp0  nobatch box.train
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
		
			tesseract mjorcen.normal.exp0.jpg mjorcen.normal.exp0 -l normal
		
		
