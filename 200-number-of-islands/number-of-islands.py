class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def visitIsland(r, c):
            if r < 0 or r >= R or c <0 or c >= C or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            visitIsland(r+1, c)
            visitIsland(r-1, c)
            visitIsland(r, c+1)
            visitIsland(r, c-1)
        
        islands = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    islands += 1
                    visitIsland(i,j)

        return islands