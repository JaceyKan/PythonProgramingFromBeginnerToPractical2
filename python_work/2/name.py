name = "ladA loVeLace"
print(name.title()) #Lada Lovelace
print(name.upper()) #LADA LOVELACE
print(name.lower()) #lada lovelace
print(name.capitalize()) #Lada lovelace

# f字符串(format)
last_name = 'jacey'
first_name = 'kan'
full_name = f'{last_name} {first_name}'
print(full_name.title())

message = f'Hello {full_name.title()}'
print(message)

full_name2 = "{} {}".format(last_name, first_name);
print(full_name2.title())

favorite_language = '  python  '
print(favorite_language.rstrip()) #  python
print(favorite_language.lstrip()) #python  
print(favorite_language.strip()) #python