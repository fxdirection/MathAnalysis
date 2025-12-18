import math


# 定义函数和它的导数
def f(x):
    return math.exp(-x)


def df(x):
    return -math.exp(-x)


# 牛顿迭代法
def newton_method(x0, epsilon=1e-6, max_iterations=1000):
    x_n = x0
    for i in range(max_iterations):
        # 检查分母是否接近零
        if abs(1 + df(x_n)) < 1e-10:
            print("Warning: Denominator is close to zero, which may cause instability.")
            break

        try:
            x_n1 = x_n - (x_n - f(x_n)) / (1 + df(x_n))
        except OverflowError:
            print("Overflow error encountered.")
            break

        if abs(x_n1 - x_n) < epsilon:
            return x_n1, i + 1
        x_n = x_n1
    return None, max_iterations


# 初始值
x0 = 0.5

# 执行牛顿迭代法
newton_result, newton_iterations = newton_method(x0)
if newton_result is not None:
    print(f"Newton's Method Result: {newton_result} after {newton_iterations} iterations")
else:
    print("Newton's method did not converge.")