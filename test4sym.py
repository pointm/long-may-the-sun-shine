from sympy import symbols, Matrix

# 定义符号
a, b = symbols("a b")

# 创建一个符号矩阵
M = Matrix([[a, b], [b, a]])

# 显示矩阵
print("M = ")
print(M)

# 计算矩阵的平方
M_squared = M**2

# 显示计算结果
print("M^2 = ")
print(M_squared)

import math

# 定义列表
values = [
    584.9007091671341,
    1120.5336041550017,
    2154.2678263424555,
    1120.5336041550017,
    584.9007091671341,
]

# 计算每个值被pi/2除之后的结果
results = [10**3 * (math.pi / 2) / value for value in values]

print("计算结果为：", results)
pass
