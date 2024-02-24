bicycles = ['trek', 'anta', 'Phoenix', 'Forever']
print(bicycles) #['trek', 'anta', 'Phoenix']

print(bicycles[0])
print(bicycles[1].title())

#通过将索引指定为-1，可让Python返回最后一个列表元素
print(bicycles[-1])
#这种约定也适用于其他负数索引。例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，依此类推
print(bicycles[-2])

message = f'my first bicycle was {bicycles[-2]}'
print(message)