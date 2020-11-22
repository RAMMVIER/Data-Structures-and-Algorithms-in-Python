# 归并排序：假设原始列表分两段有序，将其合成为一个有序列表
# 归并排序不可在原地排序

# 步骤：
#   1. 分解：将列表越分越小，直至分成一个元素
#   2. 终止条件：一个元素必然是有序的
#   3. 合并：将两个有序列表合并，列表逐渐增大


import random


# 合并过程
def merge(li, low, mid, high):
    """
    :param li: 输入的原始列表
    :param low: 列表第一个元素的下标
    :param mid: 第一段有序列表中最后一个元素的下标
    :param high: 列表最后一个元素的下标
    :return: void
    """

    i = low
    j = mid + 1                                         # j指向第二段有序列表的第一个元素
    ltmp = []                                           # 存储排序后的列表

    while i <= mid and j <= high:                       # 只要左右都有数，比大小
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行结束后，两个有序列表必有一个没有元素了

    # 如果第一部分害有元素
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    # 如果第二部分害有元素
    while j <= high:
        ltmp.append(li[j])
        j += 1

    li[low:high + 1] = ltmp


def merge_sort(li, low, high):
    if low < high:                                  # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


# test
test_list = list(range(1000))
random.shuffle(test_list)
print(test_list)
merge_sort(test_list, 0, len(test_list) - 1)
print(test_list)
