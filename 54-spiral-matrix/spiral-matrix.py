class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])  # Initialize horizontal boundaries
        top, bottom = 0, len(matrix)    # Initialize vertical boundaries
        
        res = []  # Result list to store spiral order
        while left < right and top < bottom:
            # Traverse from left to right along the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom along the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left

            # Check if there are remaining rows and columns to process
            if not (left < right and top < bottom):
                break
            
            # Traverse from right to left along the bottom row
            for i in reversed(range(left, right)):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up

            # Traverse from bottom to top along the left column
            for i in reversed(range(top, bottom)):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right
        
        return res  # Return the result list

# TC = O(m * n), where m is the number of rows and n is the number of columns (each element is visited once)
# SC = O(1), excluding the result list which stores all elements of the matrix