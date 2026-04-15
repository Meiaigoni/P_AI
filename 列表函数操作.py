# 列表----可变序列
# 可进行添加、删除和修改等操作
# 访问和处理速度慢
# 不可作为字典的键

# 列表操作
users = ['xujingliang', 'sunyanan', 'wuyou']

# append() 列表最后边添加元素
users.append("wutong")
print(users)

# insert() 在列表的指定位置添加元素
users.insert(1, "wutong")
users.insert(2, "wutong")
users.insert(3, "wutong")
print(users)

# pop() 删除末尾元素和指定索引位置的元素
users.pop()  # 删除末尾的元素
users.pop(0)  # 删除索引0处的元素

# count()  返回某个元素在列表里的数量
print(users.count("wutong"))

# extend()  合并两个列表
users.extend(["sunyanan", "sunyanan", "sunyanan"])
print(users)

# index() 返回元素在列表中首次出现位置的索引
index = users.index("sunyanan")
print(str(index))

# remove() 删除指定元素
users.remove("xujingliang")
print(users)

# sort()  对列表进行排序
# sorted() 对内置列表进行排序
# reverse()  反转列表顺序
# clear()  清除列表元素
# copy()  复制列表

# 一维列表生成式
# lst=[expression for item in range]
# lst=[expression for item in range if condition]
import random
lst=[item for item in range(1,11)]
print(lst)
lst=[item*item for item in range(1,11)]
print(lst)
lst=[random.randint(1,100) for _ in range(10)]
print(lst)

# 选择符合条件的元素创建列表
lst=[item for item in range(10) if item%2==0]
print(lst)

# 二维列表
# 创建
lst=[
    ['city','环比','同比'],
    ['bj','102','202'],
    ['sz','100','200']
]

# 遍历二维列表
for row in lst:
    for item in row:
        print(item,end='\t')
    print()

# 列表生成式生成四行五列的二维列表
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)
