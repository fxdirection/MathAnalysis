def phi1(x):
    return 1 / (1 + 2 * x**2)

def find_root(initial_guess, tolerance):
    x_k = initial_guess
    while True:
        x_k1 = phi1(x_k)
        if abs(x_k1 - x_k) < tolerance:
            break
        x_k = x_k1
    return x_k1

# 设置初始猜测值和容忍度
initial_guess = 1.5
tolerance = 1e-5

# 计算根
root = find_root(initial_guess, tolerance)
print(f"根{root}在1.5附近收敛精度小于{tolerance}")