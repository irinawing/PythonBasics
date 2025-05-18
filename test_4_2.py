"""
Задача 2.

Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

counts = {}
res = []

for sym in input().split():
    # добавляем суффикс только если символ уже был
    res.append(sym if sym not in counts else f"{sym}_{counts[sym]}")
    counts[sym] = counts.get(sym, 0) + 1

print(*res)