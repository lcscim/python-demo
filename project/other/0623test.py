import urllib.request
import random

url = 'http://www.whatismyip.com.tw/'

iplist = ['60.216.177.152:8118','118.190.95.26:9001','171.12.133.160:47102']

proxy_support = urllib.request.ProxyHandler({'https':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
