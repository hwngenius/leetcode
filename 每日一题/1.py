from typing import List
from collections import *

class Solution:
    def towSum(self,nums:List[int],target:int)->int:
        dict={}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]