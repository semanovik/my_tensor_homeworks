# В строке удалить все буквы "а" и подсчитать количество удаленных символов

text_with_a = input('Из введенного сюда текста будут удалены все буквы "а": ')
text_without_a = text_with_a.replace("а", "")
print(len(text_with_a) - len(text_without_a))
