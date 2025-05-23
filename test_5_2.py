"""
Задание 2

values = [True, False, True, None, True]

result = []
for v in values:
    if v is True:
        result.append('yes')
    else:
        if v is False:
            result.append('no')
        else:
            result.append('unknown')

print(result)

Перепишите приведенный код на list comrehension
"""

values = [True, False, True, None, True]

result = ['yes' if v is True else 'no' if v is False else 'unknown' for v in values]

print(result)