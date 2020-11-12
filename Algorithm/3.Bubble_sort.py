# 冒泡排序
# 关键点：排序遍历次数与无序区/有序区，总遍历次数为n-1
# 每一次遍历无序区元素数量+1，i = 无序区元素数量
# 内层循环中j作为遍历用的指针，遍历次数为n-i-1
# 时间复杂度：O(n^2)


import random


def bubble_sort(li):
    for i in range(len(li) - 1):            # 第i次遍历
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


# test
# test_list = [random.randint(0, 10000) for i in range(10)]
test_list = [4, 5, 6, 1, 2, 3]
print(test_list)
bubble_sort(test_list)
print(test_list)
