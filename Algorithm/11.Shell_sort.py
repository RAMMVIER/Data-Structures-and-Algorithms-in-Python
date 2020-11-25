# 希尔排序：一种分组插入排序算法
#   1. 取一个整数d1=n/2，将元素分为d1个组，每组相邻两个元素之间距离为d1，在各组内进行直接插入排序
#   2. 娶第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，即所有元素在同一组内进行直接插入排序
# 希尔排序的每一次并不使得某些元素有序，而是使整体元素趋近于有序，最后一次排序是所有数据有序

# 希尔排序的时间复杂度讨论较为复杂，与所选取的gap序列相关

import random


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


# test
test_list = list(range(1000))
random.shuffle(test_list)
shell_sort(test_list)
print(test_list)
