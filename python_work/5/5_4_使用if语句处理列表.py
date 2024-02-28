requested_toppings = ['mushrooms', 'garlic','extra cheese']

for requested_topping in requested_toppings:
    print(f"Add {requested_topping}")

print("\nFinished making your pizza!")

# --------------------------
# 比萨店的青椒用完了，该如何处理呢？
# 为妥善地处理这种情况，可在for循环中包含一条if语句
print("\n")
for requested_topping in requested_toppings:
    if requested_topping == 'garlic':
        print("Sorry, we are out of garlic right now!")
    else:
        print(f"Add {requested_topping}")

print("\nFinished making your pizza!")

# --------------------------
# 确定列表不是空的
print("------------------------")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'garlic':
            print("Sorry, we are out of garlic right now!")
        else:
            print(f"Add {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")
# --------------------------
# 使用多个列表
print("------------------------")
available_toppings = ['mushrooms', 'green peppers', 'onion', 'extra cheese', 
                      'olives', 'pinapple', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Add {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print("Your pizza has finished!")
else:
    print("Are you sure you want a plain pizza?")