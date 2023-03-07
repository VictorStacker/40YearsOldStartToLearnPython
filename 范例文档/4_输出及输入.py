age = 18
name = '小明'
weight = 105.5
student_id = 1
hight = 182

print('我的名字是%s' % name)
# 我的名字是小明

print('我的学号是%04d' % student_id)
# 我的学号是0001

print('我的体重是%.2f⽄' % weight)
# 我的体重是105.50⽄

print('我的名字是%s，今年%d岁了，体重是%.2f斤，身高是%d' % (name, age, weight, hight))
# 我的名字是小明，今年18岁了，体重是105.50斤，身高是182

print('我的名字是%s，明年%d岁了' % (name, age + 1))
# 我的名字是小明，明年19岁了

name = "小明"
age = 18
love = "打游戏"

# 1、不带编号
print("大家好,我是{},今年{}岁,喜欢{}".format(name, age, love))

# 2、带数字编号
print("大家好,我是{2},今年{0}岁,喜欢{1}".format(age, love, name))

# 3、附带关键字
print("大家好,我是{name},今年{age}岁,喜欢{love}".format(age=age, name=name, love=love))

name = "小明"
age = 18
love = "打游戏"
print(f"大家好,我是{name},今年{age}岁,喜欢{love}")

# 输入
password = input('请输⼊您的密码：')
print(f'您输⼊的密码是{password}')

print(type(password))
# <class 'str'>

name = input("请输入用户名：")
password = input("请输入密码：")

print("您的用户名是：%s" % name)
print("您的密码是：%s" % password)
