"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count, cycle

n = int(input("Введите целое число:"))

for i in count(n):
    print(i)

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in cycle(new_list):
    print(i)