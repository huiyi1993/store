class students():
    __name = ""
    __age = ""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    def show(self,name,age):
        print("大家好，我叫",name,"今年",age,"岁。")
    def campare(self,student):
        if self.__age>student.getage():
            print("我比同桌大",self.__age-student.getage(),"岁。")
        elif self.__age<student.getage():
            print("我比同桌小",student.getage()-self.__age,"岁。")
        elif self.__age==student.getage():
            print("我和同桌的年龄一样大！！！")
c=students()
c.setname("张三")
c.setage(18)
s=students()
s.setname("李四")
s.setage(20)

c.campare(s)









