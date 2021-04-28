'''
    商城：
        1.商品
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1够了，就添加我的购物车，薪资减去相对应的金额
            4.2不够，买其他的。
        继续买东西，一直到输入Q获取q，退出
'''
import random
a="电脑5折优惠券"
b="充电宝满600-300"
coupons=[a,b]
mycoupons=[]
shop=[
    ["充电宝",100,100],
    ["电脑",5000,100],
    ["手机",4000,100],
    ["键盘",500,100],
    ["鼠标",200,100],
    ["充电器",100,100],
    ["手机壳",50,100]
]
salary=int(input("请输入薪资："))
mycart=[]
integral=[]
getcoupons=random.choice(coupons)
print("------您获得了优惠券：",getcoupons,"------")
mycoupons.append(getcoupons)
print("--------优惠券库-------")
print(mycoupons)
print("---------------------")
while True:
    for index,value in enumerate(shop):
        print(index,"   ",value)
    id=input("请输入商品编号：")
    if id.isdigit():
        id=int(id)
        if id>=len(shop):
            print("--------请输入正确编号！！！！---------")
        else:
            if salary>=shop[id][1]:
                if id==1:
                    num=input("请输入购买数量：")
                    if num.isdigit():
                        if int(num)<=shop[id][2]:
                            if a in mycoupons:
                                c=input("是否使用优惠券：")
                                if c=="是":
                                    i=int(num)-1
                                    mycart.append([shop[id][0],(shop[id][1]*0.5)+(shop[id][1]*i),num])
                                    salary=salary-(mycart[-1][1])
                                    coupons.remove(a)
                                    integral.append(mycart[-1][1])
                                    print("----------添加购物车成功！！------------")
                                elif c=="否":
                                    mycart.append([shop[id][0],shop[id][1]*int(num),num])
                                    salary = salary - shop[id][1]
                                    integral.append(mycart[-1][1])
                                    print("----------添加购物车成功！！------------")
                                else:
                                    print("---------输入非法字符--------")
                            else:
                                mycart.append([shop[id][0],shop[id][1]*int(num),num])
                                salary = salary - shop[id][1]
                                integral.append(mycart[-1][1])
                                print("----------添加购物车成功！！------------")
                        else:
                            print("----------库存不足----------")
                    else:
                        print("---------输入非法字符--------")

                elif id==0:
                    num=input("请输入购买数量：")
                    if num.isdigit():
                        if int(num)<=shop[id][2]:
                            if b in coupons:
                                if int(shop[id][1]*int(num))>=600:
                                    d=input("是否使用优惠券：")
                                    if d=="是":
                                        mycart.append([shop[id][0],int(shop[id][1]*int(num))-300,num])
                                        salary=salary-(mycart[-1][1])
                                        mycoupons.remove(b)
                                        integral.append(mycart[-1][1])
                                        print("----------添加购物车成功！！------------")
                                    elif d=="否":
                                        mycart.append([shop[id][0],shop[id][1]*int(num),num])
                                        salary = salary - shop[id][1]
                                        integral.append(mycart[-1][1])
                                        print("----------添加购物车成功！！------------")
                                    else:
                                        print("输入非法字符")
                                else:
                                    mycart.append([shop[id][0],shop[id][1]*int(num),num])
                                    salary = salary - shop[id][1]
                                    integral.append(mycart[-1][1])
                                    print("----------添加购物车成功！！------------")
                            else:
                                mycart.append([shop[id][0],shop[id][1]*int(num),num])
                                salary = salary - shop[id][1]
                                integral.append(mycart[-1][1])
                                print("----------添加购物车成功！！------------")
                        else:
                                print("----------库存不足----------")
                    else:
                        print("---------输入非法字符--------")
                else:
                    num=input("请输入购买数量：")
                    if num.isdigit():
                        if int(num )<= shop[id][2]:
                            mycart.append([shop[id][0],shop[id][1]*int(num),num])
                            salary = salary - shop[id][1]
                            integral.append(mycart[-1][1])
                            print("----------添加购物车成功！！------------")
                        else:
                                print("----------库存不足----------")
                    else:
                        print("---------输入非法字符--------")
            else:
                print("---------余额为：",salary,"！！钱不够！！！----------")
    else:
        if id=="Q" or id=="q":
            print("----------欢迎下次光临！！----------")
            break
        else:
            print("--------输入非法字符----------")
print("----------您购买了以下商品----------")
print("编号    商品名   总价  购买数量")
for index,value in enumerate(mycart):
    print(index,"   ",value)
print("积分为：",sum(integral)/10)
print("总金额为：￥",sum(integral))
print("---------------------------------")


























