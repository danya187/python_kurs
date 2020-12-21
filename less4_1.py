from sys import argv

name, time, salary, bonus = argv
try:
    res = float(time) * float(salary) + float(bonus)
    print(f'заработная плата сотрудника  {res}')
except ValueError as e:
    print("Ошибка ввода")
    print(e)
