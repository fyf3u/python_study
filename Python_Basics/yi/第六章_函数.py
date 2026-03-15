# 第六章
# 6.1函数概述
# 函数是组织好的、实现单一功能或相关联功能的代码段。可以将其视为一段有名字的代码，这类代码可以在需要的地方以“函数名()”的形式调用。
# 优点，使用函数编程可以使程序模块化，即减少了冗余代码，又让程序结构更为清晰；既能提高开发人员的编程效率，又方便后期的维护和扩展。
# 6.2函数的定义和调用
# 6.2.1定义函数
def add():
    result = 10+10
    print(result)
# 6.2.2调用函数
add() # 20
# 6.2.3扩展：函数的嵌套定义
def add_modify(a,b):
   result = a+b
   print(result)
   def test():
       print("我是内层函数")
   test() #
# test() # 外部无发调用 编译器报错
add_modify(1, 3) # 4  我是内层函数

# 6.3 函数参数的传递
# 6.3.1 位置参数的传递
def get_max(a,b):
    if a>b :
        print(f"{a}是较大的值")
    elif a==b :
        print("两个值相等")
    else :
        print(f"{b}是较大的值")
get_max(8,9)

# 6.3.2关键字参数的传递
def connect(ip,port) :
    print(f"成功链接设备{ip}：{port}")
connect(port=8080,ip="127.0.0.1")  # 成功链接设备127.0.0.1：8080
# Python3.8中新增了仅限位置新参的语法，使用“/”来限定部分形参只接采用位置参数传递方式的实参。即符号“/”之前的参数只能接收采用位置参数传递的实参，之后的都可以。
def func(a,b,/,c):
    print(a,b,c)
#func(a=0,1,2) #报错
#func(0,b=1,2) #报错
func(0,1,c=2) # 正确
func(0,1,2) # 正确

# 6.3.3默认参数的传递
def connect(ip,port=8080) :
    print(f"成功链接设备{ip}：{port}")
connect(ip="127.0.0.1")  # 成功链接设备127.0.0.1：8080
connect(ip="127.0.0.1",port=80)  # 成功链接设备127.0.0.1：80

# 6.3.4参数的打包与解包
# 1.打包
def test(*args):
    print(args)
test(1,'a',0.4,'b') #(1, 'a', 0.4, 'b')

def test(**kwargs):
    print(kwargs)
test(k1="v1",k2="v2",k3="v3") # {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# 2.解包
def test(a,b,c):
    print(a,b,c)
nums_s = (11,22,33)
test(*nums_s) # 11 22 33
nums_d = {"a":11,"b":2,"c":33}
test(**nums_d) # 11 2 33
# 6.3.5混合传递
def test(a,b,c=80,*args,**kwargs):
    print(a,b,c,args,kwargs)
test(1,2) # 1 2 80 () {}
test(1,2,3) # 1 2 3 () {}
test(1,2,3,5) # 1 2 3 (5,) {}
test(1,2,3,4,key='value') #1 2 3 (4,) {'key': 'value'}
