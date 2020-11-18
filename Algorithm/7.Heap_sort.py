# 二叉树的顺序存储方式：
#   父节点下标(i)，推导左孩子节点下标：i -> 2i+1
#   父节点下标(i)，推导右孩子节点下标：i -> 2i+2
#   孩子节点下标(i)，推导父节点下标：(i-1)//2

# 堆是一种特殊的完全二叉树
#   大根堆：任意一节点都比其孩子节点大
#   小根堆：任意一节点都比其孩子节点小
#   堆的向下调整：当根节点的左右子树都是堆时，可以通过一次向下的调整来将其变换成一个堆

# 堆排序的过程：
#   1.建立堆
#   2.得到堆顶元素，为最大元素
#   3.去掉堆顶，将堆最后一个元素放到堆顶，此时通过一次调整重新使堆有序
#   4.堆顶元素为第二大元素
#   5.重复步骤3，直到堆变空

# 堆排序的时间复杂度：O(nlogn)
#   sift()函数每次规模减半，向左右调整只取一侧，O(logn)


# 调整
def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根元素
    :param high: 堆的最后一个元素
    :return:
    """
    i = low                                                         # 最开始指向根节点
    j = 2 * i + 1                                                   # 最开始指向左孩子节点
    tmp = li[low]                                                   # 存储堆顶
    while j <= high:                                                # 只要j的位置有节点，持续循环
        if j + 1 <= high and li[j + 1] > li[j]:                     # 右孩子节点存在且大于左
            j = j + 1                                               # 指向右孩子节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j                                                   # 向下一层
            j = 2 * i + 1                                           # 向下一层
        else:                                                       # tmp更大，将tmp放在i的位置
            li[i] = tmp
            break
    else:
        li[i] = tmp                                                 # 将tmp放在叶子节点


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):                           # 从最后一个非叶子节点逆序遍历到根节点
        # i表示建堆时调整的部分的根的下标，high用于判断j是否越界
        sift(li, i, n - 1)
        # 建堆完成

    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)                                          # i-1是新的high


# test
test_list = [0, 5, 9, 2, 3, 1, 4, 7, 6, 8]
heap_sort(test_list)
print(test_list)
