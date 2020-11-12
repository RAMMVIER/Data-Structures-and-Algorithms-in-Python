# 选择排序，每次遍历中选择最小的元素


def select_sort(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


# test
test_list = [3, 4, 6, 7, 8, 1, 9, 2, 5]
print(select_sort(test_list))
