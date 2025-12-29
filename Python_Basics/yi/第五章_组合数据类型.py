# 第五章 组合数据类型
# 5.1 认识组合数据类型
# 1.序列类型
# 序列类型来源于数学概念中的数列。数列是按一定顺序排成一列的一组数，每个数称为这个数列的项，每项不是在其他项之前，就是在其他项之后。
# 序列类型在数列的基础上进行了扩展，Python中的序列支持双向索引:正向递增索引和反向递减索引。
# 正向递增索引：从0开始，由左向右依次递增，如 0、1、2、..、n。
# 反向递减索引：从-1开始，由右向左依次递减，如-n、...、-2、-1。
# Python中常用的序列类型主要包括3种:字符串(str)、列表(list)和元组(tuple)。第四章已经介绍字符串，下面5.2和5.3分别介绍列表和元组。
#
# 2.集合类型
# Python中集合的概念与数学中集合的概念一致，其具备三个特征：
# 确定性：元素是确定的。
# 互异性：元素互不相同。
# 无序性：元素没有顺序，若多个集合中的元素仅顺序不同，那么这些集合本质上是同一集合。
# Python要求放入集合中的元素必须是不可变类型(Python中整形、浮点型、字符串类型和元组属于不可变类型；列表、字典和集合本身属于可变的数据类型)。在本章5.5节介绍集合。
# 3.映射类型
# 映射类型以键值对的形式存储元素，键值对中的键与值之间存在映射关系。
# 字典(dict)是Python中唯一的内置映射类型，字典的键必须遵循以下两个原则:
# 1). 每个键只能对应一个值，不允许同一个键在字典中重复出现；即key不重复，仅有唯一value。
# 2). 字典中的键是不可变类型。
# 将在本章5.6节介绍字典
#
# 5.2 列表
# 5.2.1 创建列表
# 1.使中括号[]创建
list1 = ['abc',10,11.26] # 字符串、整型、浮点型
list2 = [list1,(1,'我是元组'),{'集合'},{'key1':'字典'}] # 列表、元组、集合、字典

# 2.使用list()函数创建
# li1 = list(1) # 因为整型不是可迭代的类型所以创建失败，报错TypeError: 'int' object is not iterable
li2 = list(range(5)) # [0, 1, 2, 3, 4]
li3 = list('python') # ['p', 'y', 't', 'h', 'o', 'n']
li4 = list([10,'python']) # [10, 'python']

# 3扩展:可迭代类型
from collections.abc import Iterable
ls = [1,2,3]
print(isinstance(ls,Iterable)) # True

# 5.2.2 访问列表元素
# 1. 索引方式访问
ls1 = ['Java','C++','JS','PHT','Python'] # 定义列表
print(ls1[len(ls1)-1]) # 正向索引访问
print(ls1[-1]) # 反向索引访问

# 2.切片方式访问
# 切片的语法结构
# list[m:n:step] 表示按步长step获取列表中索引m~n对应的元素(不包含list[n]),step默认为1； m和n都可以省略，若m省略，表示从首开始，若n省略，表示到尾结束。
ls2 = ['P','y','t','h','o','n']
print(ls2[1:4:2]) # 按步长4获取索引1~4['y','t','h']对应的元素， ['y', 'h']
print(ls2[2:]) # 获取索引2~末尾的元素 ['t', 'h', 'o', 'n']
print(ls2[:3]) # 获取索引起始~3的元素 ['P', 'y', 't']
print(ls2[:]) # 获取所有元素

# 3. 循环中依次访问
li = ['P','y','t','h','o','n']
for i in li:
    print(i ,end=' ')  # 最终结果 P y t h o n

print()
# 4.扩展： 判断元素是否包含在列表内
li = ['P','y','t','h','o','n']
print( 'o' in li) # True
print('1' not in li) # True

# 5.2.3 添加列表元素
# 1. append()方法，用于在列表末尾添加新的元素
ls1 = ['a','b','c','d','e']
ls1.append(1)
print(ls1) # ['a', 'b', 'c', 'd', 'e', 1]
# 2.extend()方法，用于在列表末尾一次性添加另外一个列表所有元素
ls2 = ['a','b','c','d','e']
ls2.extend([1,2,3]) # ['a', 'b', 'c', 'd', 'e', 1, 2, 3]
print(ls2)
# 3.instert()方法，按照索引在指定位置插入新元素
ls3 = ['a','b','c','d','e']
ls3.insert(int(len(ls3)/2),[12,3,4,])
print(ls3) # ['a', 'b', [12, 3, 4], 'c', 'd', 'e']

# 5.2.4 元素排序
# 1. sort()方法， 按照特定顺序排序
ls_one = [4,2,9,7,3]
ls_one1 = [4,2,9,7,3]
ls_two = ['Java','PHT','Python']
ls_one.sort()
ls_one1.sort(reverse=True)
ls_two.sort(key=len)
print(ls_one) # 升序 [2, 3, 4, 7, 9]
print(ls_one1) # 降序 [9, 7, 4, 3, 2]
print(ls_two) # 计算字符串长度，reverse默认False升序 ['PHT', 'Java', 'Python']

# 2. sorted()方法， 按照升序排列，返回升序排序后的新列表，不会对原来列表产生影响
lt_one = [4,2,8,6,1,9]
ls = sorted(lt_one)
print(ls) # [1, 2, 4, 6, 8, 9]
# 3 . reverse()方法，逆置元素，把元素从右向左依次排序存放，会覆盖原列表
list = ['a','b','c','d']
list.reverse()
print(list) # ['d', 'c', 'b', 'a']


# 5.2.5 删除列表元素
# 1. del()语句，删除指定下标的元素
ls1 = ['p','y','t','h','o','n']
del ls1[0]
print(ls1) # ['y', 't', 'h', 'o', 'n']

# 2.remove()语句，移除指定的元素， 若有多个则只移除匹配的第一个元素
ls2 = ['p','y','t','h','o','n']
#ls2.remove('a') #不在会报错 ValueError: list.remove(x): x not in list
if 'y' in ls2:
    ls2.remove('y')
print(ls2) # ['p', 't', 'h', 'o', 'n']

# 3.pop()语句，移除列表某个指定下标的元素，若未指定则移除最后一个元素
ls3 = ['p','y','t','h','o','n']
l = ls3.pop()
print(l) #  n
# ls3.pop(len(ls3)) # 下标越界 IndexError: pop index out of range
ls3.pop(2)
print(ls3) # ['p', 'y', 'h', 'o']

# 4.clear()方法，清空整个列表
ls4 = [1,3,5,75,510]
print(ls4) # [1, 3, 5, 75, 510]
ls4.clear()
print(ls4) # [] /被清空


# 5.2.6 列表推导式
ls = [2,4,5,3]
ls = [x*x for x in ls]
print(ls) # [4, 16, 25, 9]
# 1.带有if语句的列表推导式
ls = [2,4,5,3,9,7,8,8]
ls1 = [x for x in ls if x>5] # 表示列表ls中大于5的值保存到新列表ls1中
print(ls1) # [9, 7, 8, 8]

# 2.嵌套for循环语句的列表推导式
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [x*y for x in ls1 for y in ls2] # 循环分别将ls1与ls2中元素的乘积保存到新列表中
print(ls3) # [4, 5, 6, 8, 10, 12, 12, 15, 18]

# 3.带有if语句和for循环的列表推导式
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [x*y for x in ls1 for y in ls2 if x*y>=10] #
print(ls3) # [10, 12, 12, 15, 18]

ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [x*y for x in ls1  if x>2
           for y in ls2  if y>2
                         if x*y>=10] #
print(ls3) # [12, 15, 18]

# 5.3 元组
t = () # 空元组
tuple1 = (1,) # 单元素元组
tuple2 = (1,2,3) # 多元素元组
tuple3 = (1,2,3,(4,5,6)) # 嵌套元组
print(t) # ()
print(tuple1) # (1,)
print(tuple2) # (1, 2, 3)
print(tuple3) # (1, 2, 3, (4, 5, 6))

t = tuple() # 空元组
tuple1 = tuple([1]) # 单元素元组
tuple2 = tuple(range(5)) # 多元素元组
tuple3 = tuple("python")  #
print(t) # ()
print(tuple1) # (1,)
print(tuple2) # (0, 1, 2, 3, 4)
print(tuple3) # ('p', 'y', 't', 'h', 'o', 'n')

t5 = (x for x in range(5)) # ‌此为生成器表达式 使用圆括号 ()，‌惰性计算逐个生成元素‌，内存占用极低 所以t5中报存的为内存地址而非值
print(t5) # <generator object <genexpr> at 0x000001FF2C97B280>

gen = (x for x in range(3))
for item in gen:
    print(item)  # 输出: 0, 1, 2


# 5.4 实训案例
# 1. 在多名学生中，选出10为成绩最好的学生，其中分别由10为评委打分，为公平去掉最高和最低成绩，计算平均得分
import random # 引入随机数
student =30
pj = []
for s in range(student):
    scores_ls = [] #创建列表
    for p in range(10): # 依次输入每位评委评价的成绩
        # scores = int(input(f'请输入第{(p+1)}位评委，为第{(s+1)}位学生的得分：'))

        scores = random.randint(20,100) #20~100随机取整数，包含20和100 用来模拟打分
        scores_ls.append(scores) # 保存进列表
    scores_ls.sort() # 升序排序
    print(f'第{(s+1)}位学生成绩评分按升序为：{scores_ls}')
    nscores_ls = scores_ls[1:len(scores_ls)-1]
    print(f'第{(s+1)}位学生成绩按照切片方式去掉最低和最低成绩之后：{nscores_ls}')
    sum_scores = 0
    for sc in nscores_ls :
        sum_scores += sc
    pj_sc = sum_scores/10
    print(f'第{(s+1)}位学生总得分为：{sum_scores}，平均的分为:{pj_sc}')
    pj.append(pj_sc) # 保存平局得分
pj.sort(reverse=True) # 升序
print(f'所有平均得分降序排列后为:{pj}')
ten_pj = pj[0:10]
print(f'最终获得之后的成绩为：{ten_pj}')

# 5.5 集合
# Python的集合（set）本身是可变类型，但Python要求放入集合中的元素必须是不可变类型；集合类型与列表和元组的区别是：集合中的元素无序但必须唯一。
# 1.创建集合
# dic1 = {} # 此为空字典。
set1 = {1} # 单元素集合
# set2 = {1,[1,2]}#不能存放可变类型，列表[]为可变类型 执行时报错: TypeError: unhashable type: 'list'
set3 = {1,'a',3.14,(2,1)}#多元素集合 不可变类型 整型、浮点型、字符串和元组
print(set3) # 输出的结果无序每次都不一样 {1, 3.14, 'a', (2, 1)}
set4 = set() # 空集合
set5 = set('python') # 传入字符串
print(set5) # 输出的结果无序每次不一样 {'t', 'n', 'p', 'h', 'o', 'y'}
set6 = set((1,2,3,'a','b','b','b','c','d','e','e')) # 传入元组
print(set6) # 元素无序但唯一 {1, 2, 3, 'b', 'd', 'a', 'e', 'c'}
set7 = set(range(10)) # 传入整数
print(set7) # 输出有序是因为 range(10)生成的有序序列  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 2.集合的常见操作
s1 = {1}
s1.add((4,5))
print(s1) # {1, (4, 5)}
s2 = {1,'a',2,'b'}
#s2.remove(3) # remove删除不存在会报错 报错  KeyError: 3
s2.discard(3) # discard删除不存在不会报错
s2.discard(1)
print(s2) # {'b', 2, 'a'}
s3 =  {1,'a',2,'b'}
y = s3.pop() # 随机移除一个元素，并返回
print(s3) # {1, 2, 'b'}
print(y) #a
s4 =  {1,'a',2,'b'}
s4.clear() # 清空集合，变为空集合
print(s4) # set()
s5 = s3.copy() # 复制集合s3的元素到s5
print(s5) # {1, 2, 'b'}
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2)) #True  判断无交集 没有相同的元素则为True
# 3.集合推导式
ls1 = [x for x in range(11)]
set1 = {x for x in ls1 if x%2==0} # 获取列表ls1中的偶数保存到集合中
print(set1) # {0, 2, 4, 6, 8, 10}

# 5.6 字典
# 5.6.1 创建字典
dict1 = {}
#dict2 = {['list']:'a'} # 执行报错 unhashable type: 'list'
#dict2 = {{'key':'value'}:'ddd'} # 执行报错 unhashable type: 'dict'
#dict3 = {{123}:"abc"} # 报错 TypeError: unhashable type: 'set'
dict2 = {"name":"张三",123:456,('a','b'):"abc"}
dict4 = dict() # 空字典
dict5 = dict({'key1':'value1'}) # 使用内置函数创建
print(dict2)

# 5.6.2 字典的访问
# 1. 直接使用键访问 dict[key]
d1 = {'age':18}
print(d1['age']) # 18
# print(d1['name']) # 报错 KeyError: 'name'

# 2.使用内置方法get()  dict.get(key)
# 若指定键key不存在则返会默认值(default)，格式为 dict.get(key,默认value)
d2 = {'name':'南一','age':18}
print(d2.get('name')) # 南一
print(d2.get('sex')) # 若key不存在且不指定默认值，则返会None
print(d2.get('address','地球人')) # 地球人

# 3.访问所有键、值和元素内置方法 dict.keys()、dict.values()、dict.items()
d2 = {'name':'南一','age':18,'email':'namyi@py.com'}
print(d2.keys()) # dict_keys(['name', 'age', 'email'])
print(d2.values()) # dict_values(['南一', 18, 'namyi@py.com'])
print(d2.items()) # dict_items([('name', '南一'), ('age', 18), ('email', 'namyi@py.com')])
for key in d2.keys():
    print(key,end=" ") # name age email
print()
for value in d2.values():
    print(value,end=" ") # 南一 18 namyi@py.com
print()
for item in d2.items():
    print(item,end=" ") # ('name', '南一') ('age', 18) ('email', 'namyi@py.com')
print()

# 5.6.3 字典元素的添加和修改
# 1. 字典元素的添加   赋值 或 update()
insert_dict = {}
print(insert_dict) # {}
insert_dict.update(md = 'abctest')
insert_dict['key1'] = 'value1'
print(insert_dict) # {'md': 'abctest', 'key1': 'value1'}

# 2.字典元素的修改  update()
dict_sut = {'stu1':'张三','stu2':'李四','st3':'王五'}
dict_sut['stu1'] = '小明'
print(dict_sut.get('stu1')) # 小明
dict_sut.update(stu2 = '小李')
print(dict_sut.get('stu2')) # 小李

# 5.6.4 字典元素的删除
print("5.6.4 字典元素的删除")
# 1.使用pop()方法删除
# 根据指定的键key删除元素，若成功，则返会删除的元素
# 2.使用popitem()方法删除
# 删除字典中的最后一个元素，若成功，则返会被删除的元素
# 3.使用clear()方法 清空字典
dict_sut = {'stu1':'张三','stu2':'李四','st3':'王五','st4':'马六','st5':'钱七'}
print(dict_sut.pop('stu1')) # 张三
print(dict_sut) # {'stu2': '李四', 'st3': '王五', 'st4': '马六', 'st5': '钱七'}
print(dict_sut.popitem()) # ('st5', '钱七')
print(dict_sut) # {'stu2': '李四', 'st3': '王五', 'st4': '马六'}
dict_sut.clear()
print(dict_sut) # {}
# 5.6.5 字典推导式
# 利用字典推导式，快速反转key-value的对应关系
ex_dict = {'key1':'value1','key2':'value2','key3':'value3'}
re_dict = { value:key for key,value in  ex_dict.items()}
print(re_dict) # {'value1': 'key1', 'value2': 'key2', 'value3': 'key3'}

# 5.7 实训案例
# 1. 登记学生成绩(student-score)，成绩越高的排位越靠前
print('1. 登记学生成绩(student-score)，成绩越高的排位越靠前,执行结果')
student_score = {'001':80,'002':170,'003':190,'004':200,'005':300}
print(f"排序后的成绩为:{student_score}")
ss = [] # 排序后放到新列表中
for key,value in student_score.items() : #遍历学生和成绩
    #print(f"{key}:{value}")
    new_dic = {key:value}
    if len(ss) == 0: # 列表没有元素直接添加
        ss.insert(0,new_dic)
    else:
        i = 0
        for x in ss: #遍历列表
            i += 1
            tag = False
            for skey,svalue in x.items() : #处理每人的成绩
                if (value > svalue) : #成绩对比，每次处理完成则结束
                    ss.insert(i-1, new_dic)
                    tag = True
                    break
                elif value == svalue :
                    ss.insert(i, new_dic)
                    tag = True
                    break
                else:  #value <= svalue
                    if i== len(ss):
                        ss.append( new_dic) #最后一位追加
                        tag = True
                        break
                    continue # 列表人都，有不符合的则跳出进行下一个对比
            if tag : break #确定位置加进去之后，列表循环也结束
print(f"排序后的成绩为:{ss}")

# 2. 实现手机通讯录功能，可以添加、查看、删除、修改和查找指定联系人
contact_list = {}  # 空字典等待存放联系人
restart_tag = True
while restart_tag:
    # contact_list_type = input("请选择通讯录功能:\n1-添加联系人\n2-查看联系人列表\n3-删除联系人\n4-修改联系人\n5-查找指定联系人\nq-退出")
    contact_list_type ='q'
    if contact_list_type.upper() == 'Q':
        print("退出通讯录，欢迎下次使用！")
        restart_tag = False
        continue
    try:
        contact_list_type = int(contact_list_type)
    except BaseException as e:
        restart = input("输入不符合标准是否重新选择：Y-是，其他键-否：")
        if restart.upper() != 'Y':
            print("结束手机通讯录功能！")
            restart_tag = False
    else:
        if contact_list_type<=0 or contact_list_type >=6 :
            print("输入项不在功能范围内！")
        else :

            if contact_list_type == 1 :
                print("---------->1-请添加联系人")
                name = input("请输入联系人姓名:")
                phone_num = input("请输入联系人手机号:")
                address = input("请输入联系人地址:")
                if contact_list.get(name) == None :
                    contact_list[name] = {"phone_num":phone_num,"address":address}
                else :
                    print(f"{name}已经存在，信息如下:\n{contact_list.get(name)}")
            elif contact_list_type == 2 :
                print("---------->2-查看联系人列表")
                print("联系人清单如下:")
                for key in contact_list.keys():
                    print(key)
                print("联系人打印结束")
                input("输入任意键继续！")
            elif contact_list_type == 3 :
                print("---------->3-删除联系人")
                print("联系人清单如下:")
                for key in contact_list.keys():
                    print(key)
                del_tag = True
                while del_tag:
                    del_name = input("请选择要删除的联系人姓名:")
                    if contact_list.get(del_name) == None:
                        yn = input(f"要删除的人{del_name}不存在，是否重新选择：Y-是，其他键-否：")
                        if yn.upper() != 'Y' :
                            print("结束删除联系人功能！")
                            del_tag = False
                    else:
                        del_info = contact_list.pop(del_name)
                        print(f"联系人{del_name}删除成功.信息如下：")
                        print(f'姓名：{del_name}')
                        for key,value in del_info.items():
                            print(f'{key}:{value}')
                        re_del = input(f"联系人{del_name}删除成功，是否继续删除：Y-是，其他键-否：")
                        if re_del.upper() != 'Y' :
                            del_tag = False
            elif contact_list_type == 4 :
                print("---------->4-修改联系人")
                print("联系人清单如下:")
                for key in contact_list.keys():
                    print(key)
                modify_tag = True
                while modify_tag:
                    modify_name = input("请选择要修改的联系人姓名:")
                    if contact_list.get(modify_name) == None:
                        yn = input(f"要修改的人{modify_name}不存在，是否重新选择：Y-是，其他键-否：")
                        if yn.upper() != 'Y':
                            print("结束修改联系人功能！")
                            modify_tag = False
                    else:
                        #del_info = contact_list.pop(modify_name)
                        #name = input("请输入联系人姓名:")
                        phone_num = input("请输入联系人手机号:")
                        address = input("请输入联系人地址:")
                        contact_list.update(modify_name={"phone_num": phone_num, "address": address})
                        print(f"联系人{modify_name}修改成功.信息如下：")
                        print(f'姓名：{contact_list.get('modify_name')}')
                        modify_del = input(f"联系人{modify_name}修改成功，是否继续删除：Y-是，其他键-否：")
                        if modify_del.upper() != 'Y':
                            modify_tag = False

            elif contact_list_type == 5 :
                print("---------->5-查找指定联系人")
                find_tag = True
                while find_tag:
                    find_name = input("请选择要查找的联系人姓名:")
                    if contact_list.get(find_name) == None:
                        yn = input(f"要查找的人{find_name}不存在，是否重新选择：Y-是，其他键-否：")
                        if yn.upper() != 'Y':
                            print("结束查找联系人功能！")
                            find_tag = False
                    else:
                        print(f"联系人{find_name}查找成功.信息如下：")
                        print(f'姓名：{contact_list.get(find_name)}')
                        find = input(f"联系人{find_name}查找成功，是否继续查询：Y-是，其他键-否：")
                        if find.upper() != 'Y':
                            find_tag = False


# 5.8 组合数据类型应用运算符
# 1. “+”运算符
# Python中的字符串、列表和元组支持“+”运算符。不过不进行数值的累加，而是拼接。
# 示例代码如下:
print('abc'+'123') # abc123
print(['a','b','c']+['c','d','e']) # ['a', 'b', 'c', 'c', 'd', 'e']
print(('3','4','c')+('c','1','2')) # ('3', '4', 'c', 'c', '1', '2')

# 2. “*”运算符
# Python中的字符串、列表和元组支持“+”运算符与整数进行乘法运算，不过结果为原数据的倍数拼接。
# 示例代码如下:
print('abc'*3) # abcabcabc
print(['a','b','c']*3) # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(('3','4','c')*3) # ('3', '4', 'c', '3', '4', 'c', '3', '4', 'c')

# 3. “in”与“not in”运算符
# Python中“in”和“not in”运算符被称为成员运算符。用于判断某个元素是否属于某个变量。
# Python中的字符串、列表、元组、集合、字典都支持成员运算符。
# 示例代码如下:
print('a' in 'Python') # False
print('a' in ['a','b','c']) # True
print('a' in ('a','b','c')) # True
print('a' in {'a','b','c'}) # True
print('a' in {'key':'value'}) # False
print('a' in {'a':'b'}) # True
print('a' in {'b':'a'}.keys()) # False
print('a' in {'b':'a'}.values()) # True
print({'b':'a'} in {'b':'a','key':'value'}.items()) # False

# 5.9 本章小结
# 不变类型：整型类型、浮点型类型、字符串和元组
# 可变类型：列表、集合和字典
# 组合类型：列表、元组、集合、字典
# 组合数据类型的异同

# 5.10 习题
# 1.列表li1=[4,5,2,7]和li2=[3,6]，将两个列表合成一个并排序输出
li1=[4,5,2,7]
li2=[3,6]
li1.extend(li2)
li1.sort(reverse=True)
print(li1)

# 2.元组suple1=(‘p’,‘y’,‘t’,[‘o’,‘n’])，请向元组的最后一个列表中添加新元素‘h’
su1=('p','y','t',['o','n'])
li = su1[(len(su1)-1)]
li.insert(0,'h')
print(li)

# 3.字符串str=’skdaskerkjsalkj’，请统计该字符串中各个字母的个数
str1='skdaskerkjsalkj'
str_list = [x for x in str1] #转为列表
str_set = {x for x in str_list} #将列表转为集合，利用元素唯一去重
print(str_set)
print(str_list)
dic = {}
for s in str_set: #遍历集合元素 在 列表中寻找相同个数的元素
    #tag = s in dic # 判断元素是否存在
    count = 0 #初始个数 此处为0是因为会从字符串中依次寻找并计数
    for x in str_list:
        if x == s :
            count += 1
            dic.update({s:count})
print(dic) #{'s': 3, 'k': 4, 'd': 1, 'a': 2, 'e': 1, 'r': 1, 'j': 2, 'l': 1}
print(f"字符串长度:{len(str1)}")
sum=0
for x in dic.values():
    sum+=x
print(f"字典value之和:{sum}")

# 4.列表ls1=[1,2,1,2,3,5,4,3,5,7,4,7,8],删除重复数据
ls1=[1,2,1,2,3,5,4,3,5,7,4,7,8]
set_ls = { x for x in ls1 } #利用集合的唯一性
print(set_ls)