user_names = ['Jacey', 'Lily', 'Joy', 'admin']

user_names.pop()
del user_names[-1]
user_names.remove('Jacey')
user_names.pop()
print(user_names)

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user_name}, thank you for logging again.")
else:
    print("We need to find some users.")

# --------------------------------
current_users = ['Jacey', 'Hellen', 'Bunny', 'joy']
new_users = ['hellen', 'Jacey', 'lily']

copy_current_users = []
for current_user in current_users:
    copy_current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in copy_current_users:
        print(f"{new_user} has been used, please change another name.")
    else:
        print("You can use the name.")

# ----------------------------
numbers = list(range(1, 10))
print(numbers)

for val in numbers:
    if val == 1:
        print("1st")
    elif val == 2:
        print("2nd")
    else:
        print(f"{val}th")