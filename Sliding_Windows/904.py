from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans, current_sum = 0, 0
        left, right = 0, 0
        count = 0
        data = defaultdict(int)
        while right < len(tree):
            while count < 3 and right < len(tree):
                if data[tree[right]] == 0:
                    count += 1
                data[tree[right]] += 1
                if count < 3:
                    current_sum += 1
                    ans = max(ans, current_sum)
                    right += 1
            while count > 2:
                data[tree[left]] -= 1
                current_sum -= 1
                if data[tree[left]] == 0:
                    count -= 1
                left += 1
            if right<len(tree):
                data[tree[right]] -= 1
                count -= 1

        return ans


tree = [0,0,1,1]
print(Solution().totalFruit(tree))
