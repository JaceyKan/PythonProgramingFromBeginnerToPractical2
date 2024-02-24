motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#添加列表元素
#append —— 附加
motorcycles.append('honda')
print(motorcycles)

#创建空列表，再添加元素
fruites = []
fruites.append('apple')
fruites.append('coconut')
print(fruites)

#insert —— 插入
fruites.insert(1, 'banana')
print(fruites)

#del —— 删除指定位置的元素
del fruites[-2]
print(fruites)

#pop —— 删除列表末尾的元素，并返回该元素
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

# remove
# remove()只删除第一个指定的值
# 如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除
colors.remove('yellow')
print(colors)




