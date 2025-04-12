import skrf as rf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 图片预处理部分
plt.style.use("fast")  # 调用配色方案
# 设置字体的最优方案，中文为宋体，英文为Times New Roman
plt.rcParams["font.family"] = (
    "Times New Roman, SimSun"  # 设置字体族，中文为SimSun，英文为Times New Roman
)
plt.rcParams["mathtext.fontset"] = "stix"  # 设置数学公式字体为stix
# 设置字体的大小，
label_size = 16  # xy轴标签的大小
legend_size = 18  # 图例的大小
axis_size = 16  # 坐标轴刻度标签的大小
plt.figure(figsize=(6, 5.5))  # 设置图片大小

# 加载TOUCHSTONE数据
xbandwindow = rf.Network("data/XBANDWIN.s2p")

# 绘制 S11 参数
xbandwindow.s11.plot_s_db(label=r"$\mathrm{S_{11}}$")

xbandwindow.s21.plot_s_db(label=r"$\mathrm{S_{21}}$")
xbandwindow.s11["6-11ghz"].plot_s_db(
    lw=3, label="所需的频段", color="red"
)  # 标出感兴趣的频段，表粗的线的宽度为3

# 设置坐标轴标签和标题
plt.xlabel("频率/ GHz", fontsize=label_size)
plt.ylabel("幅值/ dB", fontsize=label_size)

# 启用次要刻度
plt.minorticks_on()

# 自定义次要刻度位置
plt.tick_params(
    axis="both", which="minor", bottom=True, top=False, left=True, right=False
)

# 设置坐标轴刻度标签大小
plt.tick_params(axis="both", which="major", labelsize=axis_size)
plt.tick_params(
    axis="both", which="minor", labelsize=axis_size - 2
)  # 次要刻度标签稍小一些

# 设置图例
plt.legend(frameon=False, fontsize=legend_size)

# 获取当前轴，准备设置子刻度
ax = plt.gca()
# 设置X轴次要刻度步长为1 GHz
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1e9))
# 设置Y轴次要刻度步长为5 dB
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

plt.grid(which="both", linestyle="--", linewidth=0.5)
# 显示图表
plt.show()
