import openpyxl
from openpyxl.styles import Font

wb = openpyxl.load_workbook('817.xlsx')
ws = wb['订单列表']
rows = ws.max_row
names = []
for each in ws['C2:C{}'.format(rows-1)]:
    for each_cell in each:
        if each_cell.value not in names:
            names.append(each_cell.value)

def geshi(name,i):
    wb.create_sheet(index = i+1,title = names[i][:30])
    wb[names[i][:30]].guess_types = True
    wb[names[i][:30]]['A1'] = '商品名称'
    wb[names[i][:30]]['B1'] = '商品数量'
    wb[names[i][:30]]['C1'] = '收货人'
    wb[names[i][:30]]['D1'] = '收货电话'
    wb[names[i][:30]]['E1'] = '收货地址'
    wb[names[i][:30]]['A1'].font = Font(bold=True, size=15)
    wb[names[i][:30]]['B1'].font = Font(bold=True, size=15)
    wb[names[i][:30]]['C1'].font = Font(bold=True, size=15)
    wb[names[i][:30]]['D1'].font = Font(bold=True, size=15)
    wb[names[i][:30]]['E1'].font = Font(bold=True, size=15)
    wb[names[i][:30]].column_dimensions['A'].width = 40
    wb[names[i][:30]].column_dimensions['E'].width = 50
    wb[names[i][:30]].column_dimensions['D'].width = 15
    j = 2
    for a in range(rows-2):
        
        if names[i] == ws['C{}'.format(a+2)].value:
            
            wb[names[i][:30]]['A{}'.format(j)] = ws['C{}'.format(a+2)].value
            wb[names[i][:30]]['B{}'.format(j)] = ws['E{}'.format(a+2)].value
            wb[names[i][:30]]['C{}'.format(j)] = ws['K{}'.format(a+2)].value
            wb[names[i][:30]]['D{}'.format(j)] = ws['L{}'.format(a+2)].value
            wb[names[i][:30]]['E{}'.format(j)] = ws['M{}'.format(a+2)].value
            j+=1
        else:
            continue
    wb.save('817.xlsx')

for i in range(len(names)):
    if len(names[i]) <= 31:
        name = names[i]
        print(name)
    else:
        name = names[i][:25]+' '+names[i][31:]
        print(name)
    

a = [{'供应商':'张三','商品':['黑贝南瓜 39.9元5斤包邮','红蜜薯5斤39元包邮 48小时内发货']},
     {'供应商':'张三','商品':['黑贝南瓜 39.9元5斤包邮','红蜜薯5斤39元包邮 48小时内发货']}]


            


