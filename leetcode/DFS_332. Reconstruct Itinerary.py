from typing import List
from collections import defaultdict, deque

#DFS(재귀)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for a, b in sorted(tickets):
            graph[a].append(b)

        result = []
        def dfs(v):
            while graph[v]:
                dfs(graph[v].popleft())
            result.append(v)
        dfs("JFK")
        return result[::-1]

#반복
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        result = []
        st = ["JFK"]
        while st:
            while graph[st[-1]]:
                st.append(graph[st[-1]].popleft())
            result.append(st.pop())
        return result[::-1]
        