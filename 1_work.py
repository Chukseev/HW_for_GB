name = 'Петя'
age = '22'
print(f'Я {name}, мне {age}')
name = input('Введите имя --> ')
age = int(input('Введите возраст --> '))
print(f'Я {name}, мне {age}')
my_seconds = int(input('Введите время в секундах --> '))
my_minutes = my_seconds // 60
my_hours = my_minutes // 60
my_seconds = my_seconds % 60

print(my_minutes)