
n = input('Введите число для нахождения суммы n\n')

n_str = n
n_int = 0
i = 3

while i > 0:
    n_int += int(n_str)
    # print(n_int)
    n_str += n
    # print(n_str)
    i -= 1

print('Сумма =',n_int)