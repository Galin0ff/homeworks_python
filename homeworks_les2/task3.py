# thrid pr4cc

# 1st task

seasons_list = ['winter', 'winter', 'spring', 'spring',
                'spring', 'summer', 'summer', 'summer', 'autumn',
                'autumn', 'autumn', 'winter']

user_answer = input('Введите месяц года числом:\n')

if user_answer.isdigit():
    user_answer = int(user_answer)
else:
    print('Введите число')

print(seasons_list[user_answer-1])

# 2d task

seasons_dict = {
    1: 'winter',
    2: 'winter',
    12: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    }

print(seasons_dict.get(user_answer))