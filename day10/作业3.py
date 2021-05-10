import random
a=random.randint(0,200000)

file=input("请输入证件照路径：")
f=open(file=file,mode="rb")
f1=open(file="D:\pythone\\"+str(a)+".jpg",mode="wb")

data=f.read()

f1.write(data)
f.close()
f1.close()
print("证件照上传成功！！！")

















