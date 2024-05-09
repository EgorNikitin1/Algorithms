# Barrier
from Optimization.DavidonFletcherPowell import dfp

import numpy as np
import sympy as sp
from sympy import symbols, diff


def derivative(func1, func2):
    x, r = symbols('x r')
    return diff(func1(x), x) + diff(func2(x, r), x)


# F = lambda x, r: x ** 2 - 4 * x - r * sp.ln(1 - x)
# F = lambda x1, x2, r: (x1 - 4) ** 2 + (x2 - 4) ** 2 - r * sp.ln(5 - x1 - x2)
# F = lambda x1, x2, r: x1 ** 2 + x2 ** 2 + 6 * x1 - 2 * x2 - r * sp.ln(1 - x1 ** 2 - x2 ** 2)

F = lambda x1, x2: -2 * x1 - 4 * x2 + x1 ** 2 + x2 ** 2 - r * sp.ln(1 - x1 - x2)

x0 = np.array([1, 0.5])
err = 0.01
C = 10
r = 1
k = 0
x = x0
while True:
    print(f"Barrier k = {k}")
    print()
    xt = dfp(F, x)

    if xt[0] + xt[1] <= 1:
        print(f"F(x) = {F(*xt)}")
        f = -2 * xt[0] - 4 * xt[1] + xt[0] ** 2 + xt[1] ** 2
        print(f"f(x) = {f}")

        P = - r * sp.ln(1 - xt[0] - xt[1])
        print(f"P(x) = {abs(P)}")
        if abs(P) <= err:
            print(f"x = {x}")
            break
    r = r / C
    x = xt
    k += 1
    print(f"x = {x}")
    print()
