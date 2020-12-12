user_template = {
    'name': ('Имя',str),
    'surname': ('Фамилия', str),
    'birth': ('Дата рождения', str),
    'country': ('Город', str),
    'email': ('Email', str),
    'phone': ('Телефон', str)
}

def my_user(**kwargs):
    result = []
    for key in kwargs:
        result.append(kwargs[key])
    result = (' '.join(result))
    return result


user_info = {}

for key,value in user_template.items():
    user_value = input(f'{value[0]}\n')
    user_info[key] = user_value

# print(user_info)

answer = my_user(**user_info)
print(answer) 