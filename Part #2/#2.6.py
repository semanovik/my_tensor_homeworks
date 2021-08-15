list = [i for i in range(0, 6)]
summ = 0
mult = 1

for i in range(list.count(0)):  # Удаляем возможные нули в списке
    list.remove(0)

for i in list:
    summ += i
    mult = mult * i

print(f'Сумма чисел списка = {summ}, Произведение чисел списка = {mult}')