from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        after=[set() for _ in range(numCourses)]
        before=[set() for _ in range(numCourses)]
        vis=[False for _ in range(numCourses)]
        count=numCourses

        for l in prerequisites:
            before[l[0]].add(l[1])
            after[l[1]].add(l[0])
        
        def check(i:int):
            nonlocal count
            if not before[i] and vis[i] is False:
                vis[i]=True
                count-=1
                for c in after[i]:
                    before[c].remove(i)
                    if not before[c]:
                        check(c)
        for i in range(numCourses):
            check(i)
        
        return count<=0

# 执行用时：
# 60 ms
# , 在所有 Python3 提交中击败了
# 31.42%
# 的用户
# 内存消耗：
# 19.1 MB
# , 在所有 Python3 提交中击败了
# 5.05%
# 的用户