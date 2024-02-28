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



