from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        index_A, index_B = 0, 0
        ans = []
        while index_A < len(A) and index_B < len(B):
            right = min(A[index_A][1], B[index_B][1])
            left = max(A[index_A][0], B[index_B][0])
            if left <= right:
                ans.append([left, right])
            if A[index_A][1] < B[index_B][1]:
                index_A += 1
            else:
                index_B += 1
        return ans


# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 85.03%
# 的用户
# 内存消耗：
# 14.3 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户