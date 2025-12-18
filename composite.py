import numpy as np


def f(x):
    return 1 / (1 + x ** 2)


def composite_trapezoidal(a, b, tol):
    n = 1
    h = (b - a)
    T1 = (h / 2) * (f(a) + f(b))
    T2 = T1

    while True:
        h /= 2
        n *= 2
        x = np.linspace(a, b, n + 1)
        y = f(x)

        T2 = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
        if abs(T2 - T1) < tol:
            break
        T1 = T2

    return T2


# 积分区间和容忍度
a, b = -4, 4
tol = 1e-6

# 计算积分
result = composite_trapezoidal(a, b, tol)
print(f"积分近似为: {result:.6e}")