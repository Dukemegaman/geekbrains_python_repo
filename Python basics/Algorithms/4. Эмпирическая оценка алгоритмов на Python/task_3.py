"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
"""
revers_1 - является рекурсивной функцией и время её выполнения зависит от количества вводимых цифр.
Самая долговыполняемая функция
revers_2 - выполняется через цикл, поэтому выполняется быстрее чем revers_1
revers_3 - обращается напрямую к индексу списка и количество итераций в ней самое маленькое.
Самая быстровыполняемая функция.
revers_4 - выполняется быстрее revers_1, но всё равно медленее revers_3 из-за сложности встроенной функции reversed
"""


from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = int("".join(reversed(str(enter_num))))
    return revers_num


def main():
    user_numb = 321
    revers_1(user_numb)
    revers_2(user_numb)
    revers_3(user_numb)
    revers_4(user_numb)


run('main()')

user_num = 321
print(timeit('revers_1(user_num)', globals=globals()))
print(timeit('revers_2(user_num)', globals=globals()))
print(timeit('revers_3(user_num)', globals=globals()))
print(timeit('revers_4(user_num)', globals=globals()))
