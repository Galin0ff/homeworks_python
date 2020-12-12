# fourth pr4cc

user_sentence = input('Введите предложени:\n')

sentence_output = user_sentence.split()
# print(sentence_output)
i = 1

for value in sentence_output:
    # print(len(value))
    print(i, 'ая строка:', value[:10])
    i += 1 