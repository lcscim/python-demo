import urllib.request
import json

if __name__ == '__main__':
    heros_url = "https://api.overwatchleague.cn/standings?locale=zh-cn"
    response = urllib.request.urlopen(heros_url)
    unicodester = json.load(response).get('meta')
    print(unicodester)
