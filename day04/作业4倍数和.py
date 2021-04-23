li=[1,5,21,30,15,9,30,24]
i=0
li1=[]
while i<len(li):
    if li[i]%5==0:
        li1.append(li[i])
    i=i+1
print("和为:",sum(li1))
# li1=[]
# for i in li:
#     if i%5==0:
#         li1.append(i)
# print("和为：",sum(li1))





