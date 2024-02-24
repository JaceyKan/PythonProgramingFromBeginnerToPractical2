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
