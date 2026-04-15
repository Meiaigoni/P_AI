# 定义一个字典
dict1 = {'name': 'yeoman', 'age': 24, 'sex': 'Male'}
print(dict1)

# 修改字典元素的值
dict1['name'] = 'yuanm'  # 为一个已经存在的 dictionary key 赋值，将简单覆盖原有的值。
print(dict1)

# 增加字典键并赋值
# update（）：将两个字典链接
dict1['Age'] = 25  # 在 Python 中是区分大小写的  age和Age是完全不同的两个key
print(dict1)

dict2={'email': '666666@qq.com'}
dict1.update(dict2)
print(dict1)

# 显示字典内容
# items（）:显示键值对，并封装在元组内
# keys()：显示键
# values（）：显示值
print(dict1)
print(dict1.items())
print(dict1.keys())
print(dict1.values())

# 查找键对应的值
# get():提取给定键对应的值，如果键不在字典中，就返回默认值。如果不显示默认值，就返回None。
print(dict1['age'])
print(dict1.get('Age'))
print(dict1.get('Zhang', '此人不存于世界'))

#
# 从字典中删除元素
# del 允许您使用 key 从一个 dictionary 中删除独立的元素
# pop():弹出特定键对应的元素并删除该键值对
# dict1.clear()  # clear 从一个 dictionary 中清除所有元素

del dict1['sex']
print(dict1)

dict1.pop('email')
print(dict1)

# popitem():根据先进先出原则，将字典最末尾的键值对弹出
person = {'name': 'Alice', 'age': '24', 'sex': 'Female'}
pop_obj = person.popitem()
print(pop_obj)
print(person)
