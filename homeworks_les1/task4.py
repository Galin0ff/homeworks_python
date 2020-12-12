
n = input('Введите число в котором мы ищем самую большую цифру: n\n')

if n.isdigit():
    n = int(n)

max_digit = n % 10

while n > 0:
    if (n % 10) > max_digit:
         max_digit = n % 10
         n = n // 10
    else:
        n = n //10

print('самая большая цифра в числе =', max_digit)