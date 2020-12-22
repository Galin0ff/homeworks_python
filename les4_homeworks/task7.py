from itertools import count


def fact(n):

    i = 1
    my_list = []

    while i <= n:
        new_el = 1
        for el in count(1):
            new_el *= el
            if i == el:
                my_list.append(new_el)
                break
        i += 1

    for facto in my_list:
        yield facto


n = int(input('Введите число факториала: '))

for el in fact(n):
    print(el)
