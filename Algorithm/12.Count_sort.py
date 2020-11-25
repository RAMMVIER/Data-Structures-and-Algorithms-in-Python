# 计数排序：已知列表中的数据范围在0-100之间，新建一个列表进行计数，该列表的下标代表对应数据，列表的值对应计数的个数，

# 时间复杂度：O(n)

import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for index, val in enumerate(count):
        for i in range(val):
            li.append(index)


# test
test_list = [random.randint(0, 100) for _ in range(1000)]
print(test_list)
count_sort(test_list)
print(test_list)
