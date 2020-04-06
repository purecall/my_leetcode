# 1. 暴力,sort，sorted_str1 == sorted_str2?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t


# 2. hash,map，统计每个字符的频次
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            dict2[c] = dict2.get(c, 0)+1
        
        if dict1 == dict2:
            return True
        else:
            return False

# 3. (2的改进),直接使用python2的Counter
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s)==Counter(t)