import openpyxl
import requests

def find_url(url):
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; MI PAD 2 MIUI/V9.6.1.0.LACCNFD)',
               'Host': 'www.yilaitong.net',
               'Connection':'Keep-Alive',
               'Accept-Encoding': 'gzip'
               }
    requests.packages.urllib3.disable_warnings()
    req = requests.get(url=url, headers=headers, verify=False).json()
    sid = []
    sname = []
    sno = []
    for i in req:
        sid.append(i.get('SID'))
        sname.append(i.get('SName'))
        sno.append(i.get('SNo'))

    result = []
    length = len(sid)
    for b in range(length):
        result.append([sid[b],sname[b],sno[b]])

    return result

def saves(url):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    wb.create_sheet(index = 0,title = '商家')
    for each in find_url(url):
        wb['商家'].append(each)

    wb.save("郑州所有商家.xlsx")
    
if __name__ == '__main__':

    url = 'https://www.yilaitong.net/index.php?s=VersionOne/Supplier/supplierList'
    saves(url)
    
