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

wzsb = client.tableRecognitionAsync(image)

# {'result': [{'request_id': '11521768_379174'}], 'log_id': 153140371183330}

requestId = wzsb.get('result')[0].get('request_id')
time.sleep(20)

""" 调用表格识别结果 """
# client.getTableRecognitionResult(requestId);

""" 如果有可选参数 """
# options = {}
# options['request_type'] = 'excel'

""" 带参数调用表格识别结果 """
result = client.getTableRecognitionResult(requestId)
url = result.get('result').get('result_data')

response = urllib.request.urlopen(url)
exc = response.read()

with open('test.xls', 'wb') as f:
    f.write(exc)

