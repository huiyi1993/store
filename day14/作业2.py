class Cook:
    __name = ""
    __age = 0
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def steamed_Rice(self):
        pass


class Big_cook(Cook):
    def Stir_fry_vegetables(self):
        pass

class Little_cook(Big_cook):
    def Steamed_Rice(self):
        print(self.getName(), "正在厨房蒸米饭！！！")
    def Stir_Fry_Vegetables(self):
        print(self.getName(), "正在炒菜！！！")

class Test(Little_cook):
    def __init__(self):
        self.setName("张三")
        self.setAge(25)
print(Test().getName(),Test().getAge())
print(Test().Steamed_Rice())
print(Test().Stir_Fry_Vegetables())
















