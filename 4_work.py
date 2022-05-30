num = int(input('Введите число --> '))
x = 0
while num > 0:
    if num % 10 > x:
        x = num % 10
    num = num // 10
print(x)