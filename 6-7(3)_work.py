def my_func(text):
    list_text = list(text)
    list_text[0] = list_text[0].upper()
    return ''.join(list_text)

text = input()
print(my_func(text))

output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(my_func(word))
    output_2.append(my_func(word))

print(f'Строка получается - {" ".join(output_1)}')
