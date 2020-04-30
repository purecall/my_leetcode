#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 通过dfs去把一个人的所有朋友找出来
        visited = [0 for _ in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M,i,visited)
                count += 1
        return count

    def dfs(self,M,i,visited):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M,j,visited)

        
# @lc code=end

