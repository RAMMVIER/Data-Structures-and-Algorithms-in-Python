# 使用队列实现Linux中的tail操作


from collections import deque


def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


# print(tail(5))
for line in tail(5):
    print(line, end='')
