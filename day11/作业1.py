# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体


class cup:
    __height = ""
    __volume = ""
    __color = ""
    __material = ""

    def setheight(self,height):
        self.__height=height
    def getheight(self):
        return self.__height
    def setvolume(self,volume):
        self.__volume=volume
    def getvolume(self):
        return self.__volume
    def setcolor(self,color):
        self.__color=color
    def getcolor(self):
        return self.__color
    def setmaterial(self,material):
        self.__material=material
    def getmaterial(self):
        return self.__material


    def deposit(self):
        print("能存放",self.__volume,"的液体")
c=cup()
c.setheight("10cm")
c.setvolume("500ml")
c.setcolor("白色")
c.setmaterial("玻璃")
c.deposit()