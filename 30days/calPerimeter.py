import math


def calperimeter(radius):
    return math.pi * radius * 2


if __name__ == '__main__':
    import this
    radiusStr = input("请输入半径：")
    try:
        radius = float(radiusStr)
    except:
        print("无法转换输入")
    print(calperimeter(radius))

# 快捷键Ctrl + / 进行注释
# 对比VS 基础IDE功能
    # import turtle
    # turtle.pensize(4)
    # turtle.pencolor('red')
    #
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    # turtle.right(90)
    # turtle.forward(100)
    #
    # turtle.mainloop()
