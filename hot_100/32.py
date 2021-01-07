class Solution:
    def longestValidParentheses(self, s: str) -> int:
        hash_table={'(':1,')':-1}
        ans=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j+1-i>ans:
                    total=0
                    for k in range(i,j+1):
                        total+=hash_table[s[k]]
                        if total<0:
                            break
                    if total==0:
                        ans=j-i+1
        return ans


# out of time