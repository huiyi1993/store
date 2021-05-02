#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
a={21:3,56:9,10:3}
# def list_count(i):
#     j=list.count(i)
#     c=set(list)
#     for n in c:
#         a[n]=j


b=[1,1,1,1,2,2,2,3,3,4]
i=set(b)
for w in i:
    q=b.count(w)
    a[w]=q
print(a)









