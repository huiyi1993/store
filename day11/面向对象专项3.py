class people:
    __name = ""
    __sex = ""
    __age = ""
    __phonebalance = 0
    __phone = ""
    __battery = ""
    __screen = ""
    __standby = ""
    __integral = 0

    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setsex(self,sex):
        self.__sex=sex
    def getsex(self):
        return self.__sex
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    def setphonebalance(self,phonebalance):
        self.__phonebalance=phonebalance
    def getphonebalance(self):
        return self.__phonebalance
    def setphone(self,phone):
        self.__phone=phone
    def getphone(self):
        return self.__phone
    def setbattery(self,battery):
        self.__battery=battery
    def getbattery(self):
        return self.__battery
    def setscreen(self,screen):
        self.__screen=screen
    def getscreen(self):
        return self.__screen
    def setstandby(self,standby):
        self.__standby=standby
    def getstandby(self):
        return self.__standby
    def setintegral(self,integral):
        self.__integral=integral
    def getintegral(self):
        return self.__integral

    def sendmessage(self):
        print(self.__name,self.__age,self.__sex,self.__phone,self.__phonebalance,self.__integral,self.__standby,self.__screen,self.__battery)
    def phone(self,num,time):
        # num=input("请输入号码：")
        # time=input("请输入通话时间：")
        time=int(time)

        if num.isdigit():

            if self.__phonebalance>=1:
                print("通话成功！！！")
                if time in range(0,10):
                    self.__phonebalance=self.__phonebalance-time*1
                    self.__integral=self.__integral-time*15
                elif time in range(10,20):
                    self.__phonebalance=self.__phonebalance-time*0.8
                    self.__integral=self.__integral-time*39
                else:
                    self.__phonebalance=self.__phonebalance-time*0.65
                    self.__integral=self.__integral-time*48
            else:
                print("您的余额不足！！！")
        else:
            print("您拨打的号码为空号！！！")

p=people()
p.setname("张三")
p.setsex("男")
p.setage("30")
p.setphonebalance(1000)
p.setphone("华为")
p.setbattery("4000ma")
p.setscreen("6寸")
p.setstandby("12h")
p.setintegral(10000)

p.phone("1",9)







