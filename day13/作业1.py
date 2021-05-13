import xlrd
import xlwt
y=[]#羽绒服销售额
n=[]#牛仔裤销售额
f=[]#风衣销售额
p=[]#皮草销售额
t=[]#T血销售额
c=[]#衬衫销售额
z=[]#总销售额
all = []#12月服饰销售情况

wb = xlrd.open_workbook(filename=r"E:\1234\study\day13\12月份衣服销售数据.xls",encoding_override=True)
sheet = wb.sheet_by_index(0)
cols = sheet.ncols
rows = sheet.nrows
for i in range(rows):
    all.append(sheet.row_values(i))

for i in range(rows):
    if i != 0:
        a = sheet.cell_value(i, 2)
        b = sheet.cell_value(i, 4)
        z.append(round(a * b, 2))
        if sheet.cell_value(i,1)=="羽绒服":
            a = sheet.cell_value(i,2)
            b = sheet.cell_value(i,4)
            y.append(round(a*b,2))
        elif sheet.cell_value(i,1)=="牛仔裤":
            a = sheet.cell_value(i, 2)
            b = sheet.cell_value(i, 4)
            n.append(round(a * b, 2))
        elif sheet.cell_value(i,1)=="风衣":
            a = sheet.cell_value(i, 2)
            b = sheet.cell_value(i, 4)
            f.append(round(a * b, 2))
        elif sheet.cell_value(i,1)=="皮草":
            a = sheet.cell_value(i, 2)
            b = sheet.cell_value(i, 4)
            p.append(round(a * b, 2))
        elif sheet.cell_value(i,1)=="T血":
            a = sheet.cell_value(i, 2)
            b = sheet.cell_value(i, 4)
            t.append(round(a * b, 2))
        elif sheet.cell_value(i,1)=="衬衫":
            a = sheet.cell_value(i, 2)
            b = sheet.cell_value(i, 4)
            c.append(round(a * b, 2))

wb1 = xlwt.Workbook()
sheet1 = wb1.add_sheet("12月份各种服饰销售情况表")
for h, u in enumerate(all):
    for g, o in enumerate(u):
        sheet1.write(h,g,o)

sheet2 = wb1.add_sheet("羽绒服")
sheet2.write(0,0,"名称")
sheet2.write(0,1,"本月销售额")
sheet2.write(1,0,"羽绒服")
sheet2.write(1,1,sum(y))

sheet3 = wb1.add_sheet("牛仔裤")
sheet3.write(0,0,"名称")
sheet3.write(0,1,"本月销售额")
sheet3.write(1,0,"牛仔裤")
sheet3.write(1,1,sum(n))

sheet4 = wb1.add_sheet("风衣")
sheet4.write(0,0,"名称")
sheet4.write(0,1,"本月销售额")
sheet4.write(1,0,"风衣")
sheet4.write(1,1,sum(f))

sheet5 = wb1.add_sheet("皮草")
sheet5.write(0,0,"名称")
sheet5.write(0,1,"本月销售额")
sheet5.write(1,0,"皮草")
sheet5.write(1,1,sum(p))

sheet6 = wb1.add_sheet("T血")
sheet6.write(0,0,"名称")
sheet6.write(0,1,"本月销售额")
sheet6.write(1,0,"T血")
sheet6.write(1,1,sum(t))

sheet3 = wb1.add_sheet("衬衫")
sheet3.write(0,0,"名称")
sheet3.write(0,1,"本月销售额")
sheet3.write(1,0,"衬衫")
sheet3.write(1,1,sum(c))

wb1.save("总数据.xls")


