# sixth pr4cc

i = 1
product_list=[]

user_answer = input('Хотите внести товар в список?\n')

while user_answer == 'Да':
    t=(i, {
        "название": input('Введите название: '),
        "цена": input('Введите цену: '),
        "количество": input('Введитее количесво: '),
        "ед": input('Введите ед. измерения: ')
    })
    product_list.append(t)
    user_answer = input('Хотите внести еще один товар в список?\n')

product_analytics = {}

for key in product_list:
    result = []
    for itm in product_list:
        result.append(itm[1][key])
    product_analytics[key] = result

print(product_analytics)

# product_list = [(1, input('Введите название'), input('Введите цену'),
#                  input('Введитее количесво'), input('Введите ед. измерения')),
#                 (2,input('Введите название'), input('Введите цену'),
#                  input('Введитее количесво'), input('Введите ед. измерения')),
#                 (3, input('Введите название'), input('Введите цену'),
#                  input('Введитее количесво'), input('Введите ед. измерения'))
#                 ]
#
# first_t= (1, {
#         "название": input('Введите название\n'),
#         "цена": input('Введите цену\n'),
#         "количество": input('Введите количество\n'),
#         "ед": input('Введите единицу измерения:\n')
#     }),
#
# second_t = (2, {
#     "название": input('Введите название\n'),
#     "цена": input('Введите цену\n'),
#     "количество": input('Введите количество\n'),
#     "ед": input('Введите единицу измерения:\n')
# })
#
# third_t = (3, {
#     "название": input('Введите название\n'),
#     "цена": input('Введите цену\n'),
#     "количество": input('Введите количество\n'),
#     "ед": input('Введите единицу измерения:\n')
# })
# ]
# print(first_t, second_t, third_t) 