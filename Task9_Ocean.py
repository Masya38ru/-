import random
import time
import os
import numpy as np


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def update_cell(x, y):
    if field[x, y] == '*':
        return '*'
    if field[x, y] == '0':
        fish, shrimp = (0, 0)
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if field[i, j] == 'fish':
                    fish += 1
                elif field[i, j] == 'shrimp':
                    shrimp += 1
        if fish == 3:
            return 'fish'
        elif shrimp == 3:
            return 'shrimp'
        else:
            return '0'

    k = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) == (x, y):
                continue
            if field[i, j] == field[x, y]:
                k += 1
    if 2 <= k <= 3:
        return field[x, y]
    else:
        return '0'


def create_new_field():
    new_field = np.copy(field)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new_field[i, j] = update_cell(i, j)
    return new_field


def print_field():
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(items_to_print[items.index(field[i, j])], end=' ')
        print()


items = ['fish', 'shrimp', '0', '*']
items_to_print = ['><>', ' j ', '   ', '###']
n, m = map(int, input('Введите размеры поля N * M через пробел\n').split())
field = np.random.choice(items, size=(n + 2, m + 2))

# # уменьшение вероятности появления горы при генерации на 33% (раскомментить)
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if field[i, j] == '*':
#             field[i, j] = random.choice(items[:2]) if random.randint(0, 2) == 0 else '*'

field[0, ::] = '0'
field[n + 1, ::] = '0'
field[::, 0] = '0'
field[::, m + 1] = '0'
while True:
    clear()
    print_field()
    field = create_new_field()
    time.sleep(1.2)
