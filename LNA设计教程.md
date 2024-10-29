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