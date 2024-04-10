# 2024.4.2 当前使用python版本3.12.2
# 当前公式引用文献DOI:10.1007/s10762-007-9207-y
import numpy as np
from math import pi, log10
from numpy import exp, sqrt, abs
import matplotlib as mpl
import matplotlib.pyplot as plt


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
    rela_miu = miu_p / miu_p1
    rela_k = k_p / k_p1
    M1 = np.array([[exp(complex(0, k_p1 * z_p)), 0], [0, exp(complex(0, -k_p1 * z_p))]])
    M2 = np.array(
        [[rela_miu + rela_k, rela_miu - rela_k], [rela_miu - rela_k, rela_miu + rela_k]]
    )
    M3 = np.array([[exp(complex(0, -k_p * z_p)), 0], [0, exp(complex(0, k_p * z_p))]])

    return 0.5 * np.linalg.multi_dot([M1, M2, M3])


if __name__ == "__main__":
    ifmatrix = False
    freqlist = np.linspace(25, 45, 1500, endpoint=True) * 10**9
    # freq = 35 * 10**9
    a = 7.11 * 10**-3
    b = 3.555 * 10**-3
    m = 1
    n = 0
    epsilon = [1, 2.7, 9, 2.7, 1]
    # epsilon = [1, 3.8, 16, 3.8, 1]
    # epsilon = [1, 1, 1, 1, 1]  # 测试用，看看匀质情况下传输矩阵对不对
    N = len(epsilon)
    miu = np.ones(N)
    thickness = [9, 1.35 * 10**-3, 0.75 * 10**-3, 1.35 * 10**-3, 9]
    # thickness = [9, 1.12 * 10**-3, 0.52 * 10**-3, 1.12 * 10**-3, 9]

    k_cutoff = kc(
        a, b, m, n
    )  # 计算TE10模式下的波导截止波数，并不是截止频率，截至频率要用c*kc/(2*pi)
    s11list = []
    s21list = []
    convlist = []
    for freq in freqlist:
        if ifmatrix == False:
            kps = []  # 计算每个介质下的波数
            for eps in epsilon:
                kps.append(kp(freq, eps, 1, k_cutoff))
            R = (
                abs(
                    (
                        (kps[4] * kps[0] * kps[2] ** 2 - (kps[3] * kps[1]) ** 2)
                        / (kps[4] * kps[0] * kps[2] ** 2 + (kps[3] * kps[1]) ** 2)
                    )
                )
                ** 2
            )
            T = (
                4
                * abs(
                    (kps[0] * kps[1] * kps[2] * kps[3])
                    / (kps[0] * kps[4] * kps[2] ** 2 + (kps[1] * kps[3]) ** 2)
                )
                ** 2
            )
            TOTAL = R + T
        if ifmatrix == True:
            M_total = np.array([[1, 0], [0, 1]])  # 传输矩阵初始化
            for var in range(N - 1):
                M_total = np.dot(
                    transfer_matrix_p(
                        freq,
                        k_cutoff,
                        thickness[var],
                        epsilon[var],
                        1,
                        epsilon[var + 1],
                        1,
                    ),
                    M_total,
                )
            M11 = M_total[0, 0]
            M12 = M_total[0, 1]
            M21 = M_total[1, 0]
            M22 = M_total[1, 1]
            R = abs(M21 / M22) ** 2
            T = abs((M11 * M22 - M12 * M21) / M22) ** 2
            TOTAL = R + T  # 你到底守不守恒?

        S11 = 10 * log10(R)
        S21 = 10 * log10(T)
        conv = 10 * log10(TOTAL)
        # S11 = R
        # S21 = T
        # conv = TOTAL
        s11list.append(S11)
        s21list.append(S21)
        convlist.append(conv)
    plt.plot(freqlist, s11list, label="S11")
    plt.plot(freqlist, s21list, label="S21")
    plt.plot(freqlist, convlist, label="Convergence")
    plt.legend()
    plt.show()
pass
