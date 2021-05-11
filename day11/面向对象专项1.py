class conditioner:
    __brand = ""
    __price = ""
    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def open(self):
        print("空调开机了")
    def close(self,time):
        time=int(time)
        print("空调将在",time,"分钟后关闭！！！")


c=conditioner()
c.setbrand("格力")
c.setprice("1999元")
print("品牌为：",c.getbrand(),"价格为：",c.getprice())
c.open()
c.close("10")











