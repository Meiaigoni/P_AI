# 集合（Set）是无序的元素集

# 创建集合
a = {3, 4, 5}
# 显示a的类型
print(type(a))
print(a)

# 集合会自动筛去重复元素
b = {3, 3, 5, 5, 4, 7, 8}
print(b)

# 可以通过将列表或元组转变成集合，从而删去重复数字
list1 = [1, 3, 3, 5, 7, 6]
a_set = set(list1)
print(a_set)

# 需注意，集合中元素只能有数值、字符串、元组，不包括列表、字典、集合
# 并集Union()、求交集Intersection、求差集Difference、求对称差集Symmetric Difference
a_set = set([8, 9, 10, 11])
b_set = {1, 2, 3, 4, 8, 9, 10}
# 并集
print(a_set | b_set)
print(a_set.union(b_set))

# 交集
print(a_set & b_set)
print(a_set.intersection(b_set))

# 差集：只出现在a_set,不在 b_set
print(a_set - b_set)
print(a_set.difference(b_set))

# 求对称差集：两个集合中不会同时出现的元素
print(a_set ^ b_set)
print(a_set.symmetric_difference(b_set))