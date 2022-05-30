my_seconds = int(input('Введите время в секундах --> '))
my_hours = my_seconds // 3600
my_minutes = (my_seconds // 60) % 60
my_seconds = my_seconds % 60

print(f'{my_hours}:{my_minutes}:{my_seconds}')