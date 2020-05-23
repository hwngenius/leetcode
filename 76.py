class Solution(object):
    def minWindow(self, s, t):
        ansNum,ansleft,ansright=len(s)+1,-1,-1
        cnt,ori={},{}
        for c in t:
            if c not in ori:
                ori[c]=1
            else:
                ori[c]+=1
            cnt[c]=0

        def attestion():
            for c in ori:
                if ori[c]>cnt[c]:
                    return False
            return True

        left,right=0,0
        while right<len(s):
            if s[right] in ori:
                cnt[s[right]]+=1
            while attestion() and left<=right:
                if right-left+1<ansNum:
                    ansNum=right-left+1
                    ansleft,ansright=left,right
                if s[left] in cnt:
                    cnt[s[left]]-=1
                left+=1
            right+=1
        if ansNum==len(s)+1:
            return ""
        return s[ansleft:ansright+1]