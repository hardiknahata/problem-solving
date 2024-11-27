class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])  # Get the number of rows and columns

        def visitIsland(r, c):
            # Base case: Stop if out of bounds or at a water cell
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # Mark the cell as visited by setting it to "0"
            # Recursively visit all neighboring cells
            visitIsland(r + 1, c)
            visitIsland(r - 1, c)
            visitIsland(r, c + 1)
            visitIsland(r, c - 1)
        
        islands = 0  # Counter for the number of islands
        for i in range(R):  # Iterate through all rows
            for j in range(C):  # Iterate through all columns
                if grid[i][j] == "1":  # If a land cell is found
                    islands += 1  # Increment the island count
                    visitIsland(i, j)  # Visit all connected land cells

        return islands  # Return the total number of islands

# TC = O(R * C), where R is the number of rows and C is the number of columns
# - Each cell is visited once during the DFS traversal.
# SC = O(R * C), for the recursion stack in the worst case when the grid is filled with land