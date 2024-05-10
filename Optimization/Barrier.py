# Barrier
from Optimization.DavidonFletcherPowell import dfp

import numpy as np
import sympy as sp
from sympy import symbols, diff


def derivative(func1, func2):
    x, r = symbols('x r')
    return diff(func1(x), x) + diff(func2(x, r), x)


def barrier(x0=np.array([0.0, 0.0], float), err=0.01, C=10):
    F = lambda x1, x2: -2 * x1 - 4 * x2 + x1 ** 2 + x2 ** 2 - r * sp.ln(1 - x1 - x2)

    r = 1
    k = 0
    x = x0
    while True:
        print(f"Barrier k = {k}")
        xt = dfp(F, x)

        if xt[0] + xt[1] <= 1:
            f = -2 * xt[0] - 4 * xt[1] + xt[0] ** 2 + xt[1] ** 2
            P = - r * sp.ln(1 - xt[0] - xt[1])
            if abs(P) <= err:
                print("Minimum is found:")
                print(f"x = {xt.round(5)}")
                print(f"f(x) = {round(f, 5)}")
                break
        print(f"r = {r}\tx = {x.round(5)}\tF(x) = {round(F(*xt), 5)}\tP(x) = {round(abs(P), 5)}\tf(x) = {round(f, 5)}\t")
        r = r / C
        x = xt
        k += 1
        print()


def main():
    barrier(np.array([1.0, 0.5], float), 0.01)


if __name__ == '__main__':
    main()
