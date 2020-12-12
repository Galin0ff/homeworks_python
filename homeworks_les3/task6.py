

def int_func(sent_t: str):
    num_ord = ord(sent_t[0])
    num_char = chr((num_ord) + 32)
    sent_t[0] = num_char
    return sent_t


sent = input('Введите предложение')
print(int_func(sent))


