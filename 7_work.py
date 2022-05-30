start = float(input('Введите результат первого дня --> '))
end = float(input('Введите конечный результат --> '))
i = 1
while start < end:
    print(f'На {i} день - %.2f' % start)
    i += 1
    start = start + start / 10


print(f'На {i} день - %.2f' % start)