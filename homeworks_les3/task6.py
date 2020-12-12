

def int_func(sentence: str) -> str:
    first_seentence
    result = list(sentence)
    char_change = ord(result[0]) - 32
    char_change = chr(char_change)
    result[0] = char_change
    return ''.join(result)


user_str = input('Введите строку: \n')
print(int_func(user_str))

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