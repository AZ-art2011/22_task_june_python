''' Задача 22: '''

digit_1 = int(input('Укажите количество элементов в первом наборе '))
digit_2 = int(input('Укажите количество элементов во втором наборе '))

set_1 = []
set_2 = []

print('')
print('Вводите элементы по одному, завершая ввод нажатием Enter')

for i in range(digit_1):
    print(f'Осталось ввести {digit_1 - i} чисел для 1-го набора')
    set_1.append(int(input('Введите число ')))
    
print('')
print('Теперь введите элементы второго набора')
    
for i in range(digit_2):
    print(f'Осталось ввести {digit_2 - i} чисел для 2-го набора')
    set_2.append(int(input('Введите число ')))

print('')
set_1 = set(set_1)
set_2 = set(set_2)
all_set = set_1 & set_2
print(f'Элементы, которые встречаются в обоих наборах: {sorted(list(all_set))}')