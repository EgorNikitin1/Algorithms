# Rosenbrock method
from math import sqrt


def rosenbrock(f, x0, err, delta0, _alpha=3, _beta=-0.5, d=((1, 0), (0, 1)), _lambda=(1, 1), N=3):
    """Метод Розенброка"""
    yt = x0  # Шаг 1
    xp = x0
    while True:
        l = 0
        delta = tuple(delta0)
        delta_update = [0.0, 0.0]
        while True:
            print(f"k")
            yp = yt
            for i in range(2):  # Шаг 2
                fun_aug = f(yt[0] + delta[i] * d[i][0], yt[1] + delta[i] * d[i][1])
                fun = f(*yt)
                print(f"fun_aug = {fun_aug}")
                print(f"fun = {fun}")
                if fun_aug < fun:  # Шаг удачен
                    yt = yt[0] + delta[i] * d[i][0], yt[1] + delta[i] * d[i][1]
                    print(f"yt = {yt}")
                    delta_update[i] = _alpha * delta[i]
                    print(f"delta{i + 1} = {delta_update[i]}")
                else:  # Шаг неудачен
                    yt = yt
                    print(f"yt = {yt}")
                    delta_update[i] = _beta * delta[i]
                    print(f"delta{i + 1} = {delta_update[i]}")
                print()

            if f(*yt) < f(*yp):  # Шаг 3
                yt = yt
                l = 0
            elif f(*yt) == f(*yp):
                l += 1
                if f(*yt) < f(*xp):
                    break
                elif f(*yt) == f(*xp):
                    if l < N:
                        if abs(delta[0]) > err and abs(delta[1]) > err:
                            yt = yt
                    else:
                        break
            delta = tuple(delta_update)

        xt = yt  # Шаг 4
        if sqrt((xt[0] - xp[0]) ** 2 + (xt[1] - xp[1]) ** 2) > err:
            diff = xt[0] - xp[0], xt[1] - xp[1]
            _lambda = (diff[1] * d[1][0] - diff[0] * d[1][1]) / (d[0][1] * d[1][0] - d[0][0] * d[1][1]), (
                        diff[1] * d[0][0] - diff[0] * d[0][1]) / (d[0][0] * d[1][1] - d[0][1] * d[1][0])
            a = (_lambda[0] * d[0][0] + _lambda[1] * d[1][0], _lambda[0] * d[0][1] + _lambda[1] * d[1][1]), (
            _lambda[1] * d[1][0], _lambda[1] * d[1][1])
            d = a[0][0] / sqrt(a[0][0] ** 2 + a[0][1] ** 2), a[0][1] / sqrt(a[0][0] ** 2 + a[0][1] ** 2)
            temp = a[1][0] * d[0] + a[1][1] * d[1]
            b = a[0], (a[1][0] - temp * d[0], a[1][1] - temp * d[1])
            d = d, (b[1][0] / sqrt(b[1][0] ** 2 + b[1][1] ** 2), b[1][1] / sqrt(b[1][0] ** 2 + b[1][1] ** 2))
            xp = xt
        else:
            print(xt)
            print(f(*xt))
            break
    return xt


def main():
    function = lambda x1, x2: 2 * x1 ** 2 + x1 * x2 + x2 ** 2  # Функция
    rosenbrock(function, (0.5, 1), 0.075, [0.1, 0.1])


if __name__ == '__main__':
    main()
