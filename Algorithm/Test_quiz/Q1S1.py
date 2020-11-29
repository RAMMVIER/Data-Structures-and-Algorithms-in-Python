# 解法1：对两个字符串转化成list进行排序，将两者对比作为返回值


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
