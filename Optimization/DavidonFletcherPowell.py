# Davidon-Fletcher-Powell

import numpy as np
import sympy as sp
from sympy import diff, symbols, sqrt


def derivative(func, x):
    """Поиск производной в точке"""
    x1, x2 = symbols('x1 x2')
    return diff(func(x1, x2), x1).subs({x1: x[0], x2: x[1]}), diff(func(x1, x2), x2).subs({x1: x[0], x2: x[1]})


def norm(x):
    """Нормирование точки"""
    return sqrt(x[0] ** 2 + x[1] ** 2)


def dfp(f, x0=np.array([0.0, 0.0], float), err1=0.1, err2=0.15, M=10):
    """Метод Дэвидона-Флетчера-Пауэлла"""
    k = 0
    A = np.eye(2)
    xp = x0
    At = A
    while True:
        print(f"k = {k}")
        grad = np.array(derivative(f, xp), float)
        if norm(grad) < err1:
            print("Minimum is found:")
            print(f"x = {xt.round(5)}")
            print("f(x) = ", end='')
            print(round(f(*xt), 5))
            break
        else:
            if k == 0:
                pass
            elif k >= M:
                print("Minimum is found:")
                print(f"x = {xt.round(5)}")
                print("f(x) = ", end='')
                print(f(*xt))
                break
            else:
                deltagrad = np.array([[(grad - np.array(derivative(f, xpp)))[0]], [(grad - np.array(derivative(f, xpp)))[1]]], float)
                deltax = np.array([[(xp - xpp)[0]], [(xp - xpp)[1]]], float)

                Ac = deltax @ deltax.T / (deltax.T @ deltagrad) - (A @ deltagrad @ deltagrad.T @ A) / (deltagrad.T @ A @ deltagrad)
                At = A + Ac

            d = -At @ grad
            t = symbols('t')
            f_aug = f(*(xp + t * d))
            t = sp.solve(sp.Eq(diff(f_aug, t), 0))[0]
            xt = xp + t * d
            xt = np.array(xt, float)
            print(f"grad_f = {grad.round(5)}\tt = {round(t, 5)}\td = {d.round(5)}\tx = {xt.round(5)}")

            if norm(xt - xp) < err2 and abs(f(*xt) - f(*xp)) < err2:
                print("Minimum is found:")
                print(f"x = {xt.round(5)}")
                print("f(x) = ", end='')
                print(f(*xt))
                break
            else:
                k += 1
        xpp = xp
        xp = xt
        print()

    return xt


def main():
    function = lambda x1, x2: 2 * x1 ** 2 + x1 * x2 + x2 ** 2  # Функция
    dfp(function, np.array([0.5, 1.0], float))


if __name__ == '__main__':
    main()
