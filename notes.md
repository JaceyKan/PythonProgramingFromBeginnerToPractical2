

## 一、起步

> 图书在线资料： https://www.ituring.com.cn/book/3038
>
> [python.org](https://www.python.org/)



### 使用Sublime Text

文件扩展名.py告诉Sublime Text，文件中的代码是使用Python编写的，这能让它知道如何运行这个程序，并以有帮助的方式突出其中的代码。

选择菜单**Tools  ——》 Build** 或按 **Ctrl + B**（在macOS系统中为Command + B）来运行程序。

![image-20240219234444768](imgs\image-20240219234444768.png)





### 使用VS Code

internalConsole  内部控制台

integratedTerminal  集成终端

![image-20240219232452512](imgs\image-20240219232452512.png)

让 VS Code 在调试控制台（而不是集成的终端窗口）中显示输出后，
将无法运行使用了 input()函数的程序。 调试控制台是只读的，这意味着它不能接受输入。  



![image-20240219234359549](imgs\image-20240219234359549.png)

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



### 4.4 使用列表的一部分

```python
# 处理列表的部分元素，Python称之为切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
# 与函数range()一样，Python在到达第二个索引之前的元素后停止。

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']

print(players[1:4]) # ['martina', 'michael', 'florence']

# 如果没有指定第一个索引，Python将自动从列表开头开始
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']

# 让切片终止于列表末尾
print(players[2:]) # ['michael', 'florence', 'eli']

# 负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任意切片。
# 例如，如果要输出名单上的最后三名队员，可使用切片players[-3:]
print(players[-3:]) # ['michael', 'florence', 'eli']

# --------------------------------------
# 遍历切片
for player in players[:4]:
    print(player)

# --------------------------------------
# 复制列表
# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:])。
my_foods = ['apple', 'cake', 'yogurt']
my_friend_foods = my_foods[:]

print(f"my favorite foods are: {my_foods}")
print(f"my friend's favorite foods are: {my_friend_foods}")

my_foods.append('ice cream')
my_friend_foods.append('orange')

print(f"my favorite foods are: {my_foods}")
print(f"my friend's favorite foods are: {my_friend_foods}")
# my favorite foods are: ['apple', 'cake', 'yogurt', 'ice cream']
# my friend's favorite foods are: ['apple', 'cake', 'yogurt', 'orange']

# -------------------------------------
# 如果只是将my_foods赋给friend_foods，就不能得到两个列表。
# 演示在不使用切片的情况下复制列表的情况:
my_colors = ['pink', 'blue', 'grey']
friend_colors = my_colors

my_colors.append('yellow')
friend_colors.append('purple')

print(f"my colors are: {my_colors}")
print(f"friends colors are: {friend_colors}")
# my colors are: ['pink', 'blue', 'grey', 'yellow', 'purple']
# friends colors are: ['pink', 'blue', 'grey', 'yellow', 'purple']
```



### 4.5 元组

```python
# 列表非常适合用于存储在程序运行期间可能变化的数据集。
# Python将不能修改的值称为不可变的，
# 不可变的列表被称为元组。
# 元组看起来很像列表，但使用圆括号而非中括号来标识。
# 定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 # TypeErro: 'tuple' object does not support item assignment

# -------------------------------------
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
# 如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号
my_tuple = (3,)

# -----------------------------------
# 使用for循环来遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# -----------------------------------
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
# 因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
dimensions = (400, 100)
print(f"Modified dimensions: {dimensions}")

# -----------------------------------
# 相比于列表，元组是更简单的数据结构。
# 如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组。
```



### 4.6　设置代码格式

**Python改进提案** (Python Enhancement Proposal,PEP)。

**PEP 8**是最古老的PEP之一，向Python程序员提供了代码格式设置指南。



* 缩进

  PEP 8建议每级缩进都使用四个空格。这既可提高可读性，又留下了足够的多级缩进空间。

  你在编写代码时绝对应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符。

* 行长

  建议每行不超过79字符

  在大多数编辑器中，可以设置一个视觉标志（通常是一条竖线），让你知道不能越过的界线在什么地方。

  PEP 8还建议注释的行长不应超过72字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符。

* 空行

  要将程序的不同部分分开，可使用空行。

  例如，如果你有五行创建列表的代码，还有三行处理该列表的代码，那么用一个空行将这两部分隔开是合适的。

  然而，你不应使用三四个空行将其隔开。



#### 在VSCode中将所有已存在的Tab转换为空格：

File ——》Preference ——》setting ——》输入 editor

![image-20240225224509856](imgs\image-20240225224509856.png)

你可以通过设置 `editor.renderWhitespace: all` 让编辑器将所有的空格符、制表符等全部都渲染出来。这样你就能够一眼看出这个文件中使用的究竟是制表符还是空格符，以及有没有在哪里不小心多打了一个空格等。



#### 设置缩进参考线

 editor.rulers: [80]



> 参考：
>
> [VSCode 优化你的编辑器设置](https://github.com/jxcangel/vscode/blob/master/13%20!%20%E4%BC%98%E5%8C%96%E4%BD%A0%E7%9A%84%E7%BC%96%E8%BE%91%E5%99%A8%E8%AE%BE%E7%BD%AE.md)
>
> [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)



### 五、if语句

```python
# 对于大多数汽车，应以首字母大写的方式打印其名称，
# 但对于汽车名'bmw'，应以全大写的方式打印
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# --------------------------------
# 在Python中检查是否相等时区分大小写。
car = 'Audi'
print(car == 'audi') # False

# 如需忽略大小写，可将变量的值转换为小写，再进行比较
print(car.lower() == 'audi') # True

# ---------------------------------
# 检查是否不相等
# 判断两个值是否不等，可结合使用惊叹号和等号(!=)，其中的惊叹号表示不
request_topping = 'mushrooms'
if request_topping != 'anchovies':
    print('Hold the anchovies.')
# 你编写的大多数条件表达式检查两个值是否相等，
# 但有时候检查两个值是否不等的效率更高。
    
# ---------------------------------
# 数值比较
age = 18
if age == 18:
    print('You are 18 years old.')

answer = 17
if answer != 42:
    print("That's not the correct answer. Please try again!")

print(age >= 21)
print(age <= 20)
# ---------------------------------
# 检查多个条件 and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 21
print(age_0 >= 21 and age_1 >= 21)

# 为改善可读性，可将每个测试分别放在一对圆括号内，但并非必须这样做。
print((age_0 >= 21) and (age_1 >= 21))
# ---------------------------------
# 使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# ---------------------------------
# 关键字in
request_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in request_toppings)
print('tomato' in request_toppings)

# ---------------------------------
# 关键字not in
banned_users = ['Lily', 'Angela', 'Hellen']
user = 'Jacey'
if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')
```



#### 5.3 if语句

```python
# --------------------------
# if语句
age = 18
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# --------------------------
# if-else语句
age2 = 17
if age2 >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
#--------------------------
# if-elif-else语句
age = 12
if age < 4:
    print("Your admission cost is free.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
# 为了让代码更简洁，可不在if-elif-else代码块中打印门票价格，
# 而只在其中设置门票价格，并在它后面添加一个简单的函数调用print()：
age_2 = 20

if age_2 < 4:
    price = 0
elif age_2 < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#--------------------------
# 使用多个elif代码块
# 可根据需要使用任意数量的elif代码块
age_3 = 70

if age_3 < 4:
    price = 0
elif age_3 < 18:
    price = 25
elif age_3 < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

#--------------------------
# 省略else代码块
# else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行。
# 这可能引入无效甚至恶意的数据。
# 如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。
age_4 = 10

if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 25
elif age_4 < 65:
    price = 40
elif age_4 >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

#--------------------------
# 测试多个条件
# 有时候必须检查你关心的所有条件。
# 在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Add mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Add pepperoni.")
if 'extra cheese' in requested_toppings:
    print('Add extra cheese.')

print("\nFinished making your pizza!")
# 如果只想执行一个代码块，就使用if-elif-else结构；
# 如果要执行多个代码块，就使用一系列独立的if语句。
```



#### 5.4　使用if语句处理列表

```python
requested_toppings = ['mushrooms', 'garlic','extra cheese']

for requested_topping in requested_toppings:
    print(f"Add {requested_topping}")

print("\nFinished making your pizza!")

# --------------------------
# 比萨店的青椒用完了，该如何处理呢？
# 为妥善地处理这种情况，可在for循环中包含一条if语句
print("\n")
for requested_topping in requested_toppings:
    if requested_topping == 'garlic':
        print("Sorry, we are out of garlic right now!")
    else:
        print(f"Add {requested_topping}")

print("\nFinished making your pizza!")

# --------------------------
# 确定列表不是空的
print("------------------------")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'garlic':
            print("Sorry, we are out of garlic right now!")
        else:
            print(f"Add {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")
# --------------------------
# 使用多个列表
print("------------------------")
available_toppings = ['mushrooms', 'green peppers', 'onion', 'extra cheese', 
                      'olives', 'pinapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Add {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print("Your pizza has finished!")
else:
    print("Are you sure you want a plain pizza?")
```



#### 5.5　设置if语句的格式

在诸如==、>=和<=等比较运算符两边各添加一个空格



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











