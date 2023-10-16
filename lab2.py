from math import factorial
import math
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np


def show_table_1(lmbd, st, rho, L, Lq, W, Wq, B, p0, q0, title):
    data_list = np.column_stack((lmbd, st, rho, L, Lq, W, Wq, B, p0, q0))
    ax = plt.subplot()
    columns = ['lambda', 'st', 'rho', 'L', 'Lq', 'W', 'Wq', 'B', 'p0', 'q0']
    the_table = ax.table(cellText=data_list, colLabels=columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    ax.axis("off")
    plt.title(title)
    plt.show()


def show_table_2(lmbd, st, rho, L, Lq, W, Wq, B, p0, q0, indices, title):
    lmbd_ = itemgetter(*indices)(lmbd)
    st_ = itemgetter(*indices)(st)
    rho_ = itemgetter(*indices)(rho)
    L_ = itemgetter(*indices)(L)
    Lq_ = itemgetter(*indices)(Lq)
    W_ = itemgetter(*indices)(W)
    Wq_ = itemgetter(*indices)(Wq)
    B_ = itemgetter(*indices)(B)
    p0_ = itemgetter(*indices)(p0)
    q0_ = itemgetter(*indices)(q0)

    data_list = np.column_stack((lmbd_, st_, rho_, L_, Lq_, W_, Wq_, B_, p0_, q0_))

    ax = plt.subplot()
    columns = ['lambda', 'st', 'rho', 'L', 'Lq', 'W', 'Wq', 'B', 'p0', 'q0']
    the_table = ax.table(cellText=data_list, colLabels=columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    ax.axis("off")
    plt.title(title)
    plt.show()


def show_plot(rho_, L_, Lq_, W_, Wq_, B_, p0_, title):
    data_list = [rho_, L_, Lq_, W_, Wq_, B_, p0_]
    columns = ['rho', 'L', 'Lq', 'W', 'Wq', 'B', 'p0']
    plt.bar(columns, data_list)
    plt.title(title)
    plt.show()


def main():
    n = 3
    lmbd = [0.1, 0.1, 0.1, 0.2, 0.5, 0.9, 2, 5, 9]  # середня інтенсивність вхідного потоку викликів
    st = [2, 5, 9, 1, 1, 1, 0.1, 0.1, 0.1]  # середній час між успішними надходженнями викликів
    iat = [round(1 / lm, n) for lm in lmbd]  # середній час обслуговування
    rho = [round(lm * s, n) for lm, s in zip(lmbd, st)]  # очікуване навантаження каналу обслуговування
    L = [round(r / (1 - r), n) for r in rho]  # середня кількість викликів у системі
    Lq = [round(l - r, n) for l, r in zip(L, rho)]  # середня кількість викликів у черзі
    W = [round(l / lm, n) for l, lm in zip(L, lmbd)]  # середній час перебування у системі
    Wq = [round(w - s, n) for w, s in zip(W, st)]  # середній час очікування(у черзі)
    B = [round(1 / (1 / s - lm), n) for s, lm in zip(st, lmbd)]  # середня тривалість періоду зайнятості системи
    c = 1
    s = [s_ for s_ in range(len(lmbd))]
    p0 = [round((1 + ((c * r) ** c / factorial(c)) * (1 / (1 - r))) ** -1, n) for r, s_ in zip(rho, s)]
    q0 = [round(1 - p, n) for p in p0]
    show_table_1(lmbd, st, rho, L, Lq, W, Wq, B, p0, q0, 'Таблиця 1')
    indices = [i for i, x in enumerate(rho) if x == 0.9]
    show_table_2(lmbd, st, rho, L, Lq, W, Wq, B, p0, q0, indices, 'Таблиця 2.\nФільтр rho = 0.9')
    for i, indx in enumerate(indices):
        show_plot(rho[indx], L[indx], Lq[indx], W[indx], Wq[indx], B[indx], p0[indx],
                  f'Графік {i + 1}.\nLambda = {lmbd[indx]}, St = {st[indx]}')


main()
