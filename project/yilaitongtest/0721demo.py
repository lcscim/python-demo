import requests

if __name__ == '__main__':
    headers = {'Host': 'api.overwatchleague.cn',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.6.0'
               }
    heros_url = "https://api.overwatchleague.cn/ranking HTTP/1.1"
    req = requests.get(url=heros_url, headers=headers).json()
    print(req)