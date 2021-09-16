n = [i for i in range(1000000)]     # делаем список от 0 до 999999
counter = 0

for i in range(len(n)):             # добавляем к каждому нешестизначному числу в списке нули в начале
    if len(str(n[i])) == 1:         # таким образом получили список от 000000 до 999999
        n[i] = '00000'+str(n[i])
    if len(str(n[i])) == 2:
        n[i] = '0000'+str(n[i])
    if len(str(n[i])) == 3:
        n[i] = '000'+str(n[i])
    if len(str(n[i])) == 4:
        n[i] = '00'+str(n[i])
    if len(str(n[i])) == 5:
        n[i] = '0'+str(n[i])


for f in n:                         # считаем кол-во счастливых в списке
    sum1 = int(str(f)[0]) + int(str(f)[1]) + int(str(f)[2])
    sum2 = int(str(f)[3]) + int(str(f)[4]) + int(str(f)[5])
    if sum1 == sum2:
        counter += 1

print(counter)




