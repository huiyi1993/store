name = "root"
pas = "admin"
count = 1

while count < 4:
     name1 = input("用户名：")
     pas1 = input("密码：")
     count = count + 1
     if pas1 == pas:
        print("登陆成功")
        break
     else:
      print("密码错误")
     while count == 4:
      print("账户锁定")
      break












