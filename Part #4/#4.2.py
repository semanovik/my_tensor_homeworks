import datetime
import time

time_to_wait = int(input('Введите продолжительность выполнения функции: '))


def decorate(funct):
    def wrapper(*args):
        time_before = datetime.datetime.now()
        print(f'Получена функция, время старта: {time_before}')
        funct(*args)
        time_after = datetime.datetime.now()
        print(f'Функция выполнена за {(time_after - time_before)}')

    return wrapper


@decorate
def some_func(time_to_wait):
    print('Set')
    time.sleep(time_to_wait)
    print('End')


some_func(time_to_wait)
