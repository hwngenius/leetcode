class Solution:
    def isValid(self, s: str) -> bool:
        para_map={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c not in para_map:
                stack.append(c)
            else:
                if stack and para_map[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

# 执行用时：
# 28 ms
# , 在所有 Python3 提交中击败了
# 98.77%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 11.63%
# 的用户