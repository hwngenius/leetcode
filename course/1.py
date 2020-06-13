from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import collections
        data = collections.Counter(nums)
        for i in range(len(nums)):
            t = target - nums[i]
            if t in data:
                if t != nums[i]:
                    return [i, nums.index(t)]
                elif data[t] >= 2:
                    ans = []
                    iter = 0
                    for i in range(len(nums)):
                        if nums[i] == t:
                            ans.append(i)
                            iter += 1
                        if iter >= 2:
                            return ans
