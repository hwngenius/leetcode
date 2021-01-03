class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums_set:
                tmp = 1
                while num + 1 in nums_set:
                    num += 1
                    tmp += 1
                ans = max(ans, tmp)

        return ans


# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 53.69%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 9.20%
# 的用户