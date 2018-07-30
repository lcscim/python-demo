from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar

if __name__ == '__main__':
    #登陆地址
    login_url = 'http://www.yilaitong.net/index.php'    
    #User-Agent信息                   
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    #Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    #登陆Form_Data信息
    Login_Data = {}
    Login_Data['UserName'] = '18903827778'       #改成你自己的用户名
    Login_Data['password'] = 'a123456'        #改成你自己的密码
    #使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)
    response1 = opener.open(req1)
    print(response1.read().decode('utf-8'))
