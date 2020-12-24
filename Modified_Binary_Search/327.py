class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
        
        self.res = 0
        
        def sort(nums):
            if len(nums) < 2: return nums
            mid = len(nums)//2
            left, right = sort(nums[:mid]), sort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            m, n = len(left), len(right)
            c = []
            i = j = 0
            for l in left:
                while i < n and right[i] - l < lower: i +=1
                while j < n and right[j] - l <= upper: j +=1
                self.res += (j-i)
            i = j = 0
            while i < m and j < n:
                if left[i] < right[j]:
                    c.append(left[i])
                    i += 1
                else:
                    c.append(right[j])
                    j += 1
            if i == m: c += right[j:]
            else: c += left[i:]
            return c
        
        sort(presum)
        
        return self.res