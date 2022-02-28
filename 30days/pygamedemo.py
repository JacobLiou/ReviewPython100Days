# 使用PyGame进行游戏开发
import pygame

def main():
    pygame.init()
    #初始化窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 绘制一个圆心
    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # # 刷新当前窗口
    # pygame.display.flip()
    # 设置标题
    pygame.display.set_caption('打球迟小秋')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    isXForward = True
    isYForward = True
    running = True
    while running:
        #从消息队列获取消息进行实践处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 实现动画 不断刷新
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就刷新 达到游戏运动效果
        pygame.time.delay(50)

        # 实现碰撞监测
        if x > 800:
            isXForward = False
        elif x < 0:
            isXForward = True
        if y > 600:
            isYForward = False
        elif y < 0:
            isYForward = True

        if not isXForward:
            x = x - 5
        else:
            x = x + 5

        if not isYForward:
            y = y - 5
        else:
            y = y + 5

if __name__ == '__main__':
    main()
