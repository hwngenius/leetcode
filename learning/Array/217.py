class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t=set()
        for i in nums:
            if i not in t:
                t.add(i)
            else:
                return True
        return False



# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 42.11%
# 的用户
# 内存消耗：
# 19.9 MB
# , 在所有 Python3 提交中击败了
# 24.03%
# 的用户