# 解法2：使用两个字典分别记录所有字母在两个字符串中出现的次数，之后进行对比


def isAnagram(self, s, t):
    """
    :param self:
    :param s: str
    :param t: str
    :return: bool
    """

    dict1 = {}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2
