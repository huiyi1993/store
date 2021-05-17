class People:
    age = ""
    sex = ""
    name = ""

class Type_Of_Work(People):
    def Wrok(self):
        print(self.name,"正在工作！！！")

class Student(Type_Of_Work):
    account = ""
    def Stady(self):
        print(self.name,"正在学习！！！")
    def sing(self):
        print(self.name,"正在唱歌！！！")

People.name = "张三"
People.sex = "男"
People.age = 30

print(Student().Stady())
print(Student().sing())
print(Type_Of_Work().Wrok())
















