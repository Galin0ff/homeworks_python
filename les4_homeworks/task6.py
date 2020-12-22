from itertools import count, cycle

for el in count(3, 2):
    if el > 10:
        break
    else:
        print(el)

prog_names = ['PyCharm', 'python 3', 'pascal turbo']

i = 0
for el in cycle(prog_names):
    if i > 4:
        break
    print(el)
    i += 1