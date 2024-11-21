class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # Get the size of the square matrix

        # Transpose the matrix by swapping elements symmetrically along the diagonal
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row to achieve the 90-degree clockwise rotation
        for row in matrix:
            row.reverse()

# TC = O(n^2), where n is the size of the matrix (both transpose and reverse take O(n^2))
# SC = O(1), as the rotation is performed in-place without extra space