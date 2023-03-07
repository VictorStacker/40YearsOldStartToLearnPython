# 查看类型type()
# 1、数值类型  整数类型int和浮点数类型float
num1 = 10
print(type(num1))
num2 = 10.5
print(type(num2))

# 布尔值bool  判断 True  False

# 字符串类型 str
var1 = '大家好'
var2 = "你好呀"

print(type(var1))
print(type(var2))

# 列表类型list
list1 = [var1, var2, 1, 2, 3, '小小', '大大']
print(list1)
print(type(list1))

# 元组类型tuple
tu1 = (var1, var2)
print(tu1)
print(type(tu1))

# 集合类型set
# 无序  不重复
set1 = {"张三", "李四", "坤哥", "篮球", "你干嘛", "坤哥"}
print(set1)
print(type(set1))

# 字典类型dict 键值对
# {"name": "张三"}  name是健  张三是值 key:value
dict1 = {"name": "张三", "age": 18, "sex": "男"}
print(dict1)
print(type(dict1))
