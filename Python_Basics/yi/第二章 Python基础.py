# 2.1 代码格式
# 2.1.1 注释
# 1.单行注释
print('Hello,Python')   # 单行注释 打印Hello,Python
# 2.多行注释
print("获取print()函数的说明文档")
print(print.__doc__)
''' 此为print()函数的说明文档
Prints the values to a stream, or to sys.stdout by default.

  sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout.
  flush
    whether to forcibly flush the stream.
'''
# 2.1.2 缩进
# 示例
if False:
    print("True")
else:
    print("False")
# 同一代码块不相同缩进导致报错
if True:
    print("True")
    print("正确")
else:
    print("False")
    print("错误")   # 缩进不一致，导致运行是报错

# 2.1.3 语句换行
string = ("Python官方建议每行代码不超过79个字符，若代码过长应该换行。Python会将圆括号、"
          "中括号和大括号中的行进行隐式链接，可以根据这个特点在语句外侧添加一对圆括号，"
          "实现过长语句的换行显示")
print(string)
# 需要注意的是，原本由圆括号、中括号和大括号包裹的语句在换行时不需要另行添加圆括号
total = ['item_one','item_two',
         'item_three','item_four']
print(total[1])
print(len(total))
# 2.2 标识符和关键字
# 2.2.1 标识符  举例
# 由字母、数字或下划线组成，且不能以数字开头
# 区分大小写。如，Study和study是不同的标识符
# 不允许使用关键字作为作为标识符
fromNo12 =1   # 合法
# from#12     # 不合法  不能包含‘#’
# 2ndObj      # 不合法  不能数字开头
# if=1        # 不合法  if是关键字
#  除了以上规则外，还有一下两点建议：
# （1）见名知意；
# （2）命名规范：
# 1)常量名-使用大写的单个单词或由下划线连接的多个单词。如，ORDER_NAME
# 2)模块名、函数名-使用小写的单词或有下划线连接的多个单词。如，low_with_under
# 3)类名-使用大写字母开头的单个或多个单词。如，Cat、CapWorld

# 2.2.2 关键词
# 查看关键词
import keyword #导入包
print(keyword.kwlist)
print(len(keyword.kwlist)) #统计个数
#  结果如下['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print('查看关键字import的声明:')
print(help("import"))

'''
The "import" statement
**********************

   import_stmt     ::= "import" module ["as" identifier] ("," module ["as" identifier])*
                       | "from" relative_module "import" identifier ["as" identifier]
                       ("," identifier ["as" identifier])*
                       | "from" relative_module "import" "(" identifier ["as" identifier]
                       ("," identifier ["as" identifier])* [","] ")"
                       | "from" relative_module "import" "*"
   module          ::= (identifier ".")* identifier
   relative_module ::= "."* module | "."+

'''
# 2.3 变量和数据类型
# 2.3.1 变量
# 定义变量    变量名 = 值
data = 100
print(data)

# 2.3.2 数据类型
# 1.数字类型
# 整型(int)
print(0,101,-239)
# 浮点型(float)
print(3.1415,4.2E-10,-2.334E-9)
# 复数类型(complex)
#print(3.12+1.2.3j)
# 布尔类型(bool)
print(True,False)

# 2.字符串 由单引号、双引号或三引号包裹的有序的字符集合
print('Pyhon123#')
print("sad")
print('''Pyhon123YEU&*!''')

# 3.列表 它可以保存任意数量、任意类型的元素，且可以被修改。 Python中使用“[]”创建列表，列表中的元素以逗号分割
list1 = [1,2,'hello']
print(list1)
list1[1]=3
print(list1)

#4 元组 与列表功能类似，可以存放任意数量、任意类型的元素，但不可以修改。python中以“()”创建元组，元素使用逗号分割
my_tuple = (1,2,'hello yz')
print(my_tuple)
#my_tuple[1] = 3 #修改会报错 TypeError: 'tuple' object does not support item assignment
print(my_tuple)

# 5.集合 集合与列表、元组类似，也可以保存任意数量、任意类型的元素，区别在于集合使用“{}”创建、集合中的元素无序且唯一。
my_set = {1,2,3,"hello"}
#print(my_set[0]) # 'set' object is not subscriptable 因为集合无需所以报错不能使用该方式获取
print(1 in my_set)  # 判断值是否存在集合 输出 True 或 False

# 6.字典 其中的元素是“键（Key）：值（Value）”形式的键值对，键不能重复。Python中使用”{}“创建字典，字典中的各元素以逗号分隔
my_dict = {"name":"张三","age":18}
print(my_dict.get("name"))  # 张三
print(my_dict.values()) #  dict_values(['张三', 18])
# 小提示: Python是动态语言，在声明变量时无须显式地指明变量的具体类型，程序执行时python解释器会自动确定数据类型，可以通过type()函数查看变量所保存数据的具体类型
my_list = [1,2,23,2]
print(type(my_list))   #<class 'list'>

# 2.3.3 变量的输入与输出
# 1. input()函数
#name = input("请输入你的名字：") # 其中"请输入你的名字："不会复制给name，只是提示词
#print('您输入的是:'+name)

# 2.print()函数 该函数用于想控制台输出数据，他可以输出任意类型的数据，其语法格式如下：
name="张三"
age = 18
print(name,age,sep="|",end='\n') # 张三|18

# 2.5 数字类型
# 2.5.1 整数类型
print(0b101)    # 二进制
print(0o5)      # 八进制
print(5)        # 十进制
print(0x5)      # 16进制
# python中内置类用于转换数据进制的函数,演示
decimal = 10    # 十进制数据
bin_num = 0b1010    # 二进制数据
print(bin(decimal)) # 十进制 转 二进制
print(oct(decimal)) # 十进制 转 八进制
print(int(bin_num)) # 二进制 转 十进制
print(hex(decimal)) # 十进制 转 十六进制

# 2.5.2 浮点型
print(1.8e3333) # inf 无穷大
print(-1.8e3333) # -inf 无穷小

# 2.5.3 复数类型
complex_one = 1.1+2j
complex_two = 1
complex_three = 2j
print(complex_one.real) # 1.0
print(complex_one.imag) # 2.0
print(complex_two.real) # 1
print(complex_two.imag) # 0
print(complex_three.real) # 0.0
print(complex_three.imag) # 2.0

# 2.5.4 布尔类型
print(bool(0)) # False
print(bool('')) # False
print(bool(1)) # True

# 2.5.5 数字类型转换
num_one = 2
num_two = 2.8
print(int(num_two))     # 2
print(float(num_one))   # 2.0
print(complex(num_one)) # (2+0j)

# 2.6 运算符
# 2.6.1 算术运算符
print(8.8/2)
print(10.8-(3+5j))

# 2.6.2 赋值运算符
num = 3
x = y = z = 10 # x,y,z赋值10
a,b = 1,2 # a=1 b=2
print(a,b) # 1 2
# 海象运算符
num_1 = 1
result = num_1 + (num_2:=2)
print(result)

# 2.6.3 比较运算符
print( 1 == 1)
print( 2 >= 1)

# 2.6.4 逻辑运算符
# 数字运算
print(1 and 2)  # 2
print(0 and 2)  # 0
print(None and 2)  # None
print(3 or 0)   # 3
print(0 or 4)   # 4
print(not 0)    # True

# 2.6.5 成员运算符
a = 'banana'
b = 'a'
print(b in a )
print(b not in a )

# 2.6.6 位运算符
a = 5
print(bin(a))  # 原值 0b101
print(bin(a<<1)) # 左移 0b1010
print(bin(a>>1)) # 左移 0b10
print(5&3) # 1  0101 & 0011
print(5|3) # 7
print(5^3) # 6
print(~5) # -6

# 2.6.7 运算符优先级
a = 2
b = 3
c = 4
print(c*a**b) # 32 先进行幂运算 4*8
print(c+a*b*(a-b)) # -2 先计算括号内容4+2*3*-1 在计算乘除 4+（-6）

# 习题 要求 用程序进行计算
# 习题1 共有29.5t水，先用4t的车运3次，剩下的用2.5t的车运，问要云几次？
print((29.5-4*3)/2.5) # 7
# 习题2 根据输入半径R，计算圆的直径和面积
r = float(input("请输入圆形半径:"))
#r=2
d = 2*r
S = 3.1415926*r**2
print('直径：',d)
print('面积：',S)


