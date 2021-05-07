import random
from DBUtils import update
from DBUtils import  select
from DBUtils import close
# 1. 空的银行的库 ： 100个

# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V2.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满

    sql="select * from users"
    data = select(sql,[])
    print(data)
    if len(data) >= 100:
        return 3

    # 判断是否存在
    sql="select * from users where id = %s"
    data=select(sql,account)

    if len(data)!=0:
        return 2

    #正常开户

    sql="insert into users value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param=[account,username,password,country,province,street,door,0,bank_name]
    update(sql,param)
    return 1

# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

#存钱逻辑
def cun_money(user,savemoney):

    sql="select * from users where id = %s"

    data=select(sql,user)
    if len(data) != 0:
        sql2 = "update  users  set  money =  money + %s where  id = %s"
        update(sql2,[savemoney,user])
        return 1
    else:
        return 0

#存钱
def save_money():
    user = input("请输入账号：")
    savemoney = input("请输入存款金额：")
    if savemoney.isdigit():
        savemoney = int(savemoney)
        status=cun_money(user,savemoney)
        if status==1:

            sql = "select * from users where id = %s"
            data=select(sql,user)

            print("存款成功，您的余额为：",data[0][7])
        elif status==0:
            print("您输入的账户不存在！！！")
    else:
        print("输入非法字符！！！")

#取钱逻辑
def git_money(user,password,gitmoney):
    #账号不存在

    sql="select * from users where id = %s"
    data=select(sql,user)
    if len(data)!=0:
        sql1="select * from users where id = %s and upassword = %s"
        data=select(sql1,[user,password])
        if len(data)!=0:
            sql2="select * from users where id = %s and upassword = %s and money >= %s"
            data=select(sql2,[user,password,gitmoney])
            if len(data)!=0:
                sql3="update users set money = money - %s where id = %s"
                update(sql3,[gitmoney,user])
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
#取钱
def with_money():
    user=input("请输入账号：")
    password=input("请输入密码：")
    gitmoney=input("请输入取款金额：")
    if gitmoney.isdigit():
        gitmoney=int(gitmoney)
        status=git_money(user,password,gitmoney)
        if status==1:
            print("您输入的账号不存在！！！")
        elif status==2:
            print("您输入的密码错误！！！")
        elif status==3:
            print("您的余额不足！！！")
        elif status==0:

            sql = "select * from users where id=%s"
            data=select(sql,user)
            print("取款成功！！！您的余额为：",data[0][7])
    else:
        print("输入非法字符！！！")

#转账逻辑
def money_transfer(outuser,takeinuser,password,outmoney):


    sql="select * from users where id=%s "
    data=select(sql,outuser)
    sql5="select * from users where id=%s"
    data1=select(sql5,takeinuser)
    if len(data)!=0 and len(data1)!=0:
        sql1="select * from users where id=%s and upassword=%s"
        data=select(sql1,[outuser,password])
        if len(data)!=0:
            sql2="select * from users where id=%s and money>=%s"
            data=select(sql2,[outuser,outmoney])
            if len(data)!=0:
                sql3="update users set money=money-%s where id=%s"
                update(sql3,[outmoney,outuser])
                sql4="update users set money=money+%s where id=%s"
                update(sql4,[outmoney,takeinuser])

                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

#转账
def out_money():
    outuser=input("请输入转账账号：")
    takeinuser=input("请输入收款账号：")
    password=input("请输入转账账号密码：")
    outmoney=input("请输入转账金额：")
    if outmoney.isdigit():
        outmoney=int(outmoney)
        status=money_transfer(outuser,takeinuser,password,outmoney)
        if status==1:
            print("您输入的账号错误！！！")
        elif status==2:
            print("您输入的密码错误！！！")
        elif status==3:
            print("您账号余额不足！！！")
        elif status==0:

            sql="select * from users where id=%s"
            data=select(sql,outuser)
            print("转账成功！您的余额为：",data[0][7])
    else:
        print("输入非法字符！！！")

# 查询逻辑
def enquiry(user,password):
    #账号不存在

    sql="select * from users where id=%s"
    data=select(sql,user)
    if len(data)!=0:
        sql="select * from users where id=%s and upassword=%s"
        data=select(sql,[user,password])
        if len(data)!=0:
            return 0
        else:
            return 2
    else:
        return 1

#查询
def query():
    user=input("请输入查询账号：")
    password=input("请输入密码：")
    status=enquiry(user,password)
    if status==1:
        print("您查询的账号不存在！！！")
    if status==2:
        print("您输入的密码错误！！！")
    if status==0:
        print("查询成功！信息如下！！！！")

        sql="select *from users where id=%s"
        data=select(sql,user)

        info='''
        ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
        -----------------------------------
        '''
        print(info %(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8]))

while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            save_money()
        elif num == 3:
            with_money()
        elif num == 4:
            out_money()
        elif num == 5:
            query()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            close()
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")







































