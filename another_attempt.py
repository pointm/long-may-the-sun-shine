import numpy as np
from numpy import exp, sqrt, log10, abs
import matplotlib.pyplot as plt

c = 3 * 10**8


def kc(a, b, m, n):
    return np.pi * sqrt((m / a) ** 2 + (n / b) ** 2)


def kp(frequency, epsilon_r, miu_r, kc):
    omega = 2 * np.pi * frequency
    return sqrt((omega**2 * epsilon_r * miu_r) / (c**2) - kc**2)


def transfer_matrix_p(frequency, epsilon_p, miu_p, zp, epsilon_p1, miu_p1, kc):
    k_in_p = kp(frequency, epsilon_p, miu_p, kc)
    k_in_p1 = kp(frequency, epsilon_p1, miu_p1, kc)
    miu_relative = miu_p / miu_p1
    kp_relative = k_in_p / k_in_p1
    M1 = np.array(
        [[exp(complex(0, k_in_p1 * zp)), 0], [0, exp(complex(0, -k_in_p1 * zp))]]
    )
    M2 = np.array(
        [
            [miu_relative + kp_relative, miu_relative - kp_relative],
            [miu_relative - kp_relative, miu_relative + kp_relative],
        ]
    )
    M3 = np.array(
        [[exp(complex(0, -k_in_p * zp)), 0], [0, exp(complex(0, k_in_p * zp))]]
    )
    return np.dot(0.5 * M1, np.dot(M2, M3))


if __name__ == "__main__":
    freqlist = np.linspace(25, 45, 2500, endpoint=True) * 10**9
    a = 7.11 * 10**-3
    b = 3.555 * 10**-3
    m = 1
    n = 0
    k_cutoff = kc(a, b, m, n)
    epslist = [1, 2.7, 9, 2.7, 1]
    # epslist = [1, 1, 1, 1, 1]
    N = len(epslist)
    miulist = np.ones(N)
    thickness = [9, 1.35 * 10**-3, 0.75 * 10**-3, 1.35 * 10**-3, 9]
    s11list = []
    s21list = []
    totallist = []
    for freq in freqlist:
        M_total = np.array([[1, 0], [0, 1]])
        for var in range(N - 1):
            MT = transfer_matrix_p(
                freq,
                epslist[var],
                miulist[var],
                thickness[var],
                epslist[var + 1],
                miulist[var + 1],
                k_cutoff,
            )
            M_total = np.dot(MT, M_total)
            pass
        M11 = M_total[0, 0]
        M12 = M_total[0, 1]
        M21 = M_total[1, 0]
        M22 = M_total[1, 1]
        R = abs(M21 / M22) ** 2
        T = abs((M11 * M22 - M12 * M21) / (M22)) ** 2
        TOTAL = R + T
        s11list.append(10 * log10(R))
        s21list.append(10 * log10(T))
        totallist.append(10 * log10(TOTAL))
        pass
    pass
    plt.plot(freqlist, s11list, label="S11")
    plt.plot(freqlist, s21list, label="S21")
    plt.plot(freqlist, totallist, label="ALL")
    plt.show()
    pass
