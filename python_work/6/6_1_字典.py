# alien
alien_0 = {'color': 'pink', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 访问字典中的值
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# ------------------------------
# 添加键值对
alien_1 = {'color': 'green', 'points': 10}
print(alien_1)

alien_1['x_position'] = 10
alien_1['y_position'] = 25
print(alien_1)
# 字典中元素的排列顺序与定义时相同。
# 如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。

# ------------------------------
# 先创建一个空字典
alien_2 = {}
alien_2['color'] = 'blue'
alien_2['points'] = 6
print(alien_2)

# ------------------------------
# 修改字典中的值
alien_3 = {'color': 'green'}
print(f"The alien3 is {alien_3['color']}.")

alien_3['color'] = 'yellow'
print(f"The alien3 is now {alien_3['color']}.")

alien_4 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position is: {alien_4['x_position']}.")

if alien_4['speed'] == 'slow':
    x_increament = 1
elif alien_4['speed'] == 'medium':
    x_increament = 2
else:
    x_increament = 3

alien_4['x_position'] += x_increament
print(f"New position is: {alien_4['x_position']}")

# ------------------------------
# 删除键值对
# 使用del语句将相应的键值对彻底删除，必须指定字典名和要删除的键
alien_5 = {'color': 'green', 'points': 10}
print(alien_5)

del alien_5['color']
print(alien_5)

# ------------------------------
# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# ------------------------------
# 使用get来访问值
alien_6 = {'color': 'pink', 'speed': 'slow'}
# print(alien_6['point']) # KeyError: 'point'

# 方法get()的第一个参数用于指定键，必不可少；第二个参数为指定的键不存在时要返回的值，可选
point_value = alien_6.get('point', 'No point value assigned.')
print(point_value)
# 调用get()时，如果没有指定第二个参数且指定的键不存在，Python将返回值None。
# 这个特殊值表示没有相应的值。None并非错误，而是一个表示所需值不存在的特殊值

# -----------------------------
# 人
friend = {
    'first_name': 'Li',
    'last_name': 'Hui Fang',
    'age': 18,
    'city': 'Da Li',
}

print(friend)

# -------------------------
# 数字
favorite_numbers = {
    'Lily': 5,
    'Yuan': 7,
    'Peach': 9,
}

# -------------------------
# 6.3 遍历字典
# 6.3.1 遍历所有键值对
user_0 = {
    'username': 'Jacey',
    'first': 'Kan',
    'last': 'Jacey',
}

for k, v in user_0.items():
    # print(f"key: {k}; value: {v}")
    print(f"{k}: {v}")
    # print(f"value: {v}")

print(user_0.items()) # dict_items([('username', 'Jacey'), ('first', 'Kan'), ('last', 'Jacey')])

# -----------------------
favorite_languages_1 = {
    'Lily': 'c',
    'Jacey': 'java script',
    'Hellen': 'python'
}

for name, language in favorite_languages_1.items():
    print(f"{name}'s favorite language is {language.title()}.")

# -------------------------
# 遍历字典中的所有键 keys()
for name in favorite_languages_1.keys():
    print(name)

# 遍历字典时默认遍历所有键
print("\n")
for name in favorite_languages_1:
    print(name)

# ------------------------------
print("\n")
friends = ['Jacey', 'Joy']

for name in favorite_languages_1:
    print(f"Hi {name}!")

    if name in friends:
        print(f"\tI see your favorite languange is {favorite_languages_1[name].title()}")

# --------------------------------
if 'eric' not in favorite_languages_1.keys():
    print(f"Eric please take our poll!")

# -------------------------------
# 按特定顺序遍历字典中的所有键 sorted()
for name in sorted(favorite_languages_1.keys()):
    print(f"{name.title()}, thanks for taking our poll!")

# ----------------------------------
# 遍历字典中的所有值 values()
print("The following languages have been mentioned.")
for language in favorite_languages_1.values():
    print(language)

# 为剔除重复项，可使用集合(set)。集合中的每个元素都必须是独一无二的
print("\n")
for language in set(favorite_languages_1.values()):
    print(language.title())

# ----------------------
# 可使用一对花括号直接创建集合
languages = {'python', 'c', 'java', 'ruby', 'java'}
print(languages)
# 不同于列表和字典，集合不会以特定的顺序存储元素。

# --------------------------
# 练习6-5.河流
rivers = {
    'chang jiang': 'china',
    'nile': 'egypt',
    'misisibi': 'emerica'
}

for river, country in rivers.items():
    print(f"The {river.title()} run through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in set(rivers.values()):
    print(country.title())

# 练习6-6.调查
favorite_languages_2 = {
    'lily': 'ruby',
    'hellen': 'c',
    'richal': 'java',
    'joy': 'c',
}

members = ['richal', 'joy', 'eric', 'carl']
for name in members:
    if name in set(favorite_languages_2.keys()):
        print(f"{name}, thanks for taking the poll!")
    else:
        print(f"{name}, please take our poll!")

# -------------------------------
# 6.4 嵌套
