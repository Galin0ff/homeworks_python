
def my_div(arg_1: float, arg_2: float) -> float:
    """
    Функция делит первый аргумент на второй.
    :param arg_1: float
    :param arg_2: float
    :return: число деления первого на второго float
    """
    if arg_2 == 0:
        print('Деление на 0 невозможно.\n')
        return 0
    else:
        return round(((arg_1 / arg_2)),2)


arg_1 = input('Введите делимое число:')
arg_2 = input('Введите делитель:')
print(my_div(int(arg_1), int(arg_2)))