import random
import math
import matplotlib.pyplot as plt
import numpy as np


def show_table_1(r, z, t, title):
    ri = r[:10] + ['...'] + r[len(r) - 3:]
    zi = z[:10] + ['...'] + z[len(z) - 3:]
    ti = t[:10] + ['...'] + t[len(t) - 3:]
    data_list = np.column_stack((ri, zi, ti))
    ax = plt.subplot()
    columns = ['ri', 'zi', 'ti']
    the_table = ax.table(cellText=data_list, colLabels=columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    ax.axis("off")
    plt.title(title)
    plt.show()


def show_table_2(intervals, xj, title):
    intervals_i = intervals[:10] + ['...'] + intervals[len(intervals) - 3:]
    xj_i = xj[:10] + ['...'] + xj[len(xj) - 3:]
    data_list = np.row_stack((intervals_i, xj_i))
    row_label = ['№ інтервалу', 'xj(т)']
    ax = plt.subplot()
    the_table = ax.table(cellText=data_list, rowLabels=row_label, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    plt.title(title)
    ax.axis("off")
    plt.show()


def show_table_3(nj, nk, title):
    data_list = np.row_stack((nj, nk))
    row_label = ['Кількість викликів', 'nk']
    ax = plt.subplot()
    the_table = ax.table(cellText=data_list, rowLabels=row_label, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    plt.title(title)
    ax.axis("off")
    plt.show()


def show_table_4(nj, Pit, Pit_, title):
    data_list = np.row_stack((nj, Pit, Pit_))
    row_label = ['Кількість викликів', 'Pi(t)', '_Pi(t)']
    ax = plt.subplot()
    the_table = ax.table(cellText=data_list, rowLabels=row_label, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    plt.title(title)
    ax.axis("off")
    plt.show()


def show_table_5(intervals, xj1, xj2, title):
    intervals_i = intervals[:10] + ['...'] + intervals[len(intervals) - 3:]
    xj2 += [0] * (len(xj1) - len(xj2))
    xj_i_1 = xj1[:10] + ['...'] + xj1[len(xj1) - 3:]
    xj_i_2 = xj2[:10] + ['...'] + xj2[len(xj2) - 3:]
    xj = [sum(x) for x in zip(xj1, xj2)]
    a = list(zip(xj1, xj2))
    xj_i = xj[:10] + ['...'] + xj[len(xj) - 3:]
    data_list = np.row_stack((intervals_i, xj_i_1, xj_i_2, xj_i))
    row_label = ['№ інтервалу', 'x1(т)', 'x2(т)', 'x1 + x2']
    ax = plt.subplot()
    the_table = ax.table(cellText=data_list, rowLabels=row_label, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    plt.title(title)
    ax.axis("off")
    plt.show()


def Pit_plot(nj, Pit, Pit_, title):
    plt.plot(nj, Pit, label="Pi(t)")
    plt.plot(nj, Pit_, label="P_i(t)")
    plt.legend()
    plt.title(title)
    plt.show()


def sum_plot(intervals, xj1, xj2, title):
    xj = [sum(x) for x in zip(xj1, xj2)]
    xj2 += [0] * (len(xj1) - len(xj2))
    plt.plot(intervals, xj1, label="f1 x1(n)")
    plt.plot(intervals, xj2, label="f2 x2(n)")
    plt.plot(intervals, xj, label="f x(n)")
    plt.legend()
    plt.title(title)
    plt.show()


def split_on_intervals(intervals, t):
    x = [[]]
    ni = 0
    for j in range(len(t)):
        if ni < len(intervals) - 1:
            if intervals[ni] < t[j] < intervals[ni + 1]:
                x[ni].append(t[j])
            else:
                x.append([])
                ni += 1
        else:
            x[ni].append(t[j])
    return x


def show_plot():
    N = 2  # номер за журналом
    T_min = 0
    r = [round(random.uniform(0, 1), 4) for i in
         range(1, 1000)]  # випадкові рівномірно розподілені числа від 0 до 1
    lmbd1 = (10 * (N + 1)) / (N + 4)  # інтенсивність викликів 1
    lmbd2 = (15 * (N + 1)) / (N + 4)  # інтенсивність викликів 2
    print(f'Лямбда 1 = {lmbd1}\nЛямбда 2 = {lmbd2}\n')
    z1 = [round(-1 / lmbd1 * math.log(r[i]), 4) for i in range(len(r))]  # інтервали між викликами 1
    z2 = [round(-1 / lmbd2 * math.log(r[i]), 4) for i in range(len(r))]  # інтервали між викликами 2
    t1 = [round(T_min + sum(z1[:k]), 4) for k in range(1, 1000)]  # послідовність моментів надходження викликів 1
    t2 = [round(T_min + sum(z2[:k]), 4) for k in range(1, 1000)]  # послідовність моментів надходження викликів 2
    show_table_1(r, z1, t1, 'Таблиця 1.1 для першого потоку')  # таблиця 1
    show_table_1(r, z2, t2, 'Таблиця 1.2 для другого потоку')  # таблиця 1
    T_max = int(max(t1))
    print(f'Кількість інтервалів: {T_max}\n')
    intervals = [i for i in range(T_min, T_max)]
    x1 = split_on_intervals(intervals, t1)  # список інтервалів 1
    x2 = split_on_intervals(intervals, t2)  # список інтервалів 2
    xj1 = [len(x1[j]) for j in
           range(len(x1))]  # кількість викликів, що потрапили у проміжок часу довжиною t = 1 хв.
    xj2 = [len(x2[j]) for j in range(len(x2))]
    show_table_2(intervals, xj1, 'Таблиця 2.1 для першого потоку')  # таблиця 2
    show_table_2(intervals, xj2, 'Таблиця 2.2 для другого потоку')  # таблиця 2
    nj1 = list(set(xj1))  # Кількість викликів
    nj2 = list(set(xj2))
    nk1 = [xj1.count(x) for x in set(xj1)]  # кількість інтервалів, у які потрапили k викликів.
    nk2 = [xj2.count(x) for x in set(xj2)]
    show_table_3(nj1, nk1, 'Таблиця 3.1 для першого потоку')  # таблиця 3
    show_table_3(nj2, nk2, 'Таблиця 3.2 для другого потоку')  # таблиця 3
    lmbd_1 = 1 / (1 / 1000 * (sum(z1)))  # модельне значення параметра потоку
    lmbd_2 = 1 / (1 / 1000 * (sum(z2)))
    print(f'Модельне лямбда 1 = {lmbd_1}\nМодельне лямбда 2 = {lmbd_2}\n')
    Pit1 = [round((lmbd1 ** i / math.factorial(i) * math.e ** (-lmbd1)), 3) for i in range(len(nk1))]
    Pit2 = [round((lmbd2 ** i / math.factorial(i) * math.e ** (-lmbd2)), 3) for i in range(len(nk2))]
    Pit_1 = [round(n / sum(nk1), 3) for n in nk1]  # ймовірність надходження i викликів за час t
    Pit_2 = [round(n / sum(nk2), 3) for n in nk2]
    show_table_4(nj1, Pit1, Pit_1, 'Таблиця 4.1 для першого потоку')  # таблиця 4
    show_table_4(nj2, Pit2, Pit_2, 'Таблиця 4.2 для другого потоку')  # таблиця 4
    Pit_plot(nj1, Pit1, Pit_1, 'Графік 1.1 для першого потоку')  # графік
    Pit_plot(nj2, Pit2, Pit_2, 'Графік 1.2 для другого потоку')  # графік
    show_table_5(intervals, xj1, xj2, 'Таблиця 5 для сумарного потоку')
    sum_plot(intervals, xj1, xj2, 'Графік 2 для сумарного потоку')
    lmbd12 = lmbd1 + lmbd2
    lmbd_12 = lmbd_1 + lmbd_2
    print(f'Сума модельних лямбда = {lmbd_12}\nЛямбда1 + лямбда 2 = {lmbd12}')


def main():
    show_plot()


main()
