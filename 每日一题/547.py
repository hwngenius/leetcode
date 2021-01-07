from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis=[False for _ in range(len(isConnected))]
        ans=0
        def travel(i):
            vis[i]=True
            # for neighbord in isConnected[i]:
            #     if not vis[neighbord]:
            #         travel(neighbord)
            for j in range(len(isConnected[i])):
                if not vis[j] and isConnected[i][j]==1:
                    travel(j)
        for i in range(len(isConnected)):
            if vis[i] is False:
                ans+=1
                travel(i)

        return ans

# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 92.93%
# 的用户
# 内存消耗：
# 15.6 MB
# , 在所有 Python3 提交中击败了
# 7.03%
# 的用户