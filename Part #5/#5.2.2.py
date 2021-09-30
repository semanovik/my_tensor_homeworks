# Вторя версия. Тут считается не только то, что содержится в каталоге, но и в подкаталогах

import os

path = r'C:\\Users\\su.novikov\\AppData\\Local\\Programs\\Python\\Python39\\'
os.chdir(path)

folders = 0
python_files = 0
exe_files = 0
files_amount = 0

for way, dirs, files in os.walk(path):
    for dire in dirs:
        folders += 1

    for file in files:
        files_amount += 1
        if '.exe' in os.path.splitext(file):
            exe_files += 1
        if '.py' in os.path.splitext(file):
            python_files += 1


file = open(r'C:\Users\su.novikov\Desktop\Homework.txt', 'w', encoding='utf-8')
file.write(f'Папок: {folders}, Python-файлов: {python_files}, ехе-файлов: {exe_files}, всего файлов: {files_amount}')
file.close()