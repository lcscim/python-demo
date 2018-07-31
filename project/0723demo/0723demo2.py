'''
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
'''

from urllib import request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    download_url = 'https://mp.weixin.qq.com/s?__biz=MzA4NDI1MTEzNA==&mid=2652655903&idx=1&sn=6a349a5db2ed8afb79287376b4e76bd3&chksm=8402e98eb37560981009563fbf8a6e54040b65dde71457c6961c8dcebdbd84ce201dc216f4f5&scene=21#wechat_redirect'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('utf-8','ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id="js_content", class_="rich_media_content ")
    soup_text = BeautifulSoup(str(texts), 'lxml')
    #将\xa0无法解码的字符删除
    print(soup_text.div.text.replace('\xa0',''))
