"""6. Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,
то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
"""


goods = []
product_id = 0
menu_items = ['name', 'price', 'units', 'stock']


while True:
    product_id += 1
    product = (product_id, {item: input(f'Enter the product {item}: ') for item in menu_items})
    goods.append(product)
    if input('Do you want to add another product? (yes/no) ') == 'yes':
        continue
    else:
        break

results = {}

for _, i in goods:
    for key in i.keys():
        if key in results.keys():
            if i[key] in results[key]:
                continue
            else:
                results[key].append(i[key])
        else:
            results[key] = [i[key]]


for key, val in results.items():
    print(key, ':', val)