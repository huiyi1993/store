import random
from DBUtils import updata
from DBUtils import select
from DBUtils import close
bank_name = "中国工商银行昌平支行"

#界面类
class Welcome:
    info = '''
    *************************
    *    银行管理系统v3.0     *
    *************************
    *1.开户                  *
    *2.存钱                  *
    *3.取钱                  *
    *4.转账                  *
    *5.查询                  *
    *6.退出                  *
    *************************
    '''
    def welcome(self):
        print(self.info)

#用户类
class User:
    __id = 0
    __name = ""
    __password = 0
    __add = None
    __balance = 0
    __time = ""
    __bank = bank_name
    def setId(self,id):
        self.__id=id
    def getId(self):
        return self.__id
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setPassword(self,password):
        self.__password=password
    def getPassword(self):
        return self.__password
    def setAdd(self,add):
        self.__add=add
    def getAdd(self):
        return self.__add
    def setBalance(self,balance):
        self.__balance=balance
    def getBalance(self):
        return self.__balance
    def setTime(self,time):
        self.__time=time
    def getTime(self):
        return self.__time
    def getBank(self):
        return self.__bank

#地址类
class Address:
    __country = ""
    __province = ""
    __street = ""
    __door = ""
    # def __init__(self,country,province,street,door):
    #     self.__country=country
    #     self.__province=province
    #     self.__street=street
    #     self.__door=door
    def setCountry(self,country):
        self.__country=country
    def getCountry(self):
        return self.__country
    def setProvince(self,province):
        self.__province=province
    def getProvince(self):
        return self.__province
    def setStreet(self,street):
        self.__street=street
    def getStreet(self):
        return self.__street
    def setDoor(self,door):
        self.__door=door
    def getDoor(self):
        return self.__door

#逻辑方法类（银行类）
class User_method:
    #开户逻辑
    def method(self,u,ad):
        #判断是否数据库已满

        sql = "select * from user"
        data = select(sql,[])
        if len(data)>=100:
            return 3
        #判断用户存不存在
        sql = "select * from user where account = %s"
        data = select(sql,u.getId())
        if len(data)!=0:
            return 2
        #正常开户
        print(u.getId())
        sql = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [u.getId(),u.getName(),u.getPassword(),ad.getCountry(),ad.getProvince(),ad.getStreet(),ad.getDoor(),u.getBalance(),u.getTime(),u.getBank()]
        updata(sql,param)
        return 1
    #存款逻辑
    def savemoney(self,u):
        #判断用户是否存在
        sql = "select * from user where account = %s"
        data = select(sql,u.getId())
        if len(data)!=0:
            sql = "update user set balance = balance + %s where account = %s"
            updata(sql,[u.getBalance(),u.getId()])
            return 1
        else:
            return 2

    #取款逻辑
    def getmoney(self,u):
        #判断账号是否存在
        sql = "select * from user where account = %s"
        data = select(sql,u.getId())
        if len(data)!=0:
            #判断密码
            sql = "select * from user where account = %s and password = %s"
            data = select(sql,[u.getId(),u.getPassword()])
            if len(data)!=0:
                #判断余额
                sql = "select * from user where account = %s and balance >= %s"
                data = select(sql,[u.getId(),u.getBalance()])
                if len(data)!=0:
                    sql = "update user set balance = balance - %s where account = %s"
                    updata(sql,[u.getBalance(),u.getId()])
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    #转账逻辑
    def transfer(self,u,user):
        #判断账号是否存在
        sql = "select * from user where account = %s"
        data = select(sql,u.getId())
        sql = "select * from user where account = %s"
        data1 = select(sql, user)
        if len(data)!=0 and len(data1)!=0:
            #判断密码
            sql = "select * from user where account = %s and password = %s"
            data = select(sql,[u.getId(),u.getPassword()])
            if len(data)!=0:
                #判断余额
                sql = "select * from user where account = %s and balance >= %s"
                data = select(sql,[u.getId(),u.getBalance()])
                if len(data)!=0:
                    sql = "update user set balance = balance -%s where account = %s"
                    updata(sql,[u.getBalance(),u.getId()])
                    sql = "update user set balance = balance + %s where account = %s"
                    updata(sql,[u.getBalance(),user])
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    #查询逻辑
    def query(self,u):
        #判断账号是否存在
        sql = "select * from user where account = %s"
        data = select(sql,u.getId())
        if len(data)!=0:
            #判断密码
            sql = "select * from user where account = %s and password = %s"
            data = select(sql,[u.getId(),u.getPassword()])
            if len(data)!=0:
                sql = "select * from user where account = %s"
                data = select(sql,u.getId())
                info = '''
                
                ----------个人信息----------
                账号：%s
                姓名：%s
                密码：%s
                地址：
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                余额：%s
                注册时间：%s
                开户行：%s
                ---------------------------
                '''
                print(info % (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],))
                return 0
            else:
                return 2
        else:
            return 1

#方法类（入口类）
# class Input():
#     #开户输入方法
#     def open_account(self):
#         u = User()
#         u.setId(random.randint(10000000, 99999999))
#         u.setName(input("请输入姓名："))
#         u.setPassword(input("请输入密码："))
#         ad = Address()
#         ad.setCountry(input("请输入国家："))
#         ad.setProvince(input("请输入省份："))
#         ad.setStreet(input("请输入街道："))
#         ad.setDoor(input("请输入门牌号："))
#         u.setAdd(ad)
#         u.setTime(input("请输入注册时间："))
#         sataue = User_method().method(u,ad)
#         if sataue==1:
#             info = '''
#                        ----------个人信息----------
#                        账号：%s
#                        姓名：%s
#                        密码：%s
#                        地址：
#                            国家：%s
#                            省份：%s
#                            街道：%s
#                            门牌号：%s
#                        余额：%s
#                        注册时间：%s
#                        开户行：%s
#                        ---------------------------
#                        '''
#
#             print("开户成功！！！")
#             print(info % (
#             u.getId(), u.getName(), u.getPassword(), ad.getCountry(), ad.getProvince(), ad.getStreet(), ad.getDoor(),
#             u.getBalance(), u.getTime(), u.getBank()))
#         elif sataue==2:
#             print("账号存在！请重新开户！！！！")
#         elif sataue==3:
#             print("数据库已满！！！！！")
#     #存款输入方法
#     def save_money(self):
#         u = User()
#         u.setId(input("请输入账号："))
#         u.setBalance(input("请输入存钱金额："))
#         sataue = User_method().savemoney(u)
#         if u.getBalance().isdigit():
#             if float(u.getBalance())>=0:
#
#                 if sataue==1:
#                     sql = "select * from user where account = %s"
#                     data = select(sql,u.getId())
#                     print("存款成功，您的余额为：",data[0][7])
#                 elif sataue==2:
#                     print("账户不存在！！！！！")
#             # else:
#             #     print("别瞎输入！！！")
#         else:
#             print("输入非法！！！")
#
#     #取款输入方法
#     def get_money(self):
#         u = User()
#         u.setId(input("请输入账号："))
#         u.setPassword(input("请输入密码："))
#         u.setBalance(input("请输入取款金额："))
#         sataue = User_method().getmoney(u)
#         if u.getBalance().isdigit():
#             if float(u.getBalance())>=0:
#                 if sataue==0:
#                     sql = "select * from user where account = %s"
#                     data = select(sql,u.getId())
#                     print("取款成功！！！余额为：",data[0][7])
#                 elif sataue==1:
#                     print("账户不存在！！！")
#                 elif sataue==2:
#                     print("密码错误！！！")
#                 elif sataue==3:
#                     print("余额不足！！！！")
#             # else:
#             #     print("别瞎输入！！！！")
#         else:
#             print("非法输入！！！")
#
#     #转账输入方法
#     def transfer_account(self):
#         u = User()
#         u.setId(input("请输入账号："))
#         user = input("请输入收款账号：")
#         u.setPassword(input("请输入密码："))
#         u.setBalance(input("请输入转账金额："))
#         sataue = User_method().transfer(u, user)
#         if u.getBalance().isdigit():
#             if float(u.getBalance())>=0:
#                 if sataue==0:
#                     sql = "select * from user where account = %s"
#                     data = select(sql,u.getId())
#                     print("转账成功！！！余额为：",data[0][7])
#                 elif sataue==1:
#                     print("账号不存在！！！")
#                 elif sataue==2:
#                     print("密码错误！！！")
#                 elif sataue==3:
#                     print("余额不足！！！")
#             # else:
#             #     print("别瞎输入！！！")
#         else:
#             print("输入非法！！！")
#
#     #查询输入方法
#     def query_account(self):
#         u = User()
#         u.setId(input("请输入账号："))
#         u.setPassword(input("请输入密码："))
#         sataue = User_method().query(u)
#         if sataue==0:
#             print("查询成功！！！！")
#         elif sataue==1:
#             print("账号不存在！！！")
#         elif sataue==2:
#             print("密码错误！！！")
#
# while True:
#     Welcome().welcome()
#     num = input("请输入业务编号：")
#     if num.isdigit():
#         num=int(num)
#         if num==1:
#             Input().open_account()
#         elif num==2:
#             Input().save_money()
#         elif num==3:
#             Input().get_money()
#         elif num==4:
#             Input().transfer_account()
#         elif num==5:
#             Input().query_account()
#         elif num==6:
#             print("欢迎下次光临！！！！！")
#             close()
#             break
#     else:
#         print("输入非法！！！！！")






































