# Second pr4cc
# commit

some_list = []
i = 0

user_values = input('Введите кол-во эл списка.\n')
if user_values.isdigit():
    user_values = int(user_values)

while user_values > 0:
    some_list.append(input("Введите эл. списка: \n"))
    user_values -= 1
    if ((i + 1) % 2) == 0:
        temp = some_list[i]
        some_list[i] = some_list[i - 1]
        some_list[i - 1] = temp
    i += 1

i = 1
for value in some_list:
    print(i,'-й элемент списка:')
    print(value)
    i += 1 