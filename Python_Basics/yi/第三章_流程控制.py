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
# bl_jsj = input('是否打开计算器(Y-打开，N-不打开):')
bl_jsj = 'n'
if 'y'.casefold() == bl_jsj.casefold() : #不区分大小写对比
    print("欢迎进入简易计算机，本程序仅提供加(+)减(-)乘(*)除(/)简单计算方式")
    num1 = float(input("请输入第一个数字:"))
    num2 = float(input("请输入第二个数字:"))
    result = 0
    is_reType = True
    while is_reType:
        type = input("请输入计算方式加(+)减(-)乘(*)除(/):")
        re_start = True
        if '+'.casefold() == type.casefold() :
            result = num1+num2
            print(f"您选择的加法计算，计算结果为{num1}+{num2}={result}")
            break
        elif '-'.casefold() == type.casefold() :
            result = num1-num2
            print(f"您选择的减法计算，计算结果为{num1}+{num2}={result}")
            break
        elif '*'.casefold() == type.casefold() :
            result = num1*num2
            print(f"您选择的乘法计算，计算结果为{num1}+{num2}={result}")
            break
        elif '/'.casefold() == type.casefold() :
            result = num1/num2
            print(f"您选择的除法计算，计算结果为{num1}+{num2}={result}")
            break
        else :
            print("选择的计算方式不在计算内！")
            reType = input("是否重新选择是(Y)，否(N)：")
            is_reType = 'y'.casefold() == reType.casefold()
            if is_reType == False : break
else: print("您选择不打开计算器，欢迎下次使用。")

# 2. 猜数字
# bl_csz = input('是否游玩猜数字游戏(Y-打开，N-不打开):')
bl_csz = 'n'
if 'y'.casefold() == bl_csz.casefold() : #不区分大小写对比
    num1 = int(input("请输入要猜测的数字:"))
    num2 = int(input("请输入猜测的数字:"))
    while True:
        if num1 != num2 :
            if num1 > num2 :
                print("猜小了！")
            elif num1 < num2 :
                print("猜大了！")
            num2 = input("请重新输入猜测的数字（非数字则退出）:")
            try:
                num2 = float(num2)
            except ValueError:
                print("欢迎下次游玩猜数字游戏")
        else:
            print("恭喜您，猜对了！")
            break
else: print("欢迎下次游玩猜数字游戏。")

# 3.3 循环语句
# 3.3.1 while语句
# 1~10之和
i = 1
result = 0
while i<=10 :
    result+=i
    i+=1
print(result)
#无限循环
# while True :
#     print('无限循环中.....')

# 3.3.2 for语句
# 循环字符串
for str in 'Python' :
    print(str)
# for语句与range()函数 组合使用
for i in range(5):
    print(i)

# 3.3.3 嵌套循环
# 1 while循环嵌套
# *组成的直角三角形
i=1
while i<=6:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print( ) # 用于换行
    i+=1

# 2 for循环嵌套
# 九九乘法表
for i in range(9):
    i+=1
    for j in range(i):
        j += 1
        print(f"{i}*{j}={i*j}",end='  ')
    print( )

# 3.4 训练案例
# 1 逢7拍手游戏
i=1
while i<=100:
    if i % 7 ==0:
        print(i)
    i+=1


# 3.5 跳转语句
# 3.5.1 break语句
for str in 'one':
    for s in 'Python' :
        if s == 't': break
        print(s)

# 3.5.2 continue 语句
for s in 'Python':
    if s == 't':
        print('?',end=' ') # 使用？代替
        continue
    print(s,end=' ')
print()
# 3.6 阶段训练-房贷计算器
# 仅计算等额本息方式,且仅计算商业贷款形式
# 年利息：year_interest 月利息：month_interest 贷款金额(万元):loan_amount  贷款期限(年):loan_term
# fd = input("是否打开房贷计算器(Y-打开，其他值不打开):")
fd = 'n'
if 'y'.casefold() == fd:
    loan_term = int(input("请输入贷款年限："))
    loan_amount = int(input("请输入贷款金额(万元)："))
    #year_interest = int(input("请输入利息(指年利息)："))
    if loan_term>5 : year_interest = 0.0475
    else : year_interest = 0.049
    month_interest = year_interest/12.0
    issue_num = loan_term*12
    print(f"月利息为：{month_interest}")
    print(f"期数：{issue_num}")
    month_money = (loan_amount*10000*month_interest*(1+month_interest)**issue_num)/((1+month_interest)**issue_num-1)
    sum_money = month_money*loan_term*12
    pay_interest = sum_money-loan_amount*10000
    print(f"月供为：{month_money}元")
    print(f"还款总额为：{sum_money}元")
    print(f"总利息为：{pay_interest}元")

