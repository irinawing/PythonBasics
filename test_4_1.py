"""
Задание 1

Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells
Output: 13
"""

import sys
import string

# Считаем весь ввод и сразу приведём к нижнему регистру
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# Разбиваем по любым пробельным символам
words = text.split()

# Убираем пунктуацию по краям и приводим к одному регистру
cleaned = [w.strip(string.punctuation).lower() for w in words]

# Отфильтровываем пустые строки
cleaned = [w for w in cleaned if w]

# Считаем количество уникальных слов
unique_words = set(cleaned)

print(unique_words)
print(len(unique_words))