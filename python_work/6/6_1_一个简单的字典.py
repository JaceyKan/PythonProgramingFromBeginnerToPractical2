alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 字典是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。
# 与键相关联的值可以是数、字符串、列表乃至字典。
# 事实上，可将任何Python对象用作字典中的值。

#---------------使用字典-------------------
new_point = alien_0['points']
print(f"You just earned {new_point} points!")

alien_1 = {'color': 'red', 'points': 5}
print(alien_1)

alien_1['x_position'] = 50
alien_1['y_position'] = 200
print(alien_1)
# 字典中元素的排列顺序与定义时相同。
# 如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。

# --------------------先创建一个空字典-----------------------
alien_2 = {}

alien_2['color'] = 'yellow'
alien_2['point'] = 15

print(alien_2)

