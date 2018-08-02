import requests
import openpyxl
import yltbj
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import NamedStyle

def find_url(url):
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; MI PAD 2 MIUI/V9.6.1.0.LACCNFD)',
               'Host': 'www.yilaitong.net',
               'Connection':'Keep-Alive',
               'Accept-Encoding': 'gzip'
               }
    req = requests.get(url=url, headers=headers).json()
    name = []
    price = []
    for i in req:
        phonename = i.get('GTitle').split("--")[1]+' '+i.get('GTitle').split("--")[2]
        name.append(phonename)
        price.append(i.get('Price'))

    time = req[0].get('UpTime')
    result = []
    length = len(name)
    for b in range(length):
        result.append([name[b],price[b]])

    return [result,time]
def save_price(a):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    highlight = NamedStyle(name="highlight")
    highlight.font = Font(bold=True, size=15)
    highlight.alignment = Alignment(horizontal='center', vertical='center')
    wb.add_named_style(highlight)
    
    for i in range(len(a)):
        salename = a[i].get('sale')
        url = a[i].get('url')
        wb.create_sheet(index = i, title = salename)
        wb[salename]['A1'] = "型号"
        wb[salename]['B1'] = "价格"
        wb[salename]['A1'].style = highlight
        wb[salename]['B1'].style = highlight
        wb[salename].column_dimensions['A'].width = 30
        c = 2
        
        for each in find_url(url)[0]:
            wb[salename].append(each)
            ws = wb[salename]['A{}'.format(c)]
            ws1 = wb[salename]['B{}'.format(c)]
            ws.alignment = Alignment(horizontal='center', vertical='center')
            ws1.alignment = Alignment(horizontal='center', vertical='center')
            c += 1
            
        wb[salename]['C1'] = find_url(url)[1]
    wb.save('测试报价.xlsx')

if __name__ == '__main__':
    save_price(yltbj.bjurls())

