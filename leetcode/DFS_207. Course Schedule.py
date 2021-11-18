from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()
        def dfs(v):
            if v in visited:
                return True                
            if v in traced:
                return False

            traced.add(v)
            for b in graph[v]:
                if not dfs(b):
                    return False

            traced.remove(v)
            visited.add(v)
            return True

        for v in list(graph):
            if not dfs(v):
                return False
        return True
