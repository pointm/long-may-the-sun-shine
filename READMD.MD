# 本库本分支用来进行ADS的自救，我将在此处进行ADS的仿真例子的创建
# 参考教程
- B站教程：[导师力荐的油管ADS入门教程，涵盖了ads绝大部分功能
](https://www.bilibili.com/video/BV1Yy4y1j7DP/?share_source=copy_web&vd_source=2c9beb25af00b14851dca086bf631efd)

## Tutorial-2 Schematic Basics-创建子电路
右键Design里面的New可以创建Symbol，这个就是你的子电路了，就能在其它电路里面调用乃至于编辑它了。。记得在原先的电路里面加上端口Pin!

## Tutorial-3 S Parameter Simulation-记得放端口
求解器方面其实也有步长之类的求解设置，也有模拟仿真噪声之类的步骤，如果要仿真噪声记得把选项打开。。还有记得放端口之后再去仿真！
比如说这个例子里面，群时延和S参数很重要，那么这两个框子就要勾选，但是噪声不是很重要就没勾选。

## Tutorial-4 Data Display in ADS-怎么看结果
仿真之后看看结果如何/怎么仿真结果。

## Tutorial-5 Real Time Tuning in ADS - 如何调谐结果
如何通过对四五个不同的参数当无敌调参大王来得到调参结果