"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

new_list = []
original_list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(original_list)):
    if original_list[i] > original_list[i-1]:
        (new_list.append(original_list[i]))

print("Исходный список: ", original_list)
print("Список, элементы которого больше предыдущего: ", new_list)