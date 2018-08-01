import requests
from urllib.request import urlretrieve
import os
import openpyxl
import yltbj

def find_price(url):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    wb.create_sheet(index = 0, title = "华为")
    wb.create_sheet(index = 1, title = "小米")
    ws1 = wb['华为']
    ws2 = wb['小米']
    ws1['A1'] = "型号"
    ws1['B1'] = "价格"
    ws2['A1'] = "型号"
    ws2['B1'] = "价格"
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; MI PAD 2 MIUI/V9.6.1.0.LACCNFD)',
               'Host': 'www.yilaitong.net',
               'Connection':'Keep-Alive',
               'Accept-Encoding': 'gzip'
               }
    heros_url1 = "https://www.yilaitong.net/?m=Android&c=Supplier&a=shopSupplier&sid=487"
    heros_url2 = "https://www.yilaitong.net/?m=Android&c=Supplier&a=shopSupplier&sid=496"
    req1 = requests.get(url=heros_url1, headers=headers).json()
    name1 = []
    price1 = []
    for i1 in req1:
        #print(i.get('GTitle'))
        phonename = i1.get('GTitle').split("--")[1]+i1.get('GTitle').split("--")[2]
        name1.append(phonename)
        price1.append(i1.get('Price'))
    result1 = []
    length1 = len(name1)
    for b1 in range(length1):
        result1.append([name1[b1],price1[b1]])

    for each1 in result1:
        ws1.append(each1)

    req2 = requests.get(url=heros_url2, headers=headers).json()
    name2 = []
    price2 = []
    for i2 in req2:
        #print(i.get('GTitle'))
        phonename = i2.get('GTitle').split("--")[1]+i2.get('GTitle').split("--")[2]
        name2.append(phonename)
        price2.append(i2.get('Price'))
    result2 = []
    length2 = len(name2)
    for b2 in range(length2):
        result2.append([name2[b2],price2[b2]])

    for each2 in result2:
        ws2.append(each2)
        
    wb.save('测试报价.xlsx')
if __name__ == '__main__':
    #find_price()
    print(bj_urls.urls)

