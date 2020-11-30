# 解法1：遍历列表求和进行对比


def twoSum(self, nums, target):
    """
    :param self:
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

    n = len(nums)
    for i in range(n):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return sorted([i, j])
