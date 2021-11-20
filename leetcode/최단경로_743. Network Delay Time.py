from typing import List
from collections import defaultdict
import heapq

#distacne를 리스트로
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        INF = int(1e9)        
        for u, v, w in times:
            graph[u].append((v, w))
        q = [(0, k)]
        distance = [INF] * (n+1)
        distance[k] = 0
        while q:
            dist, node = heapq.heappop(q)
            if distance[node] < dist:
                continue
            for v, w in graph[node]:
                cost = dist + w
                if cost < distance[v]:
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))
        distance[0] = 0
        result = max(distance)
        return result if result != INF else -1
#distance를 defaultdict로
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)   
        for u, v, w in times:
            graph[u].append((v, w))
        q = [(0, k)]
        distance = defaultdict(int)
        while q:
            dist, node = heapq.heappop(q)
            if node not in distance:
                distance[node] = dist
                for v, w in graph[node]:
                    cost = dist + w
                    heapq.heappush(q, (cost, v))
        
        return max(distance.values()) if len(distance) == n else -1
