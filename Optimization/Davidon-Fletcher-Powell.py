# Davidon-Fletcher-Powell

import numpy as np
import sympy as sp
from sympy import diff, symbols, sqrt


def derivative(func, x):
    x1, x2 = symbols('x1 x2')
    return diff(func(x1, x2), x1).subs({x1: x[0], x2: x[1]}), diff(func(x1, x2), x2).subs({x1: x[0], x2: x[1]})


def norm(x):
    return sqrt(x[0] ** 2 + x[1] ** 2)


def dfp(f, x0=np.array([0, 0]), err1=0.1, err2=0.15, M=10):

    k = 0
    A = np.eye(2)
    xp = x0
    At = A
    while True:
        print(f"k = {k}")
        grad = np.array(derivative(f, xp))
        print(f"Gradient = {grad}")
        if norm(grad) < err1:
            print(f"xt = {xt}")
            break
        else:
            if k == 0:
                pass
            elif k >= M:
                print(f"xt = {xt}")
                break
            else:
                deltagrad = np.array([[(grad - np.array(derivative(f, xpp)))[0]], [(grad - np.array(derivative(f, xpp)))[1]]])
                deltax = np.array([[(xp - xpp)[0]], [(xp - xpp)[1]]])

                Ac = deltax @ deltax.T / (deltax.T @ deltagrad) - (A @ deltagrad @ deltagrad.T @ A) / (deltagrad.T @ A @ deltagrad)
                At = A + Ac

            d = -At @ grad
            t = symbols('t')
            f_aug = f(*(xp + t * d))
            t = sp.solve(sp.Eq(diff(f_aug, t), 0))[0]
            print(f"t = {t}")
            xt = xp + t * d
            print(f"xt = {xt}")

            if norm(xt - xp) < err2 and abs(f(*xt) - f(*xp)) < err2:
                break
            else:
                k += 1
        xpp = xp
        xp = xt
        print()

    return xt


def main():
    function = lambda x1, x2: 2 * x1 ** 2 + x1 * x2 + x2 ** 2
    dfp(function, np.array([0.5, 1]))


if __name__ == '__main__':
    main()
