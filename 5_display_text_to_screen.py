import pygame as pg
import time

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
red = (255, 0, 0)  # 添加红色

car_width = 73  # 添加车的图片的宽度，汽车的位置只是指其左上角的像素的位置，只有加上这75像素宽度才是它右侧的像素点的位置

clock = pg.time.Clock()  # 实例化时钟类
crashed = False  # 初始化游戏崩溃监视器
carImg = pg.image.load(
    r"./asset/racecar.png"
)  # 导入车辆的精精灵 将racecar.png 图像加载到的 carImg 变量中。


def car(x, y):  # 定义汽车函数，将车辆绘制到指定坐标的屏幕上
    gameDisplay.blit(
        carImg, (x, y)
    )  # “Blit”基本上只是将图像绘制到屏幕上，但我们还没有完全将其显示在显示器上。在图形中，通常有很多工作是在后台完成的，只有每次更新(update方法被执行)完成后，屏幕才会在视觉上更新。


###################################


def text_objects(text, font):
    testSurface = font.render(text, True, black)
    return (
        testSurface,
        testSurface.get_rect(),
    )  # get_rect()方法可以神不知鬼不觉的得到一个包裹着文字的矩形，并且还可以不现实这个矩形


def message_display(text):
    largeText = pg.font.Font(
        "YAHEI CONSOLAS HYBRID.TTF", 115
    )  # 定义了一个字体与字体的大小
    TextSurf, TextRect = text_objects(
        text, largeText
    )  # 绘制了字体与包裹着字体的一个矩形
    TextRect.center = (
        (display_width / 2),
        (display_height / 2),
    )  # 将矩形居中于屏幕的正中央
    gameDisplay.blit(
        TextSurf, TextRect
    )  # 绘制这个文字与矩形，但是需要注意的是现在只是后台绘制，需要update()函数之后才是正式的添加到屏幕中心

    pg.display.update()

    time.sleep(2)

    game_loop()  # 在完成崩溃文字的绘制之后休息一段时间然后重启游戏
    ###################################
    # P.S. 作者的碎碎念: 作者认为在这里game_loop()函数最好的调用方式应该在crash_function()里面
    # 并且应该在 message_display()函数之后，这样子可以让游戏的重启更加符合直觉。
    # 因为你不应该让你所有的想显示的信息的函数导致游戏重启，
    # (也就是应该先显示重要的提示或者文字，其次再重启游戏)
    ###################################

    pass


def crashed():  # 未来我们希望crashed()函数能够更加复杂，但是现在我们还是简单的做一个文字显示函数罢
    message_display("！哇奥！")


###################################


def game_loop():

    x = display_width * 0.45  # 在屏幕的特定位置，确定小车的初始坐标
    y = display_height * 0.8
    x_change = 0  # 1
    # car_speed = 0  # 1

    gameExit = False

    while not gameExit:

        for event in pg.event.get():
            if event.type == pg.QUIT:  # 判断是否崩溃的方法是用户是否点击退出窗口
                gameExit = True
            if (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):  # 现在判断是否崩溃的方法还有用户是否点击ESC键
                gameExit = True

            print(event)

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

        x += x_change  # 不需要事件出现变化才会使得坐标更新
        # 而是从始至终都会更新坐标，这也是按下左右键不动车车就会一直变化的原因

        gameDisplay.fill(white)
        car(x, y)
        if (
            x + car_width > display_width or x < 0
        ):  # 在车的右像素超过屏幕右边的时候，或者车的左像素超过屏幕左边的时候，就触发判定
            crashed()  # 此时触发崩溃了的函数，这个函数可以告诉用户已经触及边界无法回头了！

        pg.display.update()
        clock.tick(60)


game_loop()
pg.quit()
quit()
