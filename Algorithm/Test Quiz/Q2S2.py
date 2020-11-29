# 解法2：使用二分查找
# 对于矩阵中某一元素，获取其行列下标：
# 行：i = num // width
# 列：j = num % width


def searchMatrix(self, matrix, target):
    """
    :param self:
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """

    height = len(matrix)
    width = len(matrix[0])
    if height == 0 or width == 0:
        return False
    
    left = 0
    right = width * height - 1

    while left <= right:
        mid = (left + right) // 2
        i = mid // width
        j = mid % width
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False
