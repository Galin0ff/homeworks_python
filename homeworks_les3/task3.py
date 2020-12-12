
def my_func(arg_1, arg_2, arg_3):
    new_sum = arg_1
    if new_sum >= arg_2:
        if arg_2 > arg_3:
            new_sum += arg_2
        else:
            new_sum += arg_3
    else:
        new_sum = arg_2
        if arg_1 > arg_3:
            new_sum += arg_1
        else:
            new_sum += arg_3
    return new_sum

t = []
i = 3

while i > 0:
    t.append(int(input('Введите цифру: ')))
    i -= 1
print(my_func(*t))
