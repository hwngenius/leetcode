class Solution:
    def romanToInt(self,s:str)->int:
        if len(s)==0:
            return 0
        c_int={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        c_index={}
        index=0
        for c in c_int.keys():
            c_index[c]=index
            index+=1
        ans=c_int[s[0]]
        for i in range(1,len(s)):
            if c_index[s[i]]>c_index[s[i-1]]:
                ans-=c_int[s[i-1]]*2
            ans+=c_int[s[i]]
        return ans

print(Solution().romanToInt("MCMXCIV"))