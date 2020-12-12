# fifth pr4cc

# rating_list = []
#
# user_values = input('Введите кол-во эл рейтинга.\n')
# if user_values.isdigit():
#     user_values = int(user_values)
#
# while user_values > 0:
#     rating_list.append(input("Введите эл. рейтинга: \n"))
#     user_values -= 1

rating_list = [7, 5, 3, 3, 2]

new_el = input('Введите новый эл. рейтинга:\n')
i = 0

while i != len(rating_list):
    if int(new_el) >= int(rating_list[i]):
        temp = rating_list[i]
        rating_list[i] = new_el
        new_el = temp
    i += 1

rating_list.append(new_el)

for value in rating_list:
    print(value) 