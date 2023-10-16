from math import factorial, fabs
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np


def show_table_1(lmbd, st, c, rho, r, p0, L, Lq, W, Wq, B, Wq_1, title):
    data_list = np.column_stack((lmbd, st, c, rho, r, p0, L, Lq, W, Wq, B, Wq_1))
    ax = plt.subplot()
    columns = ['lambda', 'st', 'c', 'rho', 'r', 'p0', 'L', 'Lq', 'W', 'Wq', 'B', '(1Wq(0))']
    the_table = ax.table(cellText=data_list, colLabels=columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    ax.axis("off")
    plt.title(title)
    plt.show()


def show_plot(L_, Lq_, W_, Wq_, B_, Wq_1_, title):
    data_list = [L_, Lq_, W_, Wq_, B_, Wq_1_]
    columns = ['L', 'Lq', 'W', 'Wq', 'B', '1-Wq']
    plt.bar(columns, data_list)
    plt.title(title)
    plt.show()


def main():
    n = 3
    lmbd = [4, 1, 0.3, 4, 3, 1, 190, 100, 20]  # середня інтенсивність вхідного потоку викликів
    st = [2, 5, 9, 1, 1, 1, 0.1, 0.1, 0.1]  # середній час між успішними надходженнями викликів
    c = [10, 10, 10, 5, 5, 5, 20, 20, 20]  # кількість каналів
    rho = [round(lm / (1 / c_ * s), n) for lm, c_, s in
           zip(lmbd, st, c)]  # очікуване навантаження каналу обслуговування
    r = [round(lm * s, n) for lm, s in zip(lmbd, st)]  # середня кількість викликів за середній час обслуговування
    s = [s_ for s_ in range(len(lmbd))]
    p0 = [round((c_ + ((c_ * rh) ** c_ / factorial(c_)) * (1 / (1 - rh))) ** -1, n) for rh, s_, c_ in
          zip(rho, s, c)]  # стаціонарні ймовірності s станів, у яких може знаходитися система
    Lq = [round(((r_ ** c_) * rh) / factorial(c_) * (1 / (1 - rh) ** 2) * p0_, n) for r_, c_, rh, p0_ in
          zip(r, c, rho, p0)]  # середня кількість викликів у черзі
    L = [round(Lq_ + r_, n) for Lq_, r_ in zip(Lq, r)]  # середня кількість викликів у системі
    W = [round(L_ / lm, n) for L_, lm in zip(L, lmbd)]  # середній час перебування у системі
    Wq = [round(W_ - st_, n) for W_, st_ in zip(W, st)]  # середній час очікування(у черзі)
    B = [round(st_ - (1 / lm), n) for st_, lm in zip(st, lmbd)]  # середня тривалість періоду зайнятості системи
    Wq_1 = [fabs(round(1 - wq, n)) for wq in Wq]
    show_table_1(lmbd, st, c, rho, r, p0, L, Lq, W, Wq, B, Wq_1, 'Таблиця 1')
    for i in range(len(W)):
        show_plot(L[i], Lq[i], W[i], Wq[i], B[i], Wq_1[i], f'Графік {i + 1}\nlambda={lmbd[i]}, st={st[i]}, c={c[i]}')


main()
