# Дана строка, содержащая полное имя файла
# Выделите из этой строки имя файла без расширения

link_input = input()
last_slash = link_input[::-1].find('\\')
end_of_name = link_input[::-1].find('.')
print(link_input[-last_slash:-(end_of_name+1)])
