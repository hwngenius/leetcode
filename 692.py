class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        from collections import Counter
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


words=["I","love","leetcode","I","love","faker"]
Solution().topKFrequent(words,2)