students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
# 1)统计不及格学生的个数
count=0
for i in students:
    if i["score"]<60:
        count=count+1
print("不及格人数为：",count)
# 2)统计未成年学生的个数
agecount=0
for j in students:
    if j["age"]<18:
        agecount=agecount+1
print("未成年人数为：",agecount)
# 3)打印手机尾号是8的学生的名字
telname=[]
for n in students:
    a=str(n["tel"])
    b=a[-1]
    b=int(b)
    if b==8:
        telname.append(n["name"])
print("手机尾号为8的同学是：",telname)
# 4)打印最高分和对应的学生的名字
maxscore=0
sconame=""
for w in students:
    if w["score"]>maxscore:
        maxscore=w["score"]
        sconame=w["name"]
print("分数最高的是：",sconame,maxscore)

# 5)将列表按学生成绩从大到小排序
max_score = students[0].get('score')
num = 0
for i in range(0,len(students)):
    for j in range(i, len(students)):
        if students[j].get('score') > max_score:
            max_score = students[j].get('score')
            num = j
    students[i], students[num] = students[num], students[i]
    max_score = 0
print(students)

# 6)删除性别保密的所有学生
for index,h in enumerate(students):

    if h["gender"]=="保密":
        del students[index]
        print(students)
















