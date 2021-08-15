list = [i for i in range(1,101)]

for i in list:
    for n in range(1, i+1):
        numbers = [f for f in range(5,n,5)]
        print(f'{n} - {numbers}')