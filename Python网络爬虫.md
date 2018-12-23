#1.爬虫简介
- 爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
- 两大特征
	- 能按照作者要求下载数据或者内容
	- 能自动在网络上流窜
- 三大步骤
	- 下载网页
	- 提取正常信息
	- 根据一定规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
	- 通用爬虫
	- 专用爬虫（聚焦爬虫）
- Python网络包简介
	- Python2.x:urllib,urllib2,urllib3,httplib,httplib2,requests
	- Python3.x:urllib,urllib3,httplib2,requests
	- Python2:urllib和urllib2配合使用，或者requests
	- Python3:urllib,requests
#2.urllib 
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:包含urllib.request产生的错误，使用try捕捉
    - urllib.parse:包含即系url的方法包含解析
    - urllib.robotparse:解析robots.txt文件
    - 案例：v1
        from urllib import request
        if __name__ == '__main__':
            url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin"
            rsp = request.urlopen(url)
            #打开url页面
            html = rsp.read().decode("utf-8")
            print(html)
- 网页编码问题解决
    - chardet 可以自动监测页面编码
    - 使用pip install chardet安装
    - 案列v2
        import urllib,chardet
        if __name__ == '__main__':
            url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin"
            rsp = urllib.request.urlopen(url)
            html = rsp.read()
            #获取该页面的编码信息返回是一个字典
            cs = chardet.detect(html)
            #在字典中获取编码信息，如果没有使用utf-8编码
            html = html.decode(cs.get("encoding","utf-8"))
            print(html)
- urlopen 的返回信息
    - 案列V3
        from urllib import request
        if __name__ == '__main__':
            url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin"
            rsp = request.urlopen(url)
            print(type(rsp))
            print(rsp)
            print("URL:{}".format(rsp.geturl()))
            print("Info:{}".format(rsp.info()))
            print("Code:{}".format(rsp.getcode()))
    - geturl:返回请求对象的url
    - info：请求返回对象的meta信息
    - getcode:返回http code请求状态码200标识成功
- request.date的使用
    - 访问网络的两种方法
        - get ：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
            - 案列v4
                from urllib import request,parse
                if __name__ == '__main__':
                    url = "http://www.baidu.com/s?"
                    wd = input("input your keyword:")
                    qs = {
                        "wd":wd
                    }
                    #获取输入文本编码后的信息
                    qs = parse.urlencode(qs)
                    fullurl = url + qs
                    rsp = request.urlopen(fullurl)
                    html = rsp.read().decode("utf-8")
                    print(html)
        - post ：
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 如果想使用post信息，需要用到date参数
            - 使用post，意味着http的请求头可能需要更改
                - Content-Type:application/x-www.form-urlencode
                - Content-Length:数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案列v5        
    - 
        
                