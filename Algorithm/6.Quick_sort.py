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
    li[left] = tmp
