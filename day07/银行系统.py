import random
# 1. 空的银行的库 ： 100个
users = {}
inuser={
    "abcd1234":{
        "username":"张三",
        "password":"123456",
        "country":"中国",
        "province":"河北省",
        "street":"新街",
        "door":"58号",
        "money":"0",
        "bank_name":"中国工商银行新街支行"
    }
}
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
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
    if len(users) >= 100:
        return 3

    # 判断是否存在
    if account in users:
        return 2

    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
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
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")
#存钱逻辑
def cun_money(user,savemoney):
    if user not in users:
        return 1
    else:
        users[user]["money"] = users[user]["money"] + savemoney
        return 0

#存钱
def save_money():
    user=input("请输入账号：")
    savemoney=int(input("请输入存款金额："))
    status=cun_money(user,savemoney)
    if status==0:
        print("存款成功，您的余额为：",users[user]["money"])
    elif status==1:
        print("您输入的账户不存在！！！")

#取钱逻辑
def git_money(user,password,gitmoney):
    #账号不存在
    if user not in users:
        return 1
    #密码不正确
    if user in users:
            if password!=users[user]["password"]:
                return 2
    #钱不够
    if user in users:
        if password==users[user]["password"]:
            if users[user]["money"]<int(gitmoney):
                return 3
    #正常
    if user in users:
        if password==users[user]["password"]:
            if users[user]["money"]>=int(gitmoney):
                users[user]["money"]=users[user]["money"]-int(gitmoney)
                return 0
#取钱
def with_money():
    user=input("请输入账号：")
    password=input("请输入密码：")
    gitmoney=input("请输入取款金额：")
    status=git_money(user,password,gitmoney)
    if status==1:
        print("您输入的账号不存在！！！")
    elif status==2:
        print("您输入的密码错误！！！")
    elif status==3:
        print("您的余额不足！！！")
    elif status==0:
        print("取款成功！！！您的余额为：",users[user]["money"])

#转账逻辑
def money_transfer(outuser,takeinuser,password,outmoney):
    #收款账号或付款账号不存在
    if outuser not in users or takeinuser not in inuser:
            return 1
    #付款账号密码错误
    if outuser in users:
        if takeinuser in inuser:
            if password!=users[outuser]["password"]:
                return 2
    #付款账号余额不足
    if outuser in users:
        if takeinuser in inuser:
            if password==users[outuser]["password"]:
                if outmoney>users[outuser]["money"]:
                    return 3
    #正常
    if outuser in users:
        if takeinuser in inuser:
            if password==users[outuser]["password"]:
                if outmoney<=users[outuser]["money"]:
                    users[outuser]["money"]=users[outuser]["money"]-outmoney
                    inuser[takeinuser]["money"]=int(inuser[takeinuser]["money"])+int(outmoney)
                    return 0
#转账
def out_money():
    outuser=input("请输入转账账号：")
    takeinuser=input("请输入收款账号：")
    password=input("请输入转账账号密码：")
    outmoney=int(input("请输入转账金额："))
    status=money_transfer(outuser,takeinuser,password,outmoney)
    if status==1:
        print("您输入的账号错误！！！")
    elif status==2:
        print("您输入的密码错误！！！")
    elif status==3:
        print("您账号余额不足！！！")
    elif status==0:
        print("转账成功！您的余额为：",users[outuser]["money"])

#查询逻辑
def enquiry(user,password):
    #账号不存在
    if user not in users:
        return 1
    #密码错误
    if user in users:
        if password!=users[user]["password"]:
            return 2
    #正常
    if user in users:
        if password==users[user]["password"]:
            return 0
#查询
def query():
    user=input("请输入查询账号：")
    password=input("请输入密码：")
    status=enquiry(user,password)
    if status==1:
        print("您查询的账号不存在！！！")
    if status==2:
        print("您输入的密码错误：")
    if status==0:
        print("查询成功！信息如下！！！！")
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
        print(info %(user,users[user]["username"],password,users[user]["country"],users[user]["province"],users[user]["street"],users[user]["door"],users[user]["money"],bank_name))

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
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")







































