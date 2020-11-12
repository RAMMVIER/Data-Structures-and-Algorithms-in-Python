# 插入排序，将无序区内当前元素寻找其在有序区内对应的位置并插入，类似于摸牌并排列
# 时间复杂度：O(n^2)


def insert_sort(li):
    for i in range(1, len(li)):             # i为摸到的牌的下标，从第二张开始
        tmp = li[i]                         # 寄存当前值
        j = i - 1                           # j为手中的牌的下标
        while li[j] > tmp and j >= 0:       # 寻找插入位置，j=-1时退出，说明已无更小值
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp                     # 插入当前牌


# test
test_list = [4, 6, 2, 1, 7, 9, 5, 8, 3]
insert_sort(test_list)
print(test_list)