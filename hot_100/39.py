class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def tracaback(combination,total,idx):
            if total==target:
                ans.append(combination[:])
            elif total<target:
                if idx<len(candidates):
                    combination.append(candidates[idx])
                    tracaback(combination,total+candidates[idx],idx)
                    combination.pop()
                    tracaback(combination,total,idx+1)
        tracaback([],0,0)
        return ans

# 执行用时：
# 100 ms
# , 在所有 Python3 提交中击败了
# 30.02%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 7.79%
# 的用户