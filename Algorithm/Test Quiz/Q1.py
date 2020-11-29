# 给定两个字符串s和t，判断t是否为s的重新排列后组成的单词
#   s = "anagram", t = "nagaram", return True
#   s = "rat", t = "car", return False

# 解法：对两个字符串转化成list进行排序，将两者对比作为返回值


def isAnagram(self, s, t):
    """
    :param self:
    :param s: str
    :param t: str
    :return: bool
    """

    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss == tt
