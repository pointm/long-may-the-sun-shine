import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = (
    " Times New Roman, SimSun"  # 设置字体族，中文为SimSun，英文为Times New Roman
)
plt.rcParams["mathtext.fontset"] = "stix"  # 设置数学公式字体为stix


x = np.linspace(0, 5)
y = np.sin(x)
plt.figure(dpi=300)
plt.plot(x, y, label="The Times New Roman")
plt.xlabel("这是sinx函数的x轴标签", fontsize=16)
plt.ylabel("这是sinx函数的y轴标签", fontsize=16)
plt.title("宋体与Times New Roman")
plt.text(
    0,
    0.0,
    "Be nice to people on the way up,\n because you will need them \non your way down.",
    fontsize=16,
)

plt.text(
    0,
    -0.75,
    "径向分布图中有n-l个极大值峰，\n有（n-l-1）个节面（不含原点），\n主峰跟随着l的增大向核移进，但l越小，\n峰数目越多，最内层的峰离核越近。\n $S_{11}$的反射系数是",
    fontsize=16,
)

plt.legend(frameon=False, fontsize=12)
plt.show()
