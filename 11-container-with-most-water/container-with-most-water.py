class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0  # Track the maximum area found
        l = 0  # Left pointer
        N = len(height)
        r = N - 1  # Right pointer

        while l < r:
            left = height[l]  # Height of the left boundary
            right = height[r]  # Height of the right boundary
            area = min(left, right) * (r - l)  # Calculate area between boundaries
            maxarea = max(area, maxarea)  # Update the maximum area
            if left < right:
                l += 1  # Move the left pointer if the left boundary is smaller
            else:
                r -= 1  # Move the right pointer otherwise
        return maxarea  # Return the maximum area found

# TC = O(n), where n is the number of elements in the array (each pointer is moved once)
# SC = O(1), as no additional data structures are used