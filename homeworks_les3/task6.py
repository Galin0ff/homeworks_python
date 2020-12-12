

def int_func(sentence: str) -> str:
    first_sentence = sentence.split()
    complit_sentence = []
    for item in first_sentence:
        result = list(item)
        char_change = ord(result[0]) - 32
        char_change = chr(char_change)
        result[0] = char_change
        item = ''.join(result)
        complit_sentence.append(item)
    return ' '.join(complit_sentence)


user_str = input('Введите строку: \n')
print('Готовое предложение:\n', int_func(user_str))

# user_str = input('Введите строку: \n')
#
# print(ord('t'))
# print(chr(116))
#
# print(ord(user_str[0]))
# char_change = ord(user_str[0]) - 32
# print(char_change)
# num_change = chr(char_change)
# print(num_change)
# user_str_list = list(user_str)
# user_str_list[0] = num_change
# print(''.join(user_str_list))