# salary = (hours * rate) + bonus
from sys import argv

if len(argv) != 4:
    print('Ошибка ввода параметров')
    exit()


def Salary(list):
    hours = int(argv[1])
    rate = int(argv[2])
    bonus = int(argv[3])
    return ((hours * rate) + bonus)


print('Заработна плата', Salary(argv))