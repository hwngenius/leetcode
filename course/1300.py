from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        l = len(arr)
        index, current_sum = 0, 0
        while index < l:
            if target - current_sum <= arr[index] * (l - index):
                break
            current_sum += arr[index]
            index += 1
        if index == l:
            return arr[-1]
        elif index == 0:
            return int(target / l + 0.5)
        else:
            t = (target - current_sum) // (l - index)
            return t if abs(target - (current_sum + (l - index) * t)) <= abs(target-(current_sum+(l-index)*(t+1))) else t + 1


arr = [4,9,3]

target = 10
print(Solution().findBestValue(arr, target))
