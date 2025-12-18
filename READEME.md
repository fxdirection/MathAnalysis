# 数值分析练习代码

该项目为作者于数值分析课程中的一些简单编程问题
一些常见数值计算方法的课堂练习脚本，覆盖积分、方程求根、矩阵特征值与约化等小例子，便于快速查看算法实现与运行结果。

## 脚本概览

- [composite.py](composite.py): 自适应复化梯形积分，示例区间 [-4, 4] 计算 $\int \frac{1}{1+x^2}\,dx$，满足收敛阈值后停止。
- [CTR.py](CTR.py): 对 $f(x)=\sqrt{x}\,\log x$ 在 [0, 1] 上用复化梯形与 Simpson 公式对比误差（示例代码中 `exact_value` 需填入解析值）。
- [constringency.py](constringency.py): 简单不动点迭代求根示例，迭代到给定容忍度。
- [newton.py](newton.py): 变形牛顿法求解 $x=f(x)$，包含分母接近零的防护。
- [newton_solution.py](newton_solution.py): 经典牛顿法求方程 $x=e^{-x}$ 的根。
- [乘幂法求特征值.py](乘幂法求特征值.py): 乘幂法估计矩阵按模最大特征值及对应特征向量。
- [反幂乘法求特征值.py](反幂乘法求特征值.py): 反幂法（带位移）逼近指定特征值并给出特征向量。
- [约化矩阵.py](约化矩阵.py): Householder 变换将对称矩阵约化为三对角形，输出结果矩阵。

## 运行方式

在仓库根目录通过 `python <脚本名>` 直接运行。例如：

```bash
python composite.py
python newton_solution.py
python 乘幂法求特征值.py
```

若需修改积分区间、容忍度或矩阵、位移参数，直接在对应脚本顶部的常量或函数调用处调整后再运行。
