# Quick Review - LNA Theory & Fundamentals
[ADS进阶教程-RF电路设计实例](https://www.bilibili.com/video/BV1XP4y1h744/?p=9&share_source=copy_web&vd_source=2c9beb25af00b14851dca086bf631efd)
设计者可以通过选择不同的低噪声器件、选择不同的器件工作点或者不同的电路拓扑结构来得到最小化总体噪声这一目的。

噪声公式，前端放大器的噪声系数会对后续的总体噪声系数造成主要的影响。

![低噪放指标](/FIGURE/LNA设计教程/低噪放指标.jpg)

主要的设计方法MMIC/RFIC/PCB三个方法进行设计。这里主要使用PCB的方法进行设计，前后的方法的优缺点主要集中在下面这张图中。

![设计工艺的优缺点](/FIGURE/LNA设计教程/不同设计工艺的优缺点.jpg)

注意事项
- MOS管的适用频段应该包括了所需设计的频段
- 经验公式：选择的管子的噪声系数的最小值应该是低噪声放大器电路所需的噪声系数的一半（居然是dB数字的一半）

可以使用SNP文件进行仿真，也可以使用管子的真实zap模型进行仿真，导入zap模型的时候直接使用菜单左侧的`File->Unarchive..`进行导入即可。SNP文件虽说可以提供S参数模型和噪声系数，但是并不能提供应有的`P1dB/P3dB`这些参数，并且也无法设计偏置电路。

# 具体的ADS步骤
## 0 找出管子的模型
ATF 21170是一个ADS自带管子模型库里面的管子，在现阶段，我们可以去ADS的安装路径`C:\Users\Pachirisu\ProgramFiles\ADS2021\oalibs\componentLib`这里面找`RF_Transistors_vendor_kit.7z`压缩包进行导入（当然我这里已经直接导入到`ASSETS`里面进行仿真。导入完成后直接进行检索就能找到管子的模型。
## 1 找出直流偏置
首先要找出管子的合适直流偏置点，我们新建一个`Schematic`，之后选择`Insert->eTemplate...`在弹出的弹窗里面选择`ads_templates:FET_curve_tracer`。这样子就得到了一个预设模板，在连接好漏极、栅极和源极之后，设置`VGS`和`VDS`的扫参的线进行扫参，便可以得到所需的图片。

![进行电路搭建](/FIGURE/LNA设计教程/FET直流偏置扫参.png)

在仿真完成后的预览图里面可以看到`VGS扫参图`，在这个图里面默认是红色曲线，如果需要彩色线条的设置，可以按照下面这个图进行设置。

![寻找管子的合适直流偏置点](/FIGURE/LNA设计教程/VGS扫参寻找直流偏置.png)

![偏置颜色的放置](/FIGURE/LNA设计教程/偏置颜色设置.png)

## 2 进行大信号仿真

### 组件搭建
进行直流偏置电路的搭建，同时在直流偏置点位上放上隔离交流的电感线圈(在ADS里面是`DC_FEED`)，在交流信号电路上面放上隔离直流的电容(符号是`DC_BLOCK`)。

加上偏置之后分别添加S参数组件、`Mu`组件和`MuPrime`组件，S参数是为了测量初步的增益，`Mu`是为了测量放大器的稳定性。

这里相比于传统的理想仿真还加上了一个`Option`组件，是因为`IEEE`对于大信号分析有温度的要求(16.85℃)，这里是为了设置仿真温度的，如果没有这个组件的话会有一个警告，但是不太影响仿真的结果。

![大信号仿真](/FIGURE/LNA设计教程/大信号仿真.png)

组件设置方面，除了设置组件带宽之外，还记得打开S参数的`Calculate Noise`选项，不然的话不会计算噪声系数！

![噪声计算设置](/FIGURE/LNA设计教程/噪声计算.png)

一切设置完毕后，点击仿真查看相应的结果。

### 结果查看
#### 稳定性$\mu,\mu^\prime$
在$\mu>1$的时候放大器的稳定性将达到绝对，ADS可以直接查看$\mu$系数。

![Mu系数](/FIGURE/LNA设计教程/Mu系数.png)

#### 增益
使用S21查看基础的增益，现在暂时先不搞，

![增益](/FIGURE/LNA设计教程/S21计算增益.png)

![噪声系数](/FIGURE/LNA设计教程/2端口噪声系数.png)

Practical Tip:
Avoid any lossy components at the input side of LNA circuit as much as possible so that the noise figure is not distorted beyond a point

实用提示：
尽量避开LNA电路输入侧的任何损耗元件，使噪声系数不至于畸变到很奇怪的地方

Practical Tips:
Its a personal choice or sometimes depends on the situation on ground to decide which kind of stability
operation one might decide to use. On a personal note, I prefer opting for unconditionally stable
operation so that you have access to all the impedance points on the Smith Chart later for matching
purposes as you will see in the tutorial. However if you decide to use conditional stability, that's fine too
just that you need tomakesure thatyou don't present any impedance inside the unstableregion toyour
LNA else it will induce the oscillations.

这是个个人选择，有时还取决于地面情况，以决定使用哪种稳定操作。
操作。就我个人而言，我更倾向于选择无条件稳定运行。
这样您就可以访问史密斯图上的所有阻抗点，以便日后进行匹配。
在教程中将会看到。不过，如果您决定使用有条件稳定，也没有问题
只是您需要确保您的 LNA 不在不稳定区域内出现任何阻抗。
否则会引起振荡。

另外一种拒绝震荡的方法是使用FEED BACK（也就是在漏的输出部分和栅极的输入部分相连在MMIC中更加常用），这种方法也可以增加稳定性，多级设计中常用（听错了的可能性微存）

