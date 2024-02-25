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