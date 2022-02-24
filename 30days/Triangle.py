import math

def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a+b+c
    else:
        return -1.0

if __name__ == '__main__':
    import this
    a = float(input("请输入三条边长1："))
    b = float(input("请输入三条边长2："))
    c = float(input("请输入三条边长3："))
    print(isTriangle(a, b, c))