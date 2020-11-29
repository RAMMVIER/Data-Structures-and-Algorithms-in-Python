# 基数排序：先根据个位数字大小进行排序，之后根据十位排序，以此类推
# 基数排序通过多关键字的原理进行排序，通过有序的桶，使得整体数据有序

# 时间复杂度：O(kn)
# 空间复杂度：O(k+n)
# k表示最大值的位数


import random


def radix_sort(li):
    # 确定列表中的最大值，最大值有几位数字则需要进行几次排序
    max_num = max(li)
    iteration = 0
    while 10 ** iteration <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # 取出当前迭代对应的位上的数字
            digit = (var // 10 ** iteration) % 10
            buckets[digit].append(var)
        # 分桶结束
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数字写回原列表
        iteration += 1


# test
test_list = list(range(1000))
random.shuffle(test_list)
radix_sort(test_list)
print(test_list)
