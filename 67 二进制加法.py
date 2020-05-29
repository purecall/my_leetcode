#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []

        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1: # 1 or 3
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2  # 0 or 1 -> 0   2 or 3 -> 1
        
        if carry == 1: # 最后还要一次进位
            answer.append('1')
        
        answer.reverse()

        return ''.join(answer)
# @lc code=end


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        # 转成十进制，相加后再转成二进制
        a,b = int(a,2),int(b,2)
        ans = str(bin(a+b))[2:] # 前两位为0b所以要截取
        return ans