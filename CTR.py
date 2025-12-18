import numpy as np


# 定义函数 f(x) = sqrt(x) * log(x)，避免 log(0) 的问题
def f(x):
    return np.sqrt(x) * np.log(x + 1e-10)  # 使用 x + 1e-10 避免 log(0)


# 复化梯形法则
def composite_trapezoidal(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    Tn = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return Tn

# 复化Simpson公式
def composite_simpson(a, b, n):
    if n % 2 == 1:
        n += 1  # 确保n是偶数
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return S

# 精确值
exact_value = -# 计算和打印结果
n_values = [2, 4, 8, 16, 32, 64, 128, 256]

print(
    f"{'n':<5} {'Tn (Trapezoidal)':>20} {'En (Trapezoidal)':>20} {'Sn (Simpson)':>20} {'En (Simpson)':>20} {'En/E2n (Trapezoidal)':>20} {'En/E2n (Simpson)':>20}")
print("-" * 80)  # 打印分隔线

for n in n_values:
    Tn = composite_trapezoidal(0, 1, n)
    Sn = composite_simpson(0, 1, n)

    En_trap = abs(exact_value - Tn)
    En_simp = abs(exact_value - Sn)

    E2n_trap = abs(exact_value - composite_trapezoidal(0, 1, 2 * n))
    E2n_simp = abs(exact_value - composite_simpson(0, 1, 2 * n))

    En_over_E2n_trap = En_trap / E2n_trap if E2n_trap != 0 else float('inf')
    En_over_E2n_simp = En_simp / E2n_simp if E2n_simp != 0 else float('inf')

    print(
        f"{n:<5} {Tn:>20.6f} {En_trap:>20.6f} {Sn:>20.6f} {En_simp:>20.6f} {En_over_E2n_trap:>20.2f} {En_over_E2n_simp:>20.2f}")