# Python内置的堆排序模块

import heapq
import random

test_list = list(range(100))
random.shuffle(test_list)

print(test_list)

# 建堆(default为小根堆)
heapq.heapify(test_list)
print(test_list)

# 弹出一个最小元素
n = len(test_list)
for i in range(n):
    print(heapq.heappop(test_list), end=',')
