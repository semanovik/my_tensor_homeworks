n = int(input())
factorial = 1
for i in range(-(n-1), 0, 2):
    factorial = factorial+(factorial * (-i))
print(factorial)
