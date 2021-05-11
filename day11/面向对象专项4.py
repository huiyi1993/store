#1
class student:
    __account = ""
    __name = ""
    __age = 0
    __sex = ""
    __height = ""
    __weight = ""
    __achievement = ""
    __add = ""
    __phone = ""
    def setaccount(self,account):
        self.__account=account
    def getaccount(self):
        return self.__account
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    def setsex(self,sex):
        self.__sex=sex
    def getsex(self):
        return self.__sex
    def setheight(self,height):
        self.__height=height
    def getheight(self):
        return self.__height
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def setachievement(self,achievement):
        self.__achievement=achievement
    def getachievement(self):
        return self.__achievement
    def setadd(self,add):
        self.__add=add
    def getadd(self):
        return self.__add
    def setphone(self,phone):
        self.__phone=phone
    def getphone(self):
        return self.__phone

    def studey(self,time):
        print(self.__name,"每天学习",time)
    def playgame(self,game):
        print(self.__name,"正在玩",game,"游戏")
    def programming(self,num):
        print(self.__name,"已经写了",num,"行代码")
s=student()
s.setaccount("1")
s.setname("张三")
s.setage(30)
s.setsex("男")
s.setheight("180cm")
s.setweight("75kg")
s.setachievement("80分")
s.setadd("cn")
s.setphone("123456")
s.studey("4h")
s.playgame("贪玩蓝月")
s.programming(10)



#2
class car:
    __model = ""
    __wheel = ""
    __colour = ""
    __weight = ""
    __tank = ""
    def seetmodel(self,model):
        self.__model=model
    def getmodel(self):
        return self.__model
    def setwheel(self,wheel):
        self.__wheel=wheel
    def getwheel(self):
        return self.__wheel
    def setcoloour(self,colour):
        self.__colour=colour
    def getcolour(self):
        return self.__colour
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def settank(self,tank):
        self.__tank=tank
    def gettank(self):
        return self.__tank

    def run(self):
        print(self.__model,"在马路上飞驰")

c=car()
c.seetmodel("法拉利")
c.setwheel("4")
c.setcoloour("红色")
c.setweight("1500kg")
c.settank("600L")
c.run()

#3
class pc:
    __model = ""
    __standby = ""
    __colour = ""
    __weight = ""
    __cpu = ""
    __memory = ""
    __hard = ""
    def setmodel(self,model):
        self.__model=model
    def getmodel(self):
        return self.__model
    def setstandby(self,standby):
        self.__standby=standby
    def getstandby(self):
        return self.__standby
    def setcolour(self,colour):
        self.__colour=colour
    def getcolour(self):
        return self.__colour
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__memory
    def sethard(self,hard):
        self.__hard=hard
    def gethrad(self):
        return self.__hard

    def playgame(self):
        print("我正在用",self.__model,"打游戏")
    def work(self):
        print("我正在用", self.__model, "电脑办公")
p=pc()
p.setmodel("联想")
p.setstandby("4h")
p.setcolour("黑色")
p.setweight("1kg")
p.setcpu("i9-1050")
p.setmemory("16g")
p.sethard("1T")
p.work()
#4
class monkey:
    __classs = ""
    __sex = ""
    __colour = ""
    __weight = ""
    def setclasss(self,classs):
        self.__classs=classs
    def getclasss(self):
        return self.__classs
    def setsex(self,sex):
        self.__sex=sex
    def getsex(self):
        return self.__sex
    def setcolour(self,colour):
        self.__colour=colour
    def getcolour(self):
        return self.__colour
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def makefire(self,material):
        print(self.__classs,"正在用",material,"造火")
    def study(self,affair):
        print(self.__classs,"正在学习",affair)
m=monkey()
m.setclasss("灵猴")
m.setsex("公")
m.setcolour("灰")
m.setweight("10kg")
m.makefire("木头")
m.study("打字")


















