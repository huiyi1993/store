import pymysql
import xlwt
import xlrd
host = "localhost"
user = "root"
password = ""
database = "bank"
con = pymysql.connect(host=host,user=user,password=password,database=database)
cursor = con.cursor()
def Db_to_excel(sql,table,name):#sql为要输入的SQL语句，table为Excel选项卡名称，name为保存文件的名字（注意加后缀）
    cursor.execute(sql)
    a = cursor.fetchall()
    wb = xlwt.Workbook()
    sheet = wb.add_sheet(table)
    for i,j in enumerate(a):
        for x,n in enumerate(j):
            sheet.write(i,x,n)
    wb.save(name)
    cursor.close()
    con.close()

def Excel_to_db(add,name,sql,param):#add为Excel路径，name为Excel标签名，sql为SQL语句，param为sql语句中变量
    u = []
    wb = xlrd.open_workbook(filename=add,encoding_override=True)
    sheet = wb.sheet_by_name(name)
    rows = sheet.nrows
    for i in range(rows):#将Excel表中数据添加到u列表中
        u.append(sheet.row_values(i))
    print(u)
    for i in u:
        # sql = "insert into newtable values(%s,%s,%s,%s,%s)"
        # param = [i[0],str(i[1]),i[2],i[3],i[4]]
        cursor.execute(sql,param)
        con.commit()
        cursor.close()
        con.close()























