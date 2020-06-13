from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def fun(pre_list,c):
            if len(pre_list)==0:
                return list(data[c])
            return_list=[]
            for l in pre_list:
                for d in data[c]:
                    return_list.append(l+d)
            return return_list
        ans=[]
        for c in digits:
            ans=fun(ans,c)
        return ans


print(Solution().letterCombinations("23"))