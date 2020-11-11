# 顺序查找：线性查找，从列表第一个元素开始顺序搜索，直到找到元素或搜索至列表最后一个元素为止
# 查找元素存在，返回元素下标
# 查找元素不存在，返回None或-1
# 时间复杂度：O(n)


def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
    else:
        return None


# test
data = [5, 10, 14, 18, 29, 45, 73]
print(linear_search(data, 45))
