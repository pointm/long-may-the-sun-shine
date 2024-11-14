import pygame as pg

pg.init()

display_width = 800
display_height = 600

gameDisplay = pg.display.set_mode(
    (display_width, display_height)
)  # 设置窗口的宽度和高度，顺便引入窗口这个类进行操作
pg.display.set_caption("A bit Racey")  # 设置标题名字

# 设置颜色的RGB值
black = (0, 0, 0)
white = (255, 255, 255)

clock = pg.time.Clock()  # 实例化时钟类
crashed = False  # 初始化游戏崩溃监视器
carImg = pg.image.load(
    r"./asset/racecar.png"
)  # 导入车辆的精将 将racecar.png 图像加载到的 carImg 变量中。


def car(x, y):  # 定义汽车函数，将车辆绘制到指定坐标的屏幕上
    gameDisplay.blit(
        carImg, (x, y)
    )  # “Blit”基本上只是将图像绘制到屏幕上，但我们还没有完全将其显示在显示器上。在图形中，通常有很多工作是在后台完成的，只有每次更新(update方法被执行)完成后，屏幕才会在视觉上更新。


x = display_width * 0.45  # 在屏幕的特定位置，确定小车的初始坐标
y = display_height * 0.8
x_change = 0  # 1
car_speed = 0  # 1

while not crashed:  # 在游戏崩溃之前会一直跑循环
    for event in pg.event.get():
        if event.type == pg.QUIT:  # 判断是否崩溃的方法是用户是否点击退出窗口
            crashed = True
        if (
            event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
        ):  # 现在判断是否崩溃的方法还有用户是否点击ESC键
            crashed = True

        print(event)

        ###################################
        if (
            event.type == pg.KEYDOWN
        ):  # 判断按键是否按下，这一段判定一直被位于循环(一直得到窗口所有事件的循环)之中
            if event.key == pg.K_LEFT:  # 按下的按键是否是左方向键？
                x_change = -5  # 如果是的话，那就把x_change赋值为-5
            elif event.key == pg.K_RIGHT:  # 按下的按键是否是右方向键？
                x_change = 5  # 如果是的话，那就把x_change赋值为55

        if event.type == pg.KEYUP:  # 判断是否有按键抬起来？
            if (
                event.key == pg.K_LEFT or event.key == pg.K_RIGHT
            ):  # 如果有左按键或者右按键抬起来的话，那么就不更改力！
                x_change = 0
        ###################################
        ##
    x += x_change  # 不需要事件出现变化才会使得坐标更新
    # 而是从始至终都会更新坐标，这也是按下左右键不动车车就会一直变化的原因
    ####

    gameDisplay.fill(white)
    car(x, y)
    pg.display.update()
    clock.tick(60)

pg.quit()
quit()
