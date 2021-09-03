"""5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

revenue = int(input('Enter company revenue'))
costs = int(input('Enter company costs'))

if revenue > costs:
    print('The company is profitable')
else:
    print('The company is unprofitable')

print('Profitability indicator: ', round(revenue / costs, 2), 'units')

employees = int(input('Enter amount of company employees'))
print('Profit per employee: ', round(revenue / employees, 2), 'currency')