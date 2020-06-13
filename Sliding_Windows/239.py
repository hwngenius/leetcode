from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if k==1:return nums
        n = len(nums) - k + 1
        ans = [0] * n
        max_index = 0
        # second_index = 0
        second_num = -100000
        max_num = -100000
        # flag = False
        for i in range(k):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        # for i in range(k):
        #     if nums[i]>second_num and i!=max_index:
        #         second_num=nums[i]
        #         second_index=i
        ans[0]=max_num
        for i in range(1, len(nums) - k+1):
            if i - 1 != max_index:
                if nums[i + k - 1] > max_num:
                    # second_num, second_index = max_num = max_index
                    max_num, max_index = nums[i + k - 1], i + k - 1
                # elif nums[i + k - 1] > second_num:
                #     second_num, second_index = nums[i + k - 1], i + k - 1

            else:
                if max_num < nums[i + k - 1]:
                    max_num, max_index = nums[i + k - 1], i + k - 1
                else:
                    max_num = max(nums[i:i + k])
                    max_index = nums[i:i + k].index(max_num) + i
            ans[i] = max_num

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
