# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that is a great trick!')
    print(f"I can't wait to see your next trick! {magician.title()}\n")

# 在for循环后面，没有缩进的代码都只执行一次，不会重复执行
print("Thank you, everyone. That was a great magic show!")