class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0  # Total water trapped
        l, r = 0, len(height) - 1  # Two pointers
        lmax, rmax = height[l], height[r]  # Track max heights from left and right

        while l < r:
            if lmax < rmax:  # Process left side
                l += 1
                lmax = max(lmax, height[l])  # Update left max height
                res += lmax - height[l]  # Add trapped water
            else:  # Process right side
                r -= 1
                rmax = max(rmax, height[r])  # Update right max height
                res += rmax - height[r]  # Add trapped water

        return res  # Return the total trapped water

# TC = O(n), single pass through the array using two pointers
# SC = O(1), constant space used