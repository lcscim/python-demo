from selenium import webdriver
from lxml import etree
import urllib.requests
import time
import random

class download_img(object):
    def __init__(self):
        self.url = 'http://jandan.net/ooxx'
        option = webdriver.FirefoxOptions()
        option.set_headless()
        self.driver = webdriver.Firefox(firefox_options=option)
    
    def pageurl(self):
        page_url = []
        for i in range(10,12):
            url = 'http://jandan.net/ooxx/page-%d#comments' % i
            page_url.append(url)
            print (url)
        return page_url
    
    def imgurl(self,url):
        self.driver.get(url)
        time.sleep(5)
        source = self.driver.page_source
        self.driver.quit()
        content = etree.HTML(source)
        imglist = content.xpath('//div[@class="text"]/p/a[@class="view_img_link"]/@href')
        for i in range(len(imglist)):
            imglist[i] = 'http:' + imglist[i]
        return imglist
    
    def downloder(self,url):
        i = 1
        for each in url:
            time.sleep(random.randint(1,10))
            name = each.split('/')[-1]            
            content = requests.get(each).content
            with open('C:\\Users\\Public\\Pictures\\Sample Pictures' % name,'wb+') as f:
                f.write(content)
            print ('下载第%s张图片' % i)
            i += 1

if __name__ == '__main__':
    img = download_img()
    pageurl = img.pageurl()
    for each in pageurl:
        imglist = img.imgurl(each)
        img.downloder(imglist)
