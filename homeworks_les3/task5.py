
def my_func(sum_list: list, old_sum: int, my_stop:bool):
    new_sum = 0
    result = 0
    if sum_list[0] == 'stop':
        my_stop = False
        return old_sum, my_stop,
    else:
        if sum_list[-1] == 'stop':
            sum_list.pop(-1)
            for key in sum_list:
                new_sum += int(key)
            old_sum += new_sum
            my_stop = False
            return old_sum, my_stop
        else:
            for key in sum_list:
                new_sum += int(key)
            old_sum += new_sum
            return old_sum, my_stop


my_stop = True
old_sum = 0

while my_stop:
    print('Для того, чтобы закончить напишите в конце stop.')
    number = input('Введите числа через пробел:\n')
    sum_list = list(number.split())
    old_sum, my_stop = my_func(sum_list, old_sum, my_stop)
    print('Сумма ваших чеисел =', old_sum, '\n')