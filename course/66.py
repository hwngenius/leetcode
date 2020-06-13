from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                t=digits[i]+1
            else:
                t=digits[i]+plus
            digits[i]=t%10
            plus=t//10
        if plus!=0:
            digits=[plus]+digits

        return digits


print(Solution().plusOne([9,9,9]))