from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus=1
        for i in range(len(digits)-1,-1,-1):
            total=digits[i]+plus
            plus=total//10
            digits[i]=total%10
        if plus!=0:
            digits=[plus]+digits
        return digits