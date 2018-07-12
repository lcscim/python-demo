from aip import AipOcr

# 定义常量  
APP_ID = '11521768'
API_KEY = 'HU6vkBZNSzBNCjc03wmKURKA'
SECRET_KEY = 'RwtseKzRBdqPQDt8y5i8Nu6zYBXVOjR2'

# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片  
filePath = "1102810104.jpg"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
# 新建文件来存储
file_name = open('ocr_text.txt','w')

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath),options)

# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')

f = result.get('words_result')
for i in f:
    file_name.write(i.get('words')+'\n')

file_name.close()
