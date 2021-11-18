import collections

from typing import List
from collections import Counter
import heapq

#Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk

#파이썬다운 방식
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]