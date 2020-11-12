# 二分查找：从有序列表的初始候选区list[0:n-1]开始，通过对待查找的值与候选区中间值的比较，使候选区减小一半
# 时间复杂度：O(logn)


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:                # 候选区有值
        mid = (left + right) // 2       # 整除用于取整数部分作为下标
        if li[mid] == val:
            return mid
        elif li[mid] > val:             # 待查找的值在mid左侧
            right = mid - 1
        else:                           # 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


# test
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(test_list, 7))
