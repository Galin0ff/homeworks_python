
gain = input('Введите выручку компании:\n')
cost = input('Введите издержки компании:\n')

if gain.isdigit() and cost.isdigit():
    gain = int(gain)
    cost = int(cost)

if gain < cost:
    print('Компания работает в убыток. Издержки больше выручки')
else:
    print('Прибыль компании составила :',gain - cost,'\n')
    number_of_staff = input('Введите кол-во сотрудников вашей компании:\n')
    if number_of_staff.isdigit():
        number_of_staff = int(number_of_staff)
    print('Прибыль на одного сотрудника составила =',round(((gain - cost)/number_of_staff), 2))