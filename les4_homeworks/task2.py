from random import randint

my_list = []
new_list = []

value = int(input('Введит кол-во эл. списка: '))
i_inc = 0

while i_inc < value:
    my_list.append(randint(-1000, 1000))
    if my_list[i_inc - 1] < my_list[i_inc]:
        new_list.append(my_list[i_inc])
    i_inc += 1

print('Изначальный список: ', my_list)
print('Обработанный список: ', new_list)
