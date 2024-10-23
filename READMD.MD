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
Tuning/调谐记得在电路层级的最高一层发起，然后再下降到子层级进行详细的调参。

## torial-6_Optimization in ADS - 表达式是自己敲进去的c
`dB(S(2,1))`的这个表达式是自己敲进去的不是直接选中的c。
表达式可以在表格的纵轴部分直接查看。
`Simulate -> Simulate Set up -> Simulation Variables Setup `里面进行变量设置的时候，选项卡要调整到`Optimization`里面进行变量设置，默认选项卡是`Tuning`，有点坑！

## torial-8_Yield Analysis - 良品率分析
分析器件在公差扰动的情况下的不同的性能变化

## Tutorial-9:Using Vendor Library Components 
了解ADS里面存储的实际上的一些组件，而不是理想上的组件的性能。
这一节讲述了加了哪些组件，怎么导入库之类的方法，主要是通过`DesignKits->Unzip Design Kit..`或者`DesignKits->Manage Libraries...`添加外部导入的库文件。

如果仿真时候报错的话，使用库组件的时候记得在最顶层放上`NetListInclude`组件进行仿真，，不同的器件厂商这个标准应该也不太一样吧。

## Tutorial-12:Polymorphism/ Dynamic Model Selection
这一部分说明了可以把一些不同的`Cell`的设计图转化到相同的`Cell`里面进行动态仿真，这样子的话就不需要再建立不同的`Cell`再进一步的在测试分支里面进行手动切换了。在相同的`Cell`里面的选择仿真小齿轮左侧的`Choose View for Simulation`即可切换视图，`Design`小方块下方会有提示的。

## Tutorial-13:Working with Touchstone/S-Parameter files in ADS
将数据S以TOUCHSTONE的格式导出到TXT里面进行保存。简单的方法是在`S-parameter`组件里面选择`SP_output`，这样子运行完成后会将`.s2p`文件保存在原先仿真文件的子文件夹`data`里面，名字就是你命名的名字。

可以使用组件`SnP`(奇怪的组件名字) 来创建关于S参数的黑盒子(可以是多端口的黑盒子) ，使用现有的黑盒子来进行多端口的仿真。

如果只是想要对S参数进行比较的话可以在数据查看页面点击`Tools->Data view tools...`进行数据的导入或者书写，写到不同的`Dataset`里面之后可以在图里面进行绘图。

