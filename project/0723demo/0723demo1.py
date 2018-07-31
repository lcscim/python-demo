import requests
import os
import time
from bs4 import BeautifulSoup

def open_url(url):    
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}                        
    response = requests.get(url,headers = header)    
    return response

def find_videos(url):
    time.sleep(2)
    html = open_url(url).read().decode('utf-8')
    soup =BeautifulSoup(html,'lxml')
    videos_url=[]
    for each in soup.find_all('div'):
        print(each)
def spider_tx():
    url='http://zanghaihua.org/'
    count=1
    find_videos(url)
   
            
if __name__=='__main__':
    spider_tx()
