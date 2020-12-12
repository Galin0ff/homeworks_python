
dog1_name = "Max"
dog2_name = "Antony"

dog1_age = 3
dog2_age = 5

user_ask = input('Сколько лет собаке\n')

if user_ask.isdigit():
    user_ask = int(user_ask)

if user_ask == 3:
    print('Это Max, ему 3 года')
elif user_ask == 5:
    print('Это Antony, ему 5 лет')
else:
    print('Такого возраста собаки у нас нет :c')