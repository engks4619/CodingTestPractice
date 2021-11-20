from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        visited = {}
        for u, v, w in flights:
            graph[u].append((v, w))
        q = [(0, src, K)]
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price
            if node not in visited or visited[node] < k:                
                if k >= 0:
                    visited[node] = k
                    for v, w in graph[node]:
                        heapq.heappush(q, (price + w, v, k - 1))
        return -1
    