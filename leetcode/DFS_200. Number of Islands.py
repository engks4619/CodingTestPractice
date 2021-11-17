from typing import List

class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:          
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1] 

        def dfs(i, j):            
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        dfs(nx, ny)     
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
    