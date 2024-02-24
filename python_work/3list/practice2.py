visitors = ['Mama', 'Baba', 'Grandma', 'Big New', 'Little Peach']
print(f'I hope you could come to dinner, {visitors[0]}')
print(f'I hope you could come to dinner, {visitors[3]}')
print(f'I hope you could come to dinner, {visitors[-1]}')

cant_come = 'Mama'
print(f"{cant_come} won't come to dinner.")
del visitors[0]
print(visitors)

visitors.append('Qiqi')
print(f'{visitors[-1]} will come to dinner.')

print('I found a big table, so that I can invite more visitors!')
visitors.insert(0, 'Grandpa')
print(visitors)
visitors.insert(3, 'Tengteng')
print(visitors)
visitors.append('Laolao')
print(visitors)

print("I am sorry, the new table can't be taken in time, only two visitors can be invited.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
uninvited = visitors.pop()
print(f"{uninvited}, sorry I can't invite you to come.")
print(visitors)

print(f"{visitors[0]} can come to dinner.")
print(f"{visitors[1]} can come to dinner.")

del visitors[-1]
del visitors[-1]
print(visitors)