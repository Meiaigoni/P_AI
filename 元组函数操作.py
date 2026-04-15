# 元组---不可变序列
# 不可进行添加、删除和修改等操作
# 访问和处理速度快
# 可作为字典的键


# 定义一个元组
tuple1 = (1, 2, 'a', 4, '5', 6)
print(tuple1)

t=tuple('helloworld')
print(t)
# 定义了一个元组之后就无法再添加或修改元组中的元素

print(tuple1[2])  # 'a' 元组的元素都有确定的顺序。元组的索引也是以0为基点的
print(tuple1[-1]) # '5' 负的索引从元组的尾部开始计数
print(tuple1[1:3]) # (2, 'a')  元组也可以进行切片操作。对元组切片可以得到（返回）新的元组，原元组不变

# 可以使用 in 运算符检查某元素是否存在于元组中。
print(1 in tuple1)
  # True

# 使用for in 进行遍历元组
for item in tuple1:
    print(item)


# 如果需要获取item的序号 可以使用下面的遍历方法：
for index in range(len(tuple1)):  # range(len(tuple1))就是生成一个自然排序列表
    print(index,tuple1[index])


# 还可以使用内置的enumerate函数
for index, item in enumerate(tuple1):
    # print('%i, %s' % (index, item))
    print(index,'---->',item)
# 元组中若只有一个元素，逗号不能省略
tuple1=(10)
print(tuple1,type(tuple1))

tuple1=(10,)
print(tuple1,type(tuple1))