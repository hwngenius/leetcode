from typing import List


class Solution:
    def leastInterval(self, tasks:List[int], n:int):
        from collections import Counter
        length = len(tasks)
        if length <= 1:
            return length
        counter = Counter(tasks)
        sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        max_time = sorted_list[0][1]
        ans = (max_time - 1) * (n + 1)
        for _, time in sorted_list:
            if time == max_time:
                ans += 1
            else:
                break
        return ans if ans > length else length
