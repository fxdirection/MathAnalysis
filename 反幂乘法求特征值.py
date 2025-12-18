import numpy as np


def inverse_power_method(A, mu, max_iter=1000, tol=1e-6):
    n = A.shape[0]
    B = A - mu * np.eye(n)  # 构造 (A - μI)
    x = np.ones(n)  # 初始向量
    lambda_prev = 0  # 初始特征值

    for _ in range(max_iter):
        # 解线性方程组 (A - μI)y = x
        y = np.linalg.solve(B, x)
        # 归一化向量
        norm = np.linalg.norm(y)
        x = y / norm
        # 计算 Rayleigh 商估计特征值
        lambda_k = mu + 1 / (x @ np.linalg.solve(B, x))
        # 判断收敛
        if np.abs(lambda_k - lambda_prev) < tol:
            break
        lambda_prev = lambda_k

    # 最终特征值为 μ + 1/(收敛值)
    eigenvalue = lambda_k
    eigenvector = x
    return eigenvalue, eigenvector


# 定义矩阵 A
A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
mu = 1.2679  # 目标近似值

# 调用反幂法
eigenvalue, eigenvector = inverse_power_method(A, mu)

print("最接近 1.2679 的特征值:", eigenvalue)
print("对应的特征向量:", eigenvector)