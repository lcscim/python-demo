import requests
from urllib.request import urlretrieve
import os

def save_img(img_url,file_name,file_path):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urlretrieve(img_url,filename=filename)
    except IOError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    headers = {'Host': 'api.overwatchleague.cn',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.6.0'
               }
    heros_url = "https://api.overwatchleague.cn/teams"
    req = requests.get(url=heros_url, headers=headers).json().get('competitors')
    print('一共有%d个队伍' %len(req))
    for i in req:
        teamname = i.get('competitor').get('name')
        players = i.get('competitor').get('players')
        for player in players:
            playername = player.get('player').get('name')
            playerurl = player.get('player').get('headshot')
            save_img(playerurl,"{0}-{1}".format(teamname,playername),'players')
