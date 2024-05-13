"""
三邊長abc
判斷是不是三角形
是的話再判斷是不是直角三角形
"""
a=int(input("邊長1:"))
b=int(input("邊長2:"))
c=int(input("邊長3:"))

if (a+b>=c and a+c>=b and b+c>=a):
    print("沒錯!這就是三角形")
    if ((a*a)+(b*b)==(c*c) or (a*a)+(c*c)==(b*b) or (b*b)+(c*c)==(a*a)):
        print("沒錯!這就是直角三角形")
    else:
        print("這不是直角三角形")
else:
    print("不是三角形")
              
