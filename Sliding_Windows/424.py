class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        frequence = defaultdict(int)
        ans, max_fre, left = 0, 0, 0
        for right in range(len(s)):
            frequence[s[right]] += 1
            max_fre = max(max_fre, frequence[s[right]])
            while right - left + 1 - max_fre > k:
                left += 1
                frequence[s[left - 1]] -= 1
            ans = max(ans, right - left + 1)

        return ans
