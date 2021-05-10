user=[]
f=open(file="scores.txt",mode="r+",encoding="utf-8")
f1=open(file="总成绩.txt",mode="w+",encoding="utf-8")
data=f.readlines()

thesum=0



for i in data:
    a=i.replace("\n","").split(" ")
    user.append(a)

    f1.write(i[0])
    f1.write(i[1])
    f1.write(" ")


for j in user:
    del j[0]
    for n in j:
        m=int(n)
        thesum=thesum+m
thesum=str(thesum)


f1.write("他们的总得分为：")
f1.write(thesum)

f.close()
f1.close()





