import numpy as np


def householder_matrix(v):
    """生成 Householder 变换矩阵"""
    v = np.array(v, dtype=float)
    v_norm = np.linalg.norm(v)
    if v_norm == 0:
        raise ValueError("向量不能为零向量")
    v = v / v_norm  # 单位化
    H = np.eye(len(v)) - 2 * np.outer(v, v)
    return H


def householder_reduction(A):
    """将对称矩阵 A 转化为三对角对称矩阵"""
    n = A.shape[0]
    Q = np.eye(n)  # 累积正交变换矩阵
    for k in range(n - 2):
        x = A[k + 1:, k]  # 当前列的下三角部分
        e1 = np.zeros_like(x)
        e1[0] = 1.0  # 标准基向量
        alpha = -np.sign(x[0]) * np.linalg.norm(x)
        v = x - alpha * e1  # Householder 向量
        v = v / np.linalg.norm(v)

        # 生成变换矩阵并扩展维度
        Hk = np.eye(n)
        Hk_sub = householder_matrix(v)
        Hk[k + 1:, k + 1:] = Hk_sub

        # 应用变换
        A = Hk @ A @ Hk
        Q = Q @ Hk
    return Q, A


# 输入矩阵
A = np.array([[1, 3, 4],
              [3, 1, 2],
              [4, 2, 1]], dtype=float)

# 执行变换
Q, tridiagonal_A = householder_reduction(A)

# 设置输出格式
np.set_printoptions(precision=4, suppress=True)
print("三对角对称矩阵：\n", tridiagonal_A)