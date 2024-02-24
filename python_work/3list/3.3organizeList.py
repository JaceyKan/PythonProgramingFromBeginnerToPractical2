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

print(len(cars3))