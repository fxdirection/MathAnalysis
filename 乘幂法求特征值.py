def matrix_multiply(A, B):
    """矩阵乘法"""
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result


def vector_norm(v):
    """向量最大分量绝对值范数"""
    return max(abs(x) for x in v)


def power_method(A, max_iter=100, tol=1e-6):
    """乘幂法求主特征值及特征向量"""
    n = len(A)
    # 初始向量转换为列向量 [[1], [1], [1]]
    v = [[1.0] for _ in range(n)]
    lambda_old = 0.0

    for _ in range(max_iter):
        # 计算矩阵与向量乘积
        Av = matrix_multiply(A, v)
        # 计算当前特征值估计
        lambda_new = vector_norm([x[0] for x in Av])
        # 归一化向量
        v = [[x[0] / lambda_new] for x in Av]

        # 检查收敛
        if abs(lambda_new - lambda_old) < tol:
            break
        lambda_old = lambda_new

    # 提取特征向量（转置为行向量）
    eigenvector = [x[0] for x in v]
    return lambda_new, eigenvector


A = [
    [2, 3, 2],
    [10, 3, 4],
    [3, 6, 1]
]

# 执行乘幂法
eigenvalue, eigenvector = power_method(A, max_iter=100)

# 结果输出
print(f"按模最大特征值: {eigenvalue:.6f}")  # 精确值应为11
print(f"对应特征向量: {[round(x, 4) for x in eigenvector]}")