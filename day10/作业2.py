f=open(file="景甜.jpg",mode="rb")
f1=open(file="python.jpg",mode="wb")

data=f.read()
f1.write(data)

f.close()
f1.close()