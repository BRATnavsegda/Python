import datetime


# Выбор формы существительного
def choose_plural(amount, variants):
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif (amount % 10 >= 2) and (amount % 10 <= 4) and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    return '{} {}'.format(amount, variants[variant])


def get_your_age(value):
    res = ''
    try:
        # Получаем список и преобразуем нужные данные от пользователя

        datetime_str = value[0] + ' ' + value[1]  # 'Введите дату и время дня рождения в формате ДД.ММ.ГГГГ ЧЧ:ММ\n-->'
        date_x = datetime.datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
        date_now = datetime.datetime.now().replace(second=0, microsecond=0)

        # Программа должна начать выполнять эту часть кода
        # только если дата рождения меньше текущей даты
        if date_x < date_now:
            delta = date_now - date_x
            # Получаем количество дней, часов и минут,
            # со дня рождения
            years = delta.days / 365
            # months = delta.days - (years * 365) -
            days = delta.days - years * 365
            hours = delta.seconds // 3600
            minutes = (delta.seconds - hours * 3600) // 60
            result = ''

            result = choose_plural(int(years), ('год ', 'года ', 'лет '))
            # Нужная строка формируется
            if days > 0:
                result += choose_plural(days, ('день', 'дня', 'дней'))
                if hours > 0:
                    result += ' и ' + choose_plural(hours, (' час', 'часа', 'часов'))
            elif hours > 0:
                result += choose_plural(hours, ('час', 'часа', 'часов'))
                if minutes > 0:
                    result += ' и ' + choose_plural(minutes, ('минута', 'минуты', 'минут'))
            else:
                result += choose_plural(minutes, ('минута', 'минуты', 'минут'))
            res = 'Сейчас вам ' + result
        else:
            res = 'Ошибка! \nУказанная вами дата из будущего...'
    except ValueError:
        # Если пользователь введет дату не по формату,
        # отработает этот обработчик исключения
        res = 'Ошибка! \nФормат ввода - ДД.ММ.ГГГГ ЧЧ:ММ'

    return res
