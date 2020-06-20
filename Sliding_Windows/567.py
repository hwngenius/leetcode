from collections import defaultdict
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        target_count = Counter(s1)
        count = defaultdict(int)
        left, right = 0, len(s1) - 1
        for i in range(left, right + 1): count[s2[i]] += 1
        if target_count == count: return True
        while right < len(s2) - 1:
            count[s2[left]] -= 1
            left += 1
            right += 1
            count[s2[right]] += 1
            flag=True
            for k,v in target_count.items():
                if count[k]!=target_count[k]:
                    flag=False
                    break
            if flag is True:
                return True
        return False


s1 = "ba"
s2 = "eidb3aoooba"
print(Solution().checkInclusion(s1, s2))
