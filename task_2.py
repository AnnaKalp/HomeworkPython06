"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
from sys import argv
from task_1 import is_valid_date

date_str = argv[1]
print(is_valid_date(date_str))


