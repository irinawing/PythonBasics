"""
Задание 3.
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику

Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")

Вывод:
same
"""

def same_by(characteristic, objects):
    """
    Проверяет, имеют ли все объекты в последовательности одинаковое значение характеристики.
    Если последовательность пуста, возвращает True.
    """
    if not objects:
        return True
    first_val = characteristic(objects[0])
    return all(characteristic(obj) == first_val for obj in objects)

# Пример использования
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")