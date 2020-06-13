class Solution:
    def topKFrequent(self, words, k):
        import heapq
        import collections
        count = collections.Counter(words)
        print(count)
        heap = [(-fre,word) for (word,fre) in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(0, k)]


words = ["I", "love", "leetcode", "I", "love", "faker"]
print(Solution().topKFrequent(words, 2))
