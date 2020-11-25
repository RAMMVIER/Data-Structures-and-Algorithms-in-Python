# 桶排序：将元素按照大小分在对应取值范围的桶中，之后对每个桶中的元素进行排序


def bucket_sort(li, n=100, max_num=10000):
    """
    :param li: 原始列表
    :param n: 分成的桶数
    :param max_num: 列表中的最大值
    :return:
    """

    # 创建n个二维列表的桶，其中的一维列表均为空
    buckets = [[] for _ in range(n)]

    # i表示var放在几号桶里
    for var in li:
        i = min(var // (max_num // n), n - 1)               # 确保最后一个元素落在最后一个桶里，而不会越界
        buckets[i].append(var)

