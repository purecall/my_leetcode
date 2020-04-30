#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start

# 通过dfs去把一个人的所有朋友找出来
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
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

# 并查集+路径压缩
class Solution1:
    def findCircleNum(self,M):
        def find(parent,i):
            root = i
            while parent[root]!=-1:
                root = parent[root]
            # 路径压缩
            while parent[i]!= -1:
                x = i            # 记录 i
                i = parent[x]    # x(i)的parent赋值给i继续while循环
                parent[x] = root # 当前这个节点的parent设置为最后的root
            return root
        
        def union(parent,x,y):
            p_x = find(parent,x)
            p_y = find(parent,y)
            if p_x != p_y:
                parent[p_x] = p_y  

        parent = [-1 for _ in range(len(M))]

        # 只要遍历一个主对角线下方的三角形， i==j的情况也不用考虑
        for i in range(0, len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    union(parent,i,j)

        count = 0
        for i in range(len(parent)):
            if parent[i]==-1:
                count+=1
        return count