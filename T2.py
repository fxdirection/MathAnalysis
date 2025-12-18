import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

def solve_bvp():
    # 问题参数
    a = 0.0  # 左边界
    b = 2.0  # 右边界
    h = 0.1  # 步长
    N = int((b - a) / h) - 1  # 内部节点数

    # 创建网格
    x = np.linspace(a, b, N + 2)
    x_inner = x[1:-1]  # 内部节点

    # 初始化矩阵A和向量b
    A = np.zeros((N, N))
    b_vec = np.ones(N)  # 方程右边是1

    # 填充矩阵A
    for i in range(N):
        xi = x[i + 1]  # 当前节点x值

        # 二阶导数项 (y''的离散)
        A[i, i] = -2 / (h ** 2)

        # 一阶导数项 (-xy'的离散)
        if i > 0:
            A[i, i - 1] += 1 / (h ** 2) + xi / (2 * h)
        if i < N - 1:
            A[i, i + 1] += 1 / (h ** 2) - xi / (2 * h)

        # y项 (+y的离散)
        A[i, i] += 1

    # 求解线性方程组
    y_inner = np.linalg.solve(A, b_vec)

    # 添加边界条件
    y = np.zeros(N + 2)
    y[1:-1] = y_inner

    # 输出结果表格
    print("数值解结果：")
    print(f"{'x_i':<10}{'y_i':<10}")
    for xi, yi in zip(x, y):
        print(f"{xi:<10.2f}{yi:<10.6f}")

    # 绘制解曲线
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'bo-', label='数值解')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('差分法求解 $y\'\' - xy\' + y = 1$ 边值问题')
    plt.grid(True)
    plt.legend()
    plt.show()

    return x, y


# 执行求解
x, y = solve_bvp()