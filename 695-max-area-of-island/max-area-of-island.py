class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            return (1 + dfs(r+1,c) +dfs(r-1,c) +dfs(r,c+1) + dfs(r,c-1))
            
        maxarea = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    maxarea = max(dfs(i, j), maxarea)
        
        return maxarea