class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        alpha={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mon','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=[]
        def traceback(idx,component:str):
            if idx==len(digits) and component:
                ans.append(component[:])
            else:
                digit=digits[idx]
                for c in alpha[digit]:
                    traceback(idx+1,component+c)
        
        traceback(0,"")
        return ans
    
# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 77.94%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 17.03%
# 的用户