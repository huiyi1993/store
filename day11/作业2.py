# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）

class botebook:
    __screen = ""
    __price = ""
    __cpu = ""
    __memory = ""
    __standby = ""

    def setscreen(self,screen):
        self.__screen=screen
    def getscreen(self):
        return self.__screen
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__memory
    def setstandby(self,standby):
        self.__standby=standby
    def getstandby(self):
        return self.__standby

    #行为
    def typing(self):
        print(self.__screen,"的屏幕很适合打字！！！")
    def playgame(self):
        print(self.__cpu,"的CPU和",self.__memory,"的内存很适合玩游戏！！！")
    def videos(self):
        print(self.__standby,"的待机时长很适合看视频！！！")

b=botebook()
b.setscreen("15寸")
b.setprice("3999元")
b.setcpu("i9-1050")
b.setmemory("16g")
b.setstandby("4h")
b.typing()
b.playgame()
b.videos()