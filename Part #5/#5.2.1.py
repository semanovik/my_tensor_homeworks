# Первая версия, где подсчитываются только файлы в каталоге

import os

path = r'C:\\Users\\su.novikov\\AppData\\Local\\Programs\\Python\\Python39\\'
os.chdir(path)

folders = 0
python_files = 0
exe_files = 0
files_amount = 0

for i in range(len(os.listdir())):
    if os.path.isdir(path + os.listdir()[i]):
        folders += 1

    if os.path.isfile(path + os.listdir()[i]):
        files_amount += 1
        if '.exe' in os.path.splitext(os.listdir()[i]):
            exe_files += 1
        if '.py' in os.path.splitext(os.listdir()[i]):
            python_files += 1


file = open(r'C:\Users\su.novikov\Desktop\Homework.txt', 'w', encoding='utf-8')
file.write(f'Папок: {folders}, Python-файлов: {python_files}, ехе-файлов: {exe_files}, всего файлов: {files_amount}')
file.close()