a = input("请输入a边：")
b = input("请输入b边：")
c = input("请输入c边：")
a = int(a)
b = int(b)
c = int(c)

if a == b and a == c:
    print("三角形为等边三角形")
elif a == b and b!=c or a == c and c!=b or b == c and c!=a:
    print("三角形为等腰三角形")
elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a* a:
    print("三角形为直角三角形")
elif a+b>c and a-b<c and a!=0 and b!=0 and c!=0:
    print("三角形为普通三角形")
else:
    print("不构成三角形")










