class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])  # Get the number of rows and columns

        def dfs(r, c):
            # Base case: Return 0 if out of bounds or cell is water/already visited
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            grid[r][c] = 0  # Mark cell as visited by turning it into water
            # Recursively calculate the area of connected land
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) +
                    dfs(r, c + 1) + dfs(r, c - 1))
        
        maxarea = 0  # Track the maximum area of any island
        for i in range(R):  # Iterate through all rows
            for j in range(C):  # Iterate through all columns
                if grid[i][j] == 1:  # If land is found, start DFS
                    maxarea = max(dfs(i, j), maxarea)  # Update maximum area
        
        return maxarea  # Return the largest island area

# TC = O(R * C)
# SC = O(R * C), for the recursion stack in the worst case when the grid is filled with land.