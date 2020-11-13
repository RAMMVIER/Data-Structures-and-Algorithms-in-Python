# 快速排序：取第一个元素p，使其归位，列表被p分为两部分，左部均小于p，右部均大于p，递归完成排序
'''
使用partition函数，先从右侧开始，right指针指向的数如果小于p，则填入p的空位，
left指针指向的数如果大于p，则填入之前right的一个空位
'''


def partition(li, left, right):
    tmp = li[left]                                      # 寄存第一个元素p
    while left < right:                                 # 当left = right时，说明仅剩一个空位，应将p插入空位
        while left < right and li[right] >= tmp:        # 从右侧找比p小的数
            right -= 1                                  # 左移一位
        li[left] = li[right]                            # 将右边比p小的数写入左边空位
        while left < right and li[left] <= tmp:         # 从左侧找比p大的数
            left += 1                                   # 右移一位
        li[right] = li[left]                            # 将左边比p大的数写入右边空位
    li[left] = tmp                                      # 结束循环后，将p归位
    return left


def quick_sort(li, left, right):
    if left < right:                                    # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)                   # 递归完成左侧排序
        quick_sort(li, mid + 1, right)                  # 递归完成右侧排序


# test
test_list = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# partition(test_list, 0, len(test_list) - 1)
quick_sort(test_list, 0, len(test_list) - 1)
print(test_list)
