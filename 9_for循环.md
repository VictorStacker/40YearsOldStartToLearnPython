### for 循环

`for`循环可以遍历任何序列的项目，如一个列表或者一个字符串等

**Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。**

for-in遍历的对象必须是**可迭代**对象

while循环的循环条件是自定义的，for循环无法定义循环条件

for循环是一种**“轮询”**机制。是对一批内容进行**“逐个处理”**

### for 循环代码格式

```python
for 临时变量 in 列表或者字符串等可迭代对象:
    循环满足条件时执行的代码
```



### for 循环代码示例

如果想要循环输出0、1、2、3、4，使用`for`循环来实现的代码如下：

```python
for i in range(5):
    print(i)
```

运行结果：

```text
0
1
2
3
4
```



### range()函数

> for循环本质上是遍历**“序列类型”**，但是，使用**range**涵数，可以获得一个简单的**数字序列**



- `range(x)`

  当range中只有1个数字时，for循环取到的数据是0....x-1

  例如：

  ```python
  for i in range(5):
      print(i)
  ```

  能输出：

  ```text
  0
  1
  2
  3
  4
  ```

  但不能输出5

  

- `range(x, y)`

  当range中有2个数字时，此时for循环取到的数据是x....y-1

  例如：

  ```python
  for i in range(3, 5):
      print(i)
  ```

  能输出：

  ```text
  3
  4
  ```

  

- `range(x, y, z)`

  当range中有3个数字时，此时for循环能取到的数据是从x...y-1但是每次间隔的数据是z

  **示例一：**

  ```python
  for i in range(1, 5, 1):
      print(i)
  ```

  运行结果：

  ```text
  1
  2
  3
  4
  ```

  **示例二：**

  ```python
  for i in range(1, 5, 2):
      print(i)
  ```

  运行结果：

  ```text
  1
  3
  ```

  **示例三：**

  ```python
  for i in range(5, 1, -1):
      print(i)
  ```

  运行结果：

  ```text
  5
  4
  3
  2
  ```



### for 循环案例

```python
sum_ret = 0  # 用来存储总和
for i in range(1, 101):
    sum_ret += i

print("1~100的和为:%d" % sum_ret)
```

运行结果如下：

```python
1~100的和为:5050
```



### break 与 continue

在循环的过程中，有时可能会因为某些条件的满足或者不满足需要结束整个`while`，还有可能在当次循环代码执行过程中剩下的不执行了而是进行一次的循环，这种时候就需要用2个功能

- 结束整个循环
- 结束本次循环

还好，`Python`的发明人，针对上述2个功能，发明除了对应的代码

- `break`，用来结束整个循环
- `continue`，用来结束本次循环



##### break 基本使用

`break`的作用是：结束它所属的整个循环

注意点：它不能单独使用，如果用的话一定需要放到循环中



**while 中使用 break**

- 未使用 break 的效果

  ```python
  i = 0
  
  while i<5:
      print('----')
      print(i)
      i = i + 1
  ```

  运行结果：

  ```text
  ----
  0
  ----
  1
  ----
  2
  ----
  3
  ----
  4
  ```

  

- 使用 break 的效果

  ```python
  i = 0
  
  while i<5:
      print('----')
      i = i+1
      break
      print(i)
  ```

  运行结果：

  ```text
  ----
  ```

  说明：

  - 当程序执行到第6行时，遇到了`break`，那么此时`break`就会将它所在的`while`循环结束，所以只输出了一次`----`



**for 循环中使用 break**

- 未使用 break 的效果

  ```python
  web_site = 'www.tulingxueyuan.com'
  
  for x in web_site:
      print(x)
  ```

  运行结果：

  ```text
  w
  w
  w
  .
  t
  u
  l
  i
  n
  g
  x
  u
  e
  y
  u
  a
  n
  .
  c
  o
  m
  ```

  

- 使用 break 的效果

  ```python
  web_site = 'www.tulingxueyuan.com'
  
  for x in web_site:
      print(x)
      break
  ```

  运行结果：

  ```text
  w
  ```

  说明：

  - 当程序执行到第5行`break`时，`break`会让整个`for`循环结束，所以只输出了第一个字母`w`



##### continue 的基本使用

**while 中使用 continue**

- 使用 continue 的效果

  ```python
  i = 0
  while i < 3:
      i = i+1
      print('----')
      continue
      print(i)
  ```

  运行结果：

  ```text
  ----
  ----
  ----
  ```

  小提示：代码执行过程通过Debug调试模式进行探究。



**for 中使用continue**

- 带有 continue 的循环示例如下：

  ```python
  web_site = 'www.tulingxueyuan.com'
  
  for x in web_site:
      print(x)
      continue
      print("----")
      
  ```

  运行结果：

  ```text
  w
  w
  w
  .
  t
  u
  l
  i
  n
  g
  x
  u
  e
  y
  u
  a
  n
  .
  c
  o
  m
  ```

  说明：

  - 当程序遇到`continue`时，会导致本次`for`循环体中剩下的代码不会执行，而是进入下一次的循环



##### 常见的用法

通过上面的案例，我们知道break、continue是可以直接放到循环中使用的

但是，在循环中直接运行break、continue有意义吗？其实你也会感觉到有些不舒服，我们一般的用法是在判断语句中使用break、continue

示例如下：

```python
i = 3
while i > 0:
    password = input("请输入密码：（还剩%d次机会）" % i)
    if password == "123456":
        print("密码输入正确")
        break
    i -= 1
```

说明：

- 如果密码输入正确，那么就不需要再次让用户输入密码，直接结束这个循环即可
- 一般情况下break、continue会在判断中使用，这样就能够实现该怎样循环的就怎样循环，不该循环的时候能立刻结束



##### 在循环嵌套中使用

阅读如下代码，思考最终会输出什么？

```python
i = 0
while i < 3:
    print("i=%d" % i)
    i += 1
    j = 0
    while j < 3:
        print("---")
        j += 1
        break
```

最终输出结果为：

```text
i=0
---
i=1
---
i=2
---
```

**看到上述输出结果，我们发现：break作用在当前的循环体，并不会影响到外层循环！**

`continue`在循环嵌套中的作用于`break`几乎一样，只不过它是结束本次循环，而`break`是结束整个循环

**切记口诀：break、continue在哪个循环中就对哪个循环起作用**



##### break 与 continue 使用总结

- `break`、`continue`只能用在循环中，除此以外不能单独使用
- `break`、`continue`在嵌套循环中，只对最近的一层循环起作用
- `break`能够立刻结束所在的循环
- `continue`的用来结束本次循环，紧接着执行下一次的循环
- 无论`break`放到`while`循环体中的任何位置，只要被执行一次，那么整个循环立刻结束



### 循环中的 else

##### 引入

看如下代码，想一想：怎样实现 "密码不正确的相应提示"

```python
i = 3
while i > 0:
    password = input("请输入密码：（还剩%d次机会）" % i)
    if password == "123456":
        print("密码输入正确")
        break
    i -= 1
```



想要实现在 "密码不正确" 时提示相应的信息，普通的做法是：

```python
login_flag = False  # 定义一个变量，用来存储是否登录成功，True表示成功 False表示不成功
i = 3
while i > 0:
    password = input("请输入密码：（还剩%d次机会）" % i)
    if password == "123456":
        login_flag = True  # 如果登录成功，那么这里就改为True
        break
    i -= 1

# 当上述的while循环结束后，判断login_flag的值，来输出对应的信息
if login_flag == True:  # 简单的写法是if login_flag:
    print("密码输入正确")
else:
    print("密码输入不正确，今日3次机会已用完，请明天再试...")
```

上述的代码整体逻辑是：

1. 循环中获取密码判断是否正确，通过一个变量来标记正确与否
2. 当循环结束后，在单独判断标记，然后输出对应的信息

问题：有么有简单的方式呢？

答：`else`



##### while...else... 的使用方式

**格式：**

```python
while 条件:
    # 条件满足时执行的代码...
else:
    # 如果上述的while循环没有调用break，就执行的代码...
```

说明：

- 只要while循环体中没有执行break，那么当while循环体中所有的代码执行完后，else中的代码也会执行
- 如果while循环中有break那么表示整个while结束，else中的代码也不会被执行



**示例：**

- 有 break 时：

  ```python
  i = 1
  while i <= 3:
      print("这是一段测试信息...")
      if i == 1:
          print("调用了break")
          break
      i += 1
  else:
      print("我是else中的代码")
  ```

  运行结果：

  ```text
  这是一段测试信息...
  调用了break
  ```

  

- 没有 break 时

  ```python
  i = 1
  while i <= 3:
      print("这是一段测试信息...")
      i += 1
  else:
      print("我是else中的代码")
  ```

  运行结果：

  ```text
  这是一段测试信息...
  这是一段测试信息...
  这是一段测试信息...
  我是else中的代码
  ```



##### 代码案例

```python
i = 3
while i > 0:
    password = input("请输入密码：（还剩%d次机会）" % i)
    if password == "123456":
        print("密码输入正确")
        break
    i -= 1
else:
    print("密码输入3次全部错误，请明日再试")
```



##### for...else... 的使用方式

**格式：**

```python
for 变量 in 可迭代对对象:
    # 正常执行的代码
else:
    # for未使用break时执行的代码
```



**示例：**

- 未使用 break

  ```python
  for i in range(5):
      print("i=%d" % i)
  else:
      print("我是else中的代码...")
  ```

  运行结果：

  ```text
  i=0
  i=1
  i=2
  i=3
  i=4
  我是else中的代码....
  ```

  

- 使用 break

  ```python
  for i in range(5):
      print("i=%d" % i)
      if i == 1:
          print("我是break哦...")
          break
  else:
      print("我是else中的代码...")
  ```

  运行结果：

  ```text
  i=0
  i=1
  我是break哦...
  ```



##### 代码案例

```python
for i in range(3, 0, -1):
    password = input("请输入密码：（还剩%d次机会）" % i)
    if password == "123456":
        print("密码输入正确")
        break
else:
    print("密码输入3次全部错误，请明日再试")
```



##### 验证 continue

我们知道`continue`的作用是结束本次循环，那么既然`break`在`for...else...`和`while...else...`中都起作用，那么`continue`呢？

接下来我们就验证一下。



验证一：

```python
i = 0
while i < 3:
    i += 1
    print("来了老弟...")
    continue
    print("一起学Python啊，别忘了来 www.tulingxueyuan.com 网站哈")
else:
    print("我是else中的代码...")
```

运行结果：

```text
来了老弟...
来了老弟...
来了老弟...
我是else中的代码...
```



验证二：

```python
for i in range(3):
    print("来了老弟...")
    continue
    print("一起学Python啊，别忘了来 www.tulingxueyuan.com 网站哈")
else:
    print("我是else中的代码...")
```

运行结果：

```text
来了老弟...
来了老弟...
来了老弟...
我是else中的代码...
```

**结论：**

- 在`while...else...`与`for...else...`中，`break`会让`else`中的代码不执行，而`continue`没有这个功能