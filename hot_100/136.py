class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table=set()
        for num in nums:
            if num not in hash_table:
                hash_table.add(num)
            else:
                hash_table.remove(num)
        for ans in hash_table:
            return ans


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 89.42%
# 的用户
# 内存消耗：
# 16.6 MB
# , 在所有 Python3 提交中击败了
# 5.63%
# 的用户