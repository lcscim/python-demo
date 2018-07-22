import requests
from urllib.request import urlretrieve

if __name__ == '__main__':
    headers = {'Host': 'api.overwatchleague.cn',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.6.0'
               }
    heros_url = "https://api.overwatchleague.cn/ranking"
    req = requests.get(url=heros_url, headers=headers).json().get('content')
    print('一共有%d个队伍' %len(req))
    for i in req:
        filename = i.get('competitor').get('name')+'.jpg'
        logo_url = i.get('competitor').get('logo')
        urlretrieve(url = logo_url, filename = filename)
    
