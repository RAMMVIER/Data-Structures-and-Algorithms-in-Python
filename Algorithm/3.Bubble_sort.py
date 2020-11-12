# 冒泡排序
# 关键点：排序遍历次数与无序区/有序区，总遍历次数为n-1
# 每一次遍历无序区元素数量+1，i = 无序区元素数量
# 内层循环中j作为遍历用的指针，遍历次数为n-i-1


import random

def bubble_sort(li):
    for i in range(len(li) - 1):            # 第i次遍历
        for j in range(len(li) - i - 1)
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


# test
li = [random.randint(0, 10000) for i in range(10)]
print(li)
bubble_sort(li)
print(li)