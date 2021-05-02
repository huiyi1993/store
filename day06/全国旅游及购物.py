city = {
    "北京":{
        "昌平区":{
            "回龙观":["永辉","永旺"],
            "龙泽":["海底捞","呷哺呷哺"]
        },
        "海淀区":{
            "公主坟":["军事博物馆","五道口切糕"],
            "香山":["香山","植物园"],
            "高校":["清华","北大"]
        },
        "朝阳区":{
            "朝阳南北塔":["世纪公园","玉渊潭公园"],
            "双塔":["双塔白醋"]
        },
        "延庆区":{
            "龙庆峡":["龙庆峡"]
        }
    }
}
def print_place(data):
    for i in data:
        print(i)
while True:
    print("--------------欢迎来到回忆旅游购物系统-------------")
    print_place(city)
    num1=input("请输入上侧列表中您要去的城市：")
    if num1 in city:
        print_place(city[num1])
        num2=input("请输入上侧列表中您要去的区域：")
        if num2 in city[num1]:
            print_place(city[num1][num2])
            num3=input("请输入上侧列表中您要去的地方：")
            if num3 in city[num1][num2]:
                print_place(city[num1][num2][num3])
                num4=input("请输入上侧列表中您想去的地方：")
                if num4 in city[num1][num2][num3]:
                    if num4=="永旺":
                       shop=input("您是否进入商店购物：")
                       if shop=="是":
                           import random

                           a = "电脑5折优惠券"
                           b = "充电宝满600-300"
                           coupons = [a, b]
                           # mycoupons为我的优惠券列表
                           mycoupons = []
                           shop = [
                               ["充电宝", 100, 100],
                               ["电脑", 5000, 100],
                               ["手机", 4000, 100],
                               ["键盘", 500, 100],
                               ["鼠标", 200, 100],
                               ["充电器", 100, 100],
                               ["手机壳", 50, 100]
                           ]
                           salary = int(input("请输入薪资："))
                           # mycart为我的购物车列表
                           mycart = []
                           # integral为每笔交易总价格列表
                           integral = []
                           getcoupons = random.choice(coupons)
                           print("------您获得了优惠券：", getcoupons, "------")
                           mycoupons.append(getcoupons)
                           print("--------优惠券库-------")
                           print(mycoupons)
                           print("---------------------")
                           while True:
                               for index, value in enumerate(shop):
                                   print(index, "   ", value)
                               id = input("请输入商品编号：")
                               if id.isdigit():
                                   id = int(id)
                                   if id >= len(shop):
                                       print("--------请输入正确编号！！！！---------")
                                   else:
                                       if salary >= shop[id][1]:
                                           if id == 1:
                                               num = input("请输入购买数量：")
                                               if num.isdigit():
                                                   if int(num) <= shop[id][2]:
                                                       if a in mycoupons:
                                                           c = input("是否使用优惠券：")
                                                           if c == "是":
                                                               i = int(num) - 1
                                                               mycart.append([shop[id][0],
                                                                              (shop[id][1] * 0.5) + (shop[id][1] * i),
                                                                              num])
                                                               salary = salary - (mycart[-1][1])
                                                               coupons.remove(a)
                                                               integral.append(mycart[-1][1])
                                                               print("----------添加购物车成功！！------------")
                                                           elif c == "否":
                                                               mycart.append([shop[id][0], shop[id][1] * int(num), num])
                                                               salary = salary - shop[id][1]
                                                               integral.append(mycart[-1][1])
                                                               print("----------添加购物车成功！！------------")
                                                           else:
                                                               print("---------输入非法字符--------")
                                                       else:
                                                           mycart.append([shop[id][0], shop[id][1] * int(num), num])
                                                           salary = salary - shop[id][1]
                                                           integral.append(mycart[-1][1])
                                                           print("----------添加购物车成功！！------------")
                                                   else:
                                                       print("----------库存不足----------")
                                               else:
                                                   print("---------输入非法字符--------")

                                           elif id == 0:
                                               num = input("请输入购买数量：")
                                               if num.isdigit():
                                                   if int(num) <= shop[id][2]:
                                                       if b in coupons:
                                                           if int(shop[id][1] * int(num)) >= 600:
                                                               d = input("是否使用优惠券：")
                                                               if d == "是":
                                                                   mycart.append(
                                                                       [shop[id][0], int(shop[id][1] * int(num)) - 300,
                                                                        num])
                                                                   salary = salary - (mycart[-1][1])
                                                                   mycoupons.remove(b)
                                                                   integral.append(mycart[-1][1])
                                                                   print("----------添加购物车成功！！------------")
                                                               elif d == "否":
                                                                   mycart.append(
                                                                       [shop[id][0], shop[id][1] * int(num), num])
                                                                   salary = salary - shop[id][1]
                                                                   integral.append(mycart[-1][1])
                                                                   print("----------添加购物车成功！！------------")
                                                               else:
                                                                   print("输入非法字符")
                                                           else:
                                                               mycart.append([shop[id][0], shop[id][1] * int(num), num])
                                                               salary = salary - shop[id][1]
                                                               integral.append(mycart[-1][1])
                                                               print("----------添加购物车成功！！------------")
                                                       else:
                                                           mycart.append([shop[id][0], shop[id][1] * int(num), num])
                                                           salary = salary - shop[id][1]
                                                           integral.append(mycart[-1][1])
                                                           print("----------添加购物车成功！！------------")
                                                   else:
                                                       print("----------库存不足----------")
                                               else:
                                                   print("---------输入非法字符--------")
                                           else:
                                               num = input("请输入购买数量：")
                                               if num.isdigit():
                                                   if int(num) <= shop[id][2]:
                                                       mycart.append([shop[id][0], shop[id][1] * int(num), num])
                                                       salary = salary - shop[id][1]
                                                       integral.append(mycart[-1][1])
                                                       print("----------添加购物车成功！！------------")
                                                   else:
                                                       print("----------库存不足----------")
                                               else:
                                                   print("---------输入非法字符--------")
                                       else:
                                           print("---------余额为：", salary, "！！钱不够！！！----------")
                               else:
                                   if id == "Q" or id == "q":
                                       print("----------欢迎下次光临！！----------")
                                       break
                                   else:
                                       print("--------输入非法字符----------")
                           print("----------您购买了以下商品----------")
                           print("编号    商品名   总价  购买数量")
                           for index, value in enumerate(mycart):
                               print(index, "   ", value)
                           print("积分为：", sum(integral) / 10)
                           print("总金额为：￥", sum(integral))
                           print("---------------------------------")
                           break
                       elif shop=="否":
                           print("------------祝您旅途愉快------------")
                           break
                       else:
                           print("-------------输入非法字符-----------")
                    else:
                        print("------------祝您旅途愉快------------")
                        break
                elif num4=="q" or num4=="Q":
                    print("--------------欢迎下次光临--------------")
                    break
                else:
                    print("未找到该地方，请重新输入！！！")

            elif num3 == "q" or num3 == "Q":
                print("--------------欢迎下次光临---------------")
                break
            else:
                print("未找到该地方，请重新输入！！！")

        elif num2 == "q" or num2 == "Q":
            print("--------------欢迎下次光临--------------")
            break
        else:
            print("没找到该区域，请重新输入！！！")

    elif num1 == "q" or num1 == "Q":
        print("--------------欢迎下次光临--------------")
        break
    else:
        print("未找到该城市，请重新输入！！！")























