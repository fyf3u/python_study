#第三章 流程控制
# 3.1 条件语句
# 3.1.1 if语句
score = 88
if score>=60:print('考试及格！')
# 3.1.2 if else语句
score = 59
if score>=60:print('考试及格！')
else : print("考试不及格")
# 3.1.3 if-elif-else语句
scores = [30,68,89,97]
for score in scores:
    if score>=90:print('优秀！')
    elif (score>=70 and score<90): print('良')
    elif (score>=60 and score<70): print('中')
    else : print("！！！未来可期！！！")

# 3.1.4 if嵌套
year = 2100
month = 2
if month in [1,3,5,7,8,10,12]:
    print(f"{year}年{month}月有31天")
elif month in [4,6,9,11]:
    print(f"{year}年{month}月有30天")
elif month == 2:
    if (year % 400 ==0 or (year %4 == 0 and year % 100 !=0 )):
        print(f'{year}年{month}月有29天')
    else :
        print(f'{year}年{month}月有28天')
else :
    print(f'{month}d不是存在的月份')

# 3.2 训练案例
# 1. 加减乘除
bl_jsj = input('是否打开计算器(Y-打开，N-不打开):')
if( 'n'.__eq__):


# 2. 猜数字