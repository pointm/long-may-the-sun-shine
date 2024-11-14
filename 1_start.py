import pygame

pygame.init()

gameDisplay = pygame.display.set_mode(
    (800, 600)
)  # 设置游戏的分辨率 set the resolution of the game.
pygame.display.set_caption("A bit Racey")

clock = pygame.time.Clock()  # 设置时钟FPS , frame per second


crashed = False

while not crashed:  # 在游戏崩溃之前会一直跑循环
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
        ):  # 现在暂时判断是否崩溃的方法只有用户是否点击退出窗口
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)
