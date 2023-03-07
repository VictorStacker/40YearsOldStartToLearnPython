# a = 123
# b = 'Hello World'
# print(a)
# print(b)
# # 变量&变量名
# # 变量为数据，变量为查找变量的名称
# # 变量为可变的
#
# a = 456
# print(a)
#
# # 查看内存地址 id() 括号中放变量名 ，每次执行都会变化，因为所有数据均为'临时存储'
# print(id(a))
#
# name1 = '大大'
# name2 = '大大'
# name3 = '大大'
# print(id(name1))
# print(id(name2))
# print(id(name3))
#
# # 如果变量名相同，则后面的变量会覆盖前者,存储位置也不同
# name4 = '中中'
# print(name4)
# name4 = '小小'
# print(name4)

# 多变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

print(id(a))
print(id(b))
print(id(c))