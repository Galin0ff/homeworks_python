
my_list = []

value = int(input('Введите кол-во эл. списка: '))

i = 0
while i < value:
    my_list.append(int(input('Введите эл. списка: ')))
    i += 1

# new_list = [el for el in my_list for next_el in my_list if (el != next_el)]

new_list = []

for el in my_list:
    j = 0
    for next_el in my_list:
        if el == next_el:
            j += 1
    if j == 1:
        new_list.append(el)

new_sec_list = [el for el in my_list for next_el in my_list ]




print(my_list)
print(new_list)
print(new_sec_list)

