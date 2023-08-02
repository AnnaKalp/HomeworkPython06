"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
    except ValueError:
        return False

    if year < 1 or year > 9999:
        return False

    if month < 1 or month > 12:
        return False

    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True


print(is_valid_date("29.02.2024"))
print(is_valid_date('29.02.2023'))
print(is_valid_date('29.02.2020'))
print(is_valid_date('32.03.2020'))
