import random
num = random.randint(0,100)
count = 0
gold=1000
while count<7 and gold>=100:
    count = count + 1
    num1 = input("请输入您要猜的号码：")
    num1 = int(num1)
    gold=gold-100
    if num1 > num:
        print("大了")
    elif num1 < num:
        print("小了")
    else:
        print("猜中了，号码为：",num1,"一共用了",count,"次。","所剩金币：",gold)
        break
    while count==7:
        print("账户锁定")
        break
while gold<100:
       input("请输入您要猜的号码：")
       print("金币不足")
       break








