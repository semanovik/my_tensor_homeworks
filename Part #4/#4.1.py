import datetime

user_date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
delta_months = int(input('Введите количество месяцев: '))


def change_month(date, months):
    # Разбиваем принятую дату на эл-ты
    year = int(date.split('.')[2])
    month = int(date.split('.')[1])
    day = int(date.split('.')[0])

    current_date = datetime.date(year, month, day)
    final_date = current_date

    # Цикл добавляет по дню до тех пор, пока не встречает тот же день месяца
    # Это означает, что циклом был пройден 1 месяц
    if months > 0:
        for i in range(0, months):
            while True:
                final_date = final_date + datetime.timedelta(days=+1)
                if final_date.day == current_date.day:
                    break

    # Аналогичный при вычитании
    else:
        for i in range(abs(months)):
            while True:
                final_date = final_date - datetime.timedelta(days=1)
                if final_date.day == current_date.day:
                    break

    return print(final_date.strftime('%d.%m.%Y'))


change_month(user_date, delta_months)
