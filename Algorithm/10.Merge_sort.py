# 归并排序：原始列表分两段有序，将其合成为一个有序列表
# 归并排序不可在原地排序


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


# test
test_list = [2, 4, 5, 7, 1, 3, 6, 8]

