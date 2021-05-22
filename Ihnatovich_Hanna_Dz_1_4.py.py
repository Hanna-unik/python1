number = abs(int( input('Введите положительное число: ')))
max = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print ('Максиммальная цифра в числе ', max)
        break