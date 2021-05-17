import time
class Oldphone:
    __Brand = ""
    def setBrand(self,brand):
        self.__Brand = brand
    def getBrand(self):
        return self.__Brand
    def Call(self,fornum):
        print("正在给",fornum,"打电话")
        for i in range(3):
            time.sleep(1)
            print(".",end="")

class Newphone(Oldphone):
    def Call(self,fornum):
        print("语音拨号中")
        for i in range(3):
            time.sleep(1)
            print(".",end="")

        super().Call(fornum)
    def Introduce(self):
        print("品牌为：",self.getBrand(),"的手机很好用！！！")

class Test(Newphone):
    def __init__(self):
        self.setBrand("华为")

print(Test().Introduce())
print(Test().Call("15232112313"))



















