import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="bank")
cursor=con.cursor()

users=[]


f=open(file="用户数据.txt",mode="r+")
data = f.readlines()
for i in data:
    a=i.replace("\n","").split(",")
    users.append(a)

for j in users:
    sql="insert into  总资产 value(%s,%s,%s)"
    param=[j[0],j[1],j[2]]
    cursor.execute(sql,param)
    con.commit()

sql="select sum(allmoney) from 总资产"
cursor.execute(sql)
data=cursor.fetchall()

cursor.close()
con.close()
print("总资产为：",data)











