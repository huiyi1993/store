import threading
import time
#篮子
basket = 0
#总制作
make = 0
#总购买
sell = 0
start = 0

class Time(threading.Thread):
    def run(self) -> None:
        global start
        while True:
            if start<10:
                start = start + 1
                time.sleep(1)
            else:
                break
class Cook(threading.Thread):
    name = ""
    def run(self) -> None:
        global basket
        global make
        while True:
            if start<10:
                if basket<300:
                    basket = basket + 1
                    make = make + 1
                else:
                    time.sleep(3)

            else:
                print("厨师总共制作", make, "个面包。")
                break

class Customer(threading.Thread):
    name = ""
    num = 0
    def run(self) -> None:
        global basket
        global sell
        while True:
            if start<10:
                if basket>0:
                    basket = basket - 1
                    sell = sell +1
                    self.num = self.num + 1

            else:
                print("顾客总共购买了", sell, "个面包。")
                break

        print(self.name,"共花费",self.num*10)




t = Time()
co1 = Cook()
co2 = Cook()
co3 = Cook()
co4 = Cook()
co5= Cook()
co6 = Cook()
cu1 = Customer()
cu2 = Customer()
cu3 = Customer()
cu4 = Customer()
cu5 = Customer()
co1.name = "张一"
co2.name = "张二"
co3.name = "张三"
co4.name = "张四"
co5.name = "张五"
co6.name = "张六"
cu1.name = "李一"
cu2.name = "李二"
cu3.name = "李三"
cu4.name = "李四"
cu5.name = "李五"

co1.start()
co2.start()
co3.start()
co4.start()
co5.start()
co6.start()
cu1.start()
cu2.start()
cu3.start()
cu4.start()
cu5.start()
t.start()






