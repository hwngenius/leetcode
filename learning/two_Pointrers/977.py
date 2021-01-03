from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        index, min_diff = 0, float("inf")
        for i, x in enumerate(A):
            if abs(x) < min_diff:
                min_diff = abs(x)
                index = i
        right = index
        left=right-1
        while left >= 0 and right < len(A):
            if abs(A[left]) < abs(A[right]):
                ans.append(A[left] * A[left])
                left -= 1
            else:
                ans.append(A[right] * A[right])
                right += 1
        while left >= 0:
            ans.append(A[left] * A[left])
            left -= 1
        while right < len(A):
            ans.append(A[right] * A[right])
            right += 1
        return ans


print(Solution().sortedSquares([-4,-1,0,3,10]))