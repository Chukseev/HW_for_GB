def division_num(a, b):
    if b != 0:
        res = a / b
        print(f'Результат - {res}')
    else:
        print('На ноль делить нельзя')
first_num = int(input('Введите первое число --> '))
second_num = int(input('Введите второе число --> '))
division_num(first_num,second_num)
