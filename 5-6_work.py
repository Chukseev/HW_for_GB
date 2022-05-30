cost = int(input('Введите издержку --> '))
revenue = int(input('Введите выручку --> '))
if revenue > cost:
    print(f'Прибыль состовляет фирмы {revenue - cost} р.')
    employees = int(input('Введите количество сотрудников --> '))
    print(f'Прибыль в расчете на одного сотрудника является {(revenue - cost) / employees} р.')
elif revenue < cost:
    print(f'У вас убыток,который состовляет {cost - revenue} р.')