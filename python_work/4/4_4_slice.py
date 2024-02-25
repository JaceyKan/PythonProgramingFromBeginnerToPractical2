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