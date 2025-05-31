"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. Решите используя sys.argv и argparse
"""

import sys

def calculate_salary(hours, rate, bonus):
    """
    Возвращает зарплату по формуле:
    (выработка в часах * ставка в час) + премия
    """
    return hours * rate + bonus

def print_usage_and_exit():
    print("Использование:")
    print("  python salary_sysargv.py <выработка_в_часах> <ставка_в_час> <премия>")
    print("Пример:")
    print("  python salary_sysargv.py 160 500 20000")
    sys.exit(1)

def main():
    # Ожидаем ровно три аргумента: часы, ставка, премия
    if len(sys.argv) != 4:
        print("Ошибка: неверное количество аргументов.")
        print_usage_and_exit()

    try:
        # sys.argv[1], sys.argv[2], sys.argv[3] — это строки из командной строки
        hours = float(sys.argv[1])
        rate = float(sys.argv[2])
        bonus = float(sys.argv[3])
    except ValueError:
        print("Пожалуйста, вводите только числовые значения для часов, ставки и премии.")
        print_usage_and_exit()

    salary = calculate_salary(hours, rate, bonus)
    print(f"Зарплата сотрудника: {salary}")

if __name__ == "__main__":
    main()