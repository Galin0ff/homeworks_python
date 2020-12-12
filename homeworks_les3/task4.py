# version 1

def my_func(x, y):

    if y == 0:
        result = 1
    elif y > 0:
        result = x
        while y > 1:
            result *= x
            y -= 1
    else:
        result = 1
        while y < 0:
            result *= (1/x)
            y += 1

    return result

print(my_func(5, -2))
print(5**(-2))