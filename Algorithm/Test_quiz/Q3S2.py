# 解法2：使用二分查找


def binary_search(self, li, left, right, val):
    while left <= right:  # 候选区有值
        mid = (left + right) // 2  # 整除用于取整数部分作为下标
        if li[mid][0] == val:
            return mid
        elif li[mid][0] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


def twoSum(self, nums, target):
    new_nums = [[nums, i] for i, nums in enumerate(nums)]
    new_nums.sort(key=lambda x: x[0])

    for i in range(len(new_nums)):
        a = new_nums[i][0]
        b = target - a
        if b >= a:
            j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
        else:
            j = self.binary_search(new_nums, 0, i - 1, b)
        if j:
            break
    return sorted([new_nums[i][1], new_nums[j][1]])
