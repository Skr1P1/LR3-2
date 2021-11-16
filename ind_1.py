#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ввести список А из 10 элементов. Определить количество элементов, кратных 3 и индексы
#последнего такого элемента.

if __name__ == '__main__':
    u = tuple(map(int, input('Введите 10 чисел -->').split(maxsplit=10)))
    s = 0
    for i in u:
        if i % 3 == 0 and i != 0:
            s += 1
            print('Индексы кратных 3 =', i)
    print(s)
