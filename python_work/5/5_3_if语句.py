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