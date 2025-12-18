import math

# 定义函数和它的导数
def f(x):
    return math.exp(-x) - x

def df(x):
    return -math.exp(-x) - 1

# 牛顿迭代法
def newton_method(x0, tolerance=1e-6, max_iterations=100):
    x_n = x0
    iteration = 0
    while iteration < max_iterations:
        x_n1 = x_n - f(x_n) / df(x_n)
        if abs(x_n1 - x_n) < tolerance:
            return x_n1, iteration + 1
        x_n = x_n1
        iteration += 1
    raise ValueError("未能在最大迭代次数内收敛")

# 初始值
x0 = 0.5

# 执行牛顿迭代法
root, iterations = newton_method(x0)
print(f"方程 x = e^(-x) 的根大约是: {root}")
print(f"迭代次数: {iterations}")