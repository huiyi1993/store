chinese = ['小明','小张','小黄','小杨']
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']
# 1)求选课学生总共有多少人
a=[]
for i in chinese:
    if i not in a:
        a.append(i)
for i in math:
    if i not in a:
        a.append(i)
for i in english:
    if i not in a :
        a.append(i)
print(len(a))
# 2)求只选了第一个学科的人的数量和对应的名字
print("选第一学科的人数：",len(chinese))
print("选第一学科的名字：",chinese)
# 3)求只选了一门学科的学生的数量和对应的名字
count=0
for i in chinese:
    if i not in math and i not in english:
        count=count+1
        print(i)
for i in math:
    if i not in chinese and i not in english:
        count=count+1
        print(i)
for i in english:
    if i not in chinese and i not in math:
        count=count+1
        print(i)
print("只选择一门学科的人数：",count)

















