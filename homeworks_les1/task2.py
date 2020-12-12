
seconds_input = input('Введите время в секундах:\n')

if seconds_input.isdigit():
    seconds_input = int(seconds_input)

hours_output = seconds_input // 3600
seconds_input = seconds_input - (hours_output * 3600)
minutes_output = seconds_input // 60
seconds_output = seconds_input % 60

str(hours_output)
str(minutes_output)
str(seconds_input)

print(hours_output,':',minutes_output,':',seconds_output)