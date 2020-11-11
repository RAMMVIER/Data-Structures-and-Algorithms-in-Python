# 汉诺塔递归，n为盘子数量，abc参数为柱子
# abc其顺序含义为，从a经过b移动至c

# 汉诺塔问题求解：
# n个盘子时：
#   1.把n-1个圆盘从a经过c移动到b
#   2.把第n个圆盘从a移动到c
#   3.把n-1个圆盘从b经过a移动到c



def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("Moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)

# test
hanoi(7, 'A', 'B', 'C')