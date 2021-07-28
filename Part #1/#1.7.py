# Посчитать количество слов в строке

text = input('Введите предложение: ').strip('!?.')
print(len(text) - len(text.replace(' ', '')) + 1)
