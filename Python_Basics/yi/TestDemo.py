
print("列表")
list = [5,1,2,4]
list.insert(0,3)
list[0]=(list[0]+1)
print(list)
print(sorted(list))

li_one = [2,1,5,6]
print(sorted(li_one[:2]))

print("元组")
suple1 = (1,2,3)
#suple1[0]=3 #元素不可变不支持修改
print(suple1)
suple2 = (x for x in range(5))

print('集合')
set1 = {1,2,3,1} #元素唯一 所以只有一个1
set1.add(4)
print(len(set1))
for x in set1:
    print(x)


print("字典")
dict1 = {"张三":{'性别':'男','年龄':18}}
print(dict1.get("a") == None)
print(dict1.pop('张三'))
dict2 = {"a":'1',"b":'2',"c":'3'}
#print(dict1[0]) # 报错 KeyError: 0
#print(dict2.get(0)) # 报错 None
dict2.update({"a":"a1"})
print(dict2)
dict3 = {}
print( 'c' in dict3)

print('其他')
while True:
    tag = True
    while tag :
        print("111")
        break # 结束本次循环，继续执行后续程序打印222
        #continue  # 跳出本次循环，不会继续执行后续程序打印222
    print("222")
    break