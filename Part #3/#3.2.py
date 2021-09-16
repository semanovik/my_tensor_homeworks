def palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    counter = 0
    for i in range(len(reversed_number)):
        if reversed_number[i] == number[i]:
            counter += 0
        else:
            counter += 1

    if counter == 0:
        print("Число палиндром")
    else:
        print("Число не палиндром")


palindrome(input("Введите число:"))
