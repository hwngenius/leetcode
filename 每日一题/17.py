from typing import List


class Solution:
    def letterCombination(self, digits: str) -> List[str]:
        reflect = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        def myfun(current_list:List[str],c:str)->List[str]:
            if current_list==[]:
                return list(reflect[c])
            ans=[]
            for s in current_list:
                for c in reflect[c]:
                    ans.append(s+c)
            return ans
        res=[]
        for c in digits:
            res=myfun(res,c)
        return res