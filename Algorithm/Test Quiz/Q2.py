# 解法1：遍历矩阵进行查找


def searchMatrix(self, matrix, target):
    """
    :param self:
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """

    for line in matrix:
        if target in line:
            return True
    return False
