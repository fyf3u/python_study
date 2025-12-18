# 第四章 符串
# 4.1 字符串介绍
# 4.1.1 字符串定义
from time import sleep

print('使用单引号定义的字符串')
print("使用双引号定义的字符串")
print("""使用三引号定义的字符串
        可以换行""")
# print('let's lear python') # 语法错误
print("let's lear python") # 使用其他两种引号
print('let\'s lear python') # 使用反斜杠 转义

# 4.1.2 转义字符
print('ab\tab')  # ab	ab 水平制表符（Tab键），一般相当于2个空格
print('ab\nabn') # ab
                 # abn    换行符
print('1123svs\rabr') # abr  回车符 开始覆盖内容到所在位置结束
print(r'转义字符中\n表示换行；\r表示回车；\b表示退格') # r或R，显示原始字符

# 4.2 字符串格式化
# 4.2.1 使用%格式字符串
print('我今年%d岁了' % 10) # 我今年10岁了
# print( '今天是%d' % '周一') # %d转化为整数，因此报错 TypeError: %d format: a real number is required, not str
name = '张三'
age = 18
six = '男'
print('姓名:%s \n年龄:%d \n性别:%s' %(name,age,six))

# 4.2.2 使用format()方法格式化字符串
print('姓名：{}； 年龄：{}； 性别：{}'.format('李四','18','男')) # 占位符{}不指定任何值
print('姓名：{1}； 年龄：{0}； 性别：{2}'.format('18','李四','男')) # 占位符{}指定下标
name,age,sex = '李四',18,'男'
print('姓名：{name}； 年龄：{age}； 性别：{sex}'.format(name=name,age=age,sex=sex)) # 占位符{}指定变量,后面进行赋值
points = 19
total = 22
print('所占百分比:{:.2%}'.format(points/total)) # 指定浮点型精度 所占百分比:86.36%

# 4.2.3 使用f-string格式化字符串
name,age,sex = '李四',18,'男'
print(f'姓名：{name}； 年龄：{age}； 性别：{sex}')

# 4.3 实训案例
# 1.进制转换
num = 10
print(f'{num}的二进制为:{bin(num)}') # 0b1010
print(f'{num}的八进制为:{oct(num)}') # 0o12
print(f'{num}的十六进制为:{hex(num)}') # 0xa

# 2 文本进度条
import time
total = 100
print('='*23,'开始下载','='*20)
for i in range(total+1):
    dian_pic = '.' * (total - i)
    xing_pic = '*' * i
    print('\r{:.0%}[{}{}]'.format(i / total, xing_pic, dian_pic),end='') #结尾不换号，是\r覆盖之前的输出内容
    #time.sleep(0.5)
print( ) # 换行
print('='*23,'下载完成','='*20)

# 4.4 字符串的常见操作
# 4.4.1 字符串的查找与替换
# 1.字符串查找 find()
str = 'Python'
result1= str.find('t')
print(result1) # 2
result1 = str.find('t',0,1)
print(result1) # -1

# 2.字符串替换 replace()
string = 'All things Are diffcult before they Are easy.'
result2 = string.replace('Are','are') # 不指定替换次数
print(result2) # All things are diffcult before they are easy.
string = ('He said,"you have to go forward ,Then ture left,'
          'Then go forward ,and Then turn right."')
result2 = string.replace('Then','then',2) # 指定替换次数
print(result2) # He said,"you have to go forward ,then ture left,then go forward ,and Then turn right."

# 4.4.2 字符串的分割与拼接
# 1.字符串分割 split()
str = 'The more efforts you male,the more fortune you get.'
print(str.split()) #['The', 'more', 'efforts', 'you', 'male,the', 'more', 'fortune', 'you', 'get.']
print(str.split('more')) #['The ', ' efforts you male,the ', ' fortune you get.']
print(str.split('e',2)) #['Th', ' mor', ' efforts you male,the more fortune you get.']

# 2.字符串拼接 join()
print('*'.join('Python')) # P*y*t*h*o*n
print('-'.join(['a','b','c'])) # a-b-c
print('|'.join({'k1':'v1','k2':'v2','k3':'v3'})) #  k1|k2|k3
print('|'.join({'k1':'v1','k2':'v2','k3':'v3'}.values())) #  v1|v2|v3