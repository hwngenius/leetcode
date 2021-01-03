class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(k * v for k, v in collections.Counter(s).most_common())


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
