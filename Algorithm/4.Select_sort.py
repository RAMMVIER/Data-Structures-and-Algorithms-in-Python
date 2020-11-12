# 选择排序，每次遍历中选择最小的元素，与列表第一个元素交换位置，实现原地排序


# 简单版选择排序，需要两个list，且需要对原list进行min、append、remove操作，效率过低
def select_sort_simple(li):                # 时间复杂度：O(n^2)
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):            # i为遍历次数，最后一个元素必是最大值，无需排列，因此为n-1次遍历
        min_location = i                    # 用于记录最小值的位置，便于进行对比，每次循环开始时，设置为当前循环的起点i
        for j in range(i + 1, len(li)):     # 在无序区进行遍历，寻找无序区内的最小值
            if li[j] < li[min_location]:
                min_location = j
        li[i], li[min_location] = li[min_location], li[i]
    return li


# test
test_list = [3, 4, 6, 7, 8, 1, 9, 2, 5]
# print(select_sort_simple(test_list))
print(select_sort(test_list))
