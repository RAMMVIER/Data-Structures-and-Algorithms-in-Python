# 桶排序：将元素按照大小分在对应取值范围的桶中，之后对每个桶中的元素进行排序


import random


def bucket_sort(li, n=100, max_num=10000):
    """
    :param li: 原始列表
    :param n: 分成的桶数
    :param max_num: 列表中的最大值
    :return: 有序列表列表
    """

    # 创建n个二维列表的桶，其中的一维列表均为空
    buckets = [[] for _ in range(n)]

    # i表示var放在几号桶里
    for var in li:
        i = min(var // (max_num // n), n - 1)               # 确保最后一个元素落在最后一个桶里，而不会越界
        buckets[i].append(var)

        # 在放数时对桶内进行排序，用新进入的数逆序对比，与比本身大的数换位，直到找到一个比其小的数为止
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break

    sorted_list = []
    for buc in buckets:
        sorted_list.extend(buc)
    return sorted_list


# test
test_list = [random.randint(1, 1000) for i in range(10000)]
print(test_list)
test_list = bucket_sort(test_list)
print(test_list)
