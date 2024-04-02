# 2024.4.2 当前使用python版本3.12.2
# 当前公式引用文献DOI:10.1007/s10762-007-9207-y
import numpy as np
from math import pi
from numpy import exp, sqrt


def kc(a, b, m, n):
    # 计算矩形波导截止波数的函数
    # a 长边长度
    # b 短边长度
    # m a边半波数
    # n b边半波数
    return sqrt((m * pi / a) ** 2 + (n * pi / b) ** 2)


def kp(frequency, epsilon_p, miu_p, k_cutoff):
    # 计算波导在第p层介质中传播电磁波时候的波数
    # frequency 当前频率
    # epsilon_p 第p层介质的相对介电常数
    # miu_p 第p层介质中的相对磁导率
    # k_cutoff 当前模式下波导的截止波数，可以使用kc函数对矩形波导进行截止波数的计算
    # omega 频率的角频率
    omega = 2 * pi * frequency
    c = 3 * 10**8
    return sqrt((omega**2 * epsilon_p * miu_p) / (c**2) - k_cutoff**2)


def transfer_matrix_p(
    frequency,
    kc,
    z_p,
    epsilon_p,
    miu_p,
    epsilon_p1,
    miu_p1,
):
    # 计算第p层介质中的传输矩阵
    # frequency 当前的计算的频率
    # kc 当前波导的截止波数
    # z_p 第p层介质的纵向长度
    # epsilon_p 第p层介质的相对介电常数
    # miu_p 第p层介质中的相对磁导率
    # epsilon_p1 第p+1层介质的相对介电常数
    # miu_p1 第p+1层介质中的相对磁导率
    # k_p 第p层介质中的传播波数
    # k_p1 第p+1层介质中的传播波数
    # rela_miu 第p层相对于第p+1层的相对磁导率，用来辅助M2矩阵的计算
    # rela_k 第p层相对于第p+1层的相对波数，用来辅助M2矩阵的计算
    # M1 第p层传输矩阵的最左边的矩阵，后面的M2、M3依次是中间的矩阵和最右边的矩阵
    k_p = kp(frequency, epsilon_p, miu_p, kc)
    k_p1 = kp(frequency, epsilon_p1, miu_p1, kc)
    rela_miu = miu_p / miu_p
    rela_k = k_p / k_p1
    M1 = np.array([[exp(complex(0, k_p1 * z_p)), 0], [0, exp(complex(0, -k_p1 * z_p))]])
    M2 = np.array(
        [[rela_miu + rela_k, rela_miu - rela_k], [rela_miu - rela_k, rela_miu + rela_k]]
    )
    M3 = np.array([[exp(complex(0, -k_p * z_p)), 0], [0, exp(complex(0, k_p * z_p))]])
    return 0.5 * M1 * M2 * M3


if __name__ == "__main__":
    freq = 35 * 10**9
    a = 7.11 * 10**-3
    b = 3.555 * 10**-3
    m = 1
    n = 0
    epsilon = [1, 2.7, 9, 2.7, 1]
    N = len(epsilon)
    miu = np.ones(N)
    thickness = [999, 1.35 * 10**-3, 0.75 * 10**-3, 1.35 * 10**-3, 999]
    # thickness = [
    #     2.68 * 10**-3,
    #     1.35 * 10**-3,
    #     0.75 * 10**-3,
    #     1.35 * 10**-3,
    #     2.68 * 10**-3,
    # ]

    k_cutoff = kc(
        a, b, m, n
    )  # 计算TE10模式下的波导截止波数，并不是截止频率，截至频率要用c*kc/(2*pi)
    kps = []  # 计算每个介质下的波数
    for index, eps in enumerate(epsilon):
        kps.append(kp(freq, eps, miu[index], k_cutoff))
    M_total = np.array([[1, 0], [0, 1]])
    for var in range(N - 1):
        M_total = np.dot(
            transfer_matrix_p(
                freq, k_cutoff, thickness[var], epsilon[var], 1, epsilon[var + 1], 1
            ),
            M_total,
        )

pass
