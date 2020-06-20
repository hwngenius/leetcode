class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        fre=defaultdict(int)
        left,ans,max_fre=0,0,0
        for right in range(len(s)):
            fre[s[right]]+=1
            max_fre=max(max_fre,fre[s[right]])
            while right-left+1-max_fre>k:
                left+=1
                fre[s[left-1]]-=1
            ans=max(ans,right-left+1)

        return ans

print(Solution().characterReplacement("ABAB",2))