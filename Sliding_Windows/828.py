class Solution:
    def uniqueLetterString(self, s: str) -> int:
        import collections
        count=collections.defaultdict(list)
        for i,c in enumerate(s):
            count[c].append(i)
        ans=0
        for l in count.values():
            v=[-1]+l+[len(s)]
            for i in range(1,len(v)-1):
                ans+=(v[i]-v[i-1])*(v[i+1]-v[i])
        return ans%(10**9+7)


print(Solution().uniqueLetterString("ABA"))
