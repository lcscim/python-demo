import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import NamedStyle

wb = openpyxl.load_workbook('817.xlsx')
ws = wb['订单列表']
rows = ws.max_row
names = []
for each in ws['C2:C{}'.format(rows-1)]:
    for each_cell in each:
        if each_cell.value not in names:
            names.append(each_cell.value)

for i in range(len(names)):
    wb.create_sheet(index = i+1,title = names[i][:4])
    wb[names[i][:4]].guess_types = True
    wb[names[i][:4]]['A1'] = '商品名称'
    wb[names[i][:4]]['B1'] = '商品数量'
    wb[names[i][:4]]['C1'] = '收货人'
    wb[names[i][:4]]['D1'] = '收货电话'
    wb[names[i][:4]]['E1'] = '收货地址'
    wb[names[i][:4]]['A1'].font = Font(bold=True, size=15)
    wb[names[i][:4]]['B1'].font = Font(bold=True, size=15)
    wb[names[i][:4]]['C1'].font = Font(bold=True, size=15)
    wb[names[i][:4]]['D1'].font = Font(bold=True, size=15)
    wb[names[i][:4]]['E1'].font = Font(bold=True, size=15)
    wb[names[i][:4]].column_dimensions['A'].width = 40
    wb[names[i][:4]].column_dimensions['E'].width = 50
    wb[names[i][:4]].column_dimensions['D'].width = 15
    '''
    for a in range(rows-2):
        if names[i] == ws['C{}'.format(a+2)].value:
            wb[names[i][:4]]['A{}'.format(a+2)] = ws['C{}'.format(a+2)].value
            wb[names[i][:4]]['B{}'.format(a+2)] = ws['E{}'.format(a+2)].value
            wb[names[i][:4]]['C{}'.format(a+2)] = ws['K{}'.format(a+2)].value
            wb[names[i][:4]]['D{}'.format(a+2)] = ws['L{}'.format(a+2)].value
            wb[names[i][:4]]['E{}'.format(a+2)] = ws['M{}'.format(a+2)].value
        else:
            continue
    '''
wb.save('817.xlsx')


            


