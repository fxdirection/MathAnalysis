import numpy as np


def f(x, y):
    return y - 2 * x / y


def exact_solution(x):
    return np.sqrt(1 + 2 * x)


def runge_kutta_4(f, x0, y0, h, N):
    x = np.zeros(N + 1)
    y = np.zeros(N + 1)
    x[0] = x0
    y[0] = y0

    for i in range(N):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)

        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x[i + 1] = x[i] + h

    return x, y


# 参数设置
x0 = 0
y0 = 1
x_end = 1
N_list = [5, 10, 20, 40, 80]

# 存储误差结果
errors = []

# 计算不同N值下的解和误差
for N in N_list:
    h = (x_end - x0) / N
    x, y = runge_kutta_4(f, x0, y0, h, N)
    y_exact = exact_solution(x)
    error = np.max(np.abs(y - y_exact))
    errors.append(error)
    print(f"N={N}, h={h:.4f}, 最大误差={error:.6f}")

# 计算收敛阶
print("\n收敛阶计算:")
for i in range(len(errors) - 1):
    p = np.log(errors[i] / errors[i + 1]) / np.log(2)
    print(f"N={N_list[i]}到N={N_list[i + 1]}, 收敛阶={p:.4f}")

# 绘制精确解和数值解对比
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
N = 20  # 选择一个N值绘图
h = (x_end - x0) / N
x, y = runge_kutta_4(f, x0, y0, h, N)
x_exact = np.linspace(x0, x_end, 100)
y_exact = exact_solution(x_exact)

plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, 'r-', label='精确解')
plt.plot(x, y, 'bo--', label=f'RK4解 (N={N})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('四阶Runge-Kutta方法求解 y\'=y-2x/y')
plt.legend()
plt.grid(True)
plt.show()