import urllib.request
import urllib.parse
import json

content = input("请输入要翻译的内容")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1529660044390'
data['sign'] = '093569408e9469545bafc4e72e1b06a3'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data,head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
