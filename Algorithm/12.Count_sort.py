# 计数排序：


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
test_list = list(range(100))
random.shuffle(test_list)
count_sort(test_list)
print(test_list)
