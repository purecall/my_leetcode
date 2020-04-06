# 1. dict的key为排序后的字符串，value为原字符串组成的list
class Solution:
    def groupAnagrams(self, strs):
        res = dict()
        for word in strs:
            key = "".join(sorted(word)) # str(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())

# 2. 不排序，每个字符串s转换为字符数count的list，再转成str，作为哈希映射的key
class Solution1:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[str(count)].append(s)
        return list(ans.values()) # [*ans.values()] 解包