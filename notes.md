

## 一、起步

> 图书在线资料： https://www.ituring.com.cn/book/3038
>
> [python.org](https://www.python.org/)



### 使用Sublime Text

文件扩展名.py告诉Sublime Text，文件中的代码是使用Python编写的，这能让它知道如何运行这个程序，并以有帮助的方式突出其中的代码。

选择菜单**Tools  ——》 Build** 或按 **Ctrl + B**（在macOS系统中为Command + B）来运行程序。

![image-20240219234444768](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219234444768.png)





### 使用VS Code

internalConsole  内部控制台

integratedTerminal  集成终端

![image-20240219232452512](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219232452512.png)

让 VS Code 在调试控制台（而不是集成的终端窗口）中显示输出后，
将无法运行使用了 input()函数的程序。 调试控制台是只读的，这意味着它不能接受输入。  



![image-20240219234359549](C:\Users\kanji\AppData\Roaming\Typora\typora-user-images\image-20240219234359549.png)

从编辑器切换到终端窗口，可按 Ctrl + `；
提供程序输入后，可再次按 Ctrl +``从终端窗口切换到编辑器窗口  



## 二、变量和简单数据类型



### 2.2 变量

#### 变量的命名和使用：

* 变量名只能包含字母、数字和下划线。

* 能以字母或下划线打头，但不能以数字打头

* 变量名不能包含空格，能使用下划线来分隔其中的单词

* 不要将Python关键字和函数名用作变量名

* 应既简短又具有描述性

* 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

* 目前而言，应使用小写的Python变量名。

  虽然在变量名中使用大写字母不会导致错误，但是大写字母在变量名中有特殊含义



#### traceback  （追踪）

程序无法成功运行时，解释器将提供一个traceback。

traceback是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。



### 2.3　字符串

```python
name = "ladA loVeLace"
print(name.title())	#Lada Lovelace
```



**空白**泛指任何非打印字符，如空格、制表符和换行符。

你可以使用空白来组织输出，让用户阅读起来更容易



* 要确保字符串末尾没有空白 `rstrip()`。

* 剔除字符串开头的空白使用方法 `lstrip()`

* 同时剔除字符串两边的空白 `strip()`

```python
favorite_language = '  python  '
print(favorite_language.rstrip()) #  python
print(favorite_language.lstrip()) #python  
print(favorite_language.strip()) #python
```



### 2.4  数

将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除



书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读

```python
universe_age = 14_000_000_000
print(universe_age) #14000000000
```

将数字分组时，即便不是将每三位分成一组，也不会影响最终的值。

在Python看来，1000与1_000没什么不同，1_000与10_00也没什么不同。

这种表示法适用于整数和浮点数，但只有Python 3.6和更高的版本支持。



常量类似于变量，但其值在程序的整个生命周期内保持不变

```python
MAX_CONNECTIONS = 5000
```



### 2.5 注释

编写注释的主要目的是阐述代码要做什么，以及是如何做的。

作为新手，最值得养成的习惯之一就是在代码中编写清晰、简洁的注释。



### 2.6 python之禅

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 复杂胜过混乱。
Flat is better than nested. 扁平胜过嵌套。
Sparse is better than dense. 稀疏胜过密集。
Readability counts. 可读性至关重要。
Special cases aren't special enough to break the rules. 特殊情况不足以违背规则。
Although practicality beats purity. 
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
应该有一种——最好只有一种——显而易见的方式来做。
Although that way may not be obvious at first unless you're Dutch.
尽管永远比立刻现在更好。
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

漂亮胜过丑陋。
明确胜过含蓄。
简单胜过复杂。
复杂胜过混乱。
扁平胜过嵌套。
稀疏胜过密集。
可读性至关重要。
特殊情况不足以违背规则。
尽管实用性优于纯粹性。
错误永远不应该悄悄地传递。
除非明确被沉默。
面对歧义，拒绝猜测的诱惑。
应该有一种——最好只有一种——显而易见的方式来做。
尽管这种方式一开始可能不明显，除非你是荷兰人。
现在胜过永远不开始。
尽管永远比立刻现在更好。
如果实现难以解释，那是个糟糕的想法。
如果实现容易解释，那可能是个好主意。
命名空间是一个非常棒的想法——让我们做更多这样的事情！
```



## 三、列表

通过将索引指定为-1，可让Python返回最后一个列表元素



```python
bicycles = ['trek', 'anta', 'Phoenix', 'Forever']
print(bicycles) #['trek', 'anta', 'Phoenix']

print(bicycles[0])
print(bicycles[1].title())

# 通过将索引指定为-1，可让Python返回最后一个列表元素
print(bicycles[-1])
# 这种约定也适用于其他负数索引。例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，依此类推
print(bicycles[-2])

message = f'my first bicycle was {bicycles[-2]}'
print(message)
```



```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#添加列表元素
#append —— 附加
motorcycles.append('honda')
print(motorcycles)

# 创建空列表，再添加元素
fruites = []
fruites.append('apple')
fruites.append('coconut')
print(fruites)

# insert —— 插入
fruites.insert(1, 'banana')
print(fruites)

# del —— 删除指定位置的元素
del fruites[-2]
print(fruites)

# pop —— 删除列表末尾的元素，并返回该元素
last_fruite = fruites.pop()
print(last_fruite)

# 使用pop()删除列表中任意位置的元素，指定要删除元素的索引即可。
colors = ['pink', 'yellow', 'blue', 'silver']
print(colors)
third_color = colors.pop(2)
print(f'my favorite color is {third_color}')
print(colors)

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop()。

# remove 删除指定值的元素
# remove()只删除第一个指定的值
# 如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除
colors.remove('yellow')
print(colors)
```



```python
# sort为列表永久排序
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort()
print(cars)
# 按与字母顺序相反的顺序排列列表元素
cars.sort(reverse=True)
print(cars)

# sorted 对列表临时排序
cars2 = ['bmw', 'audi', 'toyato', 'subaru']
print(sorted(cars2))
print(sorted(cars, reverse=True))
print(cars2)

# reverse 反转列表元素的排列顺序
# 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用reverse()即可。
cars3 = ['bmw', 'audi', 'toyato', 'subaru']
cars3.reverse()
print(cars3)

print(len(cars3)) # 4
```



## 四、操作列表

```python
# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that is a great trick!')
    print(f"I can't wait to see your next trick! {magician.title()}\n")

# 在for循环后面，没有缩进的代码都只执行一次，不会重复执行
print("Thank you, everyone. That was a great magic show!")
```



### 4.3 创建数值列表

```python
# 函数range()让你能够轻松地生成一系列数
for value in range(5):
    print(value) # 0 1 2 3 4
print("\n")

# 函数range()让Python从指定的第一个值开始数，并在到达你指定的第二个值时停止
# 因为它在第二个值处停止，所以输出不包含该值（这里为5）
for value in range(1, 5):
    print(value) # 1 2 3 4

# 创建数字列表，可使用函数list()将range()的结果直接转换为列表
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

# 使用函数range()时，还可指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

# 将前10个整数的平方加入一个列表
squares = []
for value in range(1, 11):
    squares.append(value**2) # 用两个星号(**)表示乘方运算
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 找出数字列表的最大值、最小值和总和：
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45

# 列表解析：
# 将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares2 = [value**2 for value in range(1, 11)]
print(squares2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```





## 附录D 使用Git进行版本控制

### 配置 .gitignore

```
pycache  // 忽略pycache文件夹
resources  // 忽略resources文件夹
```



### 撤销修改

放弃最后一次提交后所做的所有修改，将项目恢复到最后一次提交的状态

```
git checkout .
```











